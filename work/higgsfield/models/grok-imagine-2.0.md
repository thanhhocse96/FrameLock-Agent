# Grok Imagine 2.0 — image edit + text-to-image (qua Higgsfield API)

> Doc kỹ thuật commit được (không chứa key). Key chỉ đọc từ env — xem `../README.md`.
> Nguồn: `https://dash.higgsfield.ai/models/xai/grok-imagine-image-2.0/llms.txt` + model page `https://console.higgsfield.ai/models/xai/grok-imagine-image-2.0` (user cung cấp 2026-09-28).

## Thông số

| Mục | Giá trị |
|-----|---------|
| Model ID | `xai/grok-imagine-image-2.0` |
| Endpoint | `https://api.higgsfield.ai/xai/grok-imagine-image-2.0` |
| Category | `image_edit`, `text2image` |
| Vai trò trong repo | **Edit keyframe có ảnh ref** (giữ bố cục + chi tiết): K7 composite, fix túi/chữ |
| Pricing | Không có giá công khai tại thời điểm ghi |

## Tham số

| Param | Type | Bắt buộc | Default | Ràng buộc |
|-------|------|-----------|---------|-----------|
| `prompt` | string | Có | — | **viết tiếng Anh**; với edit: instruction giữ gì/đổi gì + vai trò từng ref |
| `quality` | string | Không | `"medium"` | `low`, `medium` |
| `image_urls` | array[string] | Không | — | Tối đa 10 URL public HTTPS (upload trước qua `/files/generate-upload-url`) |
| `resolution` | string | Không | `"1k"` | `1k`, `2k` (keyframe chốt dùng `2k`) |
| `aspect_ratio` | string | Không | `"auto"` | `auto`, `1:1`, `1:2`, `2:1`, `3:2`, `2:3`, `4:3`, `3:4`, `16:9`, `9:16` — keyframe video dùng `16:9` |

Ví dụ `params.json` đầy đủ: xem `grok-imagine-2.0.params.example.json` cùng thư mục.
Script repo: `../run_grok_imagine_20.py` (stdlib, đọc `HF_KEY`, poll tự động, tải ảnh về `.local/`).

## Quy ước ref cho K7 (ghi vào prompt)

- Ref 1 (composite tròn): giữ nguyên bố cục — chị áo navy bưng nồi đất ở giữa-phải, túi dựng bên trái, bếp sáng.
- Ref 2 (túi thật): giữ nguyên bao bì, logo SK, chữ `CÁ ĐỤC KHO TIÊU`, màu xanh dương.
- Output: khung 16:9 sạch (không viền đen, không crop tròn), túi trái — nồi giữa — chị sau.

## Ánh xạ với quy ước repo

- Prompt trong `params.json`/`input.md` **tiếng Anh** (invariant D-003).
- `params.json` mỗi experiment thêm: `prompt_source`, `keyframe`, `ref_roles` (vai trò từng ref).
- Ảnh ref phải là URL public — file local upload trước qua presigned URL, **không** gửi key vào URL storage.
