#!/usr/bin/env python3
"""Generate and validate repository inventory from the filesystem."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
PREFERRED_SERIES_ORDER = [
    "C-Pro-Series",
    "Q-Series",
    "Q-Pro-Series",
    "Q-HE-Series",
    "Q-Max-Series",
    "Q-Ultra-8K-Series",
    "K-Pro-Series",
    "K-Max-Series",
    "K-HE-Series",
    "V-Max-Series",
    "P-HE-Series",
    "L-Series",
    "Mice",
    "Keycap Profiles",
]
IGNORED_TOP_LEVEL_DIRS = {"docs", "scripts"}


def iter_series() -> list[Path]:
    preferred_index = {
        name: index for index, name in enumerate(PREFERRED_SERIES_ORDER)
    }
    discovered = []
    for path in REPO_ROOT.iterdir():
        if not path.is_dir():
            continue
        if path.name.startswith(".") or path.name in IGNORED_TOP_LEVEL_DIRS:
            continue
        if any(child.is_dir() and not child.name.startswith(".") for child in path.iterdir()):
            discovered.append(path)
    return sorted(
        discovered,
        key=lambda path: (preferred_index.get(path.name, len(preferred_index)), path.name),
    )


def series_model_dirs(series_path: Path) -> list[Path]:
    return sorted(
        path
        for path in series_path.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    )


def manifest_for_model(model_path: Path) -> dict[str, object]:
    files = sorted(
        path
        for path in model_path.iterdir()
        if path.is_file() and not path.name.startswith(".")
    )
    ext_counts = Counter(path.suffix.lower() or "[noext]" for path in files)
    readme_present = any(path.name.lower() == "readme.md" for path in files)
    data_files = [path for path in files if path.name.lower() != "readme.md"]
    return {
        "model": model_path.name,
        "series": model_path.parent.name,
        "path": str(model_path.relative_to(REPO_ROOT)),
        "file_count": len(data_files),
        "readme_present": readme_present,
        "extensions": dict(sorted(ext_counts.items())),
        "files": [path.name for path in data_files],
    }


def collect_inventory() -> dict[str, object]:
    series_entries = []
    total_models = 0
    total_files = 0
    manifests = []

    for series_path in iter_series():
        models = series_model_dirs(series_path)
        total_models += len(models)
        series_file_count = 0
        series_manifests = []
        for model_path in models:
            manifest = manifest_for_model(model_path)
            series_manifests.append(manifest)
            manifests.append(manifest)
            series_file_count += manifest["file_count"]
        total_files += series_file_count
        series_entries.append(
            {
                "series": series_path.name,
                "model_count": len(models),
                "file_count": series_file_count,
                "models": [manifest["model"] for manifest in series_manifests],
            }
        )

    return {
        "total_models": total_models,
        "total_files": total_files,
        "series": series_entries,
        "manifests": manifests,
    }


def device_model_count(inventory: dict[str, object]) -> int:
    return sum(
        entry["model_count"]
        for entry in inventory["series"]
        if entry["series"] != "Keycap Profiles"
    )


def render_summary_markdown(inventory: dict[str, object]) -> str:
    lines = [
        "# Repository Inventory",
        "",
        "Generated from the current filesystem using `scripts/repo_inventory.py`.",
        "",
        f"- Total model directories: **{inventory['total_models']}**",
        f"- Total data files across model directories: **{inventory['total_files']}**",
        "",
        "## Series Summary",
        "",
        "| Series | Models | Data Files |",
        "|---|---:|---:|",
    ]
    for entry in inventory["series"]:
        lines.append(
            f"| {entry['series']} | {entry['model_count']} | {entry['file_count']} |"
        )
    lines.extend(
        [
            "",
            "## Per-Model Manifests",
            "",
        ]
    )
    for manifest in inventory["manifests"]:
        ext_text = ", ".join(
            f"`{ext}` x{count}" for ext, count in manifest["extensions"].items()
        )
        lines.append(f"### {manifest['series']} / {manifest['model']}")
        lines.append("")
        lines.append(f"- Path: `{manifest['path']}`")
        lines.append(f"- Data files: {manifest['file_count']}")
        lines.append(f"- README present: {'yes' if manifest['readme_present'] else 'no'}")
        lines.append(f"- Extensions: {ext_text}")
        lines.append("")
    return "\n".join(lines) + "\n"


def render_summary_json(inventory: dict[str, object]) -> str:
    return json.dumps(inventory, indent=2) + "\n"


def validate_readme(inventory: dict[str, object], readme_path: Path) -> list[str]:
    text = readme_path.read_text()
    errors = []

    # Count device models (exclude Keycap Profiles which are documentation-only)
    device_models = device_model_count(inventory)

    # Check badge -- either static URL or dynamic endpoint
    badge_match = re.search(r"models%20uploaded-(\d+)-", text)
    badge_json_path = REPO_ROOT / ".github" / "badges" / "model-count.json"
    if badge_match:
        badge_count = int(badge_match.group(1))
        if badge_count != device_models:
            errors.append(
                f"Badge count is {badge_count}, expected {device_models}."
            )
    elif badge_json_path.exists():
        badge_data = json.loads(badge_json_path.read_text())
        badge_count = int(badge_data.get("message", "0"))
        if badge_count != device_models:
            errors.append(
                f"Badge JSON count is {badge_count}, expected {device_models}."
            )
    else:
        errors.append("Could not find model badge count in README or badge JSON.")

    # Check bold model count line -- supports "N models" or "N device models"
    total_match = re.search(r"\*\*(\d+)\s+(?:device\s+)?models\.", text)
    if total_match:
        stated_total = int(total_match.group(1))
        if stated_total != device_models:
            errors.append(
                f"README total says {stated_total} models, expected {device_models}."
            )
    else:
        errors.append("Could not find the bold total model count line in README.")

    mouse_match = re.search(r"\| \*\*Mouse Series\*\* \| Mouse \| .* \((\d+) models\) \|", text)
    if mouse_match:
        stated_mouse_total = int(mouse_match.group(1))
        actual_mouse_total = next(
            entry["model_count"]
            for entry in inventory["series"]
            if entry["series"] == "Mice"
        )
        if stated_mouse_total != actual_mouse_total:
            errors.append(
                f"Mouse Series says {stated_mouse_total} models, expected {actual_mouse_total}."
            )
    else:
        errors.append("Could not find the Mouse Series row in README.")

    if "Q0 Plus" not in text:
        errors.append("README Q Series row does not mention Q0 Plus.")

    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate and validate repository inventory from the filesystem."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate = subparsers.add_parser("generate", help="Generate inventory output.")
    generate.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format.",
    )
    generate.add_argument(
        "--output",
        type=Path,
        help="Optional output path. Prints to stdout when omitted.",
    )

    validate = subparsers.add_parser("validate", help="Validate README counts.")
    validate.add_argument(
        "--readme",
        type=Path,
        default=REPO_ROOT / "README.md",
        help="README path to validate.",
    )

    count = subparsers.add_parser("count", help="Print the current model count.")
    count.add_argument(
        "--device-only",
        action="store_true",
        help="Exclude Keycap Profiles from the total.",
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    inventory = collect_inventory()

    if args.command == "generate":
        if args.format == "json":
            output = render_summary_json(inventory)
        else:
            output = render_summary_markdown(inventory)
        if args.output:
            args.output.write_text(output)
        else:
            sys.stdout.write(output)
        return 0

    if args.command == "count":
        count = device_model_count(inventory) if args.device_only else inventory["total_models"]
        print(count)
        return 0

    errors = validate_readme(inventory, args.readme)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("README inventory checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
