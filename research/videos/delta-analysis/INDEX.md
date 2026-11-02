# Index — research video và Delta Analysis

Đây là index cho case và research video mới, không thay thế `research/images/mapping.md`. Tra cứu qua bảng trước khi mở case. Ngày lập: 2026-10-12.

| ID | Entry | Loại / model lịch sử | Delta / lỗi | Bằng chứng |
|---|---|---|---|---|
| DA-PROTOCOL | [protocol.md](protocol.md) | Quy trình v0.2, tham khảo ui-debug | Năm trục State Delta; ISOLATE → DIFF → PROVE | Chưa validation end-to-end |
| DA-RESEARCH | [research-notes.md](research-notes.md) | Tài liệu chính thức + tổng hợp | Motion, timing, input conflict | Nguồn ngoài được dẫn riêng |
| DA-001 | [Morph chai và dĩa](cases/project-retrospectives.md#da-001) | MiniMax H3 theo journal | Pose + trạng thái + hình dạng đổi cùng lúc | Journal báo lỗi và cách xử lý; chưa xem lại media |
| DA-002 | [Nối cảnh bếp nhiều thay đổi](cases/project-retrospectives.md#da-002) | Kling O3; Seedance 2.0 theo journal | Scale + tay/vật; fade ngoài ý muốn | Journal báo hai thử nghiệm fail; chưa xem lại media |
| DA-003 | [Nhịp cart](cases/project-retrospectives.md#da-003) | MiniMax H3 theo journal | Glide chậm so với spec tua nhanh | Lỗi được ghi; prompt sửa chưa chạy |
| DA-004 | [Số cá và zoom](cases/fish-count-zoom.md) | Ví dụ user; model chưa rõ | Count 1→3 + framing; chọn prompt/keyframe theo spec | Chỉ có mô tả; chưa có video hoặc thử nghiệm |
| DA-005 | [Husband Frame 1→2](cases/husband-f1-f2-experiment.md) | Seedance 1.5 Pro; 480p 4s/10s silent | Count + sống/chín + xẻng + framing | Baseline user duyệt; morph ghép cá; 10s còn thừa miếng/vi phạm blocking; tổng $0.2184552 |
| DA-005-RETRO | [Tổng kết ba run](../../../journal/2026-10-12-video-delta-analysis-retro.md) | Kinh nghiệm fail và spec user | Hô biến, count, morph, phạm vi kết luận model | Đã dừng theo user; phương pháp promote skill 1.0.0 |

Khi thêm case, thêm một dòng tại đây với model/version/provider nếu biết, tag lỗi, nguồn, trạng thái kiểm chứng. Không suy luận provider/version còn thiếu từ tên thương mại.
