# Case seed từ journal dự án

Ngày nhập index: 2026-10-12. Các case sau được đọc từ journal, chưa mở media/log local trong phiên này. Không phục dựng prompt gốc, timestamp, settings hoặc run ID còn thiếu. Các câu kết luận mạnh trong journal được giới hạn về đúng tập thử lịch sử.

<a id="da-001"></a>
## DA-001 — morph chai và dĩa khi nhiều trạng thái đổi

- Model/mode: MiniMax H3 image-to-video kẹp hai đầu, theo journal; version/provider cụ thể của từng run chưa xác minh.
- Spec ghi nhận: chuỗi cá đục kho tiêu, đồ bay/rót vào nồi; không méo hình giữa clip.
- Delta: chai đứng → nghiêng; đồ nằm → bay; dĩa → nồi. Không phải một delta đơn giản.
- Lỗi: clip K1→K2 đầu bị morph/méo hình.
- Can thiệp được ghi: tách thành bay lên, rót/lốc, hũ trong bọt, dĩa/nồi với dòng chảy làm neo. Ở clip 2v2, sốt đặc đục che cá tới khi cá nằm trong nồi.
- Bằng chứng: `journal-reported`; journal mô tả xử lý, không có số đo pass hoặc prompt trước/sau đầy đủ tại đây.
- Ứng dụng đề xuất: xét tách hành động trước khi thêm negative; che morph chỉ khi spec cho phép mất tầm nhìn. Không bảo đảm giữ hình học của vật bị che và không chứng minh model luôn dở mọi biến hình.
- Nguồn: [retro, mục Pitfall + cách fix và Bài học chốt](../../../../journal/2026-09-28-ca-duc-kho-tieu-retro.md); [keyframe splitting, mục 8–9](../../../../journal/2026-09-28-keyframe-splitting.md).

<a id="da-002"></a>
## DA-002 — scale và tay/vật đổi, xuất hiện fade

- Model: Kling O3 và Seedance 2.0 theo journal; version endpoint/settings đầy đủ chưa xác minh.
- Input/spec: nối cảnh bếp 2→3 kẹp hai đầu, đổi scale và tay/vật; mục tiêu chuyển liên tục.
- Quan sát được ghi: Kling O3 6s static + timestamp → fade; Seedance 2.0 6s FPV one-take, blocking mép trên, cấm fade → vẫn fade.
- Trạng thái: `journal-reported`, hai thử nghiệm được báo fail. Không suy rộng “mọi model đều fail”.
- Quyết định production được ghi: dựng cắt cho cặp multi-change; vật ra/vào qua mép khung; hành động cất dụng cụ không cần phô diễn giữa khung.
- Hướng prompt push-in/blur trong phần nguyên tắc là đề xuất, không được xem là pass chỉ vì có trong journal. “Static + khác scale fail chắc” là heuristic lịch sử, không phải định luật chung.
- Ứng dụng: kiểm tra delta phụ về scale/camera trước; nếu spec cấm cut, đề xuất sửa keyframe hoặc tách motion, không tự thay spec bằng cut.
- Nguồn: [cross-scale note, mục Kết quả test nối 2→3 và Nguyên lý ra/vào bằng mép khung](../../../../journal/2026-10-06-cross-scale-transition-note.md).

<a id="da-003"></a>
## DA-003 — cart glide chậm so với spec tua nhanh

- Model/mode: MiniMax H3 kẹp hai đầu, theo journal.
- Spec: timelapse/fast-forward giữa đông lạnh → quầy → cốp xe.
- Quan sát được ghi: `clipA-v1-v4-retry` và `clipB-v4-v5` glide mượt chậm, sai nhịp/năng lượng.
- Prompt/can thiệp đề xuất: motion tốc độ/biên độ rõ, foreground anchor, blur bridge hoặc speed-ramp, settle cuối.
- Trạng thái: lỗi `journal-reported`; fix `proposed-unverified`. Journal ghi “chưa làm”, không có run pass cho hướng sửa.
- Ứng dụng: phân biệt lỗi nhịp với lỗi shape; không coi chữ “fast” hay tăng duration tự nó chữa được. Thay một biến để kiểm tra giả thuyết; timing/model capability cần xác minh theo tool hiện dùng.
- Nguồn: [cart note, mục Yêu cầu user và Kế hoạch test](../../../../journal/2026-09-29-cart-video-timelapse-note.md).

Fragment SeedDance hourglass ở [note 2026-10-06](../../../../journal/2026-10-06-seeddance-tempo-note.md) thiếu toàn văn/nguồn/model chính xác; không dùng như prompt gốc hoàn chỉnh hay fix đã kiểm chứng. Claim “tắt audio giải phóng capacity” chưa có bằng chứng trong dữ liệu đã đọc.
