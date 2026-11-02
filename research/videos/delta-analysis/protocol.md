# Quy trình Delta Analysis — bản đề xuất v0.2

Tham khảo skill [ui-debug — State Delta Framework](../../../../skvn-marine/.agents/skills/ui-debug/SKILL.md), đọc ngày 2026-10-12. Đây là tham chiếu local sang repo kế bên; checkout độc lập cần có repo đó để mở link. Kế thừa: đọc clue → xác định states → phân tích năm trục → ISOLATE → DIFF → PROVE. Chỉ chuyển giao phương pháp; các lệnh WordPress/DevTools và quy tắc CSS không áp dụng cho video.

## Nguyên tắc — delta trước, nguyên nhân sau

Liệt kê clues từ mô tả user trước khi đề xuất sửa. Clue là hướng điều tra, không phải bằng chứng nguyên nhân. “Ảnh sau zoom in có ba miếng cá” cho thấy số lượng nhìn thấy và framing khác nhau; chưa chứng minh cá đã được thêm, bị nhân đôi hay được reveal.

Phân biệt hai loại cặp state:

- **START / END:** hai trạng thái mong muốn của chuyển cảnh. Cả hai có thể đúng; delta là công việc cần thực hiện, chưa phải bug.
- **EXPECTED / ACTUAL:** trạng thái theo spec và trạng thái video thực tế, so tại cùng thời điểm/giai đoạn và vùng quan sát. Delta này mới mô tả lỗi. Nếu có run đạt và run lỗi, so thêm **WORKING / BROKEN** với input/settings của từng run.

Không đổi tên START thành “đúng” và END thành “sai”. Khi chưa có video hoặc run lỗi, đầu ra là phân tích rủi ro và phương án thử, không phải chẩn đoán nguyên nhân đã xác nhận.

## Năm trục State Delta cho video

| Trục từ ui-debug | Chuyển sang video | Phép kiểm tra phân biệt |
|---|---|---|
| Environment | Model/version/provider, mode và control thực có | Đối chiếu cấu hình/request thực của working và broken; tên model giống nhau chưa đủ |
| Time | Trước/sau hành động, lúc contact, lúc camera đổi, lúc lỗi bắt đầu | Xác định khoảng cuối còn đúng → đầu thấy sai; xem dày hơn quanh khoảng đó |
| Layer | Spec → keyframe/ref → prompt/request thực gửi → generation → dựng/export | Tìm tầng đầu tiên lệch contract; so clip gen gốc và bản dựng nếu cả hai có sẵn |
| Scope | Một miếng cá hay toàn chảo; một vùng, một đoạn, một cặp frame hay nhiều run | So vùng lỗi với vùng đối chứng; xem lỗi có bắt đầu cùng camera/occlusion không |
| Data/State | Số lượng, identity, pose, contact, trạng thái cá, framing trong ảnh và từng frame video | Đối chiếu spec, input thực và output; đếm vật nhìn thấy, đánh dấu vật bị che/chưa rõ |

Một thử nghiệm fail chỉ làm yếu giả thuyết trong điều kiện đã thử. Không áp dụng máy móc suy luận “bỏ một thành phần mà vẫn lỗi → thành phần đó không liên quan”, vì generation có ngẫu nhiên và tương tác giữa các biến.

## Input và mức bằng chứng

Thu thập: ảnh A/B và vai trò (first/last frame hay reference), spec user, video lỗi hoặc mô tả, prompt đã chạy, model/version/provider, mode, duration, settings/seed nếu có. Trường thiếu ghi `chưa rõ`; không tự điền từ một run khác. Ngữ cảnh repo có nhiều model, không có một model mặc định cho mọi case.

Spec phải nêu: thay đổi mong muốn, phần phải giữ, camera, timing, có cho cut/fade/che khuất không, ưu tiên khi yêu cầu xung đột. Nếu chưa rõ một chi tiết khác biệt là có chủ ý hay lỗi của keyframe, hỏi trước khi viết prompt phụ thuộc vào nó.

Quan sát trực tiếp: ghi timestamp hoặc khoảng thời gian, vùng ảnh/vật, bằng chứng frame và phần đã xem. Frame lấy mẫu có thể bỏ sót lỗi giữa hai mẫu; tăng mật độ quanh vùng nghi lỗi. Nếu chưa xem được video, ghi `user-reported`, không viết “AI đã xem”. Mô tả của user là bằng chứng về báo cáo, chưa phải xác minh trực tiếp cơ chế lỗi.

## Delta 1 — ảnh A so với B

Lập bảng `đối tượng/thuộc tính | A | B | chủ ý? | phải giữ? | độ chắc chắn` cho danh tính, số lượng, pose, vị trí, contact, trạng thái, kích thước, camera/framing, nền, ánh sáng và chữ/logo. Kiểm tra tất cả trục dù user gọi là “một chi tiết”. Hai ảnh không xác định duy nhất hành động ở giữa.

Phân biệt khác biệt quan sát được với nguyên nhân: vật nhỏ đi trong ảnh có thể do camera lùi, vật di chuyển hoặc đổi kích thước. Chưa đủ bằng chứng thì giữ các khả năng, không chốt camera move.

Thiết kế cầu nối: chuyển động nào đưa A đến B, vật đi qua đâu, tay nào giữ vật, lúc nào tiếp xúc/che khuất, thời điểm hoàn thành và settle. Vật thêm/bớt phải có đường vào/ra nếu spec yêu cầu liên tục; không mặc định cho nó tan hoặc xuất hiện giữa khung.

Nếu A/B đổi cả scale và vật nhưng spec khóa camera, ghi mâu thuẫn. Đề xuất chỉnh keyframe, đổi camera hoặc dựng cắt theo quyền user cho phép; không cố chữa bằng câu chữ mâu thuẫn. Timing chỉ là mục tiêu cần kiểm chứng trên model/mode được chọn.

## Delta 2 — video thực tế so với spec

Mỗi lỗi một dòng:

| Timestamp / vùng | Spec | Thực tế | Nguồn quan sát | Giả thuyết nguyên nhân | Case gần nhất | Chỉnh sửa | Tiêu chí pass |
|---|---|---|---|---|---|---|---|
| Chưa có ca mới | Chưa rõ | Chưa rõ | Chưa có media | Chưa kết luận | Tra INDEX | Chưa đề xuất fix cụ thể | Do spec quyết định |

Nhóm lỗi: identity/shape, xuất hiện-biến mất, contact/topology, quỹ đạo, nhịp, camera, cut/fade, endpoint, ánh sáng, text. Một video có thể có nhiều lỗi; chọn lỗi ưu tiên theo spec thay vì tự chọn chi tiết dễ sửa nhất.

## Truy xuất kinh nghiệm và chọn sửa

### ISOLATE — thu hẹp bài toán nhưng giữ điều kiện gây lỗi

Chọn đoạn/vùng nhỏ nhất còn thể hiện lỗi; dùng đúng input và request của run lỗi nếu có. Với hai ảnh chưa có clip, đây là thiết kế case tối giản, chưa phải tái hiện bug. Chỉ loại phần không liên quan khi nó không làm mất điều kiện lỗi. Đổi camera, ảnh hay số cá để đơn giản hóa phải ghi rõ là can thiệp.

### DIFF — so states trước khi chọn can thiệp

Lập bảng `thuộc tính | expected/working | actual/broken | khác biệt quan sát | chưa biết`. Tách camera khỏi số lượng và identity. Sau đó ghi `giả thuyết | bằng chứng ủng hộ/phản bác | thử nghiệm phân biệt | outcome dự đoán`. Truy xuất case gần nhất để chọn thứ tự thử, không dùng case thay cho quan sát hiện tại.

### PROVE — thử lại đúng điều kiện lỗi và kiểm tra output

Ghi baseline và biến sửa; chạy lại điều kiện lỗi cũ khi được phép generation. So toàn clip theo tiêu chí đã đặt, gồm vùng/thời điểm lỗi và phần phải giữ. Có điều kiện thì lặp baseline và candidate với cùng ngân sách mẫu, báo số pass trên tổng số run và settings; một candidate pass chỉ chứng minh mẫu đó đạt, chưa chứng minh nguyên nhân hoặc độ ổn định. Nếu chưa chạy thì ghi `proposed-unverified`.

Prompt có chữ “three fish” hoặc đã tạo ảnh trung gian không chứng minh output giữ đúng ba miếng. Đây là tương đương anti-pattern của ui-debug: kiểm tra text trong source thay vì behavior thực. Tránh đổi hàng loạt prompt/ref/model rồi gán thành công cho một sửa đổi.

Tra `INDEX.md`, mở đúng case liên quan. Xếp theo cơ chế lỗi, cấu trúc delta, model/mode/provider và ràng buộc user. Nêu cả điểm giống và khác. Case cùng model có ích nhưng không chứng minh fix sẽ thành công; case khác model chỉ là ứng viên transfer.

Phân biệt ba lớp: **quan sát**, **giả thuyết**, **kết quả thử**. Dùng trạng thái `journal-reported`, `directly-observed`, `proposed-unverified`, `tested-pass`, `tested-fail`; trạng thái pass/fail phải có tiêu chí và nguồn. Một request completed không đồng nghĩa video đạt spec.

Chọn lớp sửa theo chẩn đoán: prompt (motion/timing/blocking), keyframe/ref (trạng thái/bố cục sai), settings/mode (thời lượng hoặc control không phù hợp), cấu trúc clip/dựng (multi-change hoặc endpoint bất khả thi). Không mặc định mọi lỗi đều sửa được bằng prompt. Không gọi mô tả end frame trong text là ràng buộc last-frame thật nếu mode không nhận last frame.

## Output mỗi lần phân tích

1. Tóm tắt delta mong muốn và phần giữ nguyên.
2. Bảng lỗi kèm timestamp/nguồn và điều chưa biết.
3. Case kinh nghiệm được dùng, giới hạn áp dụng và giả thuyết ưu tiên.
4. Patch tối thiểu: câu cũ → câu mới (nếu có prompt gốc); prompt hoàn chỉnh tiếng Anh; thay đổi keyframe/settings/dựng ghi riêng.
5. Kế hoạch thử: biến được đổi, biến được giữ, tiêu chí pass/fail và bước tiếp khi fail.

Đầu báo cáo liệt kê clues và loại cặp state. Mỗi đề xuất phải trả lời: delta nào được xử lý, vì sao chọn tầng sửa đó, kết quả nào sẽ làm yếu giả thuyết. Không mặc định thêm keyframe hoặc viết lại prompt trước bước DIFF.

Mỗi thử nghiệm ưu tiên đổi một biến. Giữ input/model/settings còn lại nếu có thể; seed cố định chỉ khi công cụ hỗ trợ và không bảo đảm tuyệt đối tính lặp lại. Nếu phải đổi nhiều biến, ghi đây là thử phối hợp, không gán kết quả cho một câu prompt. Xác nhận cải thiện qua lặp có kiểm soát khi cần, tránh kết luận từ một mẫu may mắn.

Tiêu chí: chi tiết đạt B, invariants giữ suốt clip, motion/contact đúng đường, nhịp đúng spec, không cut/fade nếu bị cấm. Không lấy frame cuối đúng làm bằng chứng cả clip đúng. Theo kinh nghiệm DA-002, giới hạn thử mặc định tối đa 3 lần cho một hướng; khi hết giới hạn, xét lại input/cấu trúc hoặc dựng. Không dùng số lần này như bảo đảm thành công.

## Ví dụ minh họa, chưa thử

A: tay giữ xẻng trên chảo. B: chảo giữ nguyên, xẻng và tay ra ngoài. Giả định spec cho phép tay rút qua mép phải, camera tĩnh, clip 5 giây. Đây là ví dụ giả lập dựa trên nguyên lý mép khung DA-002, không phải ca đã pass.

```text
A continuous close-up with a locked-off camera. The hand carries the spatula smoothly out through the right edge of the frame during the first three seconds. The spatula stays firmly held by the hand throughout the movement. The pan and fish remain stationary, with consistent shape and lighting. For the final two seconds, hold on the pan and fish in the ending composition.
```

Check: tay/xẻng ra qua mép phải, không tan giữa khung, cá/chảo không đổi hình, camera giữ framing, thời điểm ra/hold đúng spec. Nếu B khác scale hoặc camera, giả định này không còn hợp lệ.

## Lưu case mới

Case gồm: ID/ngày; input/đường dẫn media local; spec; model/mode/settings; prompt trước/sau; delta A/B; quan sát video và provenance; case nguồn; giả thuyết; biến đổi; kết quả/pass-fail; phạm vi transfer. Ghi lịch sử thử nối tiếp, không xóa lần fail. Chỉ promote kinh nghiệm khi kết quả có bằng chứng; chỉ promote template theo quy tắc test của repo.
