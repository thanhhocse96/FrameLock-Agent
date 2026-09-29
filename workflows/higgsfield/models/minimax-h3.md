# MiniMax H3 — text / image / reference-to-video (qua Higgsfield API)

> Doc kỹ thuật commit được (không chứa key). Key chỉ đọc từ env — xem `../README.md`.
> Nguồn: `llms.txt` các biến thể `text-to-video`, `image-to-video`, `reference-to-video` + model pages console (user cung cấp 2026-09-28).

## Thông số chung

| Mục | Giá trị |
|-----|---------|
| Category / Kind | `text2video`/`image2video` / `inference` |
| Khả năng | Video 2K, 5–15s, không audio |
| Pricing | Output 2K **$0.13/giây** (clip 5s ≈ $0.65); 5 ref đầu free, ref thứ 6+ $0.08/ref |

| Biến thể | Model ID | Endpoint |
|----------|----------|----------|
| text-to-video | `minimax/h3/text-to-video` | `https://api.higgsfield.ai/minimax/h3/text-to-video` |
| image-to-video | `minimax/h3/image-to-video` | `https://api.higgsfield.ai/minimax/h3/image-to-video` |
| reference-to-video | `minimax/h3/reference-to-video` | `https://api.higgsfield.ai/minimax/h3/reference-to-video` |

## Tham số (text-to-video)

| Param | Type | Bắt buộc | Default | Ràng buộc |
|-------|------|-----------|---------|-----------|
| `prompt` | string | Có | — | `minLength: 1`, **viết tiếng Anh** |
| `duration` | integer | Không | `5` | 5–15 (giây) |
| `resolution` | string | Không | `"2K"` | Chỉ `2K` |
| `aspect_ratio` | string | Không | `"auto"` | `auto`, `adaptive`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| `aigc_watermark` | boolean | Không | `false` | — |

Ví dụ `params.json` đầy đủ: xem `minimax-h3.params.example.json` cùng thư mục.
Script repo: `../run_minimax_h3.py --mode text-to-video|image-to-video` (stdlib, đọc `HF_KEY`, poll tự động, tải video về `.local/`).

## Tham số image-to-video (kẹp 2 đầu — dùng cho 4 clip kịch bản)

| Param | Bắt buộc | Ghi chú |
|-------|----------|---------|
| `prompt` | Có | Motion EN (diễn giữa 2 frame) |
| `image_url` | Có | Frame đầu (URL public) |
| `end_image_url` | Không | Frame cuối — **luôn dùng** để khóa bố cục |
| `duration` / `resolution` / `aspect_ratio` / `aigc_watermark` | Như text | 5–15s / chỉ `2K` / `16:9` cho kịch bản này |

## Biến thể reference-to-video (dự phòng giữ chuỗi)

Nhận `image_urls` (1–9 ref), `video_urls` (1–3), `audio_urls` (0–3): nhồi cả dải keyframe + ảnh túi/cá làm ref trong 1 request. Chưa wire vào script — chỉ dùng khi image-to-video rớt chuỗi (tốn hơn: $0.65/clip 5s + $0.08/ref từ ref thứ 6).

## Auth (server-side, không commit key)

```bash
export HF_KEY="KEY_ID:KEY_SECRET"         # Python + cURL
export HF_CREDENTIALS="KEY_ID:KEY_SECRET" # TypeScript
```

Header cho gọi HTTP trực tiếp: `Authorization: Key $HF_KEY`. SDK TypeScript chặn chạy browser.

## Gọi API

- `POST` endpoint trên → nhận `{request_id, status_url, cancel_url, status}`.
- Poll `status_url` tới trạng thái terminal: `completed` (có `video.url`) / `failed` (có `error`) / `nsfw` / `canceled`.
- Script repo: `../run_minimax_h3.py --mode text-to-video|image-to-video` (stdlib, đọc `HF_KEY`, poll tự động, tải video về `.local/`).

### cURL (tham khảo nhanh)

```bash
curl --request POST \
  --url 'https://api.higgsfield.ai/minimax/h3/text-to-video' \
  --header "Authorization: Key $HF_KEY" \
  --header "Content-Type: application/json" \
  --data @- <<'JSON'
{
  "prompt": "A cinematic scene at sunset",
  "duration": 5,
  "resolution": "2K",
  "aspect_ratio": "auto",
  "aigc_watermark": false
}
JSON
```

### Python SDK (nếu đã `pip install higgsfield-client`)

```python
import higgsfield_client

result = higgsfield_client.subscribe(
    "minimax/h3/text-to-video",
    arguments={
        "prompt": "A cinematic scene at sunset",
        "duration": 5,
        "resolution": "2K",
        "aspect_ratio": "auto",
        "aigc_watermark": False,
    },
)
print(result)
```

## Ánh xạ với quy ước repo

- Prompt trong `params.json`/`input.md` **tiếng Anh** (invariant D-003).
- `params.json` mỗi experiment thêm: `prompt_source` (template/digest đã fill), `seed` (để trống nếu API không hỗ trợ — MiniMax H3 không có param seed).
- Kết quả tốt → promote: copy prompt vào `research/videos/raws/` (ghi nguồn là experiment path) → digest (tone/shot/composition) → mapping → template.
