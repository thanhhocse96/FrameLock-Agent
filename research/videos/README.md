# Research video và Delta Analysis

Ngày mở lại phạm vi: 2026-10-12. User cho phép research video và Delta Analysis sau quyết định compact D-010; hiện giới hạn quy trình bắt buộc ở **chuỗi sinh có cả first/last frame làm conditioning** (AGENTS.md §7). Đã thực hiện ba run DA-005 theo yêu cầu user bằng script local; không khôi phục runner/API vào workflows. User đã dừng thử DA-005.

Mục tiêu: từ hai ảnh khác nhau ở một chi tiết, xác định chuyển động nối hợp lý; từ video lỗi hoặc mô tả của user, so với spec để đề xuất chỉnh sửa có căn cứ trong kinh nghiệm dự án.

- [Index video](INDEX.md): điểm tra cứu chung cho case mới và hồ sơ legacy.
- [Quy trình phân tích](delta-analysis/protocol.md): input, so sánh, truy xuất kinh nghiệm, prompt và kiểm chứng.
- [Research nền tảng](delta-analysis/research-notes.md): nguồn chính thức và giới hạn chuyển giao giữa model.

Case production được lưu riêng với raw/digest influencer: case chứa spec, quan sát, thử nghiệm và kết quả; không gọi journal là raw prompt. Pipeline ảnh và mapping ảnh giữ nguyên. Khi thu thập prompt influencer video, cần raw nguyên văn có nguồn + URL + ngày và schema digest được duyệt trước khi ghi.

Media, frame trích, output và log dài đặt tại `.local/` (gitignored); index chỉ giữ đường dẫn, không chứa binary hay key. Phân tích tiếng Việt; prompt đề xuất tiếng Anh. Prompt minh họa chưa thử không được promote thành template đã kiểm chứng.

## Layout cho case mới — user duyệt 2026-10-12

```text
research/videos/
  INDEX.md
  methods/<method-slug>.md
  cases/<case-slug>/
    case.md
    runs/<run-id>.md

.local/video-runs/<case-slug>/<run-id>/
  ...
```

- `case.md`: brief, mục đích Business (chưa rõ thì ghi chưa rõ), spec/acceptance, thứ tự và cặp frame đầu/cuối mỗi đoạn, liên kết lịch sử run, tổng kết, điều chưa thử và trạng thái dừng/promote.
- `runs/<run-id>.md`: ID/ngày/đoạn; input và vai trò conditioning; prompt EN; model/provider/mode/settings; delta và biến đổi; job ID/trạng thái; phí thực/chưa rõ; quan sát có timestamp và provenance; feedback user; verdict và đường dẫn artifact local. Ghi cả lần fail/blocked/cancelled.
- `methods/`: chỉ phương pháp dùng chung mới. Hồ sơ/phương pháp cũ trong `delta-analysis/` và journal giữ nguyên, index chung trỏ trực tiếp tới nguồn. Index legacy là snapshot lịch sử, không thêm case mới ở đó.
- Một case cho một chuỗi/mục đích, không tách theo từng retry. Slug kebab-case; run có thứ tự như `001-baseline`, `002-morph`; không tạo scaffold rỗng. Case mới dùng artifact layout mới, không di chuyển `.local/work/` cũ.

Workflow Business chỉ lấy phần có bằng chứng phù hợp với mục đích/acceptance và nêu case nguồn, phạm vi, hạn chế. Kinh nghiệm fail có thể thành quy tắc tránh lỗi hoặc phân tích; không gọi prompt fail là template đạt. Chi tiết áp dụng: AGENTS.md §7 và skill `video-delta-analysis`.
