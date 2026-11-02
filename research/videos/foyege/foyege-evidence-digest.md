# Foyege — digest bằng chứng và chuyển giao sang video B2B

Ngày: 2026-10-28. Trạng thái: **research quan trọng, skill nháp; chưa xác nhận workflow Draconia, chưa có generation mới**.

User chốt nghiên cứu Foyege để hiểu cách làm video B2B; đánh giá Draconia Malfoy diễn có hồn, ít artifact, chi phí khá cao. Đây là feedback và mốc chất lượng của user, không phải kết quả đo artifact, bảng chi phí hay xác nhận quy trình sản xuất của tác giả. Mục tiêu là học cách đưa ý đồ câu chuyện thành diễn xuất đọc được và sản phẩm có thể nghiệm thu.

## Nguồn và mức bằng chứng

Đây là digest tài liệu tổng hợp và phần text prompt user bổ sung ngày 2026-10-28. Không đưa vào mapping ảnh. Ba tài liệu đầu vào giữ nguyên; khi sử dụng kết luận của chúng, đọc các giới hạn trong digest này. Header cũ của S3 nói toàn file là tái tạo, nhưng hiện chỉ áp dụng phần Template/Master phía trên: Appendix A/B/C mới là text copy do user cung cấp. Không sửa hoặc tự dịch lại nội dung copy.

| ID | Nguồn | Có thể chứng minh / giới hạn |
|---|---|---|
| S1 | [Tổng hợp và test](foyege-analysis-and-tests.md), §2–8 | Báo cáo thứ cấp về bài đăng, diễn giải kịch bản và ba test; không thay cho media/request gốc |
| S2 | [Phân tích sâu](foyege-prompt-structure-deep-analysis.md), §1–8 | Diễn giải cơ chế của người tổng hợp; không phải thực nghiệm độc lập |
| S3 | [Prompt tái tạo](foyege-prompt-templates-en.md), Important note và A/B/C | Cấu trúc prompt được tái tạo bằng tiếng Anh; không dùng để trích lời Foyege |
| P-A | [Appendix A](foyege-prompt-templates-en.md#appendix-a-xcomfoyege24status2109113006953263233), Global Settings/Core Rules/Storyboard/Consistency | Text copy user cung cấp, tiếng Anh, prompt biến hình 15s; chưa rõ bản Anh gốc hay bản dịch; chưa có prompt đánh nhau 30s trong phụ lục này |
| P-B | [Appendix B](foyege-prompt-templates-en.md#appendix-b-xcomfoyege24status2102610496683933915), các mục tiếng Trung 0–13s và 声音与连续性 | Text copy user cung cấp, tiếng Trung; xác nhận được nội dung chỉ đạo trên văn bản |
| P-C | [Appendix C](foyege-prompt-templates-en.md#appendix-c-xcomfoyege24status2100222945499263146), 人物与参考图/流动影像与胶片质感/剪辑与抽帧节奏/声音 | Text copy user cung cấp, tiếng Trung; xác nhận được nội dung chỉ đạo trên văn bản |
| U1 | Feedback user ngày 2026-10-28, ghi ở đầu digest | Định hướng chất lượng và mục đích B2B; không xác nhận chi phí cụ thể |

Nguồn ngoài do S1/S3 dẫn: [A — biến hình/đánh nhau](https://x.com/Foyege24/status/2109113006953263233), [B — bướm hóa người](https://x.com/Foyege24/status/2102610496683933915), [C — DEADSHOT](https://x.com/Foyege24/status/2100222945499263146). Thử mở ngày 2026-10-28: A trả 403, B/C cache miss. Không đọc được self-reply, chưa đối chiếu prompt hoặc video. Các thông tin ngày đăng, model, duration và tác giả trong S1/S3 vẫn là source-reported, không nâng thành verified. Không suy tool của Draconia từ ba bài khác.

Nhãn dùng trong digest: **reported** = tài liệu kể lại; **text-supported** = thấy trực tiếp trong text copy user cung cấp; **interpretation** = diễn giải; **proposed** = đề xuất của phiên này; **verified** chỉ dành cho đối chiếu thực tế có bằng chứng. Phiên này xác nhận nội dung text, không xác nhận chất lượng media hay độ khớp từng chữ với self-reply trên X. Kênh/URL nằm ở từng Appendix; ngày nhận bản copy trong repo: 2026-10-28; ngày thu thập gốc và URL self-reply riêng chưa rõ.

## Ma trận nhận định → khả năng sử dụng

| ID | Nhận định / nguồn cụ thể | Mức bằng chứng | Quyết định khi tạo skill |
|---|---|---|---|
| F01 | Ảnh reference được gán vai trò riêng. Nguồn: P-A Global Settings; P-B hai dòng reference; P-C 人物与参考图 | text-supported | Dùng bảng vai trò input để tránh yêu cầu mâu thuẫn; hiệu lực thực phụ thuộc mode hỗ trợ |
| F02 | Ba cách tổ chức thời gian: beat, pha trạng thái, montage. Nguồn: P-A Storyboard 15s; P-B 0–13s; P-C 剪辑与抽帧节奏 và năm pha | text-supported | Xem như ba lựa chọn thiết kế; không buộc một beat/giây hay cấm phối hợp; chưa có text fight 30s |
| F03 | Motif cánh/mắt nối hai hình dạng. Nguồn: P-B 蝴蝶与眼纹, 7.5–10s và 第10秒 | text-supported về yêu cầu; interpretation về tác dụng | Đề xuất neo nhận diện nếu phù hợp câu chuyện; không chứng minh giữ identity tốt hơn mọi cách khác |
| F04 | Động cơ tiến–lùi và hành động phải trả giá trong Draconia. Nguồn: S1 §2.4, §3.1–3.2 | interpretation, chưa đối chiếu tập phim | Dùng làm gợi ý phân tích mục tiêu/trở lực/lựa chọn/hệ quả; không gán đây là workflow chính thức |
| F05 | Test gộp mắt/đầu/thân có drift; test mắt riêng tốt hơn; cascade đọc được thứ tự. Nguồn: S1 §5.1–5.3 | reported, thiếu media tại checkout và settings đầy đủ | Tách chuyển động là fallback đáng thử; chưa chứng minh nguyên nhân hoặc giới hạn model |
| F06 | Bản dựng cascade 6s còn mặt già hơn ở mảnh sau. Nguồn: S1 §5.3 | reported | Cắt nối có thể giải timing nhưng vẫn cần kiểm tra identity tại cut; không gọi pass toàn diện |
| F07 | Nhịp mắt nhanh → đầu theo → giữ; retime riêng chuyển động. Nguồn: S1 §6 | spec/đề xuất và kinh nghiệm được kể lại | Đưa vào phương án thử; không có clip sau retime được đối chiếu để xác nhận đạt |
| F08 | Lặp cuối prompt chống quên; phủ định khiến model làm ngược. Nguồn: S2 §1, §6–7 | giải thích cơ chế chưa có bằng chứng | Không đưa vào skill như sự thật; có thể thử prompt rõ/ít mâu thuẫn mà không viện cơ chế này |
| F09 | Đổi thứ tự mục làm prompt yếu; model không có xương mắt nên không làm được cascade. Nguồn: S2 §1, §7 | suy diễn không được test chứng minh | Loại khỏi nguyên tắc; không suy kiến trúc model từ một output lỗi |
| F10 | Prompt 4s nhưng output 10s. Nguồn: S1 §5.1–5.2 | reported, duration request chưa rõ | Phân biệt duration cấu hình với thời điểm hành động trong clip; chưa kết luận model không hiểu thời gian |
| F11 | Chỉ lấy đầu clip, mọi shot chỉ một tầng động, mọi clip chỉ một kiểu timeline. Nguồn: S1 §7; S2 §3–4, §7–8 | khái quát vượt mẫu | Chọn đoạn tốt theo quan sát bất kể vị trí; giảm độ phức tạp theo lỗi, không mặc định đóng băng diễn viên |
| F12 | Film → Blender → control map → AI. Nguồn: S1 §4.3 | pipeline được đề xuất, chưa có provenance Draconia | Giữ như hướng nghiên cứu; không nhận là workflow Foyege hoặc mặc định mọi provider hỗ trợ |

## Điều đáng học về kịch bản

### Đối chiếu bổ sung sau khi có text copy

Các kết luận sau dựa trực tiếp vào P-A/B/C; chúng mô tả **prompt yêu cầu gì**, chưa chứng minh output đã thực hiện được:

- **Không có thứ tự mười mục giống nhau cho cả ba.** P-A nhóm reference trong Global Settings rồi đến Characters/Core Rules/Storyboard; P-B mở bằng reference và các mục ánh sáng, chủ thể, pha thời gian; P-C mở bằng brief, nhân vật, lớp ảnh, nhịp dựng. Master template S3 là tổng hợp của người phân tích. Skill nên giữ chức năng cần thiết, không bắt model điền cùng một khuôn.
- **Timeline có quan hệ nguyên nhân và điều kiện reveal.** P-A: va chạm → sập mái → bị thương → thủ ấn → lắp giáp → phản công. P-B: từng vùng ánh sáng mất → chỉ còn motif → che thay đổi cơ thể/khoảng cách → bật đèn mới cho thấy người. Bài học chuyển giao đề xuất: ghi khán giả được biết gì ở mỗi beat, điều gì chưa lộ và sự kiện nào cho phép lộ; không chỉ ghi giây.
- **Trạng thái hư hại phải tồn tại.** P-A Core Rules và Negative Prompt yêu cầu dấu phá hủy còn tới cuối, không tái sinh công trình. Với B2B có thể chuyển thành ledger trạng thái vật: trước/sau thao tác, tay cầm, vật đã đặt/chưa đặt, chi tiết không được tự hồi phục. Đây là gợi ý thiết kế, chưa thử sản phẩm thực.
- **Giữ không đồng nghĩa bất động.** P-B 10–13s cho phép vi biểu cảm, thở, tóc và camera hand-held tiếp tục; nhân vật không đi/chuyển đầu/biến dạng tiếp. P-C yêu cầu nhân vật, tóc, áo, sương và lớp phơi sáng chuyển động khác tốc độ. Điều này bác cách đọc “một shot chỉ một tầng động” như luật Foyege.
- **Độ rõ được phân bố có chủ đích.** P-C cho mắt, tay cầm và súng là điểm đọc rõ giữa blur/đúp ảnh; không phải mọi pixel đều sắc. Chuyển giao đề xuất: định nghĩa vùng mang ý nghĩa hoặc cần đúng sản phẩm, rồi cho phép stylization ở vùng khác nếu brief cho phép; không dùng style để che lỗi bắt buộc sửa.
- **Lệnh có phạm vi, và text vẫn có chỗ cần phân giải.** P-A vừa đóng băng môi trường vừa cấm freeze frame; nên phân biệt trạng thái môi trường với đóng băng toàn khung. P-A còn yêu cầu mảnh vụn xoay trong 6–13s dù Core Rules nói chúng treo đứng: ghi đây là căng thẳng nội bộ, không tự gọi spec hoàn hảo. P-C cho phép đúng credit và tên phim; không thể kế thừa lệnh “no text” từ A sang mọi prompt.
- **Text montage chưa là bằng chứng hậu kỳ.** P-C yêu cầu cắt/抽帧 ngay trong prompt. Chưa biết phần nào model sinh, phần nào tác giả dựng thêm. Phân biệt timeline được yêu cầu trong generation với edit thực đã có project/output.

Kết quả cập nhật: F01–F03 tăng từ reported lên text-supported; F04–F12 về Draconia, test lịch sử và cơ chế model không tự tăng mức bằng chứng vì có thêm prompt của ba sản phẩm khác.

Nguồn xuất phát: F04/S1 §3.1–3.2. Phần dưới là **thiết kế đề xuất**, không phải kết luận đã kiểm chứng về tác giả.

Một cảnh có thể đẹp và sạch lỗi nhưng không làm người xem hiểu thêm gì. Khi chuyển sang B2B, bắt đầu từ điều người xem cần hiểu/tin/làm và bằng chứng doanh nghiệp thực sự có; sau đó mới chọn tình huống có nhân vật. Không ép mọi video sản phẩm thành phim tình cảm hay cliffhanger.

Đối với cảnh có người, mô tả mục tiêu trước mắt, điều cản, lựa chọn và hệ quả. Subtext là khoảng cách giữa điều muốn và điều sẵn sàng bộc lộ. Có thể biểu đạt bằng tiếp tục một công việc, ngập ngừng trước quyết định, thay đổi cách đáp lại đối tác; không cần mặc định mím môi, liếc mắt hoặc lạnh lùng.

Điểm bàn giao cho diễn xuất là beat có ID, tác nhân kích hoạt, hành động có mục đích, điều cần giấu, trạng thái trước/sau và điều khán giả cần đọc được. Shot size, ánh sáng và chuyển động camera phục vụ việc đọc beat. Một cảnh có thể chứa nhiều thay đổi cảm xúc nếu cần; giữ nguyên nhân–hệ quả thay vì đếm cảm xúc.

## Điều đáng học về diễn xuất AI

Nguồn xuất phát: F01–03, F05–07. Phần chuyển giao là **proposed**.

Tách ba câu hỏi khi đánh giá: (a) người xem hiểu phản ứng gì và vì sao; (b) phản ứng có nhịp phù hợp không; (c) identity, anatomy, contact và continuity có lỗi không. Video hết artifact chưa tự có diễn xuất tốt; video có phản ứng hay nhưng sai sản phẩm cũng chưa đủ nghiệm thu B2B.

Với một beat, xác định đích nhìn trong không gian, sự kiện gây phản ứng, hành vi chính, biên độ và khoảng giữ. Cho phép hơi thở, chớp mắt, dịch trọng tâm nếu phù hợp; không yêu cầu cơ thể bất động tuyệt đối để chữa mọi lỗi. Không dùng một bộ dấu hiệu cơ mặt như từ điển cảm xúc cố định.

Nếu output gộp nhiều chuyển động không đạt, cân nhắc đơn giản hóa blocking, input rõ hơn, tách shot hoặc dựng; chọn theo lỗi thực tế và giá trị beat. Frame cuối shot trước làm ảnh đầu shot sau là liên kết first-frame, không tự trở thành conditioning bằng cả first/last frame. Không kích hoạt `video-delta-analysis` chỉ vì có hai ảnh reference.

## B2B: nghiệm thu và chi phí

Đây là rubric đề xuất cho dự án tiếp theo, không phải KPI đã được khách hàng chốt:

| Trục | Cách kiểm tra | Điều cần chốt theo brief |
|---|---|---|
| Ý đồ | Người xem mô tả được lựa chọn/thay đổi của nhân vật hoặc thông tin sản phẩm | Thông điệp và nhóm người xem |
| Diễn xuất | Xem tốc độ giao hàng; phản ứng có tác nhân, đích nhìn, nhịp đáp lại | Mức biểu đạt, tự nhiên hay stylized |
| Kỹ thuật | Xem toàn progression và vùng cut; ghi timestamp lỗi mặt/tay/đồ/vật | Lỗi nào bắt buộc sửa, lỗi nào chấp nhận |
| Thương hiệu | Đối chiếu asset/claim đã duyệt | Logo, pack, màu, quy trình sản phẩm phải đúng |
| Khả năng sửa | Thay một beat mà giữ các beat đã duyệt | Những phần phải cố định giữa phiên bản |
| Kinh tế | Tổng chi phí / giây thành phẩm được chấp nhận | Ngân sách, trần thử, lịch bàn giao |

Ghi riêng chi phí generation (kể cả run fail nếu bị tính), công dựng/retouch và tổng production khi có số liệu. Không biết thì ghi chưa rõ, không quy thành 0. Nếu chưa có giây được chấp nhận, chỉ báo tổng chi phí và trạng thái chưa có output đạt; không tạo tỉ số giả. Đánh giá chi phí Draconia của user chưa đủ để suy số lần thử, model đắt hay quy trình hậu kỳ cụ thể.

## Cảnh thử bàn giao giữa hai skill — chỉ trên văn bản

Brief giả định để kiểm tra skill: phim B2B 15s về bàn giao trong xưởng; người xem là người phụ trách mua hàng; muốn thể hiện sự phối hợp có trách nhiệm. Không gán tên doanh nghiệp, chứng nhận, độ chính xác hoặc cam kết hiệu suất. Chưa có product asset nên không dựng cận sản phẩm như bằng chứng chất lượng.

| Beat | Tình huống và ý đồ | Điều khán giả cần đọc | Gợi ý shot |
|---|---|---|---|
| B01, khoảng 0–5s | Người phụ trách còn chờ đồng nghiệp hoàn tất kiểm tra; muốn tiếp tục bàn giao nhưng không thúc ép | Sự chờ đợi có lý do | Trung cảnh cho thấy hai người và quan hệ không gian |
| B02, khoảng 5–10s | Đồng nghiệp ra dấu đã xong; người phụ trách nhìn nhận tín hiệu rồi gật đầu nhỏ | Quyết định tiếp tục bắt nguồn từ xác nhận, không phải vui vô cớ | Cận vừa người nhận tín hiệu; tín hiệu được thiết lập ở shot trước |
| B03, khoảng 10–15s | Hai người bắt đầu bước tiếp cùng nhau | Sự phối hợp chuyển thành hành động | Trung cảnh; chừa khoảng kết cho thông tin thương hiệu nếu được cung cấp |

Đây là timing dựng dự kiến, không phải duration request. Cảnh không chứng minh kiểm định đạt hay một quy trình công nghiệp thực tế; trước production cần đối chiếu hành vi với nghiệp vụ khách hàng.

Spec diễn xuất B02: ban đầu chú ý tới đồng nghiệp ngoài khung ở camera-left; khi nhận tín hiệu đã thiết lập, ánh nhìn ổn định và một cái gật nhẹ thể hiện đồng ý tiếp tục. Không cần xoay đầu theo mắt nếu đầu đã hướng đúng. Camera giữ góc; vai và nhịp thở được phép tự nhiên. Continuity bắt buộc: cùng người, trang phục và hướng đối tác. Biểu cảm cần đọc là sự xác nhận kín đáo, không phải nụ cười quảng cáo.

Prompt minh họa EN — chưa chạy, không phải prompt của Foyege:

```text
Medium close-up of the adult handover lead in the approved workshop setting. Preserve the approved character identity and workwear. The colleague is offscreen at camera-left, at the same eye level established in the preceding shot. The lead is already attending to that colleague. After receiving the colleague's completion signal, the lead gives one small, deliberate nod acknowledging that they can proceed, then holds that attentive expression briefly. Keep the reaction restrained and purposeful, with natural breathing and small incidental posture adjustments. Maintain the established camera angle and eyeline. Play the action at normal speed; the nod should read as a decision, not an exaggerated greeting. End with the lead ready to move into the next shot.
```

Input đề xuất: reference nhân vật và bối cảnh đã duyệt, chỉ khi mode hỗ trợ; chưa có asset thực trong bài thử. Settings/model/provider/duration generation: chưa chọn. Hậu kỳ: giữ đủ thời gian để đọc tín hiệu → phản ứng; không retime toàn thân chỉ để đạt số giây. Fallback nếu một shot khó đọc: sửa cách thiết lập tín hiệu hoặc độ rõ phản ứng trước khi tăng số shot.

Kết quả kiểm tra văn bản ngày 2026-10-28: B02 giữ nguyên trigger, ý đồ và đích nhìn từ kịch bản sang prompt; không áp mắt-trước-đầu máy móc; settings không bị bịa; không sinh claim doanh nghiệp. **Chỉ đạt kiểm tra bàn giao trên văn bản. Chưa đánh giá cảm xúc, artifact, chi phí hoặc tác dụng thực của skill bằng video.**

## Thử nghiệm và điều kiện promote

1. Lấy một đoạn Draconia cụ thể có quyền truy cập: ghi tập/URL/timecode, điều thấy ở tốc độ thật, cut, eyeline, âm thanh, phản ứng; tách suy đoán cách tạo. Video thành phẩm không tiết lộ số retry hoặc rig.
2. Nếu tìm được prompt/request/output và hậu kỳ tương ứng, nối chúng bằng provenance; tránh so prompt một sản phẩm với video sản phẩm khác.
3. Với test mới được cấp ngân sách: giữ input/model/mode/duration/settings khi so hai cách chỉ đạo cùng beat, ghi seed nếu có; lặp phù hợp ngân sách để tránh kết luận từ một may mắn. Đổi nhiều biến thì chỉ gọi so hai phương án tổng thể.
4. Chấm ý đồ, diễn xuất và artifact riêng; giữ cả feedback người xem và kiểm tra kỹ thuật. Thử một cảnh khác trước khi khái quát sang workflow B2B.
5. Promote quy tắc hẹp khi có output kiểm chứng, phạm vi model/mode, chi phí và tiêu chí đạt; lưu thất bại và ngoại lệ. Không gọi prompt mẫu hoặc kỹ thuật dựng này là template đạt.

Hai skill canonical: [write-video-script](../../../skills/write-video-script/SKILL.md) và [direct-ai-performance](../../../skills/direct-ai-performance/SKILL.md), bản 0.1.0 nháp. Chúng hệ thống hóa cách ra quyết định, không tuyên bố tái tạo workflow Foyege. Phiên này dừng ở digest, skill và kiểm tra văn bản; không submit generation, không phát sinh phí generation.
