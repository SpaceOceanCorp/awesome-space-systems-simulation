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

GUIDE_REQUIRED_LINK_PREFIXES = ("../tools/", "../benchmarks/")
BENCHMARK_REQUIRED_HEADINGS = (
    "Problem statement",
    "Reference implementation",
    "Required outputs",
    "Error metrics",
    "Cross-tool results",
    "Validation status",
    "Last reviewed",
    "Status",
)


def entry_blocks(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    starts = [i for i, line in enumerate(lines) if line.startswith("### ")]
    for index, start in enumerate(starts):
        end = starts[index + 1] if index + 1 < len(starts) else len(lines)
        yield start + 1, lines[start][4:].strip(), lines[start:end]


def heading_anchor(heading: str) -> str:
    normalized = re.sub(r"[^a-z0-9 _-]", "", heading.lower())
    return re.sub(r"[ ]+", "-", normalized.strip())


def check_guides_and_benchmarks(errors):
    guides_root = ROOT / "guides"
    if not guides_root.is_dir():
        errors.append("guides/: missing task-guide directory")
    else:
        guide_files = sorted(path for path in guides_root.glob("*.md") if path.name != "README.md")
        if not guide_files:
            errors.append("guides/: no task-guide pages found")
        for path in guide_files:
            text = path.read_text(encoding="utf-8")
            if not re.search(r"^## ", text, re.MULTILINE):
                errors.append(f"{path.relative_to(ROOT)}: missing second-level guide headings")
            for heading in ("Problem type", "Recommended starting points", "Selection constraints", "Common mistakes"):
                if not re.search(rf"^## {re.escape(heading)}$", text, re.MULTILINE):
                    errors.append(f"{path.relative_to(ROOT)}: missing guide heading {heading}")
            if "../tools/" not in text:
                errors.append(f"{path.relative_to(ROOT)}: no primary catalog link")
            if not any(prefix in text for prefix in GUIDE_REQUIRED_LINK_PREFIXES):
                errors.append(f"{path.relative_to(ROOT)}: no catalog or benchmark link")
            if "limitations" not in text.lower() and "non-official" not in text.lower():
                errors.append(f"{path.relative_to(ROOT)}: missing limitations or integration caveat")

    benchmarks_root = ROOT / "benchmarks"
    benchmark_files = sorted(path for path in benchmarks_root.rglob("*.md") if path.name != "README.md")
    for path in benchmark_files:
        text = path.read_text(encoding="utf-8")
        headings = set(re.findall(r"^## (.+)$", text, re.MULTILINE))
        missing = [heading for heading in BENCHMARK_REQUIRED_HEADINGS if heading not in headings]
        if missing:
            errors.append(f"{path.relative_to(ROOT)}: missing benchmark headings: {', '.join(missing)}")


def main() -> int:
    errors = []
    names = {}
    statuses = {"reviewed": 0, "pending review": 0, "reference-only": 0}
    reviewed_categories = set()
    category_counts = {}
    category_reviewed = {}
    maintenance_counts = {}

    check_guides_and_benchmarks(errors)

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

    markdown_files = sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)
    for source in markdown_files:
        text = source.read_text(encoding="utf-8")
        for link in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
            if link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_path, _, fragment = link.partition("#")
            target = (source.parent / target_path).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{source.relative_to(ROOT)}: link escapes repository {link}")
                continue
            if not target.is_file():
                errors.append(f"{source.relative_to(ROOT)}: broken internal link {link}")
            elif fragment:
                target_text = target.read_text(encoding="utf-8")
                headings = re.findall(r"^#{1,6} (.+)$", target_text, re.MULTILINE)
                anchors = {heading_anchor(name) for name in headings}
                if fragment not in anchors:
                    errors.append(f"{source.relative_to(ROOT)}: missing internal anchor {link}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    overview_links = re.findall(r"\[Open\]\(([^)]+)\)", readme)

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
