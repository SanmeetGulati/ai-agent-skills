#!/usr/bin/env python3
"""Check required skill metadata and relative Markdown links without dependencies."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []
skills = sorted((root / "skills").iterdir())
if not skills:
    errors.append("No skills found")
for skill in skills:
    if not skill.is_dir():
        continue
    entry = skill / "SKILL.md"
    if not entry.is_file():
        errors.append(f"{skill.name}: missing SKILL.md")
        continue
    content = entry.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", content, re.S)
    if not match:
        errors.append(f"{skill.name}: missing frontmatter")
        continue
    frontmatter = match.group(1)
    if not re.search(rf"^name:\s*{re.escape(skill.name)}\s*$", frontmatter, re.M):
        errors.append(f"{skill.name}: name must match directory")
    if not re.search(r"^description:\s*\S", frontmatter, re.M):
        errors.append(f"{skill.name}: missing description")
    for markdown in skill.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", markdown.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0]
            if target and not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                if not (markdown.parent / target).exists():
                    errors.append(f"{markdown.relative_to(root)}: missing link {target}")
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"Validated {sum(p.is_dir() for p in skills)} skills")
