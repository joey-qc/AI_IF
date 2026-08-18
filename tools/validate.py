#!/usr/bin/env python3
"""
Deterministic Validation Tool for AI Interactive Fiction (AI_IF)

Validates machine-governed JSON artifacts against their authoritative JSON Schemas,
verifies schema validity, and checks basic repository consistency.

Exit Codes:
  0 = All requested validation passed cleanly
  1 = One or more files failed JSON/schema/repository validation
  2 = Tool, usage, file-not-found, or configuration failure
"""

import sys
import os
import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Any

try:
    import jsonschema
    from jsonschema import Draft202012Validator
except ImportError:
    print("Error: jsonschema 4.26.0 is required. Run 'pip install -r requirements-dev.txt'.", file=sys.stderr)
    sys.exit(2)


# Authoritative artifact filename to schema mapping
SUPPORTED_ARTIFACTS: Dict[str, str] = {
    "game-package.json": "schemas/game-package.schema.json",
    "validation-report.json": "schemas/validation-report.schema.json",
    "runtime-fidelity-report.json": "schemas/runtime-fidelity-report.schema.json",
    "runtime-state.json": "schemas/runtime-state.schema.json",
    "case-board-current.json": "schemas/case-board-current.schema.json",
}


def normalize_path(path: Path, repo_root: Path) -> str:
    """Return relative path with forward slashes for consistent output across platforms."""
    try:
        rel = path.relative_to(repo_root)
        return rel.as_posix()
    except ValueError:
        return path.as_posix()


def format_json_path(error: jsonschema.ValidationError) -> str:
    """Format ValidationError json_path consistently (e.g. $.playerConfig.imageMode or $)."""
    if hasattr(error, "json_path") and error.json_path:
        return error.json_path
    path = "$"
    for elem in error.absolute_path:
        if isinstance(elem, int):
            path += f"[{elem}]"
        else:
            path += f".{elem}"
    return path


def load_and_verify_schema(schema_rel_path: str, repo_root: Path) -> Tuple[bool, Any, str]:
    """Load and verify that a schema file is valid JSON and a valid JSON Schema."""
    schema_full_path = repo_root / schema_rel_path
    if not schema_full_path.exists():
        return False, None, f"Schema file not found: {schema_rel_path}"

    try:
        with open(schema_full_path, "r", encoding="utf-8") as f:
            schema_data = json.load(f)
    except json.JSONDecodeError as e:
        return False, None, f"Schema file is malformed JSON ({schema_rel_path}): {e}"
    except Exception as e:
        return False, None, f"Failed to read schema file ({schema_rel_path}): {e}"

    try:
        Draft202012Validator.check_schema(schema_data)
    except jsonschema.SchemaError as e:
        return False, None, f"Schema file is not a valid JSON Schema ({schema_rel_path}): {e.message}"
    except Exception as e:
        return False, None, f"Schema validation error ({schema_rel_path}): {e}"

    return True, schema_data, ""


def validate_single_file(file_path: Path, repo_root: Path, schema_cache: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Validate a single JSON artifact against its authoritative schema.
    Returns (passed: bool, error_messages: List[str]).
    """
    display_path = normalize_path(file_path, repo_root)
    filename = file_path.name

    if filename not in SUPPORTED_ARTIFACTS:
        return False, [f"Unsupported artifact: '{filename}' has no registered JSON schema."]

    schema_rel_path = SUPPORTED_ARTIFACTS[filename]

    if schema_rel_path not in schema_cache:
        ok, schema_data, err_msg = load_and_verify_schema(schema_rel_path, repo_root)
        if not ok:
            print(f"Tool Configuration Error: {err_msg}", file=sys.stderr)
            sys.exit(2)
        schema_cache[schema_rel_path] = schema_data

    schema_data = schema_cache[schema_rel_path]

    # Load JSON instance
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            instance = json.load(f)
    except json.JSONDecodeError as e:
        return False, [f"$ (root): Malformed JSON syntax - {e.msg} at line {e.lineno} col {e.colno}"]
    except Exception as e:
        return False, [f"$ (root): Unable to read file - {e}"]

    # Validate instance against schema
    validator = Draft202012Validator(schema_data)
    raw_errors = list(validator.iter_errors(instance))

    if not raw_errors:
        return True, []

    # Format and sort errors by JSON path deterministically
    formatted_errors: List[Tuple[str, str]] = []
    for err in raw_errors:
        path_str = format_json_path(err)
        formatted_errors.append((path_str, err.message))

    formatted_errors.sort(key=lambda x: (x[0], x[1]))
    error_lines = [f"{p}: {msg}" for p, msg in formatted_errors]
    return False, error_lines


def perform_repository_checks(repo_root: Path) -> Tuple[bool, str, List[str]]:
    """
    Perform deterministic repository consistency checks against games/index.json.
    Returns (passed: bool, display_name: str, error_messages: List[str]).
    """
    index_path = repo_root / "games" / "index.json"
    display_name = "games/index.json"

    if not index_path.exists():
        return False, display_name, ["$ (root): Catalog index file games/index.json does not exist."]

    try:
        with open(index_path, "r", encoding="utf-8") as f:
            index_data = json.load(f)
    except json.JSONDecodeError as e:
        return False, display_name, [f"$ (root): Malformed JSON in catalog index - {e.msg}"]
    except Exception as e:
        return False, display_name, [f"$ (root): Unable to read games/index.json - {e}"]

    if not isinstance(index_data, list):
        return False, display_name, ["$ (root): Catalog index must be a top-level JSON array."]

    errors: List[str] = []
    seen_case_ids: Dict[str, int] = {}
    seen_folders: Dict[str, int] = {}

    for idx, entry in enumerate(index_data):
        if not isinstance(entry, dict):
            errors.append(f"[{idx}]: Entry is not a JSON object.")
            continue

        case_id = entry.get("caseId")
        folder = entry.get("folder")

        # Check duplicate caseId
        if case_id:
            if case_id in seen_case_ids:
                errors.append(f"[{idx}].caseId: Duplicate caseId '{case_id}' (first seen at index {seen_case_ids[case_id]}).")
            else:
                seen_case_ids[case_id] = idx

        # Check duplicate folder
        if folder:
            if folder in seen_folders:
                errors.append(f"[{idx}].folder: Duplicate folder '{folder}' (first seen at index {seen_folders[folder]}).")
            else:
                seen_folders[folder] = idx

            # Check folder existence on disk
            folder_path = repo_root / folder
            if not folder_path.exists() or not folder_path.is_dir():
                errors.append(f"[{idx}].folder: Indexed folder '{folder}' does not exist on disk.")

            # Check metadata consistency against game-package.json if present
            pkg_path = folder_path / "game-package.json"
            if pkg_path.exists():
                try:
                    with open(pkg_path, "r", encoding="utf-8") as pf:
                        pkg_data = json.load(pf)
                    if isinstance(pkg_data, dict):
                        pkg_meta = pkg_data.get("caseMetadata", {})

                        # Compare fields when present in both locations
                        keys_to_compare = ["caseId", "status", "validationStatus", "playtestStatus"]
                        for k in keys_to_compare:
                            idx_val = entry.get(k)
                            pkg_val = pkg_meta.get(k)
                            if idx_val is not None and pkg_val is not None and idx_val != pkg_val:
                                errors.append(
                                    f"[{idx}].{k}: Catalog index mismatch for '{k}': index has '{idx_val}', but game-package.json has '{pkg_val}'."
                                )
                except Exception:
                    pass  # JSON parse errors on package are caught during package validation

    errors.sort()
    return len(errors) == 0, display_name, errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Deterministic AI_IF Validation Tool")
    parser.add_argument("file", nargs="?", help="Path to a single supported JSON file to validate")
    parser.add_argument("--all", action="store_true", help="Recursively inspect and validate all supported artifacts in games/")

    args = parser.parse_args()

    if not args.all and not args.file:
        parser.print_help()
        sys.exit(2)

    repo_root = Path(__file__).resolve().parent.parent

    schema_cache: Dict[str, Any] = {}

    # Verify all 5 authoritative schemas first
    for filename, schema_rel in SUPPORTED_ARTIFACTS.items():
        ok, schema_data, err_msg = load_and_verify_schema(schema_rel, repo_root)
        if not ok:
            print(f"Tool Configuration Error: {err_msg}", file=sys.stderr)
            sys.exit(2)
        schema_cache[schema_rel] = schema_data

    if args.file and not args.all:
        target_file = Path(args.file)
        if not target_file.is_absolute():
            target_file = (repo_root / target_file).resolve()

        if not target_file.exists():
            print(f"Error: Target file not found: {args.file}", file=sys.stderr)
            sys.exit(2)

        filename = target_file.name
        if filename not in SUPPORTED_ARTIFACTS:
            print(f"Error: Unsupported artifact '{filename}'. Supported filenames: {', '.join(SUPPORTED_ARTIFACTS.keys())}", file=sys.stderr)
            sys.exit(2)

        passed, errors = validate_single_file(target_file, repo_root, schema_cache)
        disp_path = normalize_path(target_file, repo_root)

        if passed:
            print(f"PASS {disp_path}")
            sys.exit(0)
        else:
            print(f"FAIL {disp_path}")
            for err in errors:
                print(f"  {err}")
            sys.exit(1)

    if args.all:
        games_dir = repo_root / "games"
        if not games_dir.exists():
            print("Error: games/ directory does not exist.", file=sys.stderr)
            sys.exit(2)

        # Collect all supported files under games/
        files_to_check: List[Path] = []
        for root, _, filenames in os.walk(games_dir):
            for fn in filenames:
                if fn in SUPPORTED_ARTIFACTS:
                    files_to_check.append(Path(root) / fn)

        # Sort file paths deterministically
        files_to_check.sort(key=lambda p: normalize_path(p, repo_root))

        total_checked = 0
        passed_count = 0
        failed_count = 0

        # Validate repository index checks
        idx_passed, idx_name, idx_errors = perform_repository_checks(repo_root)
        total_checked += 1
        if idx_passed:
            passed_count += 1
            print(f"PASS {idx_name}")
        else:
            failed_count += 1
            print(f"FAIL {idx_name}")
            for err in idx_errors:
                print(f"  {err}")

        # Validate each supported file
        for filepath in files_to_check:
            total_checked += 1
            disp_path = normalize_path(filepath, repo_root)
            passed, errors = validate_single_file(filepath, repo_root, schema_cache)
            if passed:
                passed_count += 1
                print(f"PASS {disp_path}")
            else:
                failed_count += 1
                print(f"FAIL {disp_path}")
                for err in errors:
                    print(f"  {err}")

        print(f"\nFiles checked: {total_checked}")
        print(f"Passed: {passed_count}")
        print(f"Failed: {failed_count}")

        if failed_count == 0:
            sys.exit(0)
        else:
            sys.exit(1)


if __name__ == "__main__":
    main()
