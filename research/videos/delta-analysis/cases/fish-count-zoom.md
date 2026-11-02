# DA-004 — một miếng cá → ba miếng cá, đồng thời zoom in

- Ngày: 2026-10-12.
- Nguồn: ví dụ user mô tả trong chat AI-GAN: “ảnh đầu trong chảo có 1 miếng cá, ảnh sau zoom in có 3 miếng cá”.
- Bằng chứng: `user-reported`; chưa có hai ảnh, video, prompt hoặc settings của run cụ thể. Đây là case thiết kế, chưa phải lỗi generation đã quan sát.
- Phương pháp: [protocol v0.2](../protocol.md), tham khảo State Delta của ui-debug.

## Clues và states

START: thấy một miếng cá trong chảo. END: thấy ba miếng cá và framing được user gọi là zoom in. Chưa biết START có thấy toàn lòng chảo không, hai miếng còn lại có bị che không, vị trí/identity/trạng thái cá có khớp không. Cũng chưa biết spec muốn thêm cá, reveal cá có sẵn hay chỉ muốn zoom.

| Trục | Delta theo mô tả | Điều chưa thể kết luận |
|---|---|---|
| Environment | Chưa rõ | Không chọn model mặc định từ journal |
| Time | Đầu → cuối | Hai miếng mới nhìn thấy xuất hiện lúc nào, bằng cách nào |
| Layer | Hai keyframe được mô tả khác count/framing | Lỗi input, thiếu prompt hay lỗi output |
| Scope | Cá và cỡ cảnh | Có delta phụ ở chảo, tay, ánh sáng hay góc không |
| Data/State | Số cá nhìn thấy 1 → 3 | Số cá thực trong scene hay chỉ visibility thay đổi |

## DIFF và phương án có điều kiện

| Spec / giả thuyết | Cách kiểm tra | Can thiệp phù hợp | Giới hạn |
|---|---|---|---|
| Chỉ muốn zoom; count lệch là ngoài ý muốn | User xác nhận count phải giữ; so identity/vị trí trong hai ảnh | Sửa keyframe để count khớp rồi thử camera-only | Chưa biết cần sửa đầu thành ba hay cuối thành một nếu chưa chốt count |
| Chủ ý thêm hai miếng | Spec xác nhận thao tác thêm; ảnh đầu không chứa đủ ba miếng | Thử prompt có đường vào/contact/đặt hai miếng; giữ hai ảnh nếu bridge khả thi | Chưa có dữ liệu để kết luận prompt-only đủ |
| Chủ ý thêm cá nhưng thêm + zoom gây lỗi phối hợp | Video cho thấy lỗi bắt đầu khi hai hành động chồng nhau, hoặc phép thử tách cho kết quả tốt hơn | Thêm B: ba miếng, giữ framing A; A→B đặt cá, B→END camera-only | B giúp tách nhiệm vụ, không chứng minh A→B hết morph; có thể cần dựng hai clip |
| Hai miếng đã có nhưng bị che | Xác minh ảnh/geometry và đường camera/occluder | Prompt reveal đúng vật che hoặc đường camera | Zoom thuần không tự giải thích reveal; không tự bịa hai miếng ngoài khung |
| Spec cho phép bỏ qua thao tác thêm | User cho phép time jump/cut | Dựng cắt giữa hai cảnh | Không phù hợp spec yêu cầu một shot liên tục |

Khuyến nghị trước trong chat “ưu tiên thêm ảnh B” là phương án có điều kiện, chưa phải fix đã chứng minh. Theo State Delta, phải xác định ý nghĩa count change và lỗi thực trước khi chọn prompt-only hay keyframe trung gian.

## ISOLATE → PROVE cho giả thuyết thêm cá

1. Baseline: giữ hai ảnh, model/mode/settings và prompt run lỗi nếu có. Ghi lỗi tại count/contact/framing, không chỉ endpoint.
2. Candidate 1: chỉ thay prompt về đường vào và thứ tự đặt cá → zoom; giữ input/settings. Kiểm tra giả thuyết thiếu cầu nối hành động.
3. Nếu vẫn fail, dùng bằng chứng để chọn bước tiếp. Candidate 2 có thể tách bằng B cùng framing A; đây là thay đổi cấu trúc/input, phải ghi riêng, không so như một thay đổi câu prompt đơn thuần. Nếu cần baseline công bằng, ghi khác biệt duration/số clip/budget.
4. Pass theo spec thêm cá: count nhìn thấy đi 1→2→3 qua thao tác đặt, mỗi miếng có identity liên tục, tiếp xúc dụng cụ/chảo hợp lý, camera đúng đường, endpoint đúng và không cut/fade nếu bị cấm. Đánh dấu đoạn bị che không quan sát được; không suy ra count/shape lúc đó được bảo toàn.

Hiện chưa chạy baseline/candidate; mọi can thiệp ở trên là `proposed-unverified`. Không có kết luận tỷ lệ thành công hoặc template đã test.
