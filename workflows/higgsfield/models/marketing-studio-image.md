# Marketing Studio Image — campaign image gen/edit (qua Higgsfield API)

> Doc kỹ thuật commit được (không chứa key). Key chỉ đọc từ env — xem `../README.md`.
> Nguồn: `https://dash.higgsfield.ai/models/marketing-studio/image/llms.txt` + model page `https://console.higgsfield.ai/models/marketing-studio/image` (user cung cấp 2026-09-28).

## Thông số

| Mục | Giá trị |
|-----|---------|
| Model ID | `marketing-studio/image` |
| Endpoint | `https://api.higgsfield.ai/marketing-studio/image` |
| Category | `image_edit`, `text2image` |
| Vai trò trong repo | **Ứng viên edit keyframe có ref** (so với Grok): giữ bố cục + sản phẩm xuyên chuỗi lùi |
| Pricing | Không có giá công khai tại thời điểm ghi |

## Tham số (direct mode — `enhance_prompt: false`, không cần preset)

| Param | Type | Bắt buộc | Default | Ràng buộc |
|-------|------|-----------|---------|-----------|
| `prompt` | string | Có | — | **viết tiếng Anh**; tối đa 5000 ký tự; với edit: giữ gì/đổi gì + vai trò từng ref |
| `quality` | string | Không | `"high"` | `low`, `medium`, `high` |
| `image_urls` | array[string] | Không | — | Tối đa 16 URL public HTTPS; bỏ trống = text-to-image thuần |
| `moderation` | string | Không | `"auto"` | `auto`, `low` |
| `resolution` | string | Không | `"2k"` | `1k`, `2k`, `4k` |
| `aspect_ratio` | string | Không | `"auto"` | `auto`, `1:1`, `3:2`, `2:3`, `4:3`, `3:4`, `16:9`, `9:16`, `21:9` — keyframe video dùng `16:9` |
| `enhance_prompt` | boolean | Không | `false` | `true` = preset mode (bắt buộc `preset_id` + ảnh sản phẩm, đắt hơn 10%) — chuỗi lùi dùng `false` |

Ví dụ `params.json` đầy đủ: xem `marketing-studio-image.params.example.json` cùng thư mục.
Script repo: `../run_marketing_studio_image.py` (stdlib, đọc `HF_KEY`, poll tự động, tải ảnh về `.local/`).

## So kèo với Grok (test K6-back cùng điều kiện)

- Cùng ref (K7 CDN), cùng `2k`/`16:9`, cùng prompt ý → chấm: giữ nồi/bếp, sạch người/túi/chữ.
- Grok: `quality: medium`. MS Image: `quality: high` (default).
- Con nào giữ chuỗi tốt hơn thì chốt cho cả chuỗi lùi K5 → K1.

## Ánh xạ với quy ước repo

- Prompt trong `params.json`/`input.md` **tiếng Anh** (invariant D-003).
- `params.json` mỗi experiment thêm: `prompt_source`, `keyframe`, `ref_roles`.
- Ảnh ref phải là URL public — file local upload trước qua `/files/generate-upload-url`.
