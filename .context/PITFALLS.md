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
| 7 | Nhét ảnh binary vào `raws/` | Chỉ text; media mẫu → `.local/` (gitignored) |
| 8 | File tiếng Việt lỗi encoding trên PowerShell | Mọi file text UTF-8 không BOM |
