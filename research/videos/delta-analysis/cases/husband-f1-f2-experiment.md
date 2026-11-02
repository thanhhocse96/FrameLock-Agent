# DA-005 — thử nối Husband-Frame-1 → Husband-Frame-2

- Ngày: 2026-10-12. User yêu cầu thử hai ảnh, chọn thông số tốn ít tiền nhất.
- Input: `.local/work/openrouter/Husband-Frame-1.png` và `Husband-Frame-2.png`, được AI xem trực tiếp trong phiên.
- Artifact: `.local/work/openrouter/2026-10-12-husband-f1-f2-delta/` (gitignored).
- Kết quả generation: API `completed`; đã tải `output.mp4`. Phí thực tế API báo **$0.0487128**. Nội dung `tested-fail` đối với continuity một shot đã chọn cho thử nghiệm; endpoint gần ảnh đích nhưng giữa clip có nhảy trạng thái.
- Job ID: `gen-vid-1791777837-4M2vndhiNUb32o5rC0Ir`; response và usage tại artifact local.

**Đóng thử nghiệm theo user ngày 2026-10-12:** dừng sau ba run, tổng $0.2184552. Không tiếp tục sinh từ skill hoặc đề xuất trong hồ sơ này. Xem [retro tổng kết](../../../../journal/2026-10-12-video-delta-analysis-retro.md) và [archive prompt/settings từng run](husband-f1-f2-run-records.md). Phương pháp được promote thành skill; không promote prompt thành template đạt.

## Clues và delta quan sát từ ảnh

| Thuộc tính | START | END |
|---|---|---|
| Framing | Thấy người, bếp và chảo | Cận lòng chảo, không thấy mặt |
| Cá nhìn thấy trong chảo | Một miếng hồng nhạt đang được tay đặt xuống | Ba miếng vàng nhạt, hình dạng/vị trí khác |
| Contact / dụng cụ | Tay trần giữ cá | Tay giữ xẻng đỏ; tay khác ở gần cán chảo |
| Dầu / bơ / hơi | Dầu khá trong, ít bọt | Nhiều bọt, có hơi |

Đây là multi-change (count, trạng thái, contact/prop, framing), không phải camera-only. Chưa có spec chi tiết ngoài yêu cầu thử cặp ảnh. Giả định thử: giữ first/last frame, nối bằng một shot cooking time-lapse, cho phép nấu tua nhanh; không tự sửa ảnh hoặc tạo ảnh trung gian.

Nguồn chọn hướng: DA-001 cảnh báo morph khi nhiều trạng thái đổi; DA-002 cảnh báo multi-change clamp. Dữ liệu lịch sử chỉ gợi ý rủi ro, không chứng minh lần thử này sẽ fail.

## Chọn thông số và ngân sách

Tra catalog OpenRouter live ngày 2026-10-12. Chỉ xét model có `supported_frame_images` chứa cả `first_frame` và `last_frame`. Không dùng first-frame-only vì bỏ điều kiện ảnh END. Chọn `bytedance/seedance-1-5-pro`, 480p, 4s, 16:9, `generate_audio=false`, seed `12102026`, một lần submit, không auto retry.

SKU không âm thanh: $0.0000012/video token. Ước tính 854×480×24×4/1024 × $0.0000012 = **$0.046116**; phí chính xác phải lấy usage thực. Đây là lựa chọn có chi phí ước tính thấp nhất trong các model hai-frame của catalog đã đối chiếu, không khẳng định rẻ nhất mọi dịch vụ. Seed chỉ là setting ghi lại, không bảo đảm deterministic output.

So sánh tối thiểu: Veo 3.1 Lite 720p 4s không audio $0.12; MiniMax H3 Max 480p 5s $0.25; Kling v3 std 720p 3s không audio $0.252. Các Seedance khác có SKU token cao hơn ở resolution/duration tối thiểu tương ứng. Catalog và settings snapshot nằm trong artifact local.

Nguồn giá/capability: [Video Models API](https://openrouter.ai/api/v1/videos/models), [Seedance 1.5 Pro](https://openrouter.ai/bytedance/seedance-1-5-pro), [Veo Lite](https://openrouter.ai/google/veo-3.1-lite). Tham khảo công thức token của provider: [Volcengine pricing](https://docs.volcengine.com/docs/ark/model-pricing?lang=en&redirect=1). Snapshot chứ không dùng giá journal cũ.

## Prompt thử (EN)

```text
A continuous accelerated cooking shot connecting the supplied first and last frames. The man finishes gently laying the first raw fish fillet into the pan and releases it. He brings two additional fillets into the pan by hand from the upper edge, placing them one at a time beside the original fillet. Each fillet stays a separate solid piece after placement. His bare hand withdraws, then his hand brings the red spatula into view from the upper edge. In a brief cooking time-lapse, the three fillets become lightly golden as butter foams and faint steam rises. The camera moves smoothly closer and slightly higher toward the pan, ending in the supplied tight close-up with three distinct golden fillets and the hand-held red spatula. Keep the same pan and kitchen. One continuous shot with stable object shapes and natural hand contact.
```

Đây là thử khả thi của cầu nối hai ảnh ở mức phí tối thiểu, chưa phải A/B chứng minh một fix. Prompt có nhiều hành động vì endpoint có nhiều delta; 4s là giới hạn kinh phí được ưu tiên, có thể thiếu thời gian thể hiện hết. Nếu fail, không tự tăng duration, đổi model hoặc chạy tiếp làm phát sinh phí.

## PROVE — tiêu chí xem output

Kiểm tra: cá thêm qua thao tác đặt thay vì tự sinh/nhân đôi; contact đúng; identity/shape cá/chảo liên tục; cooked state có progression; xẻng được tay đưa vào; camera tiến gần đúng hướng; endpoint có ba miếng và xẻng; không cut/fade. Xem frame lấy mẫu toàn clip, tăng mật độ quanh điểm count/shape đổi. Phân biệt API completed với nội dung pass. Ghi timestamp, vùng quan sát và phần chưa quan sát được; không suy ra bảo toàn vật bị che.

## Kết quả quan sát và delta lỗi

File thực: H.264, **864×496**, 24fps, 97 frames (~4.04s), không có audio stream. `480p` là tier request; không ghi output thực là đúng 854×480. Metadata lưu trong artifact.

AI xem 32 mẫu trải toàn clip ở 8fps và 15 frame gốc liên tiếp quanh 3.208–3.792s; xem thêm frame cuối 97. Nhãn thời gian contact sheet 8fps là xấp xỉ; cửa sổ dense tính theo index frame gốc/24fps. Chưa đánh giá mọi contact ở từng frame toàn clip.

| Khoảng thời gian | Expected theo prompt thử | Quan sát | Verdict |
|---|---|---|---|
| ~0–1.4s | Thả miếng đầu, đặt thêm hai miếng | Tay mang thêm cá xuống chảo; các mẫu sau có ba miếng | Cầu nối count có hành động nhìn thấy; chưa chứng minh mọi identity/contact đúng |
| ~1.4–2.3s | Tay rút sau placement, cooking time-lapse | Tay còn nhấc/đặt lại cá; miếng giữa xuất hiện mặt vàng sậm trong khi hai miếng còn nhạt | Chưa đạt thứ tự sạch như prompt; không suy ra thời gian nấu thực từ time-lapse |
| ~2.75–3.4s | Xẻng được đưa vào, camera tiến gần | Xẻng đỏ đi vào từ mép trên; framing tiến gần chảo | Đúng hướng cầu nối prop/camera ở các mẫu |
| **3.417→3.458s (frame 83→84)** | Shape/identity và vị trí liên tục trong một shot | Bố cục, hình dạng và màu nhóm cá đổi đột ngột; xẻng/framing cũng nhảy sang bố cục gần đích | **Fail continuity**; bằng chứng trực tiếp ở hai frame kề nhau, không phải chỉ suy từ endpoint |
| ~4.000s, frame 97 | Ba miếng vàng, xẻng, cận chảo như END | Gần bố cục END về nội dung và framing | Endpoint nhìn gần đích; chưa đo pixel similarity và không cứu lỗi giữa clip |

Giả thuyết ưu tiên: cầu nối hành động chưa đủ bảo toàn geometry khi buộc hội tụ END khác trạng thái/vị trí trong thời lượng ngắn. Chưa chứng minh nguyên nhân là duration, endpoint, prompt hay model; một run không loại trừ các khả năng này. Không gọi đây là fade: cửa sổ đã xem cho thấy nhảy bố cục giữa hai frame kề nhau.

## Quyết định sau thử

### Feedback user và hướng morph — 2026-10-12

User đã xem clip và xác nhận “thấy ổn”. Trạng thái acceptance: **user-accepted** cho clip hiện tại. Verdict continuity fail ở trên vẫn mô tả đúng phép kiểm tra theo giả định một shot giữ shape đã chọn trước run; không đồng nghĩa user từ chối clip.

User đề xuất dùng morph cho phần cá đổi hình dạng. Đây là hướng thiết kế `proposed-unverified`, chưa chạy thêm: cho phép cá đổi shape có chủ ý trong một cửa sổ ngắn, giữ count ba miếng và correspondence một-một, tránh hợp nhất/tách miếng; phối hợp chuyển màu sống→vàng, bơ/hơi và camera hội tụ END. Morph có chủ ý vẫn cần progression qua nhiều frame, khác với nhảy bố cục frame 83→84 của bản thử.

Candidate prompt patch (EN, đề xuất lúc đầu; sau đó đã dùng trong thử 2):

```text
During the final cooking transition, the three fish fillets smoothly morph into their corresponding cooked shapes in the ending frame. Each fillet remains separate, following a continuous path into its final position. Their surfaces gradually turn golden as butter foams and a brief veil of steam passes over the pan. The camera continues its smooth push-in, then settles on the ending composition.
```

Nếu thử patch, thay đoạn `stable object shapes` bằng ràng buộc count/correspondence phù hợp; không vừa yêu cầu shape bất biến vừa yêu cầu morph. Giữ ảnh/model/settings của baseline để kiểm tra patch trước, không tự tăng duration hay phí. Count, contact, camera và endpoint vẫn là tiêu chí; shape được phép đổi trong cửa sổ user chọn. Tính tự nhiên và mức chấp nhận morph do user đánh giá. Chưa xác nhận Seedance tuân thủ morph/correspondence ở cặp ảnh này.

### Thử 2 — morph có chủ ý (2026-10-12)

User yêu cầu “Thử nghiệm tiếp”. Artifact riêng: `.local/work/openrouter/2026-10-12-husband-f1-f2-morph/`. Chỉ đổi field `prompt`; ảnh conditioning, model, seed, duration, resolution, aspect ratio và audio giữ giống baseline. So sánh field được lưu ở `comparison.json`, không output base64 ảnh ra chat.

Patch thay câu cooking time-lapse bằng đoạn morph phía trên, đồng thời thay `stable object shapes` bằng `three separate fillets throughout the cooking transition`. Đây là một can thiệp về mục tiêu morph với hai chỉnh sửa câu liên quan, không tách được tác động từng câu từ một run. Phần thao tác đặt cá/xẻng và camera giữ nguyên.

Tiêu chí mới cho đoạn cuối: hình dạng được phép đổi dần; giữ ba miếng riêng biệt với correspondence một-một và quỹ đạo liên tục, không nhảy bố cục như baseline tại frame 83→84. Giữ yêu cầu contact, camera và endpoint. Trạng thái/phí/kết quả sẽ ghi sau khi job và frame được kiểm tra; chưa coi user đã duyệt clip candidate.

**Kết quả thử 2:** job `gen-vid-1791779142-y9kYanO61cQiD4Sfl85h`, API completed, usage **$0.0487128**. Tổng hai run **$0.0974256**. Một lần submit cho candidate, không auto retry. Video đã tải và trích 97 frame gốc; xem 32 mẫu overview, 15 frame liền nhau 3.208–3.792s, và frame 58/61/63/65 (~2.375/2.500/2.583/2.667s) để kiểm tra chuyển trạng thái sớm hơn.

| Hạng mục | Quan sát candidate | So với baseline / kết luận |
|---|---|---|
| Endpoint convergence ~3.417–3.458s | Ba miếng đã ở bố cục gần END; thay đổi quanh xẻng/camera liên tục trong cửa sổ dense đã xem | Không thấy cú nhảy bố cục lớn như baseline ở cửa sổ này; cải thiện quan sát của mẫu |
| Progression sống→chín | Hai miếng thêm đã có mặt vàng khi được đưa vào; miếng ban đầu còn hồng tới ~2.375s | Không tuân theo ý đồ đặt cá rồi nấu cả ba theo cùng progression |
| Morph/contact ~2.500–2.667s | Tay mang một phần cá vàng xuống trên miếng hồng; phần mới phủ/hòa thành miếng vàng lớn trước khi tay rút | Chưa đạt correspondence một-một; có dấu hiệu thêm/ghép phần cá thay vì chỉ morph miếng đang nằm trong chảo |
| Prop/camera cuối | Xẻng đi vào từ trên và camera tiến gần; ba miếng nhìn thấy riêng sau đoạn chuyển | Cầu nối cuối có tính liên tục tốt hơn ở các mẫu đã xem; chưa chứng minh mọi frame toàn clip đúng |

Verdict: **cải thiện phần cuối, `tested-fail` với tiêu chí morph một-một toàn progression**. Một run mỗi prompt chỉ cho thấy khác biệt output; seed giống nhau không loại trừ randomness hay chứng minh từ “morph” là nguyên nhân duy nhất. Candidate chưa có feedback user.

Hướng sửa tiếp (chưa chạy): sau khi ba miếng đã được đặt, tay trần rút hẳn; chỉ ba miếng đang nằm trong chảo đổi màu/shape tại chỗ, không mang cá chín khác vào hoặc ghép phần cá. Đây là sửa blocking/contact dựa trên lỗi mới, không tự kết luận cần đổi model hoặc tăng duration.

### Thử 3 — blocking ngoài khung và timeline 10 giây (2026-10-12)

User feedback: video giống hô biến cá từ tay. User chốt không sinh thêm đĩa; camera đang tiến vào, tay chỉ cần ra khỏi frame và quay vào đã cầm cá. User đồng ý phương án đặt cá sống → tay rút → cooking time-lapse → xẻng vào → kết thúc cận cảnh và yêu cầu tăng lên khoảng 10s.

Giả thuyết thiết kế: nguồn cá nằm ngoài khung là đủ, nhưng phải có nhịp tay ra hoàn toàn, retrieval ngoài khung và re-entry đã cầm cá; không hình thành miếng cá trong tay còn nhìn thấy. Camera giữ đường vào/ra đủ rộng trong placement. Không cần reveal đĩa; ảnh đầu có props nền sẵn, không yêu cầu xóa props đó.

Artifact riêng `.local/work/openrouter/2026-10-12-husband-f1-f2-blocking-10s/`. Giữ hai ảnh gốc, Seedance 1.5 Pro, 480p, silent, seed 12102026; đổi cả `prompt` và `duration=10`. Đây là thử phối hợp theo spec mới, không chứng minh riêng tác động tăng duration hoặc một câu prompt. Một lần submit, không auto retry. Ước tính ở kích thước nominal 854×480: **$0.11529**, kiểm tra rate/capability live trước submit.

| Timeline mục tiêu | Hành động | Count / camera |
|---|---|---|
| 0–1s | Thả miếng đầu, tay rút hoàn toàn qua mép trên | Một miếng sống; camera tiến chậm |
| 1–2s | Tay lấy miếng thứ hai ngoài khung | Một miếng giữ nguyên; không reveal đĩa |
| 2–3.5s | Tay vào đã cầm miếng sống thứ hai, chạm chảo mới thả, tay rút | Một → hai; giữ đường re-entry |
| 3.5–4.5s | Tay ngoài khung lấy miếng thứ ba | Hai miếng đứng yên |
| 4.5–6s | Tay vào đã cầm miếng sống thứ ba, đặt/thả rồi rút | Hai → ba miếng sống |
| 6–8.4s | Tay trần ngoài khung; ba miếng tại chỗ chuyển vàng/shape bằng time-lapse; bơ/hơi tăng | Ba miếng riêng biệt; camera siết dần |
| 8.4–9.4s | Tay vào đã cầm xẻng đỏ; tay kia giữ cán chảo | Ba miếng vàng; hội tụ END |
| 9.4–10s | Settle ở ảnh cuối | Ba miếng và xẻng, không jump |

Tiêu chí cần xem: tay thực sự ra hoàn toàn và có khoảng vắng; cá đi qua mép khung đã được cầm, không sinh từ lòng bàn tay; miếng tiếp xúc chảo rồi mới release; không đưa miếng chín mới vào, không ghép/split; cooking chỉ bắt đầu sau placement; không cần plate reveal; camera/endpoint đúng. Timestamp là mục tiêu prompting, không bảo đảm model tuân chính xác.

Trạng thái output, usage và verdict được ghi sau khi kiểm tra job/video.

**Kết quả thử 3:** job `gen-vid-1791779877-8POWDv7mjJgLnQUbDmgA`, completed, phí **$0.1210296**; tổng ba run **$0.2184552**. Actual output 864×496, 24fps, 241 frames (~10.04s), không audio. Đã xem 30 overview samples ở 3fps (timestamp xấp xỉ) và frame gốc 81/129/153/180/241 (~3.333/5.333/6.333/7.458/10.000s).

| Delta cần sửa | Quan sát bản 10s | Đánh giá |
|---|---|---|
| Hand exit → re-entry đã cầm cá | Sau miếng đầu, tay với về mép trái, trở lại có cá; các lần tiếp không có nhịp tay rút hoàn toàn ngoài khung như spec | Nhịp đầu có nguồn ngoài khung rõ hơn; toàn chuỗi chưa đạt blocking |
| Chỉ thêm hai miếng | Tới frame 153 (~6.333s), nhìn thấy **bốn miếng** riêng: hai vàng bên trái/trước, một hồng giữa, một bên phải | Fail count; không chỉ lỗi màu/shape |
| Cả ba sống trước cooking window | Miếng được tay đưa vào đã có phần vàng trước 6s | Fail state/timing |
| Morph một-một tại chỗ | Frame 180 (~7.458s) miếng bên phải nở thành geometry gần END, miếng hồng giữa vẫn nhìn thấy; endpoint cuối còn ba | Không đủ correspondence; phần cá thừa bị che/hòa/mất khi hội tụ, chưa xác định chính xác cơ chế ở mọi frame |
| Camera/xẻng/endpoint | Camera tiến gần, xẻng xuất hiện, cuối nhìn gần END với ba miếng vàng | Cầu nối cuối có, không chứng minh toàn clip thực tế |

Verdict theo spec: **`tested-fail`** về blocking/count/state. User chưa đánh giá bản 10s. Timeline dễ đọc hơn ở các mẫu đầu, nhưng tăng duration và prompt mới chưa đủ loại lỗi sinh/ghép cá. Không gán riêng cải thiện hoặc lỗi cho duration vì thử đã đổi cả duration và prompt. Một run không chứng minh model không thể thực hiện bài toán.

Hướng nghiên cứu tiếp, chưa thực hiện: thu hẹp placement thành từng đoạn một lần tay ra/vào và một miếng thêm, dùng keyframe count đúng làm checkpoint, rồi nối cooking/camera riêng. Giữ retrieval ngoài khung theo spec user; không tự thêm đĩa. Muốn giữ một shot vẫn cần thử blocking tối giản hoặc control phù hợp, không chỉ nhồi thêm negatives. Không tự chạy generation thứ tư.

Mỗi run có một lần submit; không auto retry. Kết quả cho thấy prompt có thể tạo thao tác thêm cá ở các mẫu nhưng chưa giải quyết continuity toàn bộ multi-change. Không promote thành template đạt.

Hướng chưa thử: tạo keyframe trung gian ba miếng với framing gần START, giữ identity/vị trí cá; tách thao tác thêm cá khỏi chuyển camera. Nếu vẫn giữ yêu cầu sống→chín và xẻng, cần thiết kế riêng progression đó hoặc cho phép time jump ở dựng. Ảnh trung gian chỉ có count đúng nhưng shape/vị trí lệch vẫn có nguy cơ tái tạo lỗi. Không tạo ảnh trung gian trong ba run đã ghi; thử nghiệm đã dừng theo user.
