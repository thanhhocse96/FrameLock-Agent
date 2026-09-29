# Soul 2 — text-to-image (qua Higgsfield API)

> Doc kỹ thuật commit được (không chứa key). Key chỉ đọc từ env — xem `../README.md`.
> Nguồn: `https://dash.higgsfield.ai/models/higgsfield-ai/soul/v2/standard/llms.txt` + model page `https://console.higgsfield.ai/models/higgsfield-ai/soul/v2/standard` (truy cập 2026-09-28).

## Thông số

| Mục | Giá trị |
|-----|---------|
| Model ID | `higgsfield-ai/soul/v2/standard` |
| Endpoint | `https://api.higgsfield.ai/higgsfield-ai/soul/v2/standard` |
| Category / Kind | `text2image` / `inference` |
| Vai trò trong repo | Sinh **keyframes** cho clip MiniMax H3 (ảnh → `image_url`/`end_image_url`) |
| Pricing | Không có giá công khai tại thời điểm ghi |

## Tham số

| Param | Type | Bắt buộc | Default | Ràng buộc |
|-------|------|-----------|---------|-----------|
| `prompt` | string | Có | — | **viết tiếng Anh** |
| `seed` | integer | Không | `null` | 1–1000000; cố định seed để tái lập keyframe |
| `style_id` | string (uuid) | Không | — | Soul Style (lấy từ catalog, không hardcode bừa) |
| `batch_size` | integer | Không | `1` | `1` hoặc `4` (dùng `4` khi cần nhiều option keyframe) |
| `resolution` | string | Không | `"720p"` | `720p`, `1080p` (dùng `1080p` cho keyframe) |
| `aspect_ratio` | string | Không | `"4:3"` | `9:16`, `16:9`, `4:3`, `3:4`, `1:1`, `2:3`, `3:2` — keyframe cho video dùng `16:9` |
| `enhance_prompt` | boolean | Không | `true` | Giữ `true` trừ khi prompt đã chốt từng chữ |

Ví dụ `params.json` đầy đủ: xem `soul-v2.params.example.json` cùng thư mục.
Script repo: `../run_soul_v2.py` (stdlib, đọc `HF_KEY`, poll tự động, tải ảnh về `.local/`).

## Giới hạn quan trọng cho case keyframe

- Biến thể `standard` này là **text-to-image thuần, không nhận ảnh reference** — giữ sản phẩm/nhân vật đồng nhất giữa các keyframe phải dựa vào: prompt tả chi tiết visual neo (màu, chất liệu, bố cục) + **cùng `seed`** + `batch_size: 4` để chọn. Không kỳ vọng neo cứng như model multi-reference.
- Keyframe cho MiniMax H3: gen `16:9` + `1080p`; ảnh thật của user (cá tươi, nồi đất) vẫn là neo mạnh nhất — Soul chỉ sinh các keyframe còn thiếu (K2, K4, K5, K6).

## Ánh xạ với quy ước repo

- Prompt trong `params.json`/`input.md` **tiếng Anh** (invariant D-003).
- `params.json` mỗi experiment thêm: `prompt_source` (template/digest đã fill), `keyframe` (K1–K6, shot nào).
- Keyframe duyệt OK → làm `image_url`/`end_image_url` cho clip MiniMax H3; không trỏ digest trực tiếp vào `.local/`.
