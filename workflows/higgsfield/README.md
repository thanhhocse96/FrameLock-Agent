# workflows/higgsfield — chạy thử Higgsfield AI (platform dir, nơi duy nhất)

> Version: 1.2.2 (2026-09-30) · Skill điều phối: `skills/higgsfield-run/SKILL.md`
> Changelog: 1.1.0 — move script từ `work/higgsfield/*.py` · 1.2.0 — gộp toàn bộ `work/higgsfield/` (docs + `models/` + `INDEX.md`) vào đây, xóa `work/` · 1.2.1 — thêm mục báo cáo chi phí `/usage` → `analytics-models-db.csv` · 1.2.2 — ghi chú dữ liệu chi tiết nằm offline trong `.local`.

## ⚠️ Chạy trên WSL (Debian), không chạy Python Windows

Máy này không có Python Windows thật (chỉ stub). Mọi script chạy qua WSL từ repo root:

```powershell
wsl -d Debian -- python3 workflows/higgsfield/run_minimax_h3.py --params <params.json> --outdir .local/work/higgsfield/<YYYY-MM-DD-slug>
```

Venv/key/toolchain chi tiết (machine-local): `.local/ENVIRONMENT.md`.
Key chỉ từ env (`HF_KEY`, `HF_CREDENTIALS`) — cấm paste key vào repo.

## Scripts

| Script | Model / việc | Version |
|--------|--------------|---------|
| `run_minimax_h3.py` | MiniMax H3 text/image-to-video (2K, 5–15s) | 1.2.0 |
| `run_soul_v2.py` | Soul 2 text-to-image (keyframes) | 1.2.0 |
| `run_grok_imagine_20.py` | Grok Imagine 2.0 edit + text-to-image (giữ ref) | 1.2.0 |
| `run_marketing_studio_image.py` | Marketing Studio image (campaign edit, giữ ref) | 1.2.0 |
| `upload_asset.py` | Upload asset lấy URL ref | 1.2.0 |

## Models đã setup

| Model | Doc | Params mẫu | Script |
|-------|-----|------------|--------|
| MiniMax H3 (`minimax/h3/text-to-video`, 2K, 5–15s) | `models/minimax-h3.md` | `models/minimax-h3.params.example.json` | `run_minimax_h3.py` |
| Soul 2 (`higgsfield-ai/soul/v2/standard`, text-to-image, keyframes) | `models/soul-v2.md` | `models/soul-v2.params.example.json` | `run_soul_v2.py` |
| Grok Imagine 2.0 (`xai/grok-imagine-image-2.0`, edit + text-to-image, giữ ref) | `models/grok-imagine-2.0.md` | `models/grok-imagine-2.0.params.example.json` | `run_grok_imagine_20.py` |
| Marketing Studio Image (`marketing-studio/image`, campaign edit, giữ ref) | `models/marketing-studio-image.md` | `models/marketing-studio-image.params.example.json` | `run_marketing_studio_image.py` |

## Tài liệu vận hành (không phải model)

| Doc | Dùng khi |
|-----|----------|
| `models/genjutsu-control.md` | Playbook control Genjutsu motion-transfer: audit ref + video nguồn, thang test rẻ→đắt, triage morph, stop-loss 3 gen |

## Setup (1 lần, machine-local)

1. Tạo API key trên dashboard Higgsfield, **không paste key vào repo**.
2. Đặt key vào biến môi trường (theo doc chính thức):
   ```powershell
   $env:HF_KEY = "KEY_ID:KEY_SECRET"          # Python + cURL (script dùng biến này)
   $env:HF_CREDENTIALS = "KEY_ID:KEY_SECRET"  # TypeScript SDK
   ```
   Hoặc ghi vào `.local/work/higgsfield/.env` (gitignored) rồi load thủ công.
3. (Tùy chọn) `pip install higgsfield-client` nếu muốn dùng SDK thay cho script stdlib.

## Workflow mỗi experiment

0. Khi user yêu cầu clip/ảnh mới, **trả lời kịch bản sơ lược trước khi chạy** (chuỗi mốc, đường đi, ràng buộc cần giữ) để user duyệt — user chốt mới chạy (quy tắc từ 2026-09-29).
1. Chọn template nguồn từ `templates/Index.md` (prompt EN) → fill biến.
2. Copy `models/minimax-h3.params.example.json` thành params thật, chạy script **trên WSL** (lệnh ở đầu file).
   Script tự ghi `input.md` + `params.json` + `run.log` vào outdir, tải video vào `output/`.
3. Gọi API (đường script), lưu media vào `output/`, log vào `run.log`.
   Đường MCP thay thế: đã cấu hình project-scope trong `../../opencode.json`
   (`higgsfield` → `https://mcp.higgsfield.ai/mcp`); sau khi restart opencode chạy
   `opencode mcp auth higgsfield` để OAuth bằng tài khoản Higgsfield (không cần key).
   Dùng MCP khi cần `create_character`/Soul ID hoặc lục history — gen thường vẫn dùng script.
4. Viết `result.md` (tiếng Việt): đạt/không đạt, so với digest nào, có promote lên `research/` không.
5. Thêm 1 dòng vào `INDEX.md` — **không commit media, chỉ commit dòng index**.

## Quy tắc tiết kiệm cost (user chốt 2026-09-29)

- Marketing Studio image: test nháp `1k` + `medium` (`models/marketing-studio-image.params.test.json`), chốt mới `2k` + `high`.
- MS không có giá công khai (~$0.24/ảnh 2k-high); mỗi làm lại tính tiền đủ nên brief-trước-chạy (bước 0).

## Báo cáo chi phí từ /usage → DB tổng (user chốt 2026-09-30)

Mục tiêu: user export report để soi model/prompt nào tốn tiền → tăng cường cách viết prompt. Không bắt buộc mỗi lần chạy, làm theo kỳ (tháng).

1. Login `https://open.higgsfield.ai/usage` → chọn kỳ (vd 2026-09-01–2026-09-30) → export CSV (`analytics-models-<from>-<to>.csv`). Trang bắt login nên không fetch tự động được — làm tay.
2. Append 1 snapshot vào `journal/analytics-models-db.csv`: mỗi model 1 dòng, `snapshot_date` = ngày export (vd 2026-09-30). Dòng nào không tính vào project (vd Genjutsu clip ref dài) đánh `included_in_project_analysis=FALSE` + ghi rõ `exclude_reason`.
3. Công thức tính lại (loại dòng excluded): `project_total_usd` = tổng `spend_usd` còn lại; `share_recalc_pct` = `spend_usd / project_total_usd * 100`; `per_req_usd` = `spend_usd / total_requests`. Kỳ 09/2026 mẫu: project 33.02 USD / 94 reqs — MiniMax H3 I2V 53.5%, Marketing Studio 39.4%.
4. Ngưỡng review prompt (tham khảo, không cứng): MiniMax I2V >50% tổng → xem lại số clip/độ dài/duration; Marketing Studio retry nhiều → brief kỹ + test `1k/medium` trước; model nào `per_req_usd` cao bất thường → kiểm tra ref dài/fail NSFW.
5. Insight rút ra (cách viết prompt tốt hơn) ghi vào `journal/YYYY-MM-DD-<slug>.md` mục Chi phí; luật lâu dài → promote vào `.context/PITFALLS.md` hoặc template.

> Lưu ý: dữ liệu chi tiết từng lần chạy luôn offline — nằm rải trong `.local/work/higgsfield/<slug>/output/` của từng session (gitignored, không lên remote), nên hơi khó xài khi cần đối chiếu ngược bill với từng lần gen. CSV từ `/usage` chỉ cho tổng theo model/kỳ; muốn biết prompt/params nào tốn bao nhiêu thì đối chiếu thêm từng dòng `INDEX.md` + `params.json` tương ứng.

## Schema `params.json` (MiniMax H3)

`prompt` (EN, bắt buộc) + `duration` 5–15 + `resolution` chỉ `2K` + `aspect_ratio` (`auto`, `adaptive`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`) + `aigc_watermark`. Thêm `prompt_source` (template/digest đã fill) để truy vết. Không có `seed`.

---

Index experiment: `INDEX.md` (1 dòng/lần chạy). Sản phẩm mỗi lần chạy → `.local/work/higgsfield/<slug>/` (gitignored).
