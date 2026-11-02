# FrameLock Agent (image-only)

**Reusable image-prompt research with coding agents.** Collect how influencers build image prompts, reverse-engineer them into reusable formulas — and keep the agent's context small while doing it.

## The problem

- Coding agents balloon context by re-reading the whole archive every session.
- Prompts that work get lost in chat history; nothing is reusable next month.

## How FrameLock answers

1. **Raw before analysis.** Reference prompts are copied verbatim (with source + URL + date) before anything is concluded from them.
2. **Everything traceable.** Each digest links every claim back to its raw; the mapping index is the single source of truth.
3. **Small agent context.** A mapping index replaces full-archive scans; working memory lives in `.context/`.
4. **Templates earn their merge.** A formula is merged only after a filled test from a real digest.

## Repository map

```
FrameLock Agent/
  AGENTS.md                  ← agent protocol (startup order, invariants, routing)
  .context/                  ← agent working memory (milestones, decisions, pitfalls)
  research/images/{raws/,digests/,mapping.md}  ← prompt research: raw → analysis → index
  templates/{images/,drafts/,Index.md}         ← reusable prompt formulas
  workflows/                 ← research commands (add-raw, digest, template) + INDEX
  docs/README.md             ← human docs index
  .local/                    ← gitignored: local media, keys
```

## Pipeline

```
raw prompt → digest (analysis) → mapping (index row) → template (reusable formula)
```

1. Copy a reference prompt verbatim into `research/images/raws/` with source, URL, and date.
2. Analyze it into `digests/` — every claim links back to the raw.
3. Add one index row to `mapping.md` (technique / tone / shot / subject keywords).
4. When a pattern repeats, forge a template in `templates/images/` with an English `UPPER_SNAKE` variable schema and a filled example.

## What is committed vs ignored

- **Committed:** protocols, schemas, templates, index rows.
- **Never committed:** media, keys (`.local/`, `*.log`, media globs — see `.gitignore`).

## Attribution & copyright

- Raw prompts are transcribed for research with source + URL + collection date. Do not re-post bulk third-party prompt text outside this repo.
- Media stays in `.local/` (gitignored) and is never published.
- License: MIT — see `LICENSE`.

## Scope & non-goals

- **Scope:** image-prompt research (raw → digest → mapping → template). New branches (video/API/platform) need user approval first (ASK — see `AGENTS.md` §4).
- **Non-goals:** a media library, a model trainer, an API runner.
