# GLOBAL — AI-GAN

> AI memory dùng chung (commit). Load đầu tiên mỗi phiên. Cập nhật khi có invariant mới hoặc promote từ phiên chat.

## Mục tiêu dự án

Thu thập cách influencer xây dựng prompt (ảnh + video) → reverse-engineer thành công thức tái dùng.

- **Input:** raw prompt text copy nguyên văn (không phải ảnh/video binary).
- **Output:** digest phân tích + mapping index + template trong `templates/`.
- **Không phải:** kho media, tool generate ảnh/video, re-post nội dung bản quyền.

## Module index

| Module | Data path | Context note |
|--------|-----------|--------------|
| research-images | `research/images/{raws/,digests/,mapping.md}` | `.context/modules/research-images.md` |
| research-videos | `research/videos/{raws/,digests/,mapping.md}` | `.context/modules/research-videos.md` |
| templates | `templates/{images/,videos/,drafts/,Index.md}` | `.context/modules/templates.md` |
| work-apis | `work/<provider>/{README.md,INDEX.md,models/}` (docs) + `workflows/<platform>/*.py` (scripts, chạy trên WSL) + `.local/work/<provider>/<slug>/` (sản phẩm) | `.context/modules/work-apis.md` |
| docs human | `docs/README.md` | Chỉ load khi task docs |

## Invariants (tóm tắt — chi tiết ở `AGENTS.md` §2)

- raw = text prompt; raw bất biến (`*_v2.md` khi sửa lỗi copy)
- Digest mọi claim truy về raw (`../raws/<file>#<đoạn>`)
- Mapping là index duy nhất để tra cứu digest
- Template merge chỉ khi đã test fill từ digest thật + `Index.md` trỏ tới
- Digest/mapping/hướng dẫn fill/`Index.md` tiếng Việt; quote prompt gốc giữ tiếng Anh
- Prompt mẫu trong template và mọi prompt kết quả khi được yêu cầu gen đều xuất tiếng Anh (biến EN `UPPER_SNAKE`)
- `work/` chỉ commit cấu trúc (`README.md` + `INDEX.md`); sản phẩm + key vào `.local/work/` (gitignored)
- Mỗi raw có nguồn + URL + ngày thu thập

## `modules/` — cách dùng

`.context/modules/` giữ invariant **theo module** (schema digest riêng ảnh/video, quy tắc template). Không duplicate schema đã có trong digest mẫu — module chỉ ghi delta/quyết định ngắn.
