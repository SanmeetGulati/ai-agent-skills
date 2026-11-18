# Contributing and maintenance

1. Make focused changes under `skills/<skill-name>/`. Keep `SKILL.md` concise and put substantial conditional guidance in referenced files.
2. Preserve valid YAML frontmatter with `name` and `description`. Match the folder name and use a description that triggers only for relevant work.
3. Run `python3 scripts/validate_skills.py`. Review the skill against representative tasks; structural validation cannot prove that recommendations or behavior are correct.
4. Review the diff for credentials, personal paths, project-specific information, unverified claims, and copied material with incompatible licensing. Submit changes for review.
5. Update your installed copy deliberately after review. Avoid copying over an existing directory without removing or backing it up first, since stale files can remain.

When changing research guidance, prefer current primary sources and make clear which claims are measured versus inferred. Do not hard-code fast-changing model or tool rankings into a skill.
