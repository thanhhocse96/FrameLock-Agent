---
name: direct-ai-performance
description: Chuyển beat kịch bản thành chỉ đạo diễn xuất AI, eyeline, blocking, nhịp phản ứng và prompt video; phân tích diễn nhựa hoặc phản ứng không đọc được. Dùng cho cảnh có nhân vật diễn, không thay quy trình chẩn đoán mọi lỗi video hay tự cấp quyền generation.
metadata:
  version: "0.1.0"
  updated: "2026-10-28"
  status: "draft"
---

# Chỉ đạo diễn xuất AI

Bản nháp phục vụ video kể chuyện/B2B, chưa kiểm chứng bằng production. Các đường dẫn tính từ root AI-GAN, không từ thư mục mirror. Canonical: `skills/direct-ai-performance/SKILL.md`.

## Từ ý đồ đến hành vi

Nhận beat, tác nhân, mục tiêu nhân vật, trạng thái trước/sau và điều người xem cần hiểu. Nếu chỉ có yêu cầu “diễn có hồn”, suy ra một spec thử từ ngữ cảnh và ghi giả định; hỏi khi thiếu thông tin quyết định phản ứng. Không tự thay kịch bản chỉ để dễ prompt.

Chọn hành vi phục vụ mục tiêu, không dịch mỗi cảm xúc thành một kiểu cơ mặt cố định. Ghi đích nhìn cụ thể trong không gian (camera-left/right, vị trí/độ cao đối tác), hành động chính, thời điểm phản ứng tương đối với trigger, biên độ và khoảng giữ. Phân biệt phía màn hình với trái/phải của nhân vật. Nhân vật có thể phản ứng qua công việc đang làm, sự ngập ngừng, cách đáp lại đối tác hoặc posture, không nhất thiết liếc mắt/mím môi.

Tách chuyển động có chủ ý, chuyển động tự nhiên được phép và continuity bắt buộc. Không đóng băng vai, tóc, hơi thở mặc định. Mắt-trước-đầu là một phương án khi phù hợp, không quy luật; không áp mốc 0.2s hay 0.5–1s cho mọi nhân vật. Phân biệt biên độ kiềm chế với slow motion; dùng tốc độ thật nếu brief muốn tự nhiên.

Chỉ định vùng cần đọc rõ (mắt, tay, điểm tiếp xúc, sản phẩm tùy beat) và chuyển động phụ được phép. Hold có thể giữ pose trong khi hơi thở/camera/tóc tiếp tục. Nếu dùng nhiều lớp chuyển động, mô tả vai trò và nhịp tương đối thay vì đóng băng mọi lớp. Scope từng lệnh: camera đứng tại chỗ có thể vẫn hand-held; môi trường dừng không phải toàn khung freeze; no text phải nhường ngoại lệ credit/title khi brief yêu cầu. Rà mâu thuẫn giữa core rule và beat cụ thể trước khi tăng độ dài prompt.

## Input, prompt và dựng

Gán vai trò từng input (identity, trang phục, môi trường, pose, motion, endpoint) theo khả năng mode thực. Hai ảnh reference không tự là first/last conditioning. Tái dùng frame cuối làm ảnh đầu shot sau cũng không tự là mode hai endpoint.

Đầu ra gồm spec diễn xuất, prompt EN đầy đủ khi được yêu cầu, input/settings riêng, phương án dựng và tiêu chí quan sát. Giữ prompt nhất quán: cảnh/nhân vật, trigger và phản ứng, eyeline/blocking, nhịp, continuity cần thiết; không bắt đủ mười mục hay lặp nhiều lần mọi cấm. Không khẳng định vị trí câu/negative prompt là cơ chế bảo đảm tuân thủ. Duration request/resolution/seed không được suy từ chữ trong prompt; chưa chọn thì ghi chưa rõ.

Khi output thất bại, chọn sửa nhỏ dựa trên lỗi: làm rõ trigger, eyeline, input, giảm hành động đồng thời hoặc đổi shot/dựng. Tách mắt/đầu/thân là fallback, không lệnh mặc định. Nếu tách shot, kiểm tra mặt, hướng nhìn và nhịp tại cut; cắt nối không tự bảo đảm liền mạch. Chọn đoạn usable theo quan sát, không mặc định đầu clip tốt nhất. Nếu retime, xem lại blink, breath, contact và âm thanh; không coi tăng tốc cả clip là chữa diễn chậm.

## Đánh giá và chi phí B2B

Tách ba verdict: đọc được ý đồ, diễn xuất/nhịp phù hợp, kỹ thuật/continuity đạt. Thêm kiểm tra brand/product khi brief có. Xem ở tốc độ giao hàng trước, sau đó kiểm tra frame quanh lỗi; ghi timestamp và mật độ mẫu đã xem. Chưa có media thì chỉ đánh giá spec hoặc ghi user/source-reported, không tuyên bố đã thấy diễn xuất đạt.

Với test, định nghĩa điều cần thấy trước khi chạy; ghi input/model/provider/mode/settings, delta, prompt, output, phí thực/chưa rõ và feedback. So hai cách prompt thì giữ biến khác khi khả thi; đổi đồng thời nhân vật, bối cảnh và câu chữ không chứng minh hiệu quả của riêng một câu. Một clip fail không chứng minh mọi model bất khả thi.

Đối với dự án có ngân sách, theo dõi tổng generation kể cả fail bị tính phí, công dựng/retouch nếu biết, và giây thành phẩm được chấp nhận. Chưa có giây đạt thì không tính giá/giây giả. Chọn fallback theo giá trị beat và ngân sách đã chốt, không cứ thử model đắt hơn. Phân tích không cấp quyền paid generation; nếu đã được phép thử thì tuân ngân sách/số submit và dừng khi đạt, hết giới hạn hoặc user dừng. Timeout chưa rõ job không tự submit lại.

## Nguồn và lưu kinh nghiệm

Khi cần căn cứ Foyege, tra `research/videos/INDEX.md` → `research/videos/foyege/foyege-evidence-digest.md`, phần đối chiếu text copy P-A/B/C và F05–F12. Phần Template/Master là tái tạo, Appendix là text copy user cung cấp; không trộn mức bằng chứng. Yêu cầu montage trong prompt không chứng minh tác giả đã dựng hậu kỳ thế nào. Media test lịch sử chưa xem lại; workflow Draconia, cơ chế model, chi phí thực và hiệu lực chuyển giao chưa được xác nhận. Không biến ví dụ thành luật chung.

Chuỗi dùng cả first/last frame làm conditioning theo `AGENTS.md §7` thì áp dụng `video-delta-analysis` và lưu case/run tại layout đã duyệt. Với mode khác, không tự gán vào quy trình đó; giữ phân tích ở hồ sơ research được user chốt, hỏi layout nếu chưa có nơi lưu phù hợp. Prompt minh họa chưa chạy giữ nhãn đề xuất, không promote thành template đạt.
