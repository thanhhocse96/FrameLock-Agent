"""Mirror canonical skills/ + workflows/ to OpenCode / Claude Code / Codex paths.

Single source of truth: skills/<name>/SKILL.md + workflows/*.md (repo root).
Executable scripts live per-platform in workflows/<platform>/*.py (NOT mirrored).
Versions tracked in workflows/INDEX.md; skill frontmatter carries metadata.version.
Mirrors (identical content, committed so all tools work on fresh clone):
  skills/<n>/SKILL.md -> .agents/skills/<n>/SKILL.md   (Codex native, OpenCode auto-loads)
                      -> .claude/skills/<n>/SKILL.md   (Claude Code native)
                      -> .opencode/skills/<n>/SKILL.md (OpenCode native)
  workflows/*.md      -> .opencode/commands/*.md       (OpenCode slash)
                      -> .claude/commands/*.md         (Claude slash, legacy format)

Codex has no commands dir: skills cover it (invoked as $skill-name).
Run: python scripts/sync-agents.py  (also: --check for CI)
"""

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKILLS = ["add-raw", "make-digest", "make-template", "higgsfield-run"]
SKILL_TARGETS = [".agents/skills", ".claude/skills", ".opencode/skills"]
WORKFLOWS = ["add-raw.md", "digest.md", "template.md", "hf-run.md"]
CMD_TARGETS = [".opencode/commands", ".claude/commands"]


def sync() -> list[str]:
    changed: list[str] = []
    for name in SKILLS:
        src = ROOT / "skills" / name / "SKILL.md"
        if not src.exists():
            print(f"missing canonical skill: {src}", file=sys.stderr)
            raise SystemExit(1)
        for target in SKILL_TARGETS:
            dst = ROOT / target / name / "SKILL.md"
            dst.parent.mkdir(parents=True, exist_ok=True)
            if not dst.exists() or dst.read_bytes() != src.read_bytes():
                shutil.copyfile(src, dst)
                changed.append(str(dst.relative_to(ROOT)))
    for wf in WORKFLOWS:
        src = ROOT / "workflows" / wf
        if not src.exists():
            print(f"missing canonical workflow: {src}", file=sys.stderr)
            raise SystemExit(1)
        for target in CMD_TARGETS:
            dst = ROOT / target / wf
            Path(dst).parent.mkdir(parents=True, exist_ok=True)
            if not Path(dst).exists() or Path(dst).read_bytes() != src.read_bytes():
                shutil.copyfile(src, dst)
                changed.append(str(Path(dst).relative_to(ROOT)))
    return changed


if __name__ == "__main__":
    changed = sync()
    if "--check" in sys.argv:
        if changed:
            print("drift detected:\n" + "\n".join(f"  {c}" for c in changed))
            raise SystemExit(1)
        print("in sync.")
    else:
        print(f"synced {len(changed)} file(s).")
        for c in changed:
            print(f"  {c}")
