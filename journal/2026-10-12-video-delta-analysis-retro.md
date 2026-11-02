# Retro — Delta Analysis và cá hô biến khi nối hai keyframe

## Bối cảnh

Ngày 2026-10-12, user mở phạm vi research video và yêu cầu xây Delta Analysis tham khảo skill ui-debug. Ca thật dùng Husband-Frame-1/2: một miếng sống đang được đặt → cận ba miếng vàng với xẻng/bơ/hơi. Đây là nhiều delta cùng lúc, không chỉ count và zoom. AI trực tiếp xem hai ảnh và frame lấy từ ba video, không coi suy luận từ endpoint là quan sát toàn clip.

Hồ sơ nguồn: [DA-005](../research/videos/delta-analysis/cases/husband-f1-f2-experiment.md); [archive ba prompt và settings](../research/videos/delta-analysis/cases/husband-f1-f2-run-records.md). Các link artifact `.local/` trong hồ sơ là machine-local, không bảo đảm có trên checkout khác.

## Việc đã làm và kết quả

Chọn Seedance 1.5 Pro qua OpenRouter vì chi phí ước tính thấp nhất trong catalog hai-frame được đối chiếu lúc chạy, dùng tier 480p, 16:9, audio false, seed 12102026. Không suy rộng đây là model rẻ nhất mọi dịch vụ hoặc tối ưu tỷ lệ thành công.

| Run | Can thiệp | Phí thực USD | Quan sát quyết định |
|---|---|---|---|
| 1, 4s | Prompt thêm hai cá, cooking và camera nối endpoint | 0.0487128 | Nhảy shape/bố cục frame 83→84 (~3.417→3.458s); endpoint gần đích |
| 2, 4s | Thay shape-lock bằng morph, giữ field khác | 0.0487128 | Cuối mượt hơn ở mẫu, nhưng ~2.5–2.7s tay mang phần cá vàng phủ/hòa với cá sống |
| 3, 10s | Timeline exit/re-entry, đặt đủ cá sống rồi cooking, xẻng và zoom | 0.1210296 | Nhịp đầu rõ hơn; các cycle exit thiếu; bốn miếng ở frame 153 (~6.333s); chín sớm và về ba ở cuối |

Actual output cả ba: 864×496, 24fps, không audio; 4s request cho 97 frame (~4.04s), 10s cho 241 frame (~10.04s). Tier request và kích thước thực khác nhau; lưu usage thực thay vì chỉ nhân giá ước tính. Tổng **$0.2184552**, đúng ba submit, không retry tự động.

Run 1 được user xem và chấp nhận về hình ảnh. User tiếp tục thử morph, rồi nhận xét cảm giác hô biến từ tay. Chấp nhận sáng tạo này không xóa phép đo continuity fail của run 1. Run 2/3 không có xác nhận pass mới. Sau run 3, user yêu cầu dừng và viết lại kinh nghiệm; **đã đóng thử nghiệm, không có run tiếp theo được phép từ yêu cầu tổng kết**.

## Pitfall và bài học có căn cứ

| Bẫy | Bằng chứng / nguồn | Điều cần làm trong case tương lai |
|---|---|---|
| Chọn thêm keyframe ngay khi thấy count khác | DA-004 và hội thoại thiết kế | Hỏi count change là chủ ý hay input lệch, tìm delta trước chọn tầng sửa |
| Có câu “hand enters” nhưng thiếu acquisition | User feedback run 2; prompt archive | Ghi exit hoàn toàn, khoảng vắng, re-entry đã giữ vật, contact rồi release; xem output để verify |
| Cho rằng phải thêm đĩa mới để giải thích nguồn | User chủ động phản biện; ảnh đã có đĩa nền | Retrieval ngoài khung là hợp lệ; không thêm prop/reveal nguồn trái ý user |
| Morph tốt cuối đồng nghĩa xử lý cả hành động | Run 2 | Kiểm tra correspondence/contact và state timing, không chỉ smoothness cuối |
| Count endpoint đúng đồng nghĩa count xuyên clip đúng | Run 3, frame 153/180/241 | Đếm theo timeline, xem vùng che, tìm lúc vật thừa hòa/mất; không bịa identity qua occlusion |
| Tăng thời lượng sẽ tự chữa blocking | Run 3, đồng thời đổi prompt và duration | Thời gian là điều kiện cho nhịp, không là bảo đảm instruction adherence; không quy nhân quả riêng cho duration |
| Prompt thật chi tiết là control cứng | Cả ba run còn count/contact/state lỗi | Timestamp/negatives là chỉ dẫn; cần alternative về keyframe/clip/control khi budget cho phép, không cứ nhồi thêm câu |
| So seed giống là deterministic A/B | Một mẫu mỗi prompt, run 3 đổi nhiều biến | Ghi biến thay đổi và giới hạn causal inference; không tính xác suất hay universal rule từ ba mẫu |

## Kết luận về mô hình và phần chưa chứng minh

User nhận định đa phần lỗi nằm ở bản chất mô hình. Bằng chứng thực nghiệm hỗ trợ nhận định hẹp hơn: **cấu hình Seedance 1.5 Pro 480p first/last-frame đã thử không giữ ổn định count, acquisition/contact và thứ tự sống→chín khi đồng thời phải hội tụ camera/endpoint**. Yêu cầu có mặt trong request nhưng output vẫn lệch, nên không thể coi thêm vài câu prompt là fix chắc chắn.

Chưa tách được ảnh hưởng của model, resolution, conditioning ảnh cuối khác geometry, độ phức tạp prompt và randomness. Không so model khác, không lặp cùng cấu hình, không test keyframe trung gian hoặc control khác. Do đó chưa chứng minh giới hạn kiến trúc, mọi model đều lỗi, hay model này không bao giờ làm được. Giữ suy luận về giới hạn model như giả thuyết vận hành có phạm vi, không đặt vào digest như fact kỹ thuật.

Phần agent cần cải thiện: không giới thiệu ảnh trung gian như đáp án mặc định; phân biệt START/END với EXPECTED/ACTUAL; không bảo đảm timelapse/morph bằng câu chữ; giải thích phí/giới hạn thử; không gọi output completed là pass. Skill được promote là **phương pháp phân tích**, không phải prompt video đã đạt.

## Cách xử lý ca tương tự trong tương lai

1. Tra index, xác nhận spec cho count/shape/time/camera. Tìm delta phụ và vùng cuối đúng → đầu sai, ưu tiên bằng chứng frame thực.
2. Nếu lỗi hô biến, kiểm tra chu trình acquisition trước; giữ yêu cầu off-screen retrieval nếu user muốn. Nếu morph, cho phép shape đổi có cửa sổ nhưng giữ count/correspondence theo spec.
3. Nếu prompt/blocking rõ vẫn fail và budget đã hết hoặc user dừng, lưu kết quả và kết thúc. Trong phiên tương lai có quyền thử mới, cân nhắc checkpoint keyframe hoặc tách mỗi clip một lần placement, rồi cooking/camera riêng. Đây là **phương án chưa thử**, không phải fix được chứng minh.
4. So output theo criterion cụ thể; lưu cả feedback user và technical verdict. Khi thử phối hợp nhiều biến, báo là phối hợp; chỉ kết luận rộng hơn khi có dữ liệu mới phù hợp.

## Promote và dừng

Đã promote quy trình thành [video-delta-analysis](../skills/video-delta-analysis/SKILL.md), phiên bản 1.0.0; [protocol](../research/videos/delta-analysis/protocol.md) giữ chi tiết State Delta. Không promote các prompt thử thành template pass. Không sửa governance `.context/`/AGENTS trong lượt tổng kết này. Không chạy thêm generation.
