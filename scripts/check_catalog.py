"""Validate catalog structure without requiring third-party dependencies."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FIELDS = (
    "Type",
    "Primary category",
    "Simulation scope",
    "Evidence level",
    "Primary domain",
    "Capability tags",
    "Language",
    "License",
    "Platform",
    "Time advancement",
    "SIL/HIL",
    "Validation status",
    "Maintenance status",
    "Review status",
)

PRIMARY_CATEGORIES = {
    "platform",
    "dynamics",
    "GNC",
    "subsystems",
    "propulsion",
    "environment",
    "robotics",
    "middleware",
    "co-simulation",
    "flight-software-and-ground",
    "verification",
    "data",
    "restricted-reference",
    "examples",
}

REQUIRED_REVIEWED_CATEGORIES = PRIMARY_CATEGORIES - {"restricted-reference", "examples"}


def entry_blocks(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    starts = [i for i, line in enumerate(lines) if line.startswith("### ")]
    for index, start in enumerate(starts):
        end = starts[index + 1] if index + 1 < len(starts) else len(lines)
        yield start + 1, lines[start][4:].strip(), lines[start:end]


def heading_anchor(heading: str) -> str:
    normalized = re.sub(r"[^a-z0-9 _-]", "", heading.lower())
    return re.sub(r"[ ]+", "-", normalized.strip())


def main() -> int:
    errors = []
    names = {}
    statuses = {"reviewed": 0, "pending review": 0, "reference-only": 0}
    reviewed_categories = set()
    category_counts = {}
    category_reviewed = {}
    maintenance_counts = {}

    catalog_roots = (ROOT / "tools", ROOT / "examples")
    markdown_files = sorted(path for root in catalog_roots for path in root.rglob("*.md"))
    for path in markdown_files:
        if ".git" in path.parts or path.name == "CONTRIBUTING.md":
            continue
        for line_number, name, block in entry_blocks(path):
            if path.name == "pending-candidates.md":
                required = ("Review status",)
            else:
                required = REQUIRED_FIELDS
            missing = [field for field in required if not any(f"**{field}:**" in line for line in block)]
            if missing:
                errors.append(f"{path.relative_to(ROOT)}:{line_number}: missing {', '.join(missing)}")
            block_text = "\n".join(block)
            fields = {
                match.group(1): match.group(2).strip()
                for match in re.finditer(r"^- \*\*([^:]+):\*\* (.+)$", block_text, re.MULTILINE)
            }
            status = fields.get("Review status")
            if status not in statuses:
                errors.append(f"{path.relative_to(ROOT)}:{line_number}: invalid review status {status!r}")
            else:
                statuses[status] += 1

            if path.name != "pending-candidates.md":
                category = fields.get("Primary category")
                if category not in PRIMARY_CATEGORIES:
                    errors.append(f"{path.relative_to(ROOT)}:{line_number}: invalid primary category {category!r}")
                else:
                    category_counts[category] = category_counts.get(category, 0) + 1
                if not re.fullmatch(r"S[0-4](?:-S[0-4])?", fields.get("Simulation scope", "")):
                    errors.append(f"{path.relative_to(ROOT)}:{line_number}: invalid simulation scope")
                if not re.fullmatch(r"V[0-4]", fields.get("Evidence level", "")):
                    errors.append(f"{path.relative_to(ROOT)}:{line_number}: invalid evidence level")
                maintenance = fields.get("Maintenance status")
                if maintenance:
                    maintenance_counts[maintenance] = maintenance_counts.get(maintenance, 0) + 1
                if status == "reviewed":
                    reviewed_categories.add(category)
                    category_reviewed[category] = category_reviewed.get(category, 0) + 1
                    if "pending review" in block_text.lower():
                        errors.append(f"{path.relative_to(ROOT)}:{line_number}: reviewed entry contains pending fields")
                    if not re.search(r"https?://", block_text):
                        errors.append(f"{path.relative_to(ROOT)}:{line_number}: reviewed entry has no official URL")
            if name in names:
                errors.append(
                    f"duplicate entry '{name}' in {path.relative_to(ROOT)}:{line_number} "
                    f"and {names[name]}"
                )
            else:
                names[name] = f"{path.relative_to(ROOT)}:{line_number}"

    missing_categories = sorted(REQUIRED_REVIEWED_CATEGORIES - reviewed_categories)
    if missing_categories:
        errors.append(f"no reviewed entry for categories: {', '.join(missing_categories)}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    overview_links = re.findall(r"\[Open\]\(([^)]+)\)", readme)
    for link in overview_links:
        target_path, _, fragment = link.partition("#")
        target = ROOT / target_path
        if not target.is_file():
            errors.append(f"README.md: broken overview target {link}")
        elif fragment:
            anchors = {
                heading_anchor(name)
                for _, name, _ in entry_blocks(target)
            }
            if fragment not in anchors:
                errors.append(f"README.md: missing overview anchor {link}")

    if errors:
        print("Catalog check failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print(
        "Catalog check passed: "
        f"{statuses['reviewed']} reviewed, "
        f"{statuses['pending review']} pending, "
        f"{statuses['reference-only']} reference-only, "
        f"{len(overview_links)} overview links."
    )
    print("Category coverage:")
    for category in sorted(category_counts):
        print(
            f"- {category}: {category_reviewed.get(category, 0)} reviewed / "
            f"{category_counts[category]} catalog entries"
        )
    print("Maintenance summary:")
    for status, count in sorted(maintenance_counts.items()):
        print(f"- {status}: {count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
