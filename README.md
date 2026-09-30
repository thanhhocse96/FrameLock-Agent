# FrameLock Agent

**Keyframe-first commercial image & video production with coding agents.** Lock the story frame by frame before spending a dollar on video — and keep the agent's context small while doing it.

FrameLock is a workflow + repo protocol for producing commercial visuals (product shots, end-cards, short ad clips) through a coding agent (currently OpenCode) and generative media APIs (currently Higgsfield: Soul, Grok Imagine, Marketing Studio Image, MiniMax H3). Every video starts as approved still frames. Every generation is traceable to its prompt, model, and cost.

## The problem

- AI video is expensive to iterate: a failed 10s clip costs real money, and "prompt and pray" burns budget.
- Coding agents balloon context by re-reading the whole asset library every session.
- Prompts that work get lost in chat history; nothing is reusable next month.

## How FrameLock answers

1. **Keyframes before video.** Still frames are generated, reviewed, and locked first. Video clips only interpolate between approved frames (first/last-frame image-to-video). No locked frames, no video render.
2. **Brief before run.** The agent presents a short shooting script (milestones, camera path, constraints) and waits for approval before spending anything.
3. **Test cheap, finish expensive.** Drafts render at low resolution/mid quality; only finals use 2K/high. Preset/upsell modes are off by default.
4. **Everything traceable.** Each run records its prompt, model, refs, and result in one index row. Any output can be reproduced or audited months later.
5. **Small agent context.** A mapping index is the single source of truth — the agent looks up entries instead of scanning the archive, keeping sessions fast and cheap.

## Two savings, stated separately

| What is saved | How |
|---|---|
| LLM context tokens | Mapping indexes (`mapping.md`, `Index.md`) replace full-archive scans; working memory lives in `.context/` |
| API spend | Frame-first approvals, cheap test renders, stop-loss limits per shot (max 3 paid gens, then change approach) |

## Repository map

```
FrameLock Agent/
  AGENTS.md                  ← agent protocol (startup order, invariants, routing)
  .context/                  ← agent working memory (milestones, decisions, pitfalls)
  research/
    images/{raws/,digests/,mapping.md}    ← prompt research: raw → analysis → index
    videos/{raws/,digests/,mapping.md}
  templates/{images/,videos/,drafts/,Index.md}  ← reusable prompt formulas
  workflows/<platform>/      ← API runners: scripts + model docs + experiment INDEX
    higgsfield/{README.md,INDEX.md,models/,run_*.py,upload_asset.py}
  journal/                   ← session notes, failure logs, style research
  docs/README.md             ← human docs index
  .local/                    ← gitignored: client media, API outputs, keys
```

## Pipeline

```
raw prompt → digest (analysis) → mapping (index row) → template (reusable formula)
                                                      → keyframes (approved stills)
                                                      → video clips (frame-to-frame)
```

1. Copy a reference prompt verbatim into `research/*/raws/` with source, URL, and date.
2. Analyze it into `digests/` — every claim links back to the raw.
3. Add one index row to `mapping.md` (technique / tone / shot / subject keywords).
4. When a pattern repeats, forge a template in `templates/` with an English `UPPER_SNAKE` variable schema and a filled example.
5. Generate stills from templates, approve them, then render video only between approved frames.

## Quickstart (5 minutes)

Requirements: Windows + WSL (Debian), Python 3.13 in WSL, a Higgsfield API key (never committed).

```powershell
# 1. Key lives in the environment only — never in the repo
$env:HF_KEY = "KEY_ID:KEY_SECRET"

# 2. Upload a local reference to get a public URL
wsl -d Debian -- python3 workflows/higgsfield/upload_asset.py --file .local/assets/product.png --content-type image/png

# 3. Run an image edit from a params file
wsl -d Debian -- python3 workflows/higgsfield/run_marketing_studio_image.py --params <params.json> --outdir .local/work/higgsfield/<YYYY-MM-DD-slug>

# 4. Run a frame-to-frame video (MiniMax H3)
wsl -d Debian -- python3 workflows/higgsfield/run_minimax_h3.py --mode image-to-video --params <params.json> --outdir .local/work/higgsfield/<YYYY-MM-DD-slug>
```

Each run writes `input.md` + `params.json` + `run.log` + `output/` into its slug dir, and adds one row to `workflows/higgsfield/INDEX.md`.

## Indicative costs (Higgsfield, at time of writing)

| Operation | Cost driver |
|---|---|
| Marketing Studio image (test: 1K/medium) | Cheapest tier — drafts |
| Marketing Studio image (final: 2K/high) | ~$0.24/render — finals only (no public price list; verify on your bill) |
| MiniMax H3 video 2K | $0.13/second (5s ≈ $0.65, 10s ≈ $1.30) |
| Preset/enhanced image mode | +10% over direct mode — off by default |

## What is committed vs ignored

- **Committed:** protocols, schemas, templates, scripts, model docs, index rows, journals.
- **Never committed:** client media, generated outputs, API keys (`.local/`, `*.log`, media globs — see `.gitignore`).

## Attribution & copyright

- Raw prompts are transcribed for research with source + URL + collection date. Do not re-post bulk third-party prompt text outside this repo.
- Client and generated media stay in `.local/` (gitignored) and are never published.
- License: MIT — see `LICENSE`.

## Scope & non-goals

- **Scope:** OpenCode agents, Higgsfield models. New providers go under `workflows/<platform>/` with `README.md` + `INDEX.md` (ask first — layouts are governed).
- **Non-goals:** a media library, a video editor, a model trainer. This repo produces prompts, frames, and traceable runs — editing happens in your NLE.
