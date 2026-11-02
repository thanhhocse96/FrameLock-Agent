# INDEX — research video first/last-frame

Điểm tra cứu chung được user duyệt ngày 2026-10-12. Case mới theo [layout](README.md); chỉ áp dụng quy trình bắt buộc khi cả first/last frame được dùng làm conditioning. Mục tiêu: tích lũy kinh nghiệm theo chuỗi để hình thành workflow phục vụ Business khi đủ bằng chứng.

Hồ sơ cũ giữ nguyên. Các dòng legacy bên dưới chỉ trỏ tới nguồn hiện hữu, không migrate/sao chép nội dung. [Index cũ](delta-analysis/INDEX.md) là snapshot lịch sử, không là nơi ghi case mới.

## Phương pháp và research chung

Ngày 2026-10-28, user chốt thêm nghiên cứu Foyege phục vụ kịch bản, diễn xuất và ứng dụng B2B. Đây là digest tài liệu thứ cấp, không phải case generation dùng hai endpoint; không thay đổi điều kiện áp dụng quy trình first/last-frame.

| ID | Nguồn | Vai trò / trạng thái |
|---|---|---|
| DA-PROTOCOL | [State Delta v0.2](delta-analysis/protocol.md) | Phương pháp legacy; ISOLATE → DIFF → PROVE |
| DA-RESEARCH | [Research nền tảng](delta-analysis/research-notes.md) | Nguồn ngoài và giả thuyết transfer; không là run pass |
| FOYEGE-01 | [Digest bằng chứng Foyege](foyege/foyege-evidence-digest.md) | Research ưu tiên cho B2B; có text copy Appendix A/B/C do user bổ sung, tách khỏi template tái tạo; hai skill 0.1.0 nháp và bài thử văn bản; chưa xác minh workflow Draconia hoặc video output |

Method mới dùng `methods/<method-slug>.md`, tạo khi có nội dung dùng chung thực sự.

## Case và nguồn kinh nghiệm

| ID | Case / nguồn | Phạm vi / mục đích Business | Trạng thái / khả năng promote |
|---|---|---|---|
| DA-001 | [Morph chai và dĩa](delta-analysis/cases/project-retrospectives.md#da-001) | MiniMax H3, chuỗi quảng cáo cá đục theo journal | Legacy, journal-reported; chưa xem lại media trong phiên |
| DA-002 | [Nối cảnh bếp nhiều thay đổi](delta-analysis/cases/project-retrospectives.md#da-002) | Kling O3/Seedance 2.0; continuity cảnh bếp | Legacy, journal báo fail; hướng tách/dựng có phạm vi |
| DA-003 | [Nhịp cart](delta-analysis/cases/project-retrospectives.md#da-003) | MiniMax H3; tua nhanh hành trình cart | Legacy, lỗi được ghi; hướng sửa chưa thử |
| DA-004 | [Một → ba miếng cá, zoom](delta-analysis/cases/fish-count-zoom.md) | Ví dụ thiết kế; mục đích Business chưa chốt | Legacy, user-reported; chưa phải run generation |
| DA-005 | [Husband Frame 1→2](delta-analysis/cases/husband-f1-f2-experiment.md) | Seedance 1.5 Pro; stock bếp/continuity, brief Business đầy đủ chưa chốt | Đã dừng sau ba run, $0.2184552; promote phương pháp/kinh nghiệm fail, không promote prompt đạt |
| DA-005-RETRO | [Retro và quyết định user](../../journal/2026-10-12-video-delta-analysis-retro.md) | Tổng kết cùng case DA-005 | Legacy; kỹ thuật và acceptance user ghi riêng |

Thêm case mới bằng một dòng trỏ `cases/<case-slug>/case.md`. Case giữ cặp frame từng đoạn và liên kết `runs/<run-id>.md`; index tóm tắt trạng thái/mục đích/nguồn workflow, không nhân bản lịch sử run. Không thêm case chỉ để đổi prompt hay duration.
