---
name: write-video-script
description: Viết hoặc phản biện kịch bản video kể chuyện và B2B, chuyển brief thành cảnh và beat có động cơ để bàn giao chỉ đạo diễn xuất. Dùng khi cần xây câu chuyện hoặc sửa logic cảnh, không tự kích hoạt cho việc chỉ sửa prompt kỹ thuật.
metadata:
  version: "0.1.0"
  updated: "2026-10-28"
  status: "draft"
---

# Viết kịch bản video

Bản nháp từ nghiên cứu Foyege, chưa kiểm chứng bằng production. Đường dẫn dưới đây tính từ root AI-GAN, dùng được cả khi đọc skill mirror. Canonical: `skills/write-video-script/SKILL.md`.

## Brief và quyết định nội dung

Xác định người xem, điều họ cần hiểu/tin/làm, thời lượng/kênh, tone và dữ kiện/asset đã có. Với B2B, phân biệt thông điệp muốn truyền với bằng chứng doanh nghiệp cung cấp; không tự bịa claim, con số hay chứng nhận. Dùng ngữ cảnh đã chốt, chỉ hỏi thiếu sót ảnh hưởng lựa chọn câu chuyện; bài thử giả định phải ghi rõ.

Chọn hình thức phù hợp: câu chuyện có người, demonstration, giải thích hoặc kết hợp. Không ép demo thành drama. Với cảnh có người, làm rõ mục tiêu trước mắt, trở lực, lựa chọn và hệ quả. Sự thay đổi có thể là thông tin, quyết định hoặc quan hệ, không nhất thiết mỗi cảnh một cảm xúc. Cho nhân vật phản ứng vì một sự kiện, tránh xâu những hình ảnh đẹp không có quan hệ nhân quả.

Khi cần subtext, phân biệt điều nhân vật muốn, điều họ thể hiện và điều họ che giấu. Không mặc định tsundere, ánh mắt lạnh, cliffhanger hoặc một công thức năm nhịp. Dùng cảnh tham khảo để tìm chức năng kể chuyện, không lấy phong cách diễn của một nhân vật áp cho mọi vai.

## Bàn giao có thể diễn được

Viết kịch bản với beat ID ổn định. Mỗi beat quan trọng cần đủ: tác nhân kích hoạt → hành động có mục đích → trạng thái trước/sau → điều khán giả cần đọc. Thêm subtext khi có; không điền trường vô nghĩa cho shot sản phẩm.

Shot/camera/âm thanh chỉ chi tiết đến mức giúp đọc ý đồ và dựng được. Timing là dự kiến biên tập, ghi riêng duration generation chưa biết. Không buộc một beat/giây; một shot có thể mang nhiều hành động nếu vẫn đọc rõ. Lựa chọn cut/hold/montage theo điều khán giả cần theo dõi. Với reveal, ghi điều khán giả đã biết, điều còn bị che và sự kiện cho phép tiết lộ; không chỉ liệt kê timestamp. Khi vật hoặc môi trường đổi trạng thái, giữ dấu thay đổi xuyên shot trừ khi kịch bản chủ ý reset.

Đánh dấu phần bắt buộc giữ (sự kiện, claim đã duyệt, continuity, thông tin sản phẩm), phần diễn viên/model có thể biến tấu và khó khăn sản xuất có thể đổi cách kể. Khi giảm độ khó kỹ thuật, giữ chức năng của beat; không tự bỏ quyết định quan trọng chỉ để clip dễ sinh.

Đầu ra tùy quy mô: brief ngắn, kịch bản/beat có thời lượng dự kiến, bàn giao diễn xuất, tiêu chí nghiệm thu và điều chưa biết. Phân tích/hướng dẫn bằng tiếng Việt; prompt generation nếu được yêu cầu bằng tiếng Anh. Không tự thêm generation vào nhiệm vụ viết kịch bản.

## Phản biện và kiểm tra

- Bỏ beat này thì người xem mất thông tin, lựa chọn hay hệ quả gì? Nếu không mất gì, cân nhắc bỏ hoặc gộp, không bắt buộc mọi shot phải làm cảm xúc đổi.
- Người xem có đủ thông tin để hiểu tác nhân trước phản ứng? Product proof đến từ asset/quy trình thật hay chỉ là hình ảnh gợi cảm giác đáng tin?
- Đích nhìn, vị trí, đồ vật và trạng thái có nối được giữa shot? Chi tiết diễn xuất có đang mâu thuẫn ý đồ?
- Với B2B, chốt phần cần khách hàng xác nhận và phạm vi sửa; không tự coi bản nháp là approved. Chỉ đề xuất KPI khi chưa có, không trình như dữ liệu thực.

Khi cần chuyển beat thành hành vi/prompt, dùng `direct-ai-performance` nếu có; bàn giao vẫn phải tự đọc được không phụ thuộc skill đó. Khi user nhắc Foyege hoặc cần căn cứ của các lựa chọn, tra `research/videos/INDEX.md` → `research/videos/foyege/foyege-evidence-digest.md` (F04, cảnh thử và giới hạn). Không nhận prompt tái tạo là raw, không nhận phân tích Draconia là workflow đã xác minh.
