# Phân tích sâu cấu trúc prompt Foyege

Ngày viết: 2026-10-28
Phạm vi: chỉ phân tích cấu trúc, chức năng từng mục, và cơ chế kiểm soát. File này không chứa bản sao nguyên văn hay bản dịch nguyên văn prompt gốc.
Nguồn gốc để đối chiếu (prompt nằm trong bình luận tự trả lời của @Foyege24, không nằm ở bài chính):
- Template A, biến hình và đánh nhau, 11/10: https://x.com/Foyege24/status/2109113006953263233
- Template B, bướm hóa người một cú máy, 23/9: https://x.com/Foyege24/status/2102610496683933915
- Template C, title sequence DEADSHOT, 16/9: https://x.com/Foyege24/status/2100222945499263146
File đi kèm: `foyege-prompt-templates-en.md` (template tiếng Anh tái tạo cấu trúc), `foyege-analysis-and-tests.md` (tổng hợp thảo luận và thử nghiệm).

## 0. Kết luận trước, để đọc nhanh

Prompt của Foyege không hay vì dài, mà hay vì nó làm đúng ba việc mà prompt thông thường hay bỏ sót: (1) chia trách nhiệm cho từng ảnh tham chiếu, (2) biến thời gian thành trạng thái có thể kiểm chứng được, (3) lặp lại quy tắc quan trọng nhất ở cuối, nơi model dễ quên nhất. Phần còn lại của file này mổ ba việc đó ra từng lớp, và chỉ ra chỗ nào là điểm yếu còn lại dù prompt có chặt đến đâu.

## 1. Thứ tự các mục: vì sao thứ tự đó quan trọng hơn độ dài

Cả ba prompt đều đi theo một thứ tự gần như cố định, và thứ tự này tự nó đã là một workflow:

1. Ảnh tham chiếu, mỗi ảnh một nhiệm vụ.
2. Bối cảnh chung.
3. Phong cách.
4. Quay phim, ánh sáng.
5. Nhân vật và hiệu ứng.
6. Quy tắc cốt lõi.
7. Timeline.
8. Âm thanh.
9. Nhất quán, lặp lại.
10. Cấm.

Phân tích chức năng từng lớp:

- Lớp 1, ảnh tham chiếu, là lớp khóa. Nếu lớp này mờ, mọi lớp sau đều trôi. Foyege không viết "dùng ảnh này làm nhân vật", mà gán nhiệm vụ hẹp: ảnh này chỉ lấy dáng tay, ảnh kia chỉ lấy mắt, ảnh còn lại chỉ lấy giáp cuối. Nhiệm vụ càng hẹp, model càng ít có cớ trộn nền của ảnh này vào mặt của ảnh kia.
- Lớp 2 và 3, bối cảnh và phong cách, là lớp khung. Chúng trả lời câu hỏi: clip này thuộc thế giới nào, chất liệu nào, ánh sáng nào. Nếu không có lớp này, model sẽ tự chọn một thế giới chung chung, thường là thế giới sạch, sáng, và không có cá tính.
- Lớp 4, quay phim, là lớp góc nhìn. Nó không chỉ nói "quay đẹp", mà nói camera ở đâu, rung thế nào, tiêu cự nào, focus khóa vào đâu. Đây là lớp quyết định clip có cảm giác phim hay cảm giác video AI trôi.
- Lớp 5, nhân vật và hiệu ứng, là lớp hành vi. Nó mô tả chuyển động bằng trọng lượng và cơ chế, không chỉ bằng tính từ cảm xúc. Ví dụ: giáp lắp từng mảnh từ lõi ra ngoài, chi tiết mặt lắp cuối; sương trôi nhanh ở lớp trước, lớp nền trôi chậm ở lớp sau. Cơ chế thì kiểm chứng được, cảm xúc thì không.
- Lớp 6, quy tắc cốt lõi, là lớp biên. Nó nói rõ cái gì không được đổi: bên trái luôn là bên trái, cái gì đứng yên, cái gì không được xảy ra. Prompt thông thường hay quên lớp này, nên model tự do đổi phe, đổi hướng, đổi tỉ lệ mà không bị coi là sai.
- Lớp 7, timeline, là lớp thời gian. Xem chi tiết ở mục 3.
- Lớp 8, âm thanh, tưởng là phụ nhưng lại là neo nhịp. Tiếng bật điện khi đèn trở lại, tiếng click ở điểm cắt, tiếng trầm khi tên phim hiện ra, tất cả đều đánh dấu mốc thời gian cho người xem, dù hình có trôi một chút thì tai vẫn nhận ra nhịp.
- Lớp 9, nhất quán lặp lại, là lớp chống quên. Model xử lý prompt theo kiểu chú ý giảm dần về cuối, nên quy tắc quan trọng nhất phải xuất hiện lại ở cuối, không chỉ ở đầu. Foyege lặp lại: cùng mặt, cùng đồ, cùng vị trí, cùng thứ tự lắp giáp, cùng motif. Lặp lại ở đây không phải là thừa, mà là cơ chế bù cho việc model hay quên đoạn đầu khi viết tới đoạn cuối.
- Lớp 10, cấm, là lớp loại trừ. Nhưng cách viết cấm của Foyege đáng chú ý: phần lớn lệnh cấm được viết kèm với lệnh khẳng định thay thế. Thay vì chỉ nói không có cái này, prompt nói rõ thay vào đó là cái gì: không phải fade toàn cục, mà là đèn tắt từng cái; không phải biến hình tức thì, mà là lắp từng mảnh; không phải slow motion, mà là cắt cứng và giữ hình rõ.

Bài học rút ra: một prompt tốt không phải là một đoạn văn dài miêu tả cảnh, mà là một bản spec có thứ tự: khóa trước, khung sau, hành vi sau nữa, biên, thời gian, âm thanh, rồi lặp lại và cấm. Đảo thứ tự cũng làm prompt yếu đi, vì model sẽ ưu tiên thông tin xuất hiện sớm và rõ ràng hơn.

## 2. Ảnh tham chiếu: một ảnh, một nhiệm vụ, và cơ chế loại trừ nền

Ba trường hợp cho thấy ba kiểu gán nhiệm vụ khác nhau, nhưng cùng một nguyên tắc:

- Trường hợp biến hình: nhiều ảnh, mỗi ảnh một vai trò rõ ràng. Ảnh cảnh chỉ lấy không gian, ảnh dáng tay chỉ lấy cử chỉ, ảnh giáp cuối chỉ lấy giáp, ảnh nhân vật gốc chỉ lấy mặt và đồ, ảnh vũ khí chỉ lấy vũ khí và tay cầm chính. Đi kèm mỗi ảnh là lệnh loại trừ: không lấy nền, không lấy chữ của ảnh không phải ảnh cảnh.
- Trường hợp bướm hóa người: chỉ hai ảnh, và ảnh thứ hai còn hẹp hơn: chỉ lấy đôi mắt. Mặt, tóc, trang phục của nhân vật nữ không lấy từ ảnh mắt, mà theo nhân vật đã có sẵn. Đây là điểm tinh tế: nếu lấy cả mặt từ ảnh mắt, nhân vật sẽ đổi mặt; nếu chỉ lấy mắt, motif mắt mới được giữ mà mặt vẫn là mặt cũ.
- Trường hợp DEADSHOT: một ảnh chính duy nhất, nhưng ảnh đó phải có phong cách mạnh. Từ một ảnh đó, prompt suy ra cả một hệ: mặt, tóc, vest, găng, súng đều là cùng một người; còn đối thủ thì chỉ được phép hiện dạng mảnh, không được phép có mặt rõ. Nghĩa là ảnh tham chiếu không chỉ khóa nhân vật chính, mà còn khóa luôn mức độ rõ của nhân vật phụ.

Ba cơ chế loại trừ đi kèm:
- Loại trừ nền và chữ: nền của ảnh nhân vật không được mang sang cảnh chính.
- Loại trừ vai trò: ảnh mắt không được quyền quyết định mặt, ảnh dáng tay không được quyền quyết định giáp.
- Loại trừ mức độ rõ: nhân vật phụ không được rõ bằng nhân vật chính, dù model có xu hướng làm mọi mặt đều rõ như nhau.

Điểm yếu còn lại của lớp này: ảnh tham chiếu chỉ khóa được cái đã có trong ảnh. Nó không khóa được cái chưa có: biểu cảm mới, góc mặt mới, tư thế mới. Vì vậy Foyege luôn kết hợp ảnh tham chiếu với timeline và với cắt nối, chứ không tin rằng một ảnh là đủ cho cả clip.

## 3. Timeline: ba cách kiểm soát thời gian, và vì sao phải chọn một

Đây là phần quan trọng nhất, vì nó trả lời trực tiếp phàn nàn "khó điều khiển timeline quá" trong thử nghiệm.

### 3.1. Cách 1: một beat một giây (bài biến hình và đánh nhau)

- Cơ chế: clip 15 giây thì có 15 beat, clip 30 giây thì có 30 beat. Mỗi beat ghi đủ ba thông tin: camera làm gì, nhân vật làm gì, hiệu ứng nào xuất hiện, và trạng thái sau beat đó là gì.
- Vì sao nó hiệu quả: model không còn phải tự chia thời gian cho một đoạn văn dài. Nó chỉ cần làm đúng một việc trong một giây, rồi chuyển sang việc tiếp theo. Thời gian trở thành một danh sách việc, không còn là một cảm giác mơ hồ.
- Vì sao nó vẫn có giới hạn: model sinh video hiện tại không đếm giây chính xác. Thử nghiệm của chúng ta đã chứng minh điều này: prompt ghi beat 4 giây nhưng output ra 10 giây, beat bị kéo giãn. Vì vậy một beat một giây chỉ là định hướng mạnh, không phải là khóa cứng. Muốn khóa cứng thì vẫn phải cắt ở edit, lấy đúng đoạn beat còn đúng mặt, bỏ phần còn lại.
- Khi nào dùng: khi clip là chuỗi hành động liên tục, có đối thủ, có va chạm, và mỗi giây đều có một thay đổi rõ ràng.

### 3.2. Cách 2: timeline theo trạng thái môi trường (bài bướm hóa người)

- Cơ chế: không chia theo giây trừu tượng, mà chia theo trạng thái của môi trường. Đèn tắt dần từng cái, rồi đen hoàn toàn, rồi đèn bật lại cùng lúc. Mỗi trạng thái là một mốc thời gian mà người xem nhìn thấy được, không cần đếm giây.
- Vì sao nó hiệu quả hơn chia giây trong trường hợp này: model khó đếm giây, nhưng dễ vẽ trạng thái. Nó vẽ được "đèn tắt" và "đen hoàn toàn" tốt hơn nhiều so với việc vẽ "ở giây thứ 7,5 thì đèn tắt". Trạng thái là thứ nhìn thấy được trong khung hình, còn giây là thứ trừu tượng nằm ngoài khung hình.
- Cơ chế phụ quan trọng: motif mắt. Đốm mắt trên cánh bướm và vân mắt của nhân vật nữ là cùng một họa tiết. Khi đèn tắt hết, chỉ còn hai đốm sáng đó, rồi khi đèn bật lại, hai đốm đó đã là mắt của nhân vật nữ. Motif này làm cho chuyển dạng không cần giải thích: người xem tự nhận ra cùng một chủ thể, vì họa tiết không đổi dù hình dạng đổi.
- Quy tắc đèn chết thật: khi đèn cuối cùng tắt, không gian phải đen hoàn toàn, không còn rim light, không còn fill. Đây là quy tắc khó nhất cho model, vì model có xu hướng giữ một chút ánh sáng để mặt còn nhìn thấy được. Foyege phải ghi rõ điều này, và ghi lại ở phần tóm tắt cuối, vì model rất hay vi phạm đúng chỗ này.
- Đoạn giữ cuối: khoảng 3 giây chân dung giữ yên, môi khép, thở nhẹ, focus khóa mắt. Đoạn giữ này không phải là phần thừa. Nó là chỗ khán giả xác nhận: đây là cùng một người, đây là cảm xúc cuối, và clip kết thúc ở một trạng thái rõ ràng, không phải ở giữa một chuyển động dở dang.
- Khi nào dùng: khi clip là một lần biến đổi duy nhất, cần cảm giác kỳ ảo nhưng vẫn rõ ràng, và khi muốn giấu điểm chuyển dạng trong bóng tối thay vì vẽ trực tiếp quá trình biến đổi.

### 3.3. Cách 3: montage mảnh vỡ và frame-drop (bài DEADSHOT)

- Cơ chế: không bắt model vẽ chuyển động liên tục đúng từng giây, mà bắt nó vẽ nhiều mảnh ngắn, mỗi mảnh 0,3-0,8 giây, xen kẽ đoạn giữ hình rõ 0,5-1 giây. Nhịp là: cắt nhanh, bắt một frame, rồi lại tăng tốc.
- Frame-drop, hiểu đúng: giữ một tư thế rõ trong chốc lát, rồi một vệt mờ theo hướng chuyển động, rồi nhảy sang tư thế tiếp theo. Sương và lớp phơi sáng vẫn trôi liên tục, nên thời gian vẫn cảm thấy đang chạy, dù model không cần vẽ chuyển động mượt từ tư thế này sang tư thế kia. Đây không phải là slow motion, cũng không phải là giật hình ngẫu nhiên. Nó là một kiểu cắt có chủ ý.
- Vì sao nó giấu được điểm yếu của model: điểm yếu lớn nhất của model video là chuyển động liên tục dài, vì càng dài càng trôi mặt, trôi tay, trôi tỉ lệ. Montage mảnh vỡ cắt bỏ đúng phần đó: model chỉ cần giữ được một tư thế rõ trong nửa giây, rồi cắt đi trước khi nó kịp trôi. Người xem tự ghép các mảnh lại thành một trận đánh, dù trên thực tế không có trận đánh trọn vẹn nào được vẽ ra.
- Quy tắc một mảnh, một thông tin: mỗi shot chỉ cho người xem một thứ: một ánh mắt, một bàn tay cầm súng, một bước chân, một vệt đỏ. Nếu một shot chứa hai thông tin, nó sẽ bị cắt ngắn và thông tin thứ hai sẽ bị mất trong nhịp nhanh. Vì vậy prompt phải viết mỗi shot như một câu ngắn, không phải một đoạn văn.
- Quy tắc đối thủ dạng mảnh: zombie không bao giờ hiện nguyên mặt rõ. Nó chỉ hiện tay, vai, lưng, mặt nghiêng mờ. Điều này có hai tác dụng: một là giữ nhân vật chính luôn nổi bật nhất, hai là giảm gánh nặng cho model, vì model không cần giữ nhất quán cho một nhân vật phụ có mặt rõ.
- Đoạn cuối là neo timeline: montage dừng đột ngột, cắt cứng sang nền đen, tên phim giữ yên tới cuối, sương vẫn trôi chậm phía sau. Tên phim ở đây không chỉ là đồ họa, mà là một trạng thái kết thúc rõ ràng: sau một chuỗi cắt nhanh, người xem được một điểm dừng cố định để thở và ghi nhớ tên phim.
- Khi nào dùng: khi clip là title sequence, teaser, hoặc bất kỳ đoạn nào cần cảm giác nhanh, mạnh, điện ảnh, nhưng không cần và không nên vẽ trọn một hành động liên tục.

### 3.4. So sánh ba cách, và quy tắc chọn

- Một beat một giây: mạnh khi hành động liên tục và có đối thủ, yếu khi model kéo giãn thời gian.
- Trạng thái môi trường: mạnh khi chỉ có một lần biến đổi, yếu khi cần nhiều hành động khác nhau trong cùng một clip, vì trạng thái môi trường không đủ để chia nhiều hành động.
- Montage mảnh vỡ: mạnh khi cần nhịp nhanh và giấu điểm yếu chuyển động, yếu khi cần cảm xúc kéo dài, vì cắt quá nhanh sẽ không cho khán giả thời gian đọc vi biểu cảm.

Quy tắc chọn, rút ra từ cả ba bài: mỗi clip chỉ chọn một cách làm timeline chính. Trộn cả ba trong một clip sẽ làm model không biết đâu là nhịp chính, và người xem cũng không biết đâu là điểm cần chú ý. Nếu clip cần cả biến đổi và hành động, hãy tách thành hai clip: một clip biến đổi theo trạng thái, một clip hành động theo beat, rồi cắt nối ở edit.

## 4. Không gian: khóa trục, khóa cái đứng yên, và khóa mức độ rõ

Ba khóa không gian xuất hiện lặp lại, và chúng quan trọng không kém timeline:

- Khóa trục: nhân vật này luôn ở bên trái, nhân vật kia luôn ở bên phải, không vượt trục. Nếu không có khóa này, model sẽ tự đổi bên khi quay camera, và người xem sẽ mất phương hướng: ai đang đánh ai, ai đang nhìn ai.
- Khóa cái đứng yên: prompt ghi rõ cái gì không được động, không chỉ cái gì được động. Môi trường đóng băng trong khi nhân vật động, vai đứng yên trong khi mắt động, camera đứng yên trong khi đầu xoay. Đây là cơ chế tách tầng, và nó chính là cơ chế đã được thử nghiệm thành công ở test mắt và test cascade: một shot chỉ cho một tầng động, các tầng còn lại đứng yên tuyệt đối.
- Khóa mức độ rõ: nhân vật chính luôn rõ, nhân vật phụ luôn mờ hoặc chỉ hiện dạng mảnh, lớp sương luôn mờ, lớp phơi sáng luôn chậm. Mức độ rõ là một dạng thứ bậc thị giác, và prompt phải ghi rõ thứ bậc đó, nếu không model sẽ làm mọi thứ rõ như nhau và khung hình sẽ phẳng.

Điểm chung của ba khóa này: chúng đều là những thứ người xem cảm nhận được ngay khi bị vi phạm, dù họ không nói ra được tên quy tắc. Đổi bên thì thấy rối, vai động theo mắt thì thấy như con rối, nhân vật phụ rõ quá thì thấy nhân vật chính bị chìm. Vì vậy prompt phải khóa chúng bằng câu khẳng định, không phải bằng câu phủ định chung chung.

## 5. Âm thanh: neo nhịp, không phải nhạc nền

Cả ba prompt đều viết âm thanh rất cụ thể, và đều cấm thoại, cấm phụ đề, và phần lớn cấm nhạc. Âm thanh ở đây không phải để cho hay, mà để đánh dấu thời gian:

- Tiếng bật điện đánh dấu khoảnh khắc đèn trở lại và nhân vật xuất hiện.
- Tiếng click cơ khí đánh dấu điểm cắt frame-drop.
- Tiếng trầm khi tên phim hiện ra đánh dấu điểm dừng của montage.
- Đoạn drop-out âm thanh ở giữa bài DEADSHOT là một khoảng lặng có chủ ý, để người xem cảm nhận được nhịp đã đổi, dù hình vẫn đang cắt nhanh.

Bài học: nếu clip không có âm thanh, timeline chỉ còn dựa vào hình, và hình của model thì hay trôi. Âm thanh là một kênh thứ hai để khóa nhịp, và nó rẻ hơn nhiều so với việc bắt model vẽ đúng từng giây.

## 6. Nhóm cấm: phân loại, và vì sao viết dạng khẳng định hiệu quả hơn

Nhóm cấm trong ba prompt có thể phân thành năm loại, và mỗi loại có một cách xử lý khác nhau:

1. Cấm về chữ và đồ họa: không chữ, không phụ đề, không watermark, không tiêu đề phụ. Loại này model hay vi phạm nhất, vì nó có xu hướng tự thêm chữ vào khung hình khi không biết vẽ gì thêm.
2. Cấm về không gian: không vượt trục, không đổi tỉ lệ, không thu nhỏ nhân vật vô cớ, không thêm nhân vật trùng lặp.
3. Cấm về thời gian: không slow motion, không freeze frame, không biến hình tức thì, không giật hình ngẫu nhiên. Lưu ý: freeze frame bị cấm ở khâu sinh, nhưng giữ hình rõ ở khâu edit thì không bị cấm. Hai việc này khác nhau: freeze frame trong sinh là model tự đóng băng một frame, còn giữ hình rõ trong edit là người dựng chọn một tư thế rõ và giữ nó trong thời gian thực.
4. Cấm về chất liệu: không hoạt hình, không nhựa, không noise cố định, không xước nặng, không neon, không máu nhỏ giọt cho tiêu đề. Loại này giữ cho clip ở đúng thế giới đã chọn, không bị trôi sang một phong cách khác giữa chừng.
5. Cấm về cảm xúc và thoại: không thoại, không lồng tiếng, không cười khi cần giữ mặt lạnh, không nhìn vào camera khi cần nhìn lệch. Loại này giữ cho diễn xuất không bị phá bởi một biểu cảm lạc tông.

Vì sao viết dạng khẳng định hiệu quả hơn: prompt là lệnh cho model vẽ cái gì, không phải là danh sách những thứ model không được nghĩ tới. Khi viết "đừng cười", model vẫn phải xử lý khái niệm cười rồi mới phủ định nó, và nó thường làm ngược lại. Khi viết "giữ mặt lạnh, môi khép", model có một hình ảnh cụ thể để vẽ. Vì vậy trong template, mỗi lệnh cấm đều nên đi kèm một lệnh khẳng định thay thế.

## 7. Điểm yếu còn lại, dù prompt có chặt đến đâu

Phân tích sâu cũng phải chỉ ra giới hạn, nếu không file này sẽ thành ca ngợi:

- Model không đếm giây chính xác. Một beat một giây là định hướng mạnh, không phải khóa cứng. Thử nghiệm đã chứng minh: beat 4 giây thành 10 giây, và chỉ có cắt ở edit mới lấy lại được đúng nhịp.
- Model không giữ được mặt trong clip dài. Càng dài, mặt càng trôi, tóc càng đổi, camera càng xoay. Vì vậy mọi prompt dài đều phải đi kèm chiến lược cắt ngắn: chỉ lấy đoạn đầu còn đúng mặt, hoặc chia thành nhiều clip ngắn rồi cắt nối.
- Model không có xương mắt riêng. Diễn xuất mắt đi trước đầu theo sau không thể ép trong một clip duy nhất, mà phải tách thành shot mắt và shot đầu, rồi cắt nối bằng frame cuối của shot trước làm ảnh đầu của shot sau.
- Model có xu hướng làm mọi thứ rõ và sáng. Nó hay giữ một chút ánh sáng trong cảnh đen hoàn toàn, hay cho nhân vật phụ mặt rõ như nhân vật chính, hay thêm chữ vào khung hình. Vì vậy các quy tắc về đen thật, về mức độ rõ, và về cấm chữ phải được lặp lại ở cuối prompt, không chỉ ghi một lần ở đầu.
- Prompt càng dài, model càng quên đoạn đầu. Vì vậy quy tắc quan trọng nhất phải xuất hiện lại ở cuối. Nếu một quy tắc chỉ xuất hiện một lần ở giữa prompt, khả năng cao là nó sẽ bị bỏ qua.

Kết luận cho người làm: prompt của Foyege là một bản spec tốt, nhưng nó không thay thế được edit. Spec giúp model sinh ra nguyên liệu đúng hướng, còn edit mới là nơi quyết định timeline cuối cùng, tốc độ cuối cùng, và nhịp cuối cùng. Đây cũng là kết luận đã được thử nghiệm xác nhận ở file tổng hợp.

## 8. Checklist dùng lại cho một clip mới, không cần copy prompt gốc

Khi viết prompt cho một clip mới, kiểm tra đủ 10 điểm này trước khi sinh:

1. Mỗi ảnh tham chiếu đã có một nhiệm vụ hẹp, và đã ghi rõ không lấy nền, chữ của ảnh không phải ảnh cảnh?
2. Bối cảnh, phong cách, ánh sáng đã đủ để model không tự chọn một thế giới chung chung?
3. Camera đã ghi rõ vị trí, tiêu cự, rung, focus khóa vào đâu?
4. Hành động đã được mô tả bằng cơ chế và trọng lượng, không chỉ bằng tính từ cảm xúc?
5. Đã khóa trục trái, phải, và đã ghi rõ cái gì đứng yên trong khi cái gì động?
6. Đã chọn một cách làm timeline duy nhất cho clip này: beat từng giây, trạng thái môi trường, hay montage mảnh vỡ?
7. Mỗi beat hoặc mỗi shot chỉ chứa một hành động và một thông tin?
8. Âm thanh đã có ít nhất một mốc đánh dấu thời gian: tiếng bật, tiếng click, tiếng trầm, hoặc khoảng lặng?
9. Quy tắc quan trọng nhất đã được lặp lại ở cuối prompt?
10. Mỗi lệnh cấm đã đi kèm một lệnh khẳng định thay thế?

Nếu thiếu một điểm, bổ sung điểm đó trước, đừng viết dài thêm phần miêu tả cảnh. Phần miêu tả cảnh dài thêm thường làm prompt yếu đi, vì nó thêm thông tin mơ hồ vào một bản spec cần chính xác.
