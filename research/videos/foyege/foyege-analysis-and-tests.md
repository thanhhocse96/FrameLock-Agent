# Tổng hợp thảo luận Foyege: phân tích, thử nghiệm, và chốt

Ngày tổng hợp: 2026-10-28
Ngôn ngữ thảo luận: tiếng Việt
File đi kèm, dành cho agent khác phân tích prompt: `foyege-prompt-templates-en.md` (cùng thư mục)
File phân tích sâu cấu trúc prompt (riêng, không gộp vào file này): `foyege-prompt-structure-deep-analysis.md` (cùng thư mục)

## Ghi chú sửa đổi — cập nhật 2026-10-28, sau yêu cầu của user

Những gì đã sửa trong lần cập nhật này, và chỉ những thứ này:
- Bổ sung link nguồn gốc X vào từng mục 2.1, 2.2, 2.3 dưới đây, mỗi mục gắn đúng link bài của nó, để người đọc và agent khác mở được bản gốc mà không phải dò lại.
- Bổ sung chính ghi chú sửa đổi này vào đầu file, ghi rõ đã sửa gì.
- Không bổ sung bản dịch nguyên văn prompt gốc của Foyege vào file này hay file prompt. Lý do đã trao đổi ở chat: đăng public trên X không phải là giấy phép mở, và file prompt chỉ giữ dạng tái tạo cấu trúc.
- Không gộp phân tích sâu vào file này. Phân tích sâu nằm ở file riêng nêu trên.

Link nguồn gốc, theo từng mục:
- Mục 2.1, biến hình và đánh nhau, 11/10: https://x.com/Foyege24/status/2109113006953263233
- Mục 2.2, bướm hóa người, 23/9: https://x.com/Foyege24/status/2102610496683933915
- Mục 2.3, title DEADSHOT, 16/9: https://x.com/Foyege24/status/2100222945499263146

## 0. Tóm tắt một câu

Foyege không công bố một "workflow chính thức" dạng tài liệu, nhưng workflow của ổng lộ ra ở bình luận tự trả lời trên X: prompt có cấu trúc chặt, timeline chia beat hoặc chia trạng thái, và kiểm soát diễn xuất bằng cách tách tầng chuyển động rồi cắt nối ở khâu edit. Thử nghiệm của chúng ta xác nhận đúng điểm này: prompt chữ thuần chỉ định hướng được diễn xuất, không ép chính xác được timeline; muốn timeline đúng thì phải khóa ảnh, chia mảnh, và làm tốc độ ở edit.

## 1. Câu hỏi gốc và quá trình tìm

### 1.1. Câu hỏi gốc

- User hỏi: Foyege chia sẻ workflow ở đâu?
- Bối cảnh: user có repo FrameLock-Agent, trong đó có ý tưởng học từ chuyên gia như Foyege khi add thông tin vào. Theo luật raw của repo đó, một nguồn học cần có video/bài cụ thể kèm URL và ngày lấy, kênh chung chưa đủ.
- Trước đó, assistant đã phản biện: vòng raw -> digest -> mapping -> template của repo còn trống, template duy nhất đúc theo ngoại lệ, và tên Foyege không xuất hiện trong repo công khai.

### 1.2. Kết quả tìm ban đầu (chưa tìm thấy)

Đã tra: memory, web với nhiều biến thể tên (foyege, foyege24, fo_yege1664, foyege27), social search Instagram/Facebook/Threads, Douyin/Xiaohongshu/Weibo, X phần nhìn thấy không cần đăng nhập.

Kết quả ban đầu:
- Không tìm thấy bài/video hướng dẫn riêng, file workflow, hay prompt collection nào gắn tên Foyege.
- Định danh đã xác minh từ credit trong các video re-upload series Malfoy/Draconia:
  - Instagram @foyege24, X @foyege24, YouTube @fo_yege1664, TikTok @foyege27.
  - Bilibili: trang cá nhân ID 1383971575, tên hiển thị Foyege (dạng tiếng Trung), mở trực tiếp ngày 2026-10-28 bị lỗi 429 nên chưa đọc được danh sách video bên trong.
  - TikTok @foyege27 khi mở ngày 2026-10-28: bio ghi "aigc creator", 52.700 follower, 2 video, 208.900 like (một lần crawl trước đó ghi 39,4k follower, số liệu không nhất quán giữa các lần crawl).
- X @Foyege24 khi kiểm tra trực tiếp ngày 2026-10-28 (không đăng nhập):
  - Tên Foyege, đã verified, 50,2K follower, 244 following, 1.692 bài đăng, tham gia từ tháng 7/2014.
  - Bio ghi đại ý: AIGC blogger, VSC Creator, founder INFINITY, đạo diễn độc quyền của Libtv, link bio trỏ tới pippit.ai.
  - Bài ghim ngày 20/10: Part Three series Malfoy, video khoảng 4 phút 47 giây, 927K view, 18K like.
  - Các bài nhìn thấy khác: 26/10 cảm ơn fan, than bị người khác repost tác phẩm để bán khóa/sản phẩm AI, báo Part IV sắp ra; 25/10 ghi chú nhạc; 24/10 video Yule Ball; 22/10 dẫn link sang YouTube/TikTok.
  - Không bài visible nào chia sẻ prompt, tutorial, danh sách tool hay behind-the-scenes.
  - Giới hạn: X hiện tường đăng nhập sau khoảng 5 bài đầu, nên phần còn lại của 1.692 bài và các tab Replies/Reposts/Media/Articles chưa kiểm chứng được ở thời điểm đó.

### 1.3. Facebook: đúng là ổ đăng lại, không phải nguồn workflow

User nghi các tài khoản ăn cắp/repost là nơi đầu tiên share trên Facebook. Kết quả search Facebook:
- Web search, kể cả dạng site:facebook.com, không trả về post Facebook nào nhắc workflow của Foyege.
- Social search Facebook trả về nhiều reel đăng lại video thành phẩm Malfoy/Draconia, ví dụ các page Hidromoss, Có Hay Không, Chơi game một mình, và một page tên Foyege.
- Không bài nào trong số đó chia sẻ prompt, tutorial, danh sách tool hay quy trình làm. Bình luận chủ yếu là khen, hỏi tên nhạc, hỏi phần tiếp theo, tranh cãi ghi credit.
- Ở một bài mang tên Foyege trên Facebook, có người bình luận nghi đây là page giả và nói Foyege không dùng Facebook. Điều này khớp với danh sách kênh chính thức không có Facebook.
- Kết luận phần này: Facebook là nơi dễ thấy bản đăng lại nhất, nhưng chưa phải nơi chứng minh được workflow gốc. Trong đợt search đó cũng chưa thấy bài bán khóa nào gắn tên Foyege trên Facebook, dù chính Foyege trên X ngày 26/10 có than phiền bị đăng lại để bán khóa/sản phẩm AI.

### 1.4. Instagram: cần liên kết tài khoản mới đọc sâu bằng Graph

User yêu cầu dùng Graph để search sâu cả bình luận trên Instagram, với lập luận Muse do Meta làm ra.
Kết quả kiểm tra:
- Instagram CLI của user chưa liên kết tài khoản nào (accounts trả về rỗng), nên không đọc được bài và bình luận của @foyege24 qua CLI.
- Muse do Meta làm ra không đồng nghĩa với việc được dùng Graph nội bộ để lục tài khoản người khác. Truy cập vẫn phải qua tài khoản của chính user đã liên kết qua Meta Accounts Center.
- Trong lúc chờ liên kết, search qua chỉ mục công khai:
  - Lọc authors=@foyege24 với truy vấn workflow/tutorial/behind the scenes/prompt/tools: 0 kết quả.
  - Bỏ lọc authors, cùng nhóm truy vấn workflow: 0 kết quả.
  - Truy vấn rộng foyege24 Malfoy/Draconia: 49 bài, phần lớn là reaction/đăng lại, trong đó có 1 reel của chính @foyege24 là Yule Ball, Part IV Coming, đăng 24/10, 140K like, 4,3K bình luận.
  - Bình luận ở đó chủ yếu là khen, bàn chuyện tình tay ba, hỏi phần tiếp theo, hỏi nhạc nền, chỉ đường sang Instagram/YouTube của Foyege để xem đủ tập. Không có bình luận nào tiết lộ workflow, tên tool hay prompt.
- Giới hạn: đây là kết quả từ search công khai, không phải toàn bộ bình luận từng bài qua Graph. Muốn đọc sâu từng bình luận thì cần user liên kết Instagram trước.

## 2. Bước ngoặt: workflow nằm ở bình luận trên X, với sản phẩm khác

User gửi 3 link X và yêu cầu xem học được gì. Cả 3 đều cho thấy cùng một pattern: bài chính đăng video thành phẩm, bình luận tự trả lời của Foyege đăng prompt.

### 2.1. Bài 11/10: biến hình và đánh nhau, thần thoại Trung Quốc cơ giới hóa

Nguồn gốc: https://x.com/Foyege24/status/2109113006953263233 — prompt nằm trong bình luận tự trả lời của @Foyege24, không nằm ở bài chính.

- Video 1 phút 38 giây, bài hợp tác trả phí, ghi là làm bằng Seedance 2.5 trong Pippit 3D Director Studio.
- Cảnh báo quan trọng: vì là quảng cáo, không được suy ra series Malfoy cũng làm bằng tool này.
- Trong bình luận có 2 prompt: một cho cảnh biến hình, một cho cảnh đánh nhau trên không.
- Cấu trúc prompt, tóm tắt: ảnh tham chiếu mỗi ảnh một nhiệm vụ; bối cảnh chung; phong cách; cách quay; quy tắc nhân vật và hiệu ứng; quy tắc cốt lõi; timeline chia beat theo từng giây; âm thanh; quy tắc nhất quán lặp lại; danh sách cấm.
- Timeline: clip 15 giây có 15 beat, clip 30 giây có 30 beat, mỗi beat ghi đủ camera, hành động và hiệu ứng.
- Khóa không gian: nhân vật này luôn ở bên trái, nhân vật kia luôn ở bên phải, không vượt trục.
- Khóa cái không động: có đoạn môi trường đóng băng trong khi nhân vật, tia chớp và camera vẫn động; cấm slow-motion, cấm freeze frame, cấm thoại.
- Biến hình phải lắp từng mảnh, từ lõi ngực ra ngoài, chi tiết mặt lắp cuối cùng, không được xuất hiện tức thì.
- Giới hạn: một câu trả lời lồng trong bài này về việc dùng model nào cần đăng nhập mới mở được, nên chưa xác minh được phần đó.

### 2.2. Bài 23/9: bướm hóa thành người phụ nữ, một cú máy dài

Nguồn gốc: https://x.com/Foyege24/status/2102610496683933915 — prompt nằm trong bình luận tự trả lời của @Foyege24, không nằm ở bài chính.

- Video 11 giây, prompt trong bình luận dài khoảng 13 giây, một cú máy liên tục, không dùng video tham chiếu.
- Chỉ dùng 2 ảnh tham chiếu: một ảnh con bướm, một ảnh chỉ đôi mắt của nhân vật nữ. Mặt, tóc và trang phục của nhân vật nữ theo nhân vật đã có sẵn, không lấy từ ảnh mắt.
- Mấu chốt nhất quán: đốm mắt trên cánh bướm được thiết kế giống hệt vân mắt của nhân vật nữ. Khi chuyển dạng, motif này là cầu nối nhận diện, mạnh hơn câu "giữ nguyên mặt".
- Camera: handheld có trọng lượng thật, thở, lệch khung nhỏ, quán tính, không push-in, không zoom, người quay đứng yên, tiêu cự tele vừa, focus cuối cùng khóa vào mắt.
- Ánh sáng làm đồng hồ cho timeline: đèn hành lang tắt dần từng cái từ xa tới gần, có khoảng thời gian rõ giữa các lần tắt, không phải fade toàn cục; sau đèn cuối cùng tắt thì không gian phải đen hoàn toàn, không còn rim light hay fill; chỉ còn hai đốm sáng mờ; rồi đèn bật lại cùng lúc và nhân vật nữ đã đứng sẵn đó.
- Cuối clip giữ chân dung khoảng 3 giây: đứng yên, môi khép, vi biểu cảm, thở nhẹ, tóc động nhẹ, focus khóa mắt, không freeze ảnh, không fade sớm.
- Âm thanh: ambience hành lang trầm, tiếng điện yếu khi mỗi đèn tắt, một tiếng bật điện ngắn khi đèn trở lại, hơi thở cuối clip; không nhạc, không thoại, không phụ đề.

### 2.3. Bài 16/9: title sequence DEADSHOT, Minimax H3

Nguồn gốc: https://x.com/Foyege24/status/2100222945499263146 — prompt nằm trong bình luận tự trả lời của @Foyege24, không nằm ở bài chính.

- Video dọc khoảng 15 giây, thể loại mở đầu phim ngắn kinh dị zombie, tên phim DEADSHOT.
- Tool ghi trong bài: Minimax H3, image-to-video, chọn ảnh tham chiếu có phong cách mạnh.
- Nhân vật chính duy nhất: phụ nữ trưởng thành mặc đồ chiến thuật đen, khóa mặt, tóc, vest, găng tay và súng.
- Đối thủ zombie chỉ xuất hiện dạng mảnh: mặt nghiêng mờ, tay vươn, vai, lưng, dáng mất cân bằng. Không bao giờ cho zombie hiện nguyên mặt rõ như nhân vật chính.
- Đây là bài giải quyết timeline theo cách khác hẳn hai bài trên, và là bài quan trọng nhất cho vấn đề timeline khó điều khiển:
  - Thay vì bắt model chạy chuyển động liên tục đúng từng giây, prompt bắt nó chạy montage mảnh vỡ: mỗi shot khoảng 0,3-0,8 giây, xen kẽ đoạn giữ hình rõ khoảng 0,5-1 giây.
  - Nhịp: cắt nhanh, bắt một frame, rồi lại tăng tốc.
  - Frame-drop được định nghĩa kiểu: giữ một tư thế rõ, rồi một vệt mờ theo hướng chuyển động, rồi nhảy sang tư thế tiếp theo. Sương và lớp phơi sáng vẫn trôi liên tục, tạo cảm giác thời gian vẫn chạy, dù model không cần vẽ chuyển động mượt.
  - Không vẽ trọn một trận đánh. Chỉ vẽ ba mảnh: trước khi chạm, khoảnh khắc chạm, sau khi chạm, để người xem tự ghép lại.
  - Các lớp chuyển động có tốc độ khác nhau: sương trước mặt trôi nhanh, lớp phơi sáng nền trôi chậm, vệt đen kéo dài rồi tan.
  - Timeline chia 5 đoạn lớn: dựng nhân vật, mảnh đối đầu đầu tiên, đỏ và phơi sáng kép xen kẽ, cao trào trừu tượng, rồi dừng montage đột ngột để hiện tên phim và giữ tới cuối. Đoạn cuối là neo timeline: cắt cứng sang nền đen, tên phim giữ yên, sương vẫn trôi chậm phía sau.
  - Âm thanh: ambience trầm thưa, tiếng vải, tiếng va chạm đồ, một tiếng súng khô, tiếng click cơ khí ở các điểm cắt frame-drop, một đoạn drop-out âm thanh ở giữa, một tiếng trầm kiềm chế khi tên phim hiện ra.
- Giới hạn: bài này hiển thị tổng 5 bình luận nhưng phần còn lại sau bình luận tự đăng prompt và một bình luận của người khác đã bị tường đăng nhập chặn, nên chưa đọc được hết các bình luận còn lại.

### 2.4. Phân tích bên ngoài về Foyege và Draconia (không phải workflow kỹ thuật)

Các phân tích tìm được chủ yếu là phân tích nội dung và vì sao hay, không phải phân tích kỹ thuật làm:
- Video lý thuyết về 3 tập Foyege: chạy lại cả 3 tập, chỉ ra cảnh nào lấy từ sách/phim, cảnh nào Foyege đổi đi, chi tiết nào đang gài cho tập sau, và các Easter egg như con chim giấy, trận Quidditch trong bão, đêm World Cup, Goblet of Fire.
- Bài Substack "The Greatest Love Story Never Told": lập luận đổi Draco thành Draconia không chỉ đổi giới tính mà đổi cấu trúc cảm xúc. Draconia yêu người mà gia đình dạy phải ghét, nên yêu Harry đồng nghĩa với phản bội căn tính Malfoy của mình. Cơ chế tsundere được mô tả gọn: mọi hành động nói "chú ý tới em", mọi lời nói nói "không chịu nổi anh". Cô tạo xung đột chỉ để có lý do đứng gần Harry, rồi lại giận khi Harry không tự hiểu điều cô không dám nói thẳng.
- Bài giải thích trend Malfoid: trend bắt đầu từ tranh vẽ của @redteneri ngày 22/9, tên Draconia do Reddit đặt ngày 29/9, clip AI anime đầu tiên xuất hiện đầu tháng 10. Foyege là nhánh khác: không phải anime mà là live-action điện ảnh, và mỗi creator có một mạch truyện riêng, không có một Part 2 chung cho tất cả. Clip Instagram của @foyege24 đạt gần 500.000 like trong 2 ngày.
- Video của Wizarding Bruno: Draconia dạy Warner Bros điều gì, vì sao khán giả mê câu chuyện này, liên hệ với thất bại của Fantastic Beasts và nguyên tắc viết nhân vật của Hollywood.
- Kết luận phần này: Foyege GOAT không phải vì một kỹ xảo duy nhất, mà vì cộng được ba thứ: một tiền đề chỉ đổi một biến số duy nhất là giới tính Draco, một động cơ nhân vật tự chạy được là tsundere kiểu tiến-lùi, và một dạng kể chuyện dài tập với cliffhanger khiến người ta phải chờ tập sau.

## 3. Tổng hợp xây dựng kịch bản (từ phân tích, không phải prompt gốc của Foyege)

### 3.1. Ba lớp kịch bản

- Lớp 1, tiền đề: chỉ đổi một biến số duy nhất. Foyege không viết lại cả Harry Potter, chỉ đổi Draco thành nữ. Mọi thứ khác giữ nguyên: gia đình Malfoy, định kiến thuần huyết, Hogwarts, Lucius. Vì chỉ đổi một biến, khán giả tự suy ra mọi hệ quả mà không cần giải thích dài.
- Lớp 2, động cơ nhân vật: Draconia có hai lực kéo ngược nhau. Muốn: được Harry chú ý, được công nhận. Sợ: thừa nhận điều đó sẽ phản bội gia đình, phản bội chính căn tính Malfoy của mình. Từ đó sinh ra động cơ tsundere tự chạy: tiến rồi lùi, châm chọc rồi lén nhìn, cứu Harry rồi phủ nhận. Cô không nói tình cảm bằng lời, cô chứng minh bằng hành động rồi phủ nhận bằng lời nói.
- Lớp 3, cấu trúc tập, mạch 5 nhịp gần như cố định:
  - Mở đầu bằng câu hỏi hình ảnh: một cảnh hành động hoặc đối đầu, không mở bằng giải thích.
  - Rạn nứt: áp lực từ gia đình, điển hình là Lucius chất vấn Draconia vì đã bảo vệ Harry.
  - Áp lực công khai: ở Hogwarts, Harry bị bắt nạt, Draconia phải chọn phe trước mặt mọi người.
  - Sự thật riêng tư: khoảnh khắc chỉ có hai người, không còn khán giả, cảm xúc thật mới lộ ra.
  - Đảo ngược và cliffhanger: Lucius cảnh cáo Harry, hoặc một nhân vật thứ ba xuất hiện, rồi cắt ở TO BE CONTINUED.

### 3.2. Luồng phân cảnh: viết theo beat, không viết theo địa điểm

Đừng liệt kê cảnh hành lang, cảnh lớp học, cảnh sân Quidditch. Viết theo bảng beat cho mỗi cảnh:
- Beat: nhân vật làm gì, ví dụ cứu Harry hay phủ nhận Harry.
- Muốn và cản: muốn ở gần Harry, bị cản bởi Lucius và bởi chính lòng kiêu hãnh của mình.
- Chuyển cảm xúc: từ khinh miệt sang hoảng sợ, rồi sang dịu lại, rồi lại cứng lên.
- Điểm kết cảnh: một câu thoại hoặc một ánh mắt chưa được giải quyết, để kéo sang cảnh sau.

Quy tắc: mỗi cảnh chỉ trả lời một câu hỏi cảm xúc. Nếu một cảnh không làm cảm xúc dịch chuyển, bỏ cảnh đó dù nó đẹp.

Mạch chung của series, tóm tắt: cứu Harry ở trại World Cup chứng minh tình cảm bằng hành động, về trang viên bị Lucius tra hỏi là trả giá cho hành động đó, ở Hogwarts bị đẩy ra công khai là trả giá lần hai, rồi khoảnh khắc riêng tư là nơi duy nhất cô không phải diễn vai Malfoy nữa. Cứ hành động, trả giá, hành động, trả giá, khán giả sẽ tự đầu tư cảm xúc.

### 3.3. Cách sắp xếp prompt để ép diễn xuất

Thứ tự prompt hiệu quả, theo kiểu đạo diễn, không phải kiểu kể chuyện:
- Khóa nhân vật trước, viết nguyên văn không đổi mỗi lần: tóc, mặt, trang phục, đoạn mô tả đã duyệt. Đừng viết lại bằng từ đồng nghĩa, AI sẽ hiểu thành người khác.
- Khóa bối cảnh và camera sau: nền nào, góc máy nào, nhân vật đứng ở đâu trong khung, ánh sáng nào.
- Mô tả khung hình tĩnh trước, chuyển động sau.
- Chia chuyển động thành nhịp có thời gian, mỗi shot chỉ một hành động chính.
- Ghi rõ ánh mắt, không ghi chung chung cảm xúc. Thay vì "buồn", hãy ghi "mắt nhìn xuống, chớp mắt một lần, môi mím lại, rồi mới ngẩng lên". Thay vì "giận", hãy ghi "nhìn thẳng không chớp, hàm siết lại, đầu hơi nghiêng về trước".
- Dùng nguyên tắc mắt đi trước đầu: mắt liếc trước, đầu xoay theo sau.
- Kết bằng phần cấm, nhưng viết theo dạng khẳng định: "cô giữ mặt lạnh, không mỉm cười, không nhìn vào camera, không có thêm nhân vật khác trong khung". Viết phủ định kiểu "đừng cười" thường kém hiệu quả hơn viết khẳng định "giữ mặt lạnh".

Mẫu prompt cho một shot (đã giao trong thảo luận, dùng nhân vật tương tự cơ chế, không ghi tên Draconia/Harry trong prompt test):
- Nhân vật: tóc bạch kim, mặt sắc, đồng phục tối với cà vạt xanh-bạc, giống ảnh tham chiếu.
- Bối cảnh: hành lang đá tối, ánh sáng lạnh, camera tĩnh, cận vừa, nhân vật ở phía phải khung.
- Nhịp: 0-2 giây nhìn xuống, môi mím; 2-3 giây mắt ngẩng lên nhìn sang trái ngoài khung; 3-4 giây giữ ánh mắt 1 giây rồi quay đầu đi, hàm siết. Mắt động trước, đầu theo sau.
- Giữ biểu cảm lạnh, không mỉm cười, không nhìn vào camera. Chuyển động chậm, kiềm chế.

Khi test một shot, chỉ kiểm tra 4 thứ theo thứ tự: mặt có đúng người không, ánh mắt có đúng hướng không, có đoạn giữ và thở không, nền và camera có giống shot trước không. Hỏng cái nào thì sửa đúng cái đó, đừng viết lại toàn bộ prompt.

## 4. Diễn xuất: mắt đi trước, đầu theo sau, thân theo sau

### 4.1. Vì sao Draconia có tính người, bản bắt chước thì nhựa

Người bắt chước thường chỉ prompt kiểu nhân vật buồn, khóc, cinematic. AI tự bịa chuyển động từ chữ đó, nên mặt trơn tuột, mắt nhìn vô định, hành động đều đều.

Foyege, nhìn từ sản phẩm, thì diễn xuất được đạo diễn theo từng nhịp, giống phim thật:
- Mắt đi trước đầu: muốn quay sang nhìn ai thì mắt liếc trước, đầu mới xoay theo sau một nhịp.
- Có đoạn giữ, đoạn thở: nhìn xuống, dừng lại, môi mím, rồi mới ngẩng lên. Không phải lúc nào cũng chuyển động liên tục.
- Ánh mắt có đích: nhìn thẳng, nhìn lệch khỏi camera, nhìn xuống, nhìn tránh đi, mỗi kiểu mang một ý khác nhau.
- Dùng cận mặt để diễn: khi mặt chiếm phần lớn khung hình, model mới có đủ pixel để vẽ chớp mắt, nhíu mày, run môi. Bản bắt chước hay quay toàn thân, mặt nhỏ nên tự động thành mặt nạ.

### 4.2. Bối cảnh cố định làm sao

Đừng để AI sinh cả ba thứ cùng một lúc. Khóa riêng từng lớp:
- Khóa nền: một ảnh nền dùng lại cho mọi shot cùng địa điểm, không sinh nền mới mỗi clip.
- Khóa camera: góc máy, tiêu cự, vị trí nhân vật trong khung gần như không đổi, chỉ đổi ở điểm cắt cảnh.
- Khóa nhân vật: một bộ ảnh tham chiếu đã duyệt, dùng lại làm reference cho mọi shot.

Khi ba lớp này đã cố định, AI chỉ còn việc làm nhân vật cử động trong khung đó, nên ít bị trôi mặt, trôi nền, trôi tỉ lệ như cách sinh tự do.

### 4.3. Film -> Blender -> AI: đúng hướng, nhưng không nhất thiết dựng nguyên nhân vật 3D

Pipeline có thật và giải thích tốt cảm giác cố định:
- Lấy tham khảo từ phim hoặc tự diễn: một đoạn chuyển động mẫu, có thể là clip phim, clip tự quay, hoặc pose keyframe.
- Đưa vào Blender để tách ra control map: video khung xương OpenPose, hoặc depth map, hoặc cả hai. Nhân vật trong Blender lúc này chỉ là hình que, không cần mặt, tóc, quần áo đẹp.
- Đưa ba thứ vào AI video gen cùng lúc: ảnh tham chiếu để khóa mặt và đồ, ảnh nền đã khóa, và video khung xương từ Blender để khóa tư thế, vị trí, thời gian chuyển động.
- AI lúc này không được tự chọn tư thế nữa, nó chỉ tô realistic lên đúng khung xương đó. Chuyển động vẫn giống người vì gốc chuyển động vốn là của người thật.

Đường nhẹ hơn, không cần Blender: motion transfer và performance capture của các tool video hiện tại, ví dụ diễn xuất mặt hoặc motion reference. Đường này nhanh hơn nhưng kiểm soát bối cảnh kém hơn đường Blender, vì không có control map cứng. Muốn bối cảnh cố định tuyệt đối thì vẫn phải khóa nền và khóa frame đầu, cuối.

Lưu ý: đây là suy luận từ sản phẩm và pipeline chuẩn, chưa phải xác nhận Foyege dùng Blender cụ thể, vì ổng chưa công bố workflow đó.

### 4.4. Vì sao video test đầu tiên không cho cảm giác mắt đi trước

User soi đúng: clip đầu tiên không cho cảm giác mắt đi trước, mà cho cảm giác mắt điều khiển cả cơ thể, như con rối.

Nguyên nhân:
- Diễn xuất thật có độ trễ theo tầng: mắt liếc trước, rất nhanh, khoảng 0,2 giây. Đầu xoay theo sau, chậm hơn, khoảng 0,3-0,5 giây. Vai và thân mới đi sau cùng, chậm nhất.
- Khi đầu đã bắt đầu xoay, mắt vẫn giữ khóa vào điểm nhìn. Mắt không quay cùng đầu, mắt neo lại, đầu mới đuổi theo mắt.
- Model image-to-video không có xương mắt riêng, xương đầu riêng. Nó biến dạng cả khung hình cùng lúc, nên khi mắt muốn nhìn sang trái, cả đầu, cả vai, thậm chí cả camera cũng bị kéo theo.

Cách sửa, đã chốt:
- Tách thành hai shot rồi cắt nối: shot 1 đầu đứng yên hoàn toàn, chỉ mắt liếc sang; shot 2 đầu mới xoay chậm theo hướng mắt đã nhìn, mắt giữ nguyên điểm khóa. Cắt giữa hai shot sẽ tạo ảo giác mắt đi trước, dù mỗi shot riêng lẻ rất đơn giản.
- Hoặc dùng rig thật: trong Blender hay face capture, xương mắt và xương đầu là hai đường keyframe riêng, lệch nhau vài frame.
- Còn nếu chỉ dùng AI video thuần, cách thực tế nhất là giảm tham vọng của mỗi shot xuống: một shot chỉ cho mắt động, shot sau mới cho đầu động, đừng bắt một clip làm cả chuỗi mắt, đầu, thân.

## 5. Thử nghiệm đã làm (kèm file và kết quả kiểm chứng bằng frame)

Tất cả file test nằm trong `~/workspace/foyege-test/`. Nhân vật test là bản tương tự cơ chế (tóc bạch kim, đồng phục tối với cà vạt xanh-bạc, hành lang gothic, biểu cảm lạnh), không ghi tên Draconia/Harry trong prompt test đầu tiên. Test mắt-đi-trước sau đó dùng nhân vật trưởng thành, bối cảnh trung tính, để tách riêng cơ chế khỏi nhân vật gốc.

### 5.1. Test 1: một clip gộp, nhịp mắt + đầu + thân trong cùng một clip

- Ảnh tham chiếu: `media-generation-test-character-ref-0-7f1c2ca5-e957-4e86-9985-ad67d2e9e8ea.webp`
  - Đã xem trực tiếp: cận mặt nghiêng 3/4, nhìn xuống, môi mím, hành lang gothic, đúng khung tĩnh yêu cầu.
- Video gốc: `media-generation-test-beat-480p-0-cdf65601-310e-4be1-8720-78d725fcdf16.mp4`
  - Thông số đo được: 768x1152, 10 giây, 24fps. Tool không tự sinh đúng 480p dù prompt ghi 480p.
- Video 480p đã nén lại: `test-beat-480p.mp4` (480x720, 10 giây).
- Prompt test: khóa ảnh tham chiếu, camera tĩnh, nhịp 0-2 giây nhìn xuống môi mím, 2-3 giây mắt ngẩng lên nhìn sang trái ngoài khung, 3-4 giây giữ ánh mắt 1 giây rồi quay đầu đi hàm siết, mắt động trước đầu theo sau, giữ biểu cảm lạnh, không mỉm cười, không nhìn vào camera, chuyển động chậm kiềm chế.
- Kiểm chứng bằng frame trích xuất (frames f_1 đến f_5):
  - Đạt một phần: mặt, tóc, đồng phục, nền giữ ổn nửa đầu; có nhịp nhìn xuống rồi ngẩng lên; biểu cảm lạnh, không cười.
  - Không đạt:
    - Nhịp thời gian bị kéo từ beat 4 giây thành 10 giây.
    - Lệnh không nhìn vào camera bị phá: giữa clip nhân vật quay thẳng mặt về camera.
    - Camera không tĩnh mà như xoay quanh nhân vật, cuối clip tóc đổi thành buộc đuôi ngựa và mặt trôi khỏi ảnh gốc.
- Kết luận test 1: prompt chia nhịp + hướng mắt có tác dụng định hướng diễn xuất, nhưng chữ thuần không đủ ép chính xác. Muốn đạt mức kiểm soát kiểu Foyege phải thêm khóa cứng: cắt clip ngắn 3-4 giây và chỉ lấy đoạn đầu còn giữ được mặt, hoặc dùng frame đầu + cuối và motion/control reference.

### 5.2. Test 2: chỉ mắt động, đầu đứng yên (tách riêng một tầng)

- Vấn đề phát sinh: video chỉ-mắt-cử-động với nhân vật dạng học sinh lần đầu không sinh được, nên đã dừng ở phân tích từ clip trước thay vì cố sinh lại theo cách khác.
- Hướng thay thế đã làm: test với nhân vật trưởng thành hoàn toàn khác, bối cảnh trung tính, không phải dạng học sinh.
- Ảnh tham chiếu mới: `media-generation-test-eyes-adult-ref-0-29a0ed44-23c5-4f1e-a0eb-ae37ffde955c.webp`
  - Đã xem trực tiếp: phụ nữ trưởng thành đầu 30, tóc nâu buộc sau, blazer tối, nền studio trung tính, mặt chính diện, mắt nhìn xuống, môi khép.
- Video gốc: `media-generation-test-eyes-adult-480p-0-c1f2c309-04ea-4149-8032-ccf99c69c83d.mp4` (768x1152, 10 giây).
- Video 480p đã nén lại: `test-eyes-adult-480p.mp4`.
- Prompt test: đầu, vai, tóc, nền, camera đứng yên hoàn toàn; chỉ tròng mắt động: nhìn xuống rồi ngẩng lên nhìn sang trái rồi giữ yên; không xoay đầu, không nghiêng đầu, không động vai, không động camera, không cười, chuyển động mắt rất nhẹ và chậm.
- Kiểm chứng bằng frame (frames2 g_1 đến g_5):
  - Đạt: đầu, vai, tóc, nền, camera đứng yên gần như tuyệt đối; chỉ tròng mắt cử động: đầu clip nhìn xuống, giữa clip ngẩng lên liếc sang trái, cuối clip giữ nguyên hướng nhìn.
  - Không còn cảm giác mắt kéo cả cơ thể đi theo như clip trước, vì không còn lệnh nào bắt đầu, thân phải động cùng lúc.
  - Chưa đạt: video gốc vẫn dài 10 giây, không phải 4 giây như prompt; bản 480p là nén lại từ bản gốc, không phải model tự sinh đúng 480p; biên độ mắt hơi lớn, nhìn hơi liếc hơn là liếc nhẹ kiểu tsundere.
- Kết luận test 2: model không tách được mắt ra khỏi đầu khi bắt nó làm cả chuỗi trong một clip, nhưng nó tách được khi chỉ giao đúng một việc: chỉ mắt động, còn lại đứng yên.

### 5.3. Test 3: cascade mắt trước, đầu sau bằng cắt nối (phương pháp DEADSHOT)

- Cách làm:
  - Mảnh 1, 0-3 giây: clip mắt ở test 2, đầu đứng yên, chỉ mắt từ nhìn xuống liếc sang trái.
  - Điểm cắt ở đúng giây thứ 3: lấy đúng frame cuối của mảnh 1 làm ảnh đầu cho mảnh 2, nên chỗ cắt gần như liền mạch, không nhảy mặt.
  - Ảnh đầu mảnh 2: `shot2-start-eyes-left.jpg` (đã xem trực tiếp: mắt đã sang trái, đầu vẫn chính diện).
  - Mảnh 2: sinh từ ảnh đó, prompt: mắt đã nhìn sang trái và giữ nguyên hướng nhìn suốt clip, đầu xoay chậm sang trái theo hướng mắt, vai, nền, camera đứng yên, giữ cùng mặt, tóc, blazer tối.
  - Video gốc mảnh 2: `media-generation-test-head-follows-480p-0-68174ee5-4765-43f3-a388-3577c4c54cda.mp4` (768x1152, 10 giây).
  - Chỉ lấy 3 giây đầu của mảnh 2, vì để dài hơn đầu sẽ xoay quá đà và mặt bắt đầu trôi.
  - Video đã cắt nối, 480p, 6 giây: `cascade-eyes-then-head-480p.mp4` (480x720, 6 giây).
- Kiểm chứng bằng frame mảnh 2 (frames3 h_1 đến h_5):
  - Đầu clip mảnh 2: mắt đã sang trái, đầu chính diện.
  - Giữa clip: đầu xoay dần sang trái, mắt vẫn giữ hướng nhìn sang trái, mặt vẫn nhận ra cùng người.
  - Cuối đoạn lấy: đầu đã xoay sang trái rõ, mắt vẫn hướng đó.
  - Giới hạn: mặt ở mảnh 2 hơi già và nhăn hơn mảnh 1 một chút, nên nếu làm series thật thì vẫn cần khóa ảnh tham chiếu chặt hơn, hoặc chỉ lấy đoạn đầu rất ngắn trước khi mặt trôi.
- Kết luận test 3: cảm giác mắt đi trước, đầu theo sau đã đọc được rõ khi timeline được làm bằng cắt nối, không phải bằng một prompt dài. Timeline cuối cùng không còn do model quyết định nữa, mà do người edit quyết định bằng cắt: 3 giây mắt, cắt cứng, 3 giây đầu.

## 6. Tốc độ: chốt là tốc độ bình thường, không phải slow motion, và tốc độ làm lại ở edit

### 6.1. Phân biệt

- Diễn kiềm chế là biên độ nhỏ: không vung tay, không quay đầu mạnh, không diễn lố. Nhưng thời gian vẫn là thời gian thực.
- Slow motion là kéo giãn thời gian: mọi thứ trôi chậm, lơ lửng, giống mơ. Cái này làm mất tính người ngay, vì người thật không di chuyển kiểu đó.
- Foyege cũng cấm slow motion trong prompt của ổng, và cấm luôn freeze frame. Ổng muốn thời gian thực, cắt cứng, và giữ hình rõ. Giữ hình rõ khác slow motion: giữ hình là không động đậy trong thời gian thực, slow motion là động đậy nhưng chậm lại.

### 6.2. Thời gian thật đã chốt cho chuỗi mắt, đầu

- Mắt liếc là một cái snap, rất nhanh, khoảng 0,2 giây, không phải lướt chậm từ từ.
- Đầu xoay theo sau, tốc độ bình thường, khoảng 0,5-1 giây là xong.
- Sau đó là giữ yên, không động đậy, khoảng 1-2 giây. Chính đoạn giữ yên này mới là chỗ khán giả đọc được cảm xúc, chứ không phải đoạn di chuyển chậm.

### 6.3. Vì sao clip test trông chậm

- Model ở đây mặc định sinh clip 10 giây với chuyển động trôi chậm, và prompt test đầu còn ghi thêm chữ slow để nó khỏi biến dạng mặt.
- Cộng với việc cắt 3 giây từ một clip 10 giây, nên hành động bị kéo dài ra.
- Đó là thỏa hiệp lúc test, không phải spec cuối.

### 6.4. Làm lại tốc độ ở edit (DaVinci Resolve)

Đúng: model chỉ sinh nguyên liệu thô, timeline cuối cùng là do edit quyết định, không phải do prompt quyết định. Ba việc theo thứ tự:
- Cắt bỏ phần trôi trước đã: clip model trả về thường có đoạn đầu lề mề và đoạn cuối mặt bắt đầu trôi. Cắt bỏ hai đầu đó, chỉ giữ đúng đoạn mắt snap, đầu xoay, và một chút đầu đoạn giữ yên.
- Tăng tốc riêng đoạn chuyển động, không tăng tốc đoạn giữ: ví dụ đoạn đầu xoay 3 giây thì cho lên 200% còn 1,5 giây, hoặc 300% còn 1 giây tùy mắt người xem. Trong Resolve thì dùng Change Clip Speed hoặc Retime Controls để đặt điểm tốc độ, chỉ tăng tốc ở đoạn xoay, đoạn giữ yên sau đó để nguyên 100%.
- Cắt trên hành động, không cắt sau hành động: cắt từ shot mắt sang shot đầu ngay tại khoảnh khắc mắt vừa chạm đích, đừng đợi đầu xoay xong mới cắt. Người xem sẽ tự cảm thấy chuyển động liên tục ở tốc độ bình thường, dù nguyên liệu gốc chậm hơn.
- Lưu ý: tăng tốc cả clip một cách đều tay sẽ làm chớp mắt và hơi thở thành giật, mất luôn vi biểu cảm. Chỉ tăng tốc đoạn di chuyển, đoạn giữ thì để nguyên, đó mới là tốc độ bình thường có cảm xúc.

Tóm gọn spec tốc độ đã chốt: diễn xuất thì mắt snap nhanh, đầu xoay tốc độ bình thường, rồi giữ yên. Không slow motion.

## 7. Chốt cuối cùng (dùng được ngay)

1. Khóa ảnh tham chiếu trước, khóa video sau. Một ảnh, một nhiệm vụ.
2. Khóa riêng ba lớp: nền, camera, nhân vật. Đừng để AI sinh cả ba cùng lúc.
3. Kịch bản chỉ đổi một biến số, động cơ nhân vật là mâu thuẫn nội tâm tự chạy, mỗi cảnh chỉ dịch chuyển một cảm xúc.
4. Prompt viết theo thứ tự: ảnh tham chiếu, bối cảnh, camera, khung tĩnh, nhịp có thời gian, ánh mắt cụ thể, phần cấm viết dạng khẳng định.
5. Timeline có ba cách đã kiểm chứng từ Foyege, chọn một cách cho mỗi clip, đừng trộn cả ba trong một clip:
   - Một beat một giây, mỗi beat ghi đủ camera, hành động, hiệu ứng.
   - Chia theo trạng thái môi trường: đèn tắt dần, đen hoàn toàn, đèn bật lại; giáp lắp từng mảnh, chi tiết mặt lắp cuối.
   - Montage mảnh vỡ: shot 0,3-0,8 giây, xen kẽ đoạn giữ hình rõ 0,5-1 giây, cắt cứng, frame-drop, không vẽ trọn một trận đánh.
6. Diễn xuất: mắt snap nhanh khoảng 0,2 giây, đầu xoay tốc độ bình thường khoảng 0,5-1 giây, rồi giữ yên 1-2 giây. Không slow motion.
7. Tách tầng chuyển động: một shot chỉ cho mắt động, shot sau mới cho đầu động, shot sau nữa mới cho thân động. Lấy frame cuối shot trước làm ảnh đầu shot sau, cắt cứng ở điểm mắt chạm đích.
8. Làm tốc độ ở edit: cắt bỏ đầu cuối trôi, tăng tốc riêng đoạn chuyển động, giữ nguyên đoạn giữ, cắt trên hành động.
9. Chỉ lấy đoạn đầu còn giữ được mặt. Clip càng dài, model càng có cơ hội trôi mặt, trôi camera, đổi tóc. Cắt ngắn là một dạng khóa.

## 8. Những gì chưa xác minh, không được suy đoán thêm

- Workflow của series Malfoy/Draconia cụ thể: chưa tìm thấy prompt nào cho series đó. Các prompt tìm được là cho ba sản phẩm khác (biến hình cơ giới, bướm hóa người, title DEADSHOT).
- Tool dùng cho series Malfoy: chưa xác minh. Seedance 2.5 và Minimax H3 chỉ được ghi trong hai bài sản phẩm khác, trong đó bài Seedance là hợp tác trả phí.
- Một số bình luận lồng trên X cần đăng nhập mới mở được, bao gồm một câu trả lời về model trong bài 11/10 và các bình luận còn lại trong bài 16/9. Những phần đó được ghi là chưa đọc được, không điền bằng suy đoán.
- Bilibili của Foyege chưa đọc được danh sách video bên trong do lỗi 429 ở thời điểm kiểm tra.
- X: phần còn lại của 1.692 bài đăng ngoài khoảng 5 bài đầu nhìn thấy không cần đăng nhập vẫn chưa kiểm chứng được ở thời điểm kiểm tra ban đầu, trừ ba bài cụ thể user gửi link sau đó đã đọc trực tiếp.
- Instagram qua Graph: chưa đọc được vì tài khoản Instagram của user chưa liên kết. Search công khai không thấy workflow, nhưng đó không phải là toàn bộ bình luận qua Graph.
- Các prompt trong file đi kèm là cấu trúc tái tạo để phân tích, không phải bản sao nguyên văn hay bản dịch nguyên văn prompt gốc của Foyege. Muốn trích dẫn nguyên văn thì mở link gốc ở mục 2 và file prompt.
