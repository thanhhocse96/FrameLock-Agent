# Retro — study sinh ảnh demo vít chữ T TOTAL

## Bối cảnh

Study **sinh ảnh tĩnh** người đàn ông dùng dụng cụ TOTAL để lắp bàn gỗ; không phải nghiên cứu video và không áp dụng nghĩa vụ first/last-frame. Ngày tổng kết: 2026-10-12.

Nguồn: tài liệu case và draft workflow do user cung cấp tại `.local/draft/`. Đã đọc báo cáo, chưa trực tiếp xem ảnh sản phẩm/reference/output gốc. Báo cáo ban đầu ghi ảnh đạt spec; nhận xét cuối của user trong chat này cập nhật rằng **vẫn mắc những lỗi cũ về tư thế tay**, nhưng **coi như hoàn thành, tạm ổn**. Giữ lịch sử báo cáo và feedback mới riêng; không gọi lỗi grip là đã được sửa.

## Việc đã làm

- Đọc case để tách kinh nghiệm ảnh khỏi phần video và các quy tắc video chưa kiểm chứng.
- Phân tích spec/count, hình học sản phẩm, extend/bit, grip, logo, contact và background; phân biệt báo cáo acceptance với bằng chứng quan sát trực tiếp.
- Viết prompt EN cho product anchor, scene đầy đủ, detail grip/contact và edit tối thiểu; đề xuất phép so crop context, reference roles, spatial grouping, product anchor, contact block và edit/regen.
- Lưu study nháp có cấu trúc tại [analysis.md](../.local/draft/total-screwdriver-image-study/analysis.md) và [prompts.md](../.local/draft/total-screwdriver-image-study/prompts.md). Link `.local/` chỉ dùng trên máy có artifact, không bảo đảm có ở checkout khác.

## Pitfall và kinh nghiệm để dùng lại

| Vấn đề | Kinh nghiệm / giới hạn bằng chứng |
|---|---|
| Tư thế tay vẫn sai theo user | Grip là lỗi tồn đọng. Prompt chi tiết, reference sản phẩm và scene đẹp chưa chứng minh cách cầm đúng; cần đối chiếu riêng với ảnh grip được user duyệt |
| Grip đúng nhưng mất ngữ cảnh trong báo cáo cũ | Phân vai reference là hướng cần giữ: source nào quyết định sản phẩm, grip, bố cục và background. Chưa có A/B mới để chứng minh tác dụng độc lập |
| Crop rộng được báo tốt hơn crop hẹp | Giữ ngữ cảnh nhận diện, nhưng không biến 42px/360px thành ngưỡng chung; chất lượng/detail và context có thể thay đổi đồng thời |
| Count, logo và contact dễ bị đánh giá chung là “ảnh đẹp” | Kiểm tra từng mục riêng. Overview giúp đếm vật; detail giúp xem ngón tay, branding và bit seated; không suy ra cả scene đạt chỉ từ một crop |
| Từ một case suy ra model không đếm/không có prior | Chỉ lưu triệu chứng và giả thuyết có phạm vi. Chưa biết model/settings/ảnh từng run nên không kết luận nguyên nhân kiến trúc |
| Viết prompt để “có bằng chứng” | Prompt tạo kế hoạch thử; bằng chứng cần output/ref và run thực. Không ghi test đã pass chỉ vì prompt đã viết |

Khi mở lại case trong tương lai, ưu tiên xác định **điểm grip lệch cụ thể** bằng ảnh thật và output: hướng ôm, vị trí ngón cái, các ngón quanh handle và quan hệ tay–tool. Đây là hướng chưa thực hiện trong lượt tổng kết; không tự đặt ngưỡng sai lệch hay tự thêm spec cơ học mới.

## Kết quả và quyết định user

- **Acceptance user:** hoàn thành ở mức tạm ổn, có lỗi tư thế tay còn tồn tại; nguồn là nhận xét trực tiếp của user, không phải AI đã xem ảnh.
- **Technical status:** chưa xác minh trực tiếp output; chưa có dữ liệu model/provider/settings/seed/job/usage của các lần sinh được user đánh giá. Không ghi strict pass, tỷ lệ thành công hoặc lỗi đã được giải quyết.
- **Kế hoạch A/B mới:** chỉ là đề xuất, chưa chạy trong chat này. Không đồng nhất nhận xét user với kết quả từng test T1–T6.
- **Quyết định:** đóng study theo user; không chạy thêm, không promote draft skill hoặc prompt thành workflow/template đạt trong lượt này. Phân tích/spec/checklist và kinh nghiệm fail có thể tham chiếu cho công việc Business tương lai.

## Chi phí

Agent không submit generation ảnh cho study này trong chat hiện tại. Chi phí các lần sinh mà user đang nhận xét **chưa có dữ liệu**, không ghi bằng 0 và không cộng vào ba run video Husband đã tổng kết riêng.

Không sửa case nguồn, raw, digest/mapping ảnh hoặc governance trong lượt ghi journal này.
