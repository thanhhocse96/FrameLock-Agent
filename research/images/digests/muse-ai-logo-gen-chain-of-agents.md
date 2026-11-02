# Digest: muse-ai-logo-gen-chain-of-agents

- Raw: `../raws/muse-ai-logo-gen-chain-of-agents.md`
- Model: không rõ trong raw (agent MUSE.AI qua media pipeline `media.generate_image` / `media.generate_icon`, resume bằng snapshot hash)
- Từ khóa: #agentic-workflow #iterative-edit #snapshot-resume #read-back-verify #quantitative-edit-fail #logo-app-icon

## Kỹ thuật (workflow + render — mỗi ý kèm Nguồn)

- Chuỗi chạy theo vòng `generate → read-back → summary → edit-tiếp`: mỗi prompt sinh 1 ảnh rồi đọc lại file (MIME, bytes, SHA256) trước khi tóm tắt — Nguồn: `../raws/muse-ai-logo-gen-chain-of-agents.md#prompt-1` (các mục `Read ... image` + `Summary` lặp lại ở mọi prompt).
- Prompt 1 sinh 4 concept song song để user chọn (minimal flat, gradient, line-art, mascot) rồi mới đi sâu 1 hướng — Nguồn: `../raws/muse-ai-logo-gen-chain-of-agents.md#prompt-1` (4 mục `Created ... icon` + `Summary` chốt 4 concept).
- Các edit kế tiếp kẹp ảnh trước bằng `Resume from: snapshot <hash>` thay vì mô tả lại từ đầu — Nguồn: `../raws/muse-ai-logo-gen-chain-of-agents.md#prompt-3` (`from snapshot 4bf8c5f2...:jneb35`), tương tự ở Prompt 4/5/7/8.
- Bước read-back chỉ kiểm tra file tồn tại, không đối chiếu ngữ nghĩa với ý user: tóm tắt read luôn diễn đạt lại prompt (`providing the image for visual inspection against ...`) chứ không đo đạc gì — Nguồn: `../raws/muse-ai-logo-gen-chain-of-agents.md#prompt-2` (mục `Read generated blue 3D wallet icon image`).
- Có bằng chứng read sai file mà không ai phát hiện: mục đọc mascot ở Prompt 1 trỏ nhầm path + SHA256 của ảnh line-art — Nguồn: `../raws/muse-ai-logo-gen-chain-of-agents.md#prompt-1` (mục `Read playful wallet mascot icon image`, path `...moneyvvibe-lineart...`, SHA `f19ca0c4...` trùng mục line-art).
- Prompt 9 là ngoại lệ duy nhất có đo đạc thật: sample màu bằng PIL ra hex (`background #F9ECD7`, `gold coin #D9A23F`...) rồi mới dựng SVG — Nguồn: `../raws/muse-ai-logo-gen-chain-of-agents.md#prompt-9` (mục `Sampled colors from moneyvvibe flat image`).

## Tone (mood/cảm xúc/màu sắc — kèm Nguồn)

- Hướng chốt: flat tối giản, ví xanh dương 2 sắc độ + thẻ xanh lá + coin vàng + nền kem — Nguồn: `../raws/muse-ai-logo-gen-chain-of-agents.md#prompt-8` (prompt EN phân biệt `darker deep navy blue` back / `lighter blue similar to Facebook blue but slightly darker` front).
- Các concept bị loại cho thấy phổ tone đã thử: emerald tin cậy, gradient violet-to-teal premium, line-art giấy stationery, mascot coral-cam thân thiện — Nguồn: `../raws/muse-ai-logo-gen-chain-of-agents.md#prompt-1` (4 prompt EN gốc).

## Shot (cỡ cảnh, góc máy — kèm Nguồn)

- Toàn chuỗi là app-icon chính diện, 1 vật thể giữa khung, không đổi góc máy — Nguồn: `../raws/muse-ai-logo-gen-chain-of-agents.md#prompt-1` (composition `wallet ... on ... background` lặp lại mọi prompt, không có từ khóa camera nào).

## Composition (bố cục, framing, điểm nhấn — kèm Nguồn)

- Bố cục chốt: ví mở hé, thẻ thò lên sau, coin vàng kẹp trong miệng ví thò lên trên, chữ `$` nổi trên coin — Nguồn: `../raws/muse-ai-logo-gen-chain-of-agents.md#prompt-4` (prompt EN `tucked in the wallet opening, peeking out from the top ... partially behind the wallet edge`).
- Prompt 6 ép chuyển 3D → flat bằng liệt kê loại bỏ (`remove all 3D embossing, soft shadows and gradients`) + neo giữ bố cục (`Keep the same composition`) — Nguồn: `../raws/muse-ai-logo-gen-chain-of-agents.md#prompt-6`.

## Chủ đề

- Thiết kế logo app ví MoneyVVibe theo chuỗi agentic liên tục; bài học chính là giới hạn của edit định lượng khi thiếu bước phân tích prompt (đưa chuỗi này cho Gemini hay model ảnh nào khác cũng lỗi tương tự vì lỗi nằm ở workflow, không ở model).

## Chuỗi fail định lượng (bằng chứng thiếu phân tích prompt)

- Prompt 3 (`Đồng xu vàng to lên nằm giữa ví`): agent hiểu sai ý user — Nguồn: `../raws/muse-ai-logo-gen-chain-of-agents.md#prompt-3` (`Lưu ý từ User: Agent hiểu sai nội dung của user`; prompt EN agent tự viết thành `positioned prominently in the center overlapping the middle of the wallet front`).
- Prompt 4 (`giảm 40%`): agent không có khái niệm 40% tính trên cái gì — Nguồn: `../raws/muse-ai-logo-gen-chain-of-agents.md#prompt-4` (`Nhận xét từ User: hình như agent của Muse không hiểu 40% ở đây nên được tính thế nào`; prompt EN chỉ diễn đạt lại thành `Shrink the gold coin by 40 percent so it is noticeably smaller`).
- Prompt 5 (`to ra 2 lần`): tư thế đúng nhưng size sai — Nguồn: `../raws/muse-ai-logo-gen-chain-of-agents.md#prompt-5` (tiêu đề user ghi `Tư thế đúng, size thì sai`).
- Prompt 7 (`to thêm 1.5 lần`): coin gần như không to hơn — Nguồn: `../raws/muse-ai-logo-gen-chain-of-agents.md#prompt-7` (`Nhận xét từ User: đồng xu không to hơn mấy`).
- Prompt 9 (`Chuyển thành illustrator`): agent hiểu thành "tự vẽ lại SVG từ màu đã sample" bằng hình khối cơ bản → vỡ bố cục; user xác nhận tính năng cần là trace ảnh sang vector chứ không phải vẽ mới — Nguồn: `../raws/muse-ai-logo-gen-chain-of-agents.md#prompt-9` (`Nhận xét từ User: Vỡ bố cục hoàn toàn, tính năng không phải chuyển ảnh sang vector`; SVG validate chỉ có `7 shapes + 1 text`, 5 group cơ bản).
- Đối chứng: Prompt 8 dùng tham chiếu định tính (`xanh của facebook nhưng đậm hơn xíu`, phân biệt mặt trước/sau) thì qua ngay không cần sửa — Nguồn: `../raws/muse-ai-logo-gen-chain-of-agents.md#prompt-8` (không có nhận xét fail nào sau prompt này).

## Từ vựng đáng chú ý (quote EN + giải thích VI)

- `Resume from: snapshot <hash>` — kẹp ảnh nguồn cho edit kế tiếp, tương đương image-to-image có ref (VI: neo ảnh trước).
- `Shrink the gold coin by 40 percent so it is noticeably smaller` — ví dụ diễn đạt lại số % thành từ mơ hồ (`noticeably smaller`), model ảnh không có thước đo nên bỏ qua số.
- `Make the gold coin 1.5 times bigger` — hệ số phóng đại tương đối, cùng số phận: không neo tuyệt đối nên output gần như giữ nguyên.
- `Convert to completely flat design: remove all 3D embossing, soft shadows and gradients, use clean flat vector shapes with solid colors only` — mẫu câu chuyển style 3D→flat tái dùng được (liệt kê loại bỏ + neo bố cục).
- `tucked in the wallet opening, peeking out from the top ... partially behind the wallet edge` — cụm neo vị trí tương đối giữa 2 vật thể, là phần duy nhất agent làm đúng ổn định qua nhiều prompt.

## Công thức rút ra (pattern tái dùng)

1. Concept song song trước, đào sâu sau: sinh N style → user chốt 1 → edit nối tiếp bằng snapshot (đúng phần Prompt 1→2 của chuỗi).
2. Người viết prompt cứ dùng số tương đối tự nhiên (`giảm 40%`, `to 1.5 lần`); agent phải có thêm 1 bước CoT tính toán để hiểu ý đồ: đo trạng thái hiện tại trên ảnh (kích thước/vị trí đang là bao nhiêu) rồi quy ra spec tuyệt đối cho prompt gen (vd coin = 0.35 chiều rộng ví). Nếu không xác định được mốc tính — như `40%` không rõ 40% của size hiện tại hay của ví — thì agent phải hỏi user, cấm đoán mò rồi gen như Prompt 4. Chuỗi này fail 4 lần liên tiếp ở Prompt 3/4/5/7 vì thiếu đúng bước này.
3. Verify phải đo bằng pixel như Prompt 9 đã làm với màu (PIL sample hex), áp dụng cho kích thước/vị trí sau mỗi edit; read-back chỉ đọc file tồn tại (thậm chí đọc nhầm file như mục mascot) thì không phải verify.
4. Tham chiếu định tính (`xanh facebook đậm hơn xíu`) tin cậy hơn số trần (`to 1.5 lần`) khi làm việc với model ảnh không có thước đo nội tại.
5. Kết thúc chuỗi: chỉ lấy ảnh, bản vector phải dựng bằng công cụ trace chuyên dụng — "chuyển thành illustrator" bằng prompt là việc model ảnh không làm được (Prompt 9 vỡ bố cục là bằng chứng).

## Ghi chú bản quyền/nguồn

- Raw do user tổng hợp từ log agent MUSE.AI (chuỗi MoneyVVibe), không phải prompt influencer công khai; không re-post nguyên khối ra ngoài repo (Invariant 9). Model cụ thể không ghi trong raw nên digest không gắn tên model nào.
