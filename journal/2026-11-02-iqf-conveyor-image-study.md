# Study ảnh — công nhân đưa fillet cá mú vào IQF

## Cập nhật run 005 — lỗi suy diễn không gian khi mở rộng ảnh

User xác định vùng bên phải phải là phần vách kim loại kín kéo dài của IQF, không phải hành lang. Đây là lỗi nội dung phát sinh khi mở rộng khung ở run 003 và được giữ trong run 004. Đã edit theo ảnh khoanh đỏ, [output 005](../.local/samples/iqf-conveyor-study/run-005.png), prompt nguyên văn trong hồ sơ local. Quan sát vách đã kín ở vùng chỉ định; chưa có user acceptance. Chi tiết mặt băng cũng có thay đổi dù prompt khóa phần còn lại: cần đối chiếu toàn ảnh sau edit cục bộ. Bài học trong case: outpaint cần xác định rõ vùng nào là vỏ thiết bị kín, vùng nào là lối đi; không tự suy diễn khoảng trống thành phòng phía sau. Tổng năm lượt generation, phí chưa rõ; không xác nhận tính cách nhiệt thực tế từ ảnh minh họa.

## Cập nhật run 004

Thêm logo SK VIETNAM dạng hộp đèn tại vùng tường user khoanh đỏ trên run 003. [Output 004](../.local/samples/iqf-conveyor-study/run-004.png); prompt và logo nguồn lưu trong hồ sơ local. Công cụ imagegen tích hợp, tổng lịch sử bốn lượt generation, phí chưa rõ. Quan sát thấy biển hộp đèn ở vị trí yêu cầu; độ trung thành từng nét logo chưa xác minh, chưa có acceptance user. Không thay đổi kết luận lỗi băng chuyền.

## Bối cảnh

Ngày 2026-11-02. User cần ảnh nhà máy: bảo hộ trắng theo ảnh 1, fillet cá mú, góc chụp và băng chuyền theo ảnh 3, chỉ một máy IQF. Sau run 001, user chỉ rõ băng chuyền lắp sai và yêu cầu chạy lại với vài công nhân, tỷ lệ 16:9. Mục tiêu sử dụng Business cụ thể chưa chốt; không tự coi ảnh là bằng chứng cấu hình nhà máy thực tế.

## Hồ sơ và bằng chứng

- [Hồ sơ đầy đủ và prompt nguyên văn](../.local/draft/iqf-conveyor-image-study.md).
- [Ảnh chuẩn hình học](../.local/samples/iqf-conveyor-study/reference-03-iqf.jpg).
- [Run 001](../.local/samples/iqf-conveyor-study/run-001.png), [run 002](../.local/samples/iqf-conveyor-study/run-002.png).
- Đây là link artifact local, gitignored; checkout khác không mặc nhiên có các file. Prompt là prompt do assistant viết và thực chạy, không phải raw influencer; không đưa vào raw/digest/mapping ảnh.

## Việc đã làm

Hai lượt dùng công cụ imagegen tích hợp với cùng ba ảnh tham chiếu, nền không trong suốt. Run 001 có một công nhân. Run 002 nhấn mạnh hình học infeed, ba công nhân và 16:9; không đưa output 001 vào làm ảnh edit. Đã sao chép ba reference và hai output về local, giữ nguyên nguồn; lưu nguyên văn prompt thực gửi, phân biệt với bản trình bày lại trong chat.

## Pitfall và phân tích lỗi

| Quan sát | Ý nghĩa / hướng xử lý |
|---|---|
| Run 001: cụm khung dài và mặt băng không thể hiện rõ đầu nạp nối vào khe theo ảnh 3; user xác nhận “băng chuyền đã lắp sai” | Đây là lỗi quan hệ không gian và cấu tạo. Một máy, inox đẹp và công nhân đúng màu chưa đủ để pass |
| Run 002: băng có chiều sâu hướng vào khe rõ hơn, nhưng con lăn đầu và các thanh khung vẫn không sao chép đúng cụm trong ảnh 3 | Có cải thiện khả năng đọc hướng băng; chưa đạt yêu cầu “y chang”. Chưa có feedback user duyệt run này |
| Ảnh 3 có các khay trên băng; hai output chuyển sang fillet trực tiếp trên lưới | Prompt đã chủ động chọn bỏ khay dù user không yêu cầu rõ. Cần phân biệt giữ cấu tạo máy với thay sản phẩm/quy trình nạp; phải chốt khay hay đặt trực tiếp khi tiếp tục |
| Run 002 có khay đặt sát/trên mép đầu băng, không rõ là bàn chuẩn bị riêng như prompt | Chưa chứng minh bố trí thao tác đúng; cần kiểm tra đường sản phẩm và vùng con lăn riêng |
| Yêu cầu 16:9 nhưng file run 002 là 1672×941 | Gần 16:9, không chính xác: 1672×9=15048, 941×16=15056. Không lặp lại khẳng định “strict 16:9” chỉ vì prompt có câu đó |
| Reference 2 là minh họa; run 002 vẫn nhận cả ba reference | Có thể tạo tín hiệu cạnh tranh về phong cách/bố cục. Đây là giả thuyết, chưa A/B chứng minh |
| Run 002 đồng thời đổi prompt hình học, số công nhân và khung hình | Không thể quy cải thiện/hỏng cho một câu prompt riêng lẻ |

## Bài học có giới hạn

Trong case này, nhắc “PRIMARY”, “GEOMETRY IS CRITICAL” và nhiều câu phủ định chưa bảo đảm sao chép cơ khí. Cần nghiệm thu hướng chuyển động, trục con lăn, mặt băng, hai cạnh bên, điểm đi vào khe và khung đỡ bằng đối chiếu reference–output. Không suy ra kết luận chung về mọi model.

Hướng thử tiếp **chưa chạy**: dùng ảnh 3 làm ảnh edit chính, giữ cụm máy/băng mong muốn, loại máy thứ hai; sau khi hình học được duyệt mới thêm người và cá. Nếu cần thêm reference, chỉ dùng ảnh 1 cho bảo hộ. Cần giữ đủ ngữ cảnh cả đầu băng lẫn khe máy, không chỉ crop riêng mặt inox. Không đảm bảo phương án này sẽ thành công trước khi có output kiểm chứng.

## Trạng thái và chi phí

- Run 001: hoàn tất generation, fail hình học theo feedback user.
- Run 002: hoàn tất generation; chưa đạt đối chiếu cơ khí nghiêm ngặt, chưa được user duyệt; tỷ lệ chỉ xấp xỉ 16:9.
- Hai lần gọi generation; model nền, seed, job ID provider và chi phí không được công cụ cung cấp. Không ghi chi phí bằng 0. Không chạy thêm khi lưu study.
- Không promote thành template/workflow đạt; không sửa governance.

## Nối tiếp run 003 — đổi vị trí công nhân

User yêu cầu chuyển người xa nhất gần cửa máy sang phía đối diện và mở khung để thấy lưng. Đã edit từ run 002 bằng imagegen, lưu prompt đầy đủ trong hồ sơ local và [output 003](../.local/samples/iqf-conveyor-study/run-003.png). Quan sát thấy ba người, người được chuyển đứng bên phải băng, hiện lưng và toàn thân. Chưa có user acceptance. Việc đổi vị trí người không giải quyết hay xác nhận các lỗi cơ khí đã ghi. Tổng lịch sử hiện có ba lần generation; phí vẫn chưa rõ. Không chạy thêm ngoài yêu cầu edit này.
