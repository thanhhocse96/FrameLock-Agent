# Nghiên cứu nhịp, continuity và chi phí cho video cinematic

Ngày: 2026-11-02. Trạng thái: nghiên cứu tổng hợp + thiết kế kiểm chứng `proposed-unverified`; chưa chạy generation mới, chưa promote thành workflow production đạt.

## 1. Brief và phạm vi bằng chứng

Mục tiêu user: video chất lượng cinematic cao, dùng cho B2B/B2C, tiết kiệm chi phí. Vấn đề báo cáo: dù dùng first/last frame để hạn chế chuyển động, video vẫn chậm; hai clip dùng chung ảnh tại điểm nối vẫn lệch chi tiết. User xác nhận gặp trên cả hai provider và nghiêng về lỗi quy trình. Tên/version hai provider, settings và clip cụ thể chưa xác định; không tự gán cho các model lịch sử.

Phiên này đọc hồ sơ nghiên cứu và nguồn ngoài, chưa xem media mới. Lỗi hiện tại là `user-reported`; dấu hiệu lặp ở hai provider làm tăng ưu tiên điều tra workflow, không chứng minh nguyên nhân chung hoặc loại trừ lỗi model. Nghiên cứu tập trung chuỗi dùng cả first/last conditioning và hậu kỳ của chuỗi. Không khởi chạy API, chuyển mode, hoặc chọn platform mới.

| Bằng chứng repo | Điều được ghi nhận | Giới hạn |
|---|---|---|
| [DA-003](../delta-analysis/cases/project-retrospectives.md#da-003) | Cart glide chậm thay vì fast-forward | Journal-reported; hướng speed-ramp/prompt chưa có run pass |
| [DA-002](../delta-analysis/cases/project-retrospectives.md#da-002) | Hai thử nghiệm khác model vẫn fade khi nối cảnh đổi scale/tay/vật | Cặp multi-change; không phải phép thử cô lập tốc độ hay seam |
| [DA-005](../delta-analysis/cases/husband-f1-f2-experiment.md) | Run đầu nhảy bố cục tại 3.417→3.458s; endpoint gần ảnh đích | Bằng chứng được lưu từ phiên đã xem; phiên này không xem lại media |
| DA-005 run 2/3 | Morph cải thiện cửa sổ cuối nhưng còn lỗi progression; tăng lên 10s không giải quyết toàn bộ | Run 3 đổi cả prompt và duration; không suy ra nhân quả riêng duration |

DA-005 tốn tổng $0.2184552 trong ba run lịch sử; đó không phải báo giá hiện hành. User acceptance và strict continuity pass được lưu riêng, phải tiếp tục giữ phân biệt này.

## 2. Phản biện giả định của workflow

### Hai endpoint không khóa chuyển động

Cho cùng trạng thái A và B vẫn có nhiều đường đi, tốc độ, gia tốc, thời điểm tiếp xúc và cách che khuất khác nhau. Giảm độ khác nhau giữa A/B có thể làm nhiệm vụ đơn giản hơn, nhưng không bảo đảm có chuyển động vừa đủ hoặc đúng nhịp. Ngược lại, A/B khác nhau quá nhiều có thể buộc một clip xử lý nhiều sự kiện không tương thích.

[MotionBridge](https://motionbridge.github.io/) nghiên cứu chính sự thiếu kiểm soát phần giữa hai frame, bổ sung trajectory, mask và các tín hiệu điều khiển khác. Đây là điểm tựa cho chẩn đoán thiếu ràng buộc đường đi; không chứng minh kiến trúc hay khả năng của hai provider user đang dùng, cũng không là đề xuất tự triển khai model mới.

### Cinematic không đồng nghĩa chậm hoặc phải nối thành một cú máy

Định nghĩa vận hành đề xuất: bố cục/ánh sáng có chủ đích, hành động và phản ứng đọc được, camera phục vụ nội dung, sản phẩm đúng, nhịp dựng và âm thanh phù hợp. Một clip mượt nhưng hành động ì ạch vẫn không đạt mục tiêu nhịp. Một quảng cáo có cắt cảnh rõ vẫn có thể cinematic. Đây là tiêu chí thiết kế cho dự án, không phải kết quả benchmark về conversion.

Chính sách bắt mọi cảnh nối liền biến mỗi cut thành bài toán bảo toàn hình học, ánh sáng, chuyển động và trạng thái giữa hai lần sinh độc lập. Cần quyết định chỗ nào thật sự phải liên tục trước khi sinh, thay vì coi mọi đường nối là một one-take cần cứu.

### Cùng ảnh input không đủ để chứng minh cùng frame output

Gọi ảnh chung là K, frame cuối thực của clip A là A_end, frame đầu thực của clip B là B_start. Điều phải đo là A_end↔K, B_start↔K và A_end↔B_start. Dùng chung K không tự chứng minh ba ảnh giống nhau. Tài liệu [Google first/last frames](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-first-and-last-frames) mô tả khả năng cấp endpoint; trang đã đọc không cung cấp cam kết pixel-identical cho mọi output.

Ngay cả A_end = B_start, mối nối vẫn có thể khựng: vận tốc trước điểm nối khác vận tốc sau điểm nối; camera, hướng tay hoặc pha hành động bị reset. Theo ngôn ngữ toán học, khớp trạng thái tại một thời điểm chưa đủ cho liên tục vận tốc. Không cần cưỡng ép gia tốc hoàn hảo cho mọi cut; yêu cầu phụ thuộc dụng ý dựng.

## 3. Chẩn đoán tốc độ: tách bốn lỗi

| Nhóm lỗi | Dấu hiệu cần quan sát | Giả thuyết / phép kiểm tra |
|---|---|---|
| Playback/timebase | Mọi thứ cùng chậm, audio hoặc duration khác bản gốc | So timestamp, duration, FPS/timebase nguồn với timeline/export; không đổi FPS tùy ý để chữa |
| Hành động bị kéo dài | Thao tác đơn giản chiếm gần cả clip | Đo onset/contact/completion, so với animatic hoặc động tác mẫu cùng loại; thử duration ngắn hơn nếu đủ chứa hành động |
| Chuyển động ít | Chủ thể gần như đứng, chỉ camera trôi | Tách chuyển động camera khỏi chủ thể; ảnh tĩnh ổn định không đồng nghĩa tốc độ đúng |
| Nhịp khởi động/dừng | Mỗi clip có khoảng đứng rồi ease-in/ease-out | Xem cửa sổ đầu/cuối; thử trim hoặc đặt điểm dựng ở pha chuyển động phù hợp |

Quan hệ minh họa: nếu cùng quãng đường d được trải trên toàn thời lượng T, vận tốc trung bình là d/T. Giảm T có thể tăng vận tốc trung bình nhưng model có thể đổi cả quỹ đạo; đây là giả thuyết để thử, không là định luật hành vi model. Tăng duration cho nhiều thao tác có thể cần thiết; tăng duration cho một động tác nhỏ cũng có thể làm vấn đề nhịp nặng hơn.

Các nguyên nhân chưa được chứng minh ở case hiện tại: prompt nhấn mạnh gentle/slow/smooth; ảnh có tư thế nghỉ; model ưu tiên chuyển động nhỏ; prompt có quá nhiều ràng buộc; duration không hợp động tác. Không gọi đó là thiên lệch training đã xác nhận, không khẳng định tắt audio làm motion tốt hơn.

[Runway guide](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide) hướng dẫn tập trung prompt vào motion, cân đối sequence/duration và xét motion cues trong ảnh. Hướng dẫn tối ưu cho Gen-4.5; áp dụng sang model khác chỉ là giả thuyết transfer.

## 4. Chẩn đoán điểm nối trước khi regenerate

1. Xác minh đúng file K được gửi cho cả hai clip, crop/aspect/resize và orientation tương thích. Hash file chỉ chứng minh byte input, không chứng minh server xử lý giống nhau.
2. Trích frame thực từ file nguồn, không dùng ảnh thumbnail hoặc screenshot player. Xác định đúng frame cuối và frame đầu theo timestamp; phân biệt duplicate frame/hold với frame bị thiếu.
3. So ba cặp A_end/K, B_start/K, A_end/B_start. Xem cả toàn khung và ROI mặt, logo, mép sản phẩm, ngón tay. Ghi màu/ánh sáng, vị trí, geometry và identity riêng.
4. Xem khoảng 0.5s trước/sau seam ở tốc độ phát thật, sau đó từng frame. Kiểm tra hướng/tốc độ camera, vật thể và motion blur. Cửa sổ 0.5s là điểm bắt đầu, mở rộng nếu lỗi kéo dài.
5. So file nguồn với export cuối. Nếu nguồn khớp mà export lệch, sửa crop/color/timebase/resampling tại khâu dựng trước.

SSIM hoặc pixel difference chỉ là công cụ hỗ trợ sau khi chuẩn hóa kích thước/màu; compression cũng gây khác pixel. Alignment có thể giúp tách sai màu khỏi sai hình nhưng không được dùng để che displacement thật. Optical flow giúp đo hướng chuyển động nhưng có thể sai trên morph, che khuất, nước hoặc blur. Human review ROI bắt buộc; không lấy một chỉ số trung bình thay cho đúng logo/count/contact.

## 5. Workflow ứng viên: dựng nhịp và phân loại điểm nối trước

Tất cả bước sau là đề xuất cần kiểm chứng trên case thật.

1. **Brief → shot list → animatic.** Mỗi shot ghi vai trò thông tin/cảm xúc, hành động chính, thời lượng sử dụng, vùng sản phẩm phải đúng, chỗ cut và âm thanh dự kiến. Chọn nhịp theo nội dung; chưa ấn định một số giây chung cho mọi B2B/B2C.
2. **Phân loại nối.** Nối liên tục chỉ khi cần giữ cùng không gian/hành động. Đổi scale, đổi thời điểm hoặc đổi trạng thái lớn: cân nhắc cut chủ ý, insert hoặc shot phản ứng. Đây là lựa chọn sáng tạo cần nằm trong spec; không tự đổi yêu cầu one-take thành montage.
3. **Kiểm tra cặp endpoint.** Liệt kê delta chính/phụ và đường đi khả thi. Đặt thời gian theo động tác; tránh endpoint vừa yêu cầu thay count/prop, nấu chín, đổi scale và camera mà không có thời gian thực hiện.
4. **Sinh có mục tiêu.** Giữ cả first/last conditioning trong phạm vi hiện tại. Prompt nêu hành động, pha thời gian và camera; không trông chờ từ “cinematic” hoặc câu phủ định sửa được mọi lỗi. Mỗi shot chỉ gánh số sự kiện thực sự cần cho beat.
5. **Chọn phần dùng được và dựng.** Trim đoạn thừa nếu còn đủ thông tin. Retime chỉ khi toàn hành động có thể đổi tốc độ mà contact/blur/audio vẫn hợp lý. Retime không sửa morph, identity hoặc logic thao tác; optical-flow interpolation có thể tạo lỗi mới.
6. **Khóa asset cần chính xác.** Logo, số liệu, CTA có thể đặt bằng đồ họa hậu kỳ. Nếu nhãn nằm trên vật chuyển động, cần tracking/occlusion/ánh sáng phù hợp; overlay đơn giản không tự giải quyết nhãn cong/quay. Với shot mô tả sản phẩm/quy trình phải chính xác, đưa chi phí sửa vào quyết định dùng clip.
7. **QA bản dựng ở kích thước phát hành.** Kiểm tra cả nhịp thật, chi tiết và âm thanh. Preview thấp phân giải chỉ dùng sàng lọc motion; không chứng minh bản final giữ được micro-detail.

| Loại shot | Ưu tiên duyệt | Lỗi không nên được che bằng “cinematic” |
|---|---|---|
| B2B trình diễn sản phẩm/quy trình | Đúng hình học, count, thứ tự/contact, thông tin đọc được | Hành động mô tả sai cơ chế hoặc sản phẩm thay chi tiết |
| B2C demo/packshot | Đúng sản phẩm, rõ lợi ích, nhịp phù hợp thông điệp | Logo/bao bì sai, kết quả thao tác không đúng |
| B2B/B2C mood/story | Diễn xuất, cảm xúc, nhịp và continuity có chủ đích | Mượt nhưng không có beat hoặc không hiểu câu chuyện |

Không giả định B2C chấp nhận sai sản phẩm hoặc B2B luôn phải chậm. Chưa có KPI chiến dịch cụ thể; không bịa conversion/retention mục tiêu.

## 6. Nghiên cứu mới: kiểm chứng theo tầng, tối thiểu lần sinh

### P0 — audit không sinh mới

Chọn một mối nối lỗi và một clip chậm, có source video + hai ảnh + prompt/settings + bản export nếu có. Lập bảng expected/actual với timestamp, lấy mẫu dày quanh seam và xem toàn clip tốc độ thật. Đo tỷ lệ phần footage dùng được, thời điểm hành động và chi phí sửa. Nếu lỗi do dựng, giải quyết ở đây trước.

### P1 — kiểm chứng tốc độ

Một cặp endpoint có một động tác rõ; cùng provider/model/version, ảnh, resolution, aspect, audio, prompt và seed nếu hỗ trợ. Baseline duration hiện tại so với duration ngắn hơn trong dải hợp lệ, vẫn đủ cho thao tác. Không thay prompt trong phép so này. Giả thuyết thắng chỉ khi động tác đúng nhịp hơn mà contact/identity không hỏng.

Nếu duration không giải quyết, lượt tiếp giữ duration và chỉ đổi chỉ đạo timing trong prompt. Không đổi đồng thời duration, prompt và model rồi quy công cho một yếu tố. Một output mỗi arm chỉ là sàng lọc; lặp ứng viên tốt với seed khác trước khi nói có tính tái lập. Seed giống nhau không bảo đảm deterministic.

### P2 — kiểm chứng seam, giữ clip A cố định

So clip B gốc nhận K với B mới nhận A_end thực làm first conditioning, last conditioning của B giữ nguyên. Chỉ làm nếu A_end đã đạt asset/identity: nếu A đã sai thì chaining sẽ truyền sai. Đây là thử thay một input, không thay mode. Hướng dùng last output làm input tiếp có trong Runway guide, nhưng không bảo đảm các provider khác giữ endpoint hay vận tốc.

Nếu A_end và K vốn đã giống hệt, phép thử này không có tương phản hữu ích: ưu tiên pha vận tốc và pipeline export. Nếu B bắt đầu khớp hơn nhưng sai tích lũy ở các clip sau, chưa đạt mục tiêu chuỗi. Không mặc định serial chaining cho toàn phim: nó tạo phụ thuộc, kéo dài chờ và có nguy cơ drift tích lũy.

### P3 — so bản dựng trước khi mở rộng generation

Dùng footage có sẵn so bản cố nối liên tục với bản cut/trim có chủ đích nếu brief cho phép. Chấm blind khi có thể: đọc hành động, nhịp, continuity, độ đúng sản phẩm, cảm nhận cinematic và thời gian hậu kỳ. Không dùng dissolve như fix mặc định: hai vật lệch hình có thể thành bóng đôi.

### Acceptance đề xuất

- Timing: onset/contact/completion theo animatic; ngưỡng sàng lọc ban đầu có thể là ±20% thời gian động tác, nhưng phải điều chỉnh theo loại hành động/brief, không phải chuẩn ngành.
- Identity: không thấy thay logo, shape, count hoặc chi tiết quan trọng ở độ phân giải bàn giao; kiểm tra cả phần giữa, không chỉ endpoint.
- Seam continuous: không thấy pop/hold/đổi hướng ngoài chủ ý ở tốc độ thật; xem dense để xác minh. Cut chủ ý chấm theo continuity dựng, không buộc pixel-match.
- Business: người duyệt hiểu hành động/thông điệp và chấp nhận bản dựng; lưu riêng với strict technical pass.
- Tái lập: ứng viên qua một lần chỉ là promising; xác nhận trên một cặp khác và thêm seed nếu ngân sách cho phép. Không báo xác suất thắng từ vài mẫu nhỏ.

[VBench](https://arxiv.org/abs/2311.17982) tách đánh giá thành nhiều chiều như identity, motion smoothness và flickering. Nghiên cứu này mượn nguyên tắc đánh giá tách chiều; không tuyên bố đã chạy VBench hoặc dùng điểm benchmark thay acceptance thương mại.

## 7. Chi phí và điều kiện dừng

**Đính chính theo user ngày 2026-11-03:** user đã tính tổng chi phí gồm mọi retry. Mục tiêu tiết kiệm là ra sản phẩm xem được trong ít lần sinh nhất, trong tổng ngân sách chấp nhận được. Không coi user đang tối ưu giá mỗi request. Theo dõi chính: tổng tiền đã tiêu, số lần sinh tới bản xem được, và acceptance của bản dựng. Chi phí trên giây duyệt bên dưới chỉ là chỉ số phân tích phụ, không thay mục tiêu user; số lần sinh ít hơn cũng không tự chứng minh tổng tiền thấp hơn nếu giá mỗi lần khác nhau.

Thời gian hậu kỳ/QA theo dõi riêng để nhận biết phương án đẩy gánh nặng sang sửa tay; chỉ quy đổi thành tiền khi có rate thống nhất. Không tự cộng khoản tiền lao động giả định vào cách user đang báo chi phí.

`C_delivered = C_keyframes + C_generation_all_attempts + C_finishing + C_QA`

`C_per_accepted_second = C_delivered / accepted_unique_seconds`

Nếu chưa có giây đạt, chỉ báo tổng đã tiêu và 0 giây đạt; không chia cho 0. Công thức mở rộng chỉ dùng khi các khoản được xác định; chưa có rate lao động thì báo thời gian riêng. Ghi thêm latency nếu deadline là yếu tố quyết định.

Ví dụ toán học giả định, không phải giá thị trường: $0.10/lần với tỷ lệ pass 20% cho kỳ vọng $0.50/clip đạt; $0.25/lần với pass 80% cho $0.3125/clip đạt, trước hậu kỳ và giả sử các lần thử độc lập, cùng độ dài/chất lượng. Model rẻ/lần không tất yếu rẻ/đầu ra. Khi chưa có dữ liệu pass đáng tin, không dùng công thức để khẳng định model thắng.

Đề xuất budget từng tầng trước paid test, dừng khi hết cap hoặc cùng failure tái diễn mà không có giả thuyết phân biệt mới. Không regenerate cả chuỗi nếu một shot hỏng. Không auto retry job timeout chưa rõ trạng thái/phí. Chỉ nâng resolution của phương án có triển vọng, nhưng vẫn QA final vì đổi tier có thể đổi output.

Phiên này không phát sinh phí generation. Chưa chốt model rẻ nhất hoặc giá hiện hành; chỉ kiểm tra capability/giá đúng provider khi có kế hoạch submit được user cho phép. DA-005 vẫn đóng, không mở lại thử cũ.

## 8. Kết luận và phạm vi promote

Giả thuyết ưu tiên: workflow đang giao quá nhiều trách nhiệm cho hai ảnh neo — vừa giữ asset, chỉ đạo nhịp, vừa bảo đảm continuity giữa các lần sinh. Cần tách chúng thành phép kiểm tra và quyết định dựng riêng. Dữ liệu hiện có hỗ trợ điều tra theo hướng này, chưa chứng minh nguyên nhân của hai provider hiện tại.

Có thể dùng ngay tài liệu này làm checklist chẩn đoán và thiết kế thí nghiệm. Chưa gọi đây là workflow cinematic đã đạt, chưa có prompt mới được kiểm chứng. Bước bằng chứng tiếp theo là P0 trên một mối nối thực và một động tác chậm; sau đó mới chọn thử nghiệm có khả năng phân biệt nguyên nhân cao nhất.

Nguồn ngoài được đọc ngày 2026-11-02: Google first/last frames, Runway Image-to-Video Guide, MotionBridge project, VBench paper (liên kết tại các luận điểm). Đây là tổng hợp phương pháp, không phải raw influencer hoặc case generation mới; index chung trỏ tài liệu này, không tạo run giả.

## 9. Thực hành animatic và sửa seam — bổ sung 2026-11-03

### Animatic không cần sinh video thử

Animatic là storyboard đặt lên timeline có thời lượng và âm thanh nháp; có thể thêm chuyển động camera/layer đơn giản. Nguồn: [Toon Boom — How to Create an Animatic](https://docs.toonboom.com/help/storyboard-pro-20/storyboard/getting-started/animatic.html). Quy trình ứng viên cho dự án:

1. Viết mỗi beat thành một hành động hoặc thông tin người xem cần nhận. Ghi cái gì phải nhìn thấy, cái gì có thể bỏ qua bằng cut. Không phát triển kịch bản mới nếu brief chưa yêu cầu.
2. Dùng ảnh hiện có, crop, phác nét/mũi tên và chữ để đặt lên timeline. Với thao tác, đánh dấu ít nhất bắt đầu → sự kiện chính/contact → hoàn tất; hai ảnh tĩnh đầu/cuối không đủ biểu diễn nhịp ở giữa. Không cần trả phí sinh thêm ảnh chỉ để làm board đẹp.
3. Đo nhịp bằng diễn thử/quay điện thoại thao tác đơn giản hoặc footage tham chiếu phù hợp; dùng làm thước đo biên tập, không tự đưa video reference vào generation. Với động tác nguy hiểm/không thể diễn, dùng proxy an toàn và đánh dấu thời gian chưa xác minh. Đặt marker onset/contact/release trước khi kéo thời lượng ảnh.
4. Thêm voice scratch, tiếng động tại contact và nhạc nháp nếu brief cần. Đặt camera move đơn giản bằng position/scale khi cần thử framing, không dùng zoom chậm mặc định thay cho động tác chủ thể.
5. Xem bản nháp ở tốc độ thật: hiểu hành động không, chờ lâu ở đâu, cắt có lặp/mất bước không, thông tin sản phẩm đủ thời gian đọc không? Chốt timing trước khi prompt. Animatic chứng minh ý đồ dựng có thể đọc được, không chứng minh model sinh đúng.
6. Bàn giao mỗi shot: ảnh đầu/cuối, thời lượng sử dụng, duration request khả dụng, marker sự kiện, chuyển động camera, trạng thái vào/ra, loại seam, ROI phải đúng và phương án cứu bằng dựng. Tách duration sinh với duration dùng; nếu model chỉ sinh dài hơn, lên kế hoạch trim/retime, không kéo dài animatic theo model.

Ví dụ minh họa, chưa phải timing chuẩn hay run: beat đặt vật xuống bàn 2s; 0–0.5s tay vào, 0.5–1.1s hạ vật, contact 1.1s, 1.1–1.4s thả, 1.4–2s tay rút. Board dùng 3–4 trạng thái hoặc proxy chuyển động. Nếu endpoint kế bắt đầu bằng tay vào lại, phát hiện lặp hành động ngay trên animatic. Với chuyển động xuyên seam, ghi cùng pha/hướng/tốc độ mong muốn ở hai phía, không bắt mỗi clip tự bắt đầu rồi dừng.

### Sửa seam theo lỗi, từ ít lần sinh nhất

| Lỗi đã xác định | Xử lý trên footage có sẵn | Khi nào phải đổi phương án |
|---|---|---|
| Frame lặp/hold/ease-out rồi ease-in | Chọn lại out/in trong cửa sổ quanh seam, bỏ phần trùng; giữ progression hành động | Không còn cặp frame tương thích: không trim cưỡng ép làm mất contact |
| Cùng geometry, lệch vị trí/scale nhỏ | Transform/crop nhẹ, kiểm tra cả cửa sổ trước/sau và độ phân giải còn lại | Có parallax hoặc hình học biến dạng: transform toàn khung không sửa được |
| Cùng hình, khác exposure/WB | Match màu và blend correction qua một đoạn nếu cần | Ánh sáng/shadow đổi cấu trúc: grade màu không đủ |
| Lệch chi tiết nhỏ ở vùng có thể theo dõi | Patch/composite từ asset đúng, track và xử lý occlusion | Mặt/tay/nhãn quay hoặc shape sai lớn có thể tốn hơn sinh lại; không gọi overlay là fix phổ quát |
| Khác geometry/identity rõ | Chọn frame khác chưa lỗi; nếu brief cho phép, dùng cut khác góc hoặc insert có sẵn | Không có footage phù hợp hoặc brief buộc continuous: sửa/sinh lại shot lỗi |
| Hình khớp, nhịp không khớp | Chọn cut theo pha hành động, trim hoặc retime nhẹ nếu phù hợp | Không có progression tương thích: một frame chung không sửa vận tốc được |

Match-on-action nối hai shot qua cùng hành động; nguồn [Adobe — continuity editing](https://www.adobe.com/creativecloud/video/hub/ideas/what-is-continuity-editing-in-film.html). Không đồng nhất cắt theo hành động với việc mọi sai chi tiết sẽ vô hình; cùng góc gần như y hệt mà sản phẩm đổi shape vẫn có thể pop. Cutaway/đổi góc chỉ được dùng khi brief cho phép và không che sai sự thật sản phẩm.

Nếu buộc sinh lại: giữ shot đạt; lấy frame cuối **được chọn để dùng** của A làm first conditioning của B, giữ endpoint cuối B, sau khi xác nhận frame A đúng asset. Nếu cắt A sớm, dùng frame mới tại điểm cắt chứ không dùng frame cuối file cũ. Kiểm tra B thực xuất ra và chuyển động hai phía; không có bảo đảm tuyệt đối. Không truyền frame đã drift làm nguồn cho cả chuỗi.

Không chèn ảnh K một frame để ép khớp: chỉ sửa một thời điểm, có thể tạo flash/hold quanh đó. Không dissolve mặc định khi vật lệch: có nguy cơ bóng đôi. Không mở batch benchmark khi mục tiêu là cứu sản phẩm ít lần sinh nhất; trước mỗi lần sinh phải chỉ rõ lỗi cần sửa và vì sao dựng hiện có không giải quyết được. Nghiên cứu so sánh có thể dùng budget riêng, không trộn với chi phí cứu bản production.
