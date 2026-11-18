# AI Agent and Engineering Skills

A collection of reusable [Agent Skills](https://agentskills.io/) for designing AI agents, developing software, and conducting machine learning work. Each skill contains a `SKILL.md` with instructions that an agent loads when the task is relevant.

## Skills

| Skill | Use it for |
| --- | --- |
| [ai-agent-architect](skills/ai-agent-architect/SKILL.md) | Design and review agent systems, assess MCP servers and tools, and select models for local agent workloads. |
| [ai-software-engineer](skills/ai-software-engineer/SKILL.md) | Design, implement, debug, and review software or AI systems with a reviewed workflow and appropriate checks. |
| [ai-ml-engineering](skills/ai-ml-engineering/SKILL.md) | Research and evaluate ML methods, design experiments, train or fine-tune models, and plan deployment and monitoring. |

The architect skill loads focused references for [architecture](skills/ai-agent-architect/references/architecture.md), [MCP and tools](skills/ai-agent-architect/references/mcp-tools.md), and [local models](skills/ai-agent-architect/references/local-models.md) only when relevant. Technology recommendations should use current sources and distinguish documented claims from tested results.

## Install for Codex

Clone this repository and copy the skill folders you want into `~/.codex/skills`. Check for existing folders first: copying into an existing skill can mix versions.

```sh
git clone https://github.com/YOUR_USERNAME/ai-agent-skills.git
cd ai-agent-skills
mkdir -p "$HOME/.codex/skills"
cp -R skills/ai-agent-architect "$HOME/.codex/skills/"
```

Replace `YOUR_USERNAME` with the GitHub owner. Repeat the copy command for the other skills as needed. Restart or reload your agent session if newly installed skills are not discovered. Other agents may use different skill directories; consult their documentation.

## Examples

- “Review my agent architecture and identify the most important reliability gaps.”
- “Find and compare MCP servers for my data source, including permissions and deployment requirements.”
- “Recommend local models for this hardware and design an evaluation for tool calling.”
- “Design a controlled experiment to compare these ML models.”

Skills are instructions, not integrations: they do not themselves install MCP servers, download models, or guarantee a particular outcome. Review skills and any referenced files before use.

## Maintenance

The repository copy is the version-controlled source for sharing. Edit a skill here, validate it, and copy the updated folder to your local skills directory when ready. Changes to `~/.codex/skills` do not automatically update this repository. Review changes and avoid committing credentials, private project details, or generated data. The automated check validates skill frontmatter and local Markdown links; it does not evaluate the quality of the instructions.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the validation and update workflow. No license has been selected; repository visibility alone does not grant reuse rights.
