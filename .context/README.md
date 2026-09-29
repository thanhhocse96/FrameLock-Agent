# `.context/` — agent working memory

> Bắt buộc đọc trước khi tạo file mới trong `.context/`. Không dump file rời ở root khi có loại mới.

## Luật phân loại

1. **Root chỉ giữ file lõi** (bảng dưới). Không thêm `NOTE_*.md`, `TODO_*.md`, log ad-hoc cạnh `GLOBAL.md`.
2. **Loại mới → subdir** (`modules/`, sau này `spikes/`, `decisions/`…).
3. **Tên file:** kebab-case, ổn định (`research-images.md`, không `Research_Images.md`).
4. **Artifact runtime** (media mẫu, dump dài) → `.local/` (gitignored).
5. **Raw/digest/mapping/template** không thuộc `.context/` — chúng nằm ở `research/` và `templates/` (data, không phải memory).

## Root — file lõi (closed set)

| File | Vai trò |
|------|---------|
| `README.md` | File này — layout + luật phân loại |
| `GLOBAL.md` | Mục tiêu dự án, module index, invariants tóm tắt |
| `MILESTONES.md` | Checklist milestone (SoT tiến độ) |
| `TENSIONS_OPEN.md` | Conflict chưa resolve |
| `TENSIONS_ACTIVE.md` | Quyết định đã chốt đang hiệu lực |
| `PITFALLS.md` | Bẫy đã biết, đọc trước khi ghi raw/digest |

## Thư mục con

| Dir | Đặt gì vào | Ví dụ |
|-----|------------|--------|
| `modules/` | Note invariant theo module data | `modules/research-images.md` |

## Liên hệ startup (`AGENTS.md` §1)

Luôn đọc: root lõi + module liên quan + pitfalls. Không load `raws/`/`digests/` mặc định — chỉ load entry được `mapping.md` trỏ tới.
