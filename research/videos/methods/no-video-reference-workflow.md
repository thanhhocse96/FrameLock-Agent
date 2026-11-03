# Workflow ứng viên: dựng theo shot, sinh từ ảnh và prompt

Ngày: 2026-11-03. Version: 0.1.0. Trạng thái: `proposed-unverified`; chưa generation, chưa promote thành workflow production đạt.

User yêu cầu workflow mới và giới hạn rõ **không dùng video tham chiếu**. Input generation chỉ gồm text và ảnh theo capability thực. Animatic là tài liệu biên tập nội bộ, không upload làm conditioning. Không dùng video-to-video, motion/performance transfer, video extension hoặc depth/pose sequence trong đề xuất này. Hậu kỳ là trim/cut/retime/color/composite thông thường; không gửi footage trở lại model làm video input.

Nguồn thiết kế: [research tempo/seam](cinematic-tempo-continuity-cost.md), [so sánh workflow và nguồn hãng/creator](animatic-blender-motion-transfer-research.md). Tài liệu này tổng hợp thành đề xuất vận hành, không thêm claim model hoặc bảng giá mới. Không thay governance, schema raw/digest/template hay layout; chưa triển khai mode/API mới.

## 1. Mục tiêu và thay đổi chính

Mục tiêu: ra bản cinematic xem được trong ít lần sinh nhất, theo tổng tiền user đã tính cả retry. Một shot phải phục vụ bản dựng và giữ chi tiết quan trọng; không chỉ đẹp khi đứng riêng.

Thay vì dựng chuỗi K1→K2→K3 rồi bắt mọi đoạn nối vô hình, thiết kế các shot có nhiệm vụ và điểm cắt trước. Chỉ yêu cầu continuous tại nơi có giá trị kể chuyện/thương mại. Không tự bỏ yêu cầu one-take khi brief thật sự cần.

Chuỗi công việc: brief → beat/shot list → animatic → ảnh chuẩn + mode → prompt → generation chọn lọc → dựng ngay → sửa theo lỗi → duyệt bản cuối.

## 2. Brief và tiêu chí đạt trước generation

Ghi ngắn: người xem, thông điệp, hành động/cảm xúc cần đọc được, độ dài/tỷ lệ khung hình bàn giao, asset sản phẩm và chi tiết phải đúng, mức cho phép cut/time jump/morph, giới hạn tiền/số lượt.

Tách ba tiêu chí: thông điệp/nhịp; hình ảnh/diễn xuất; brand/product/continuity. Khi chưa chốt campaign KPI, chỉ ghi mục tiêu truyền đạt, không bịa conversion. Chưa có budget thì workflow vẫn lập được, nhưng không tự submit paid generation.

## 3. Shot list và animatic bằng ảnh tĩnh

- Mỗi shot có một nhiệm vụ chính: đặt bối cảnh, thể hiện thao tác, phản ứng, cho thấy lợi ích hoặc kết thúc/CTA. Một nhiệm vụ có thể gồm vài bước liên quan; không tự cắt vụn mọi động tác.
- Dùng ảnh sẵn có, crop và phác nét; đặt lên timeline, thêm lời đọc/SFX nháp khi cần. Với hành động, dùng các trạng thái trước/contact/sau và marker sự kiện. Không dùng dissolve giữa hai ảnh để giả định model biết chuyển động ở giữa.
- Đặt thời lượng theo nhịp đọc hành động và thông tin. Phát bản nháp ở tốc độ thật; bỏ đoạn chờ và lặp ý trước khi trả phí video.
- Chốt loại nối: hard cut có chủ đích, cut theo hành động, insert/cutaway, hoặc continuous bắt buộc. Shot continuous có thêm yêu cầu pha chuyển động tại đầu/đuôi.
- Đầu ra: thứ tự shot, thời lượng sử dụng, marker sự kiện, kiểu nối và âm thanh dự kiến. Animatic kiểm tra cấu trúc/nhịp dự kiến, không chứng minh motion model sẽ đúng.

### Phiếu shot tối thiểu

Đây là checklist trong method, không thay schema research hiện hữu:

| Trường | Nội dung cần chốt |
|---|---|
| ID / nhiệm vụ | Người xem hiểu hoặc cảm thấy gì sau shot |
| Trạng thái vào → ra | Vị trí, pose, props, count, tình trạng sản phẩm |
| Hành động / nhịp | Sự kiện chính, thời điểm dự kiến, phần giữ để đọc |
| Camera | Một chỉ đạo rõ hoặc giữ máy; không mặc định slow push-in |
| Thời lượng dùng / request | Hai giá trị riêng; request theo capability thực |
| Ảnh conditioning | START, END nếu cần, identity/product/style nếu mode hỗ trợ |
| Nối vào / ra | Cut hay continuous; hướng nhìn/chuyển động cần giữ |
| Chi tiết bắt buộc | ROI sản phẩm, tay/contact, mặt hoặc text |
| Cách cứu bằng dựng | Trim, cutaway/crop hợp lệ; điều không được che |
| Ngân sách | Cap tiền và lượt còn lại |

## 4. Ảnh chuẩn và cách chọn endpoint

Tạo bộ ảnh tối thiểu cho nhân vật, sản phẩm, bối cảnh và look cần lặp. Dùng đúng state/trang phục/props theo shot; chỉ bổ sung góc nhìn cần thiết. Ưu tiên giữ tỷ lệ, lighting direction, eyeline và screen direction qua cut. Không cố dùng một portrait cho mọi framing.

| Nhu cầu | Input đề xuất |
|---|---|
| Biết trạng thái đầu, cho phép kết thúc linh hoạt | START + text, thêm reference ảnh nếu mode hỗ trợ |
| Kết thúc phải đến bố cục/trạng thái xác định | START + END, sau khi kiểm tra đường chuyển khả thi |
| Nhân vật/product lặp qua các shot khác góc | Reference ảnh/Element theo mode, không coi ảnh đó là endpoint nếu chưa gán |

Đây là đề xuất lựa chọn mode cho workflow mới, không triển khai hoặc tự đổi mode của case đang chạy. Không tuyên bố first-frame-only luôn nhanh hơn hoặc ít lỗi hơn. END có ích khi cần điểm đến cụ thể; không thêm END chỉ để hy vọng chuyển động ít đi.

Kiểm tra cặp START/END trước sinh: scale, count, dụng cụ, trạng thái vật, ánh sáng, tư thế và framing. Nếu nhiều delta không thể diễn trong duration, sửa cặp ảnh/beat hoặc bố trí cut khi brief cho phép. Không bù endpoint mâu thuẫn bằng prompt dài.

## 5. Prompt chỉ đạo motion và diễn xuất

Cấu trúc ứng viên: hành động chính → thứ tự/nhịp → camera → điều cần giữ → âm thanh nếu dùng. Với reference ảnh, gán vai trò rõ. Không mô tả lại mọi chi tiết đã đúng trong ảnh.

Tách nhịp người và nhịp máy: camera di chuyển chậm không đồng nghĩa tay/người slow motion. Timestamps là chỉ đạo, không timer được bảo đảm. “Cinematic” không thay được hành động/contact/eyeline rõ.

Ví dụ minh họa do phiên này soạn, chưa thử; settings thực phải phù hợp 4s và ảnh đã chuẩn bị:

```text
One continuous shot. The person places the box on the table at an ordinary, purposeful pace. During the first two seconds, lower the box, make contact with the tabletop, and release it. During the remaining two seconds, withdraw both hands while the box stays in place. Keep the camera fixed and the contact point clearly visible. Preserve the person's identity and the box's proportions and label layout. Soft room tone and one contact sound when the box touches the table.
```

Nếu dùng END, thêm chỉ đạo kết thúc phù hợp ảnh và kiểm tra END thể hiện đúng tay đã rút. Nếu request bắt buộc dài hơn timing cần dùng, quyết định rõ phần action/hold và phần sẽ trim; không chỉ đổi số giây trong prompt rồi giả định duration đã đổi.

## 6. Sinh chọn lọc và đặt vào bản dựng ngay

1. Chọn shot có rủi ro chi phối toàn phim để kiểm tra sớm: contact khó hoặc product hero cần đúng. Giữ brief/model/mode/settings và input thực trước submit.
2. Bắt đầu một candidate cho shot đó trong budget được duyệt. Không sinh batch cả phim khi chưa biết ảnh/look/nhịp có dùng được.
3. Đưa candidate vào đúng vị trí timeline. Xem tốc độ thật, thông điệp, nhịp, hai seam và ROI. Sau đó xem từng frame tại vùng nghi ngờ.
4. Nếu đạt, giữ take và tiếp tục shot kế. Nếu fail, phân loại lỗi trước khi sinh lại. Không đổi nhiều biến rồi gán nguyên nhân cho một câu prompt.
5. Với shot dễ, chọn cấu hình có thể dùng trực tiếp khi hợp lý. Không bắt mọi shot qua preview thấp rồi sinh final lần hai; đổi tier/model có thể đổi output và tăng lượt. Chất lượng final vẫn phải được duyệt.

Shot đạt đầu tiên là mẫu look/nhịp để đối chiếu, không chứng minh mọi shot sau cùng cấu hình đều đạt.

## 7. Bảng sửa lỗi ưu tiên ít lần sinh

| Lỗi | Xử lý trước retry | Nếu vẫn cần sinh lại |
|---|---|---|
| Chờ quá lâu ở đầu/cuối | Trim phần thừa, tránh mất hành động chính | Làm rõ onset/action; xét duration hợp động tác |
| Toàn hành động chậm | Kiểm tra playback; retime nếu contact/blur/diễn/audio vẫn hợp | Sửa timing hoặc duration, mỗi lượt một can thiệp có lý do |
| Sai thứ tự/contact/count | Không tăng tốc để che lỗi logic | Sửa blocking hoặc ảnh; đơn giản hóa hành động đúng brief |
| Sai product/identity | Chọn đoạn khác; composite thường nếu khả thi | Sửa reference/shot hoặc chỉ sinh lại shot lỗi |
| Lệch màu/scale nhẹ tại cut | Grade/transform/crop với giới hạn chất lượng | Sửa ảnh nguồn nếu lỗi hệ thống |
| Continuous seam bị pop | Tìm out/in tốt hơn, loại frame rác/hold; không chèn ảnh neo một frame | Dùng frame A thực đã đạt làm START B; END B nếu cần, rồi kiểm tra output thực |
| Geometry hai phía không khớp | Đổi cut/insert chỉ khi brief cho phép | Nếu buộc continuous, cần sửa/sinh lại; không hứa dissolve cứu được |

Tái dùng một frame trích từ output là **ảnh input**, vẫn thuộc workflow không-video-reference. Không upload clip A làm conditioning cho B. Không truyền frame đã sai chi tiết qua cả chuỗi.

Nếu không còn phương án sửa phù hợp budget, dừng shot và báo rõ phần không đạt; không tự đổi ý đồ hoặc chuyển sang motion transfer.

## 8. Ví dụ bản dựng minh họa, không phải kịch bản đã duyệt

Giả sử video sản phẩm 12s, được phép hard cut:

| Shot | Thời lượng dùng minh họa | Nhiệm vụ | Input dự kiến | Nối |
|---|---|---|---|---|
| S01 | 2s | Đặt bối cảnh sử dụng | START; hành động nhỏ | Hard cut sang thao tác |
| S02 | 4s | Đặt sản phẩm lên bàn, thấy contact | START + END nếu cần pose cuối | Cut khi động tác đã đọc được |
| S03 | 3s | Cho thấy một chi tiết/lợi ích | START phù hợp góc cận; motion nhỏ | Hard cut sang hero |
| S04 | 3s | Nhận diện sản phẩm và CTA | Ảnh hero chuẩn; có thể dựng đồ họa trực tiếp nếu brief cho phép | Kết |

Độ dài trên timeline không phải duration tối thiểu của model. S04 không bắt buộc gọi AI video nếu ảnh và đồ họa đã đủ nhiệm vụ; phải xem trong toàn cut để tránh cảm giác kết thúc bằng slideshow ngoài chủ ý. Không ghép bốn shot thành một hành trình camera liên tục chỉ để tránh cut.

## 9. Đo chi phí và acceptance

Ghi tổng tiền thực gồm ảnh/video/edit tính phí và retry; refund chỉ trừ khi thực nhận. Ghi riêng số request, số candidate tính phí, số lượt tới bản xem được, thời gian dựng/sửa. Budget và stop condition đặt trước paid work.

Acceptance: xem được ở tốc độ phát hành; hiểu hành động/thông điệp; product/identity đúng vùng quan trọng; không có contact/count lỗi; seam đạt theo loại cut đã chốt; âm thanh ăn khớp và không có tiếng/nhạc ngoài ý đồ. User acceptance và strict technical verdict lưu riêng.

Dừng khi bản dựng đạt, không tự sinh thêm để “xem có đẹp hơn không”. Không có tỷ lệ đạt hoặc cam kết tiết kiệm cho workflow 0.1.0. Cần một sản phẩm thật để kiểm chứng trước promote. Chuỗi thực có cả START/END tuân thủ case/run AGENTS §7; không tạo run giả ở giai đoạn đề xuất.
