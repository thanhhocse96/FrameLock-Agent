---
name: video-delta-analysis
description: Phân tích delta và ghi kinh nghiệm cho chuỗi video sinh dùng cả first frame và last frame làm conditioning. So spec với output, truy xuất case để sửa continuity, morph, count, blocking và camera; không tự áp dụng cho text-to-video, first-frame-only hoặc hai ảnh reference; không tự cấp quyền generation.
metadata:
  version: "1.2.0"
  updated: "2026-10-12"
---

# Video Delta Analysis

Tìm delta trước, giả thuyết nguyên nhân sau. Kế thừa State Delta của `ui-debug`; hướng dẫn này tự chứa phương pháp, không cần repo ui-debug để thực hiện.

Các đường dẫn dữ liệu dưới đây tính từ root AI-GAN, không tính từ thư mục mirror của skill. Canonical: `skills/video-delta-analysis/SKILL.md`.

## Điều kiện áp dụng và hồ sơ chuỗi

Chỉ tự áp dụng khi có cả first/last frame được dùng làm conditioning, theo AGENTS.md §7. Nếu chưa rõ vai trò hai ảnh, làm rõ trước; không coi hai reference là hai endpoint. Một case giữ cả chuỗi và lịch sử run, không tách case theo mỗi lần đổi prompt. Ghi mục đích Business nếu có, cặp frame từng đoạn, spec, từng run kể cả fail/blocked/cancelled, phí thực/chưa rõ, feedback, tổng kết và lý do dừng. Khi đủ bằng chứng thì dùng case để đề xuất workflow phù hợp mục đích Business; phương án chưa thử không promote thành fix đã đạt.

## Chọn đúng states và nguồn

- START/END: hai trạng thái mong muốn; khác nhau không tự đồng nghĩa bug.
- EXPECTED/ACTUAL: spec và output tại cùng giai đoạn/vùng; đây là delta lỗi.
- WORKING/BROKEN: dùng khi có hai run so sánh, ghi cả khác biệt input/settings.
- Chưa có ảnh/video thì phân tích từ mô tả, ghi `user-reported`; không viết đã xem. Nếu xem mẫu frame, ghi khoảng thời gian và mật độ mẫu, mở dày hơn quanh lỗi; không suy ra vật bị che vẫn giữ identity/count.

Tra `research/videos/INDEX.md` trước, rồi đọc đúng case liên quan; không glob mò case/digest. Đọc `research/videos/delta-analysis/protocol.md` khi cần bảng năm trục, schema báo cáo hoặc quy trình kiểm chứng đầy đủ; đây là method legacy giữ tại chỗ. Với thêm/bớt vật khi zoom, cooking morph hoặc thao tác tay, đọc DA-005 qua index: báo cáo có ba run, prompt/settings, timestamp và feedback user. Không load `.local/` mặc định; chỉ mở artifact của case cần chẩn đoán hoặc user yêu cầu.

## ISOLATE → DIFF → PROVE

1. Liệt kê clues và điều chưa biết. Chốt delta có chủ ý, phần phải giữ, camera/timing và mức cho phép cut, time-lapse, morph, occlusion. Dùng ngữ cảnh đã có; chỉ hỏi lựa chọn còn thiếu ảnh hưởng trực tiếp đến giải pháp.
2. Kiểm tra năm trục: environment (model/provider/mode), time (lúc bắt đầu lệch), layer (spec → input → request → generation → dựng), scope (vật/vùng/đoạn), data/state (count/identity/pose/contact/trạng thái/framing). Thu hẹp case nhưng không xóa điều kiện gây lỗi.
3. DIFF mọi thay đổi, kể cả delta phụ mà user không nêu. Ví dụ “một → ba miếng cá, zoom” còn có sống→chín, tay trần→xẻng, bọt/hơi và vị trí/hình dạng. Hai ảnh chưa xác định duy nhất chuyển động ở giữa.
4. Tách **quan sát**, **giả thuyết**, **can thiệp**, **kết quả**. Chọn tầng sửa theo bằng chứng: prompt/blocking, input/keyframe, mode/settings, cấu trúc clip/dựng. Case lịch sử chỉ hướng thứ tự thử; nêu khác biệt model/mode/spec và phần chưa transfer.
5. PROVE bằng output tại điểm lỗi và toàn progression theo tiêu chí đã đặt. Endpoint đúng, request completed, hay prompt có đủ từ khóa không chứng minh clip đạt. Nếu chưa chạy, đánh dấu `proposed-unverified`.

## Kinh nghiệm làm thay đổi quyết định

- Vật ra/vào cần đường đi. Retrieval ngoài khung là hợp lệ khi user muốn; không tự thêm đĩa hoặc reveal nguồn. Hand exit phải thật sự hoàn toàn, có nhịp vắng, re-entry đã cầm vật từ lúc đầu nhìn thấy; chạm bề mặt rồi mới release. Camera phải chừa đường vào/ra trong pha thao tác.
- Count nhìn thấy, identity và contact là ba phép kiểm tra riêng. End có ba miếng nhưng giữa clip có bốn rồi hòa về ba vẫn sai khi spec cấm thêm/ghép. Chưa rõ do che khuất thì ghi chưa rõ, đừng tự đếm vật ẩn.
- Morph có chủ ý cho phép đổi shape nhưng không tự cho phép sinh thêm, merge/split hay jump. Xác định correspondence, quỹ đạo và cửa sổ morph; bỏ shape-lock mâu thuẫn. Nếu giữ count/identity là ưu tiên, kiểm tra hai mục này suốt đoạn chuyển.
- Handling và cooking là hai tiến trình khác nhau. Khi cần sống→chín nhanh, hỏi/ghi quyền time-lapse hoặc time jump; không mô tả là thời gian thực. Nếu spec yêu cầu tay rút trước cooking, kiểm tra chín sớm và việc mang cá chín phủ lên cá sống.
- Timestamp, câu phủ định, seed và duration dài hơn không bảo đảm tuân thủ. DA-005 ghi 10s vẫn thừa cá/không exit đủ. Đó là giới hạn quan sát của cấu hình đã thử, không là kết luận mọi model bất khả thi.
- Chấp nhận sáng tạo của user khác strict pass theo spec. Lưu cả hai; đừng gọi clip user duyệt là bị từ chối vì chỉ số kỹ thuật khác. Spec đổi thì cập nhật tiêu chí run tiếp, giữ lịch sử cũ.

## Output và lưu trữ

Đầu ra gồm clues/states, delta mong muốn, bảng `thời điểm/vùng | expected | actual | bằng chứng`, case nguồn, giả thuyết, sửa tối thiểu và tiêu chí kiểm chứng. Prompt kết quả bằng tiếng Anh; phân tích bằng tiếng Việt. Khi có prompt gốc, nêu patch và prompt hoàn chỉnh; keyframe/settings/dựng ghi riêng.

Case mới lưu ở `research/videos/cases/<case-slug>/case.md`; mỗi run ở `runs/<run-id>.md`, cùng thư mục case. Thêm/cập nhật một dòng trong `research/videos/INDEX.md`, case liên kết run theo thứ tự. `case.md` giữ brief/spec, mục đích Business nếu có, cặp frame từng đoạn, tổng kết/acceptance và nguồn để hình thành workflow; chưa biết mục đích Business thì ghi chưa rõ. Method mới chung cho nhiều case ở `research/videos/methods/`; không tạo file rỗng chỉ để đủ layout.

Mỗi run lưu prompt/settings trước-sau, biến giữ/đổi, timestamp, mẫu đã xem, usage thực/chưa rõ, feedback user, phương án chưa thử và lý do dừng. Artifact mới ở `.local/video-runs/<case-slug>/<run-id>/`. Case production không giả làm raw influencer; không sửa raw bất biến hoặc mapping ảnh để chứa video. Media/log/request base64/key không đưa vào research; prompt và settings không nhạy cảm lưu text để kinh nghiệm không phụ thuộc artifact local. User đã chốt giữ nguyên hồ sơ/artifact cũ: chỉ index chung trỏ tới legacy, không migrate, sao chép lại hoặc ghi case mới vào index legacy.

## Ranh giới thử nghiệm

Phân tích hoặc gọi skill không tự cho phép paid generation. Nếu user đã yêu cầu thử, làm trong phạm vi/budget đã chốt và giới hạn số submit; không xin lại quyền sáng tạo đã có. Kiểm tra capability/giá hiện hành bằng nguồn chính thức/API, chọn mức rẻ phù hợp control cần dùng, báo phí thực sau run. Giữ seed/input/settings khi so prompt nếu được; đổi nhiều biến thì ghi thử phối hợp, không gán nhân quả cho riêng một biến. Dừng theo user hoặc giới hạn đã chốt; không auto retry/submission sau timeout chưa rõ job. Không promote prompt lỗi thành template đạt; có thể promote phương pháp phân tích và kinh nghiệm fail thành skill.
