# PITFALLS — bẫy đã biết

> Đọc trước khi ghi raw/digest/mapping/template.

| # | Bẫy | Cách tránh |
|---|-----|------------|
| 1 | Copy prompt thiếu nguồn/URL/ngày → digest mồ côi, dính bản quyền | Raw template bắt buộc 3 field nguồn ở đầu file |
| 2 | Sửa file raw sau khi digest đã trỏ → link `../raws/<file>#<đoạn>` gãy | Raw bất biến; lỗi copy → file mới `*_v2.md` |
| 3 | Digest bịa kỹ thuật không có trong raw | Mọi nhận định kèm `Nguồn:`; không suy diễn model nếu raw không nói |
| 4 | Quên thêm dòng mapping → digest "vô hình" | Self-check `AGENTS.md` §5: ghi digest xong thêm mapping ngay |
| 5 | Tìm digest bằng glob thay vì mapping | Mapping là SoT; glob chỉ khi audit toàn kho |
| 6 | Template chưa test đã merge | Template mới giữ `templates/drafts/`; merge khi fill được từ ≥1 digest thật |
| 7 | Nhét ảnh/video binary vào `raws/` | Chỉ text; media → `.local/` (gitignored) |
| 8 | File tiếng Việt lỗi encoding trên PowerShell | Mọi file text UTF-8 không BOM |
| 9 | Paste API key vào `work/`/`research/`/`templates/` | Key chỉ từ env hoặc `.local/work/<provider>/.env` (gitignored); review diff trước commit |
| 10 | Commit media/log/output vào `work/` | `work/` chỉ `README.md` + `INDEX.md`; sản phẩm → `.local/work/<provider>/<slug>/` (đã có guard trong `.gitignore`) |
| 11 | Digest trỏ thẳng vào `.local/work/` (link local, người khác không mở được) | Promote: copy prompt vào `research/*/raws/` (ghi nguồn experiment) rồi mới digest |
| 12 | Experiment thiếu `params.json` (model/seed/size) → không tái lập được | Schema tối thiểu: model+version, prompt_source, seed, size, duration_sec (`workflows/higgsfield/README.md`) |
| 13 | Prompt motion dính từ mạnh (`slams`, `burst`) → cờ `nsfw`, mất request | Viết mềm (`pours`, `mist`, `settle`); tra `docs/nsfw-filter-words.md` trước khi gen; bị cờ thì đổi từ rồi mới chạy lại |
