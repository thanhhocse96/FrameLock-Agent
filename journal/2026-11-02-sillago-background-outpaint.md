# Retro — mở nền ảnh cá đục thành 3:4

## Bối cảnh

User yêu cầu mở background lên trên và dưới, tỷ lệ 3:4, không thêm vật thể không liên quan; đồng thời ghi nhật ký theo protocol. Đây là ảnh tĩnh, không áp dụng protocol video first/last-frame.

## Việc đã làm

Một lượt imagegen tích hợp, dùng ảnh gốc 2559×1440 làm edit input. Prompt khóa bố cục thành dải ngang trung tâm và chỉ cho nối nền tabletop tối ở trên/dưới. Lưu [prompt, thông số và kiểm tra](../.local/draft/sillago-background-study.md), [reference](../.local/samples/sillago-background-study/reference.png), [output](../.local/samples/sillago-background-study/run-001.png). Các link local gitignored, checkout khác không mặc nhiên có artifact.

## Kết quả và pitfall

- Output 1086×1448, đã đọc kích thước file: đúng 3:4. Không đạt kích thước gợi ý 1536×2048, nhưng user chỉ yêu cầu tỷ lệ.
- Quan sát: nền trên/dưới tiếp tục mặt nền tối, không thấy props/đồ ăn/chữ mới; cụm bảy cá và nguyên liệu còn ở trung tâm.
- Không chứng minh phần gốc giữ nguyên pixel: imagegen có thể tái tạo cả chi tiết ngoài vùng muốn sửa. Chưa có acceptance user; không ghi pass tuyệt đối về bảo toàn ảnh gốc.

## Bài học chốt trong phạm vi case

Định nghĩa rõ vùng được sinh là nền trống cùng vật liệu và ánh sáng, cùng hướng mở canvas; cấm zoom/crop và thêm đối tượng. Một kết quả phù hợp chưa chứng minh hiệu quả độc lập của từng câu prompt. Chưa thử workflow mask/khóa pixel, chưa promote thành template hoặc sửa governance.

## Chi phí

Một lần generation hoàn tất. Model nền, seed, phí và provider job ID chưa được cung cấp; không ghi bằng 0.
