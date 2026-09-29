# AI-GAN — Reverse-engineer công thức prompt ảnh & video

Thu thập cách influencer xây dựng prompt → phân tích thành digest (kỹ thuật, chủ đề, từ vựng) → index qua `mapping.md` → đúc thành template tái dùng trong `templates/`.

> **Raw = text prompt, không phải media.** `research/*/raws/` chỉ chứa copy nguyên văn prompt (`.md`/`.txt`). Ảnh/video mẫu (nếu có) để ở `.local/` (gitignored), không commit.

## Bản đồ repo

| Path | Vai trò |
|------|---------|
| `AGENTS.md` | Protocol cho agent (startup, invariants, routing) |
| `.context/` | Working memory agent (milestones, tensions, pitfalls, modules) |
| `research/images/` | Prompt ảnh: `raws/` + `digests/` + `mapping.md` |
| `research/videos/` | Prompt video: `raws/` + `digests/` + `mapping.md` |
| `templates/` | Prompt context/template tái dùng, index ở `Index.md` |
| `workflows/<platform>/` | Chạy thử API: script + docs + `models/` + `INDEX.md` (chạy trên WSL); sản phẩm ở `.local/work/` |
| `docs/README.md` | Index docs human |
| `.local/` | Scratch + media mẫu local + sản phẩm `workflows/` (không commit) |

```
AI-GAN/
  AGENTS.md
  README.md                ← file này
  .context/                ← memory agent (không phải docs human)
  research/
    images/{raws/,digests/,mapping.md}
    videos/{raws/,digests/,mapping.md}
  templates/{images/,videos/,drafts/,Index.md}
  workflows/<platform>/{README.md,INDEX.md,models/,*.py}   ← chạy trên WSL
  docs/README.md
  .local/                  ← gitignored (+ work/<provider>/<slug>/ sản phẩm)
```

## Pipeline

```
raw (copy prompt) → digest (phân tích) → mapping (index) → template (đúc công thức)
```

1. Copy nguyên văn prompt influencer vào `research/{images,videos}/raws/<slug>.md` + ghi nguồn/URL/ngày.
2. Viết `digests/<slug>.md` theo schema (kỹ thuật, chủ đề, từ vựng, model) — mọi claim link về raw.
3. Thêm 1 dòng vào `mapping.md` (từ khóa kỹ thuật/chủ đề/model).
4. Khi ≥2 digest cùng pattern → đúc template vào `templates/{images,videos}/`, trỏ từ `templates/Index.md`.

Chi tiết: `.context/GLOBAL.md` + `.context/modules/*.md`.
