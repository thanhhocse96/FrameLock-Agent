# Research nền tảng — 2026-10-12

## Kết quả sơ bộ

Hai ảnh cho biết trạng thái đầu/cuối, nhưng cần spec để chọn hành động nối. Khung Delta Analysis được đề xuất ở [protocol](protocol.md) là tổng hợp của phiên này, chưa được validation bằng generation mới.

Runway hướng dẫn image-to-video tập trung prompt vào motion, camera và tiến trình thời gian; ảnh input định hình composition, subject, lighting và style. Hướng dẫn hiện được tối ưu cho Gen-4.5, nên không coi cú pháp là chuẩn bắt buộc của MiniMax/Kling/Seedance. Nguồn: [Runway Image to Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide), mục Introduction và Text prompt; truy cập 2026-10-12.

Runway cũng nêu motion cues trong ảnh có thể mâu thuẫn với prompt; đề xuất chỉnh input khi thử nhiều lần vẫn không ra motion mong muốn. Điều này hỗ trợ việc đưa keyframe vào chẩn đoán, thay vì chỉ sửa chữ. Nguồn: [Runway guide](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide), FAQ về motion cues.

Trình tự hành động có thể viết bằng ngôn ngữ tự nhiên hoặc timestamp; cần cân đối sequence với duration. Đây là hướng dẫn cho Runway, không bảo đảm model khác tuân theo timestamp tương tự. Nguồn: [Runway guide](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide), Sequential prompting.

Các nguồn cũ trong journal, tên model, giá, độ dài clip hỗ trợ và filter không được xem là thông tin hiện hành nếu chưa kiểm tra endpoint/provider đang dùng. Phiên này dùng journal cho kinh nghiệm lịch sử và nguồn Runway cho nguyên tắc prompting; chưa xác minh capability hiện tại của MiniMax H3, Kling O3 hoặc Seedance 2.0.

## Giả thuyết cần kiểm tra

| Giả thuyết | Điểm tựa | Thử nghiệm phân biệt |
|---|---|---|
| Delta thật chỉ có một thuộc tính giúp giảm morph | DA-001/002 gợi ý multi-change là rủi ro | Cùng model/settings: cặp một delta so với cặp có delta phụ; ghi cả motion và invariants |
| Đường ra/vào vật rõ giúp giảm biến mất giữa khung | Nguyên lý mép khung DA-002 | Prompt cơ sở so với prompt thêm đúng một câu quỹ đạo mép; kiểm tra contact và exit |
| Động từ và timing cụ thể cải thiện nhịp | DA-003 và guidance sequential prompting | Tách thử motion verb và timing; không thay cả hai rồi quy công cho một yếu tố |
| Lỗi do input conflict có thể cần sửa keyframe | Runway FAQ; trạng thái ref sai trong journal cá đục | Giữ prompt, sửa đúng motion cue/trạng thái input; kiểm tra delta phụ |

Chưa có dữ liệu để gán xác suất thành công. Mỗi đề xuất cần ghi nguồn, giả thuyết và tiêu chí pass. Một fix ảnh, một prompt fragment hoặc request completed không được nâng thành bằng chứng fix video.

## Ca đầu tiên cần để kiểm chứng

Chọn một cặp ảnh A/B và một video lỗi thuộc cùng run, prompt/settings gốc, spec của user. Ưu tiên đúng bài toán một chi tiết thay đổi; ghi delta phụ nếu có. Quan sát video hoặc nhận mô tả có provenance, lập bảng delta, chọn một can thiệp và đánh giá toàn clip. Hiện chưa có input cụ thể của ca mới trong chat nên chưa đưa ra prompt sửa lỗi cho một video thực tế.
