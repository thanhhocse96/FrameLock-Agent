# Animatic, Blender và motion transfer: nghiên cứu workflow AI video

Ngày kiểm tra nguồn: **2026-11-03**. Trạng thái: desk research, không generation mới, không benchmark pass-rate. User yêu cầu mở rộng nghiên cứu sang motion transfer, Higgsfield/Seedance và thực hành animator/producer; đây là phạm vi nghiên cứu được yêu cầu, chưa là quyền triển khai platform/mode hoặc paid generation.

Liên quan: [nghiên cứu tempo/continuity trước](cinematic-tempo-continuity-cost.md), [index video](../INDEX.md). Không thay đổi governance hoặc layout. Prompt minh họa dưới đây do phiên này soạn, `proposed-unverified`; không phải prompt influencer chép lại hoặc template đạt.

## 1. Câu hỏi và kết luận điều hành

Mục tiêu user: video cinematic dùng được B2B/B2C, tổng tiền có tính mọi retry, ưu tiên **ít lần sinh để có sản phẩm xem được**. Công chuẩn bị/hậu kỳ ghi bằng thời gian riêng; không tự quy đổi thành tiền lao động.

Kết luận từ tập nguồn đã đọc:

1. Animatic và Blender không loại trừ nhau. Animatic chốt bản dựng; Blender là một cách làm previs và có thể tạo tín hiệu chuyển động cho model.
2. Cần phân biệt: hai endpoint, video reference, V2V transformation, performance transfer, depth/pose control và AI mocap ra 3D. Đầu vào giống là “video” không đồng nghĩa cơ chế điều khiển giống nhau.
3. Hướng Blender → AI có bằng chứng thực hành và được hãng hỗ trợ, nhưng không có dữ liệu đối chứng đủ để kết luận luôn ít retry/rẻ hơn.
4. Với camera/layout/timing cứng, đáng thử đưa chuyển động mẫu thay cho mô tả thuần. Với diễn xuất tinh tế, có thể quay người thật làm mẫu ít công hơn dựng rig. Với sản phẩm phải chính xác, cần cân nhắc giữ asset trong render/compositing thay vì yêu cầu model tái tạo mọi pixel.
5. Blender không tự sửa seam hoặc chuyển động chậm: source sai timing, model retime, camera bị diễn giải lại và appearance drift vẫn tồn tại.

Các mục 4–5 bao gồm suy luận/đề xuất của nghiên cứu, không phải benchmark xác nhận trên provider user. Chưa biết chính xác hai provider/version của các clip đang lỗi.

## 2. Cách đánh giá nguồn

- **D — tài liệu hãng:** xác nhận chức năng được công bố; không chứng minh pass-rate hoặc ROI ngoài thực tế.
- **P — người làm trực tiếp:** bài breakdown, lời phỏng vấn về tác phẩm của họ. Có giá trị thực hành nhưng có thể chọn mẫu đẹp, thiếu log fail, hoặc quảng bá sản phẩm.
- **C — cộng đồng:** kinh nghiệm tự báo cáo; nghề nghiệp, cấu hình và output có thể chưa xác minh.
- **L — đầu mối chưa xác minh:** repost/nguồn thứ cấp, trang gốc không đọc được. Không dùng làm bằng chứng kỹ thuật độc lập.

Phiên này đọc nội dung văn bản công khai. Không tải hoặc kiểm định toàn bộ video demo từng frame; mọi verdict chất lượng của tác phẩm bên ngoài là source-reported. Không tính nhiều bài cùng tái bản một demo là nhiều lần chứng minh.

### Sổ nguồn và nội dung sử dụng

| ID | Loại / nguồn | Ghi nhận có thể dùng và giới hạn |
|---|---|---|
| D01 | [ByteDance: Seedance 2.0 launch, 2026-02-12](https://seed.bytedance.com/en/blog/official-launch-of-seedance-2-0) | Công bố reference ảnh/video/audio, gồm motion/camera. Đây là capability, không cam kết bám đúng mọi frame. |
| D02 | [ByteDance: Seedance 2.5 launch, 2026-07-31](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) | Nêu hỗ trợ clay render/motion reference, 30s và tối đa 30 ảnh + 10 video + 10 audio. Không suy từ thông báo launch ra quyền truy cập hoặc giá tài khoản hiện tại. |
| D03 | [Higgsfield: Seedance help](https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-seedance) | Hướng dẫn single-shot theo hành động, setting/light, camera, mood; gán vai trò reference. Giá thay đổi theo setting và hiện trên nút Generate. Web và MCP/API có cách tính credits khác nhau. |
| D04 | [Higgsfield: Seedance 2.5 prompting, 2026-08-13](https://higgsfield.ai/blog/seedance-2-5-prompting-guide) | Multi-shot chia style, scene, references, blocking, từng shot, camera, physics/light/audio. Hãng nói thử nhiều lần nhưng không đưa bộ log đủ để tính tỷ lệ đạt theo tiêu chí của user. |
| D05 | [Higgsfield: 3D Jutsu, 2026-09-05](https://higgsfield.ai/blog/higgsfield-3d-jutsu) | Scene 3D có object/camera sửa được trước video; là workspace trình duyệt, không phải Blender plugin. Đây là bằng chứng hướng sản phẩm, không chứng minh rẻ hơn Blender. |
| D06 | [Higgsfield: Genjutsu help, 2026-10-26](https://higgsfield.ai/creator-hub/help-center/tools/how-do-i-use-genjutsu) | Phân biệt motion transfer dựng lại cảnh với object swap sửa thành phần. Prompt có thể không cần; text thêm hướng sửa. Không coi lời quảng bá giữ nguyên mọi thứ là cam kết pixel-perfect. |
| D07 | [Higgsfield: Kling help, 2026-08-01](https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-kling) | Motion Control dùng ảnh nhân vật và video động tác rõ, framing tương thích, tránh cut. Không tự suy ra đây là bộ tái tạo toàn scene Blender. |
| D08 | [Runway: Act-Two](https://help.runwayml.com/hc/en-us/articles/42311337895827-Performance-Capture-with-Act-Two) | Ảnh nhân vật cho phép gesture transfer; video nhân vật giữ body/camera của video và nhận facial performance. Tài liệu nêu boomerang khi character video ngắn hơn performance. |
| D09 | [Luma: Ray3 Modify guide, 2025-12-12](https://lumalabs.ai/learning-hub/ray3-modify-user-guide) | Có mức bám source; tăng Reimagine có thể giảm camera preservation. Guide này ghi “end” có thể lấy mốc 5s khi source dài hơn, nên phải kiểm tra đúng phiên bản/UI. |
| D10 | [Lightricks: IC-LoRA training modes](https://github.com/Lightricks/LTX-Video-Trainer/blob/main/docs/training-modes.md) | Phân biệt control adapter depth/pose/canny với LoRA style; có pretrained adapters. Không đồng nghĩa mọi frontend/model hỗ trợ cùng tổ hợp control. |
| D11 | [NVIDIA: Controlled Video with ComfyUI](https://build.nvidia.com/playbooks/video-gen-guide) | Workflow được mô tả là 3D → keyframe có depth → first/last video. Không phải toàn bộ camera trajectory 3D được truyền vào video model. |
| D12 | [Higgsfield: edit one element / giá minh họa](https://higgsfield.ai/blog/edit-ai-video-without-regenerating) | Bài có bảng credit cho edit và cập nhật Lite. Đây là snapshot công khai, không phải báo giá checkout tài khoản. |
| D13 | [Higgsfield changelog](https://higgsfield.ai/creator-hub/changelog) | Entry Lite 2026-10-19 có thông số khác help ngày 26; ghi nhận thay đổi/chưa đồng bộ, không tự chọn thông số thuận lợi nhất. |
| P01 | [Hugo Caumo: Pushups for Love, 2026-10-24](https://3d-agent.com/blog/ai-short-film-blender-workflow) | Breakdown 18s, bốn shot: blockout → camera/motion reference → hình nhân vật → AI → dựng. Tác giả báo từng sửa cả blockout lẫn prompt và trim frame cuối bị chèn reference. Có liên hệ quảng bá 3D-Agent; không công bố tổng retry. |
| P02 | [Arub: Blender previz → V2V, cập nhật 2026-10-15](https://playbook.arub.ai/en/blender-previz-video-to-video/) | Tác giả tách motion/layout từ video khỏi appearance ảnh. Báo source ngắn bị kéo chậm khi output 15s; dùng source đủ 15s. Ghi nhận riêng arub-cast/MiniMax H3, không áp cho mọi model. |
| P03 | [Kévin Mendiboure: CATACOMBES, phỏng vấn Creative Bloq](https://www.creativebloq.com/ai/how-a-filmmaker-turned-a-10-year-old-unmakeable-movie-idea-into-reality-with-ai) | Tác giả báo 3.229 lượt **ảnh + video**, 242 giờ; dựng song song generation, khó continuity/đối thoại. Không chuyển con số thành video retry/shot hoặc chi phí tiền chưa công bố. |
| P04 | [Inferstudio / James Vinson / Nathan Su / Nour Hassoun, Autodesk case, 2026-09-24](https://blogs.autodesk.com/media-and-entertainment/2026/09/24/how-inferstudio-used-flow-studios-ai-mocap-to-make-a-3d-animated-film-they-didnt-know-was-possible/) | Dự án Daughter of the Inner Stars: footage diễn viên → AI mocap → animation được cleanup; asset làm thủ công. Animation TD Hassoun sửa dữ liệu. Đây là AI hỗ trợ 3D, khác generative V2V. Case do vendor xuất bản. |
| P05 | [Ryan Phillips / Promise, phỏng vấn Contagious, 2026-01-27](https://www.contagious.com/en/article/treat-ai-as-an-actor-or-co-author-on-set-f9fb9140287a441587ed5b955a5d21c8) | Có hướng khám phá từ hình/ý tưởng rồi phát triển câu chuyện; không mọi filmmaker khóa shot hết từ đầu. Đọc phần công khai, không tuyên bố đã xem toàn phỏng vấn subscriber. |
| C01 | [BradClarkAI: một năm AI filmmaking](https://www.reddit.com/r/aifilmmaking/comments/1v7hm7e/everything_ive_learned_after_1_year_of_ai/) | Tác giả mô tả visual canon, breakdown, shot plan và rough cut để giảm lãng phí. Có liên hệ sản phẩm workflow; tự báo cáo, không có đối chứng tiền/retry. |
| L01 | [Passport Rush repost/discussion](https://www.reddit.com/r/ProAI/comments/1w5qf0y/a_first_look_at_our_upcoming_aiintegrated_hybrid/) → [X gốc](https://x.com/higgsfield_ai/status/2095173479243063664) | Repost gắn nguồn Higgsfield; người bình luận tự nhận animator phản biện thiếu micro-control. X gốc bị 403, không coi repost là một studio độc lập hay prompt gốc đã xác minh. |
| L02 | [AI Primer: Blender previs creators](https://www.ai-primer.com/creative/stories/blender-previs-ai-animation-workflow) | Có đầu mối HalimAlrasihi, GlennHasABeard, koldo2k. Chưa xác minh các thread gốc; không dùng báo cáo $10/generation làm giá chuẩn hoặc dữ liệu A/B. |

## 3. Animator/producer có thực sự bàn vấn đề này không?

Có, nhưng chia thành những mục tiêu sản xuất khác nhau:

- **P01/P02 — creator thực hành previs → AI:** nguồn hữu ích cho cách gán vai trò reference và xử lý lỗi chuyển động; chưa có log đủ để khẳng định số lần sinh giảm bao nhiêu.
- **P03 — đạo diễn ưu tiên bản phim cuối:** bằng chứng rằng output cinematic có thể đi cùng lượng thử lớn. Lời tác giả “không được shot đúng lần đầu” là kinh nghiệm cá nhân, không là định luật AI video.
- **P04 — ê-kíp animation:** đầu tư vào dữ liệu chuyển động sửa được. Việc sửa timing/contact trong scene khác với trả tiền tái sinh video khi sai. Không lấy thành công phim 3D để chứng minh generative transfer giữ sản phẩm đúng.
- **P05 — hướng khám phá sáng tạo:** hữu ích lúc tìm concept. Với B2B có storyboard/brand đã duyệt, tự do ứng biến có thể tăng chi phí revision; đây là suy luận của nghiên cứu.
- **C01/L01 — cộng đồng:** bàn trực tiếp continuity và khả năng điều khiển chi tiết. Có cả ủng hộ lẫn phản đối. Không kết luận toàn ngành đã đồng thuận.

Khoảng trống quan trọng: không nguồn nào trong tập đã đọc cung cấp đối chứng cùng brief, cùng acceptance và toàn bộ chi phí để chứng minh “Blender + transfer luôn rẻ hơn mô tả”. Showcase thường cho biết phương pháp và output được chọn; số mẫu bỏ, mức retouch và revision khách hàng còn thiếu.

## 4. So sánh cơ chế, tránh chọn sai công cụ

| Nhánh | Tín hiệu thật đưa vào generation | Phần vẫn phải suy đoán | Phù hợp để nghiên cứu |
|---|---|---|---|
| A. Animatic → text + first/last | Hai trạng thái + chỉ đạo chữ | Hầu hết progression ở giữa | Shot đơn giản, sáng tạo linh hoạt |
| B. Blender chỉ xuất keyframe | Composition/pose chính xác hơn ở endpoint | Timing/đường đi giữa vẫn chưa được truyền | Cần framing nhất quán; không gọi là motion transfer |
| C. Blender RGB video → reference/V2V | Mẫu nhìn thấy theo thời gian | Appearance, phần bị che; mức bám phụ thuộc mode | Camera, blocking, nhịp có yêu cầu cụ thể |
| D. Video người thật → performance transfer | Biểu cảm/body theo khả năng model | Nhận dạng, tương tác scene và phần ngoài framing | Diễn xuất/phản ứng/gesture |
| E. Blender → depth/pose/canny control | Tín hiệu cấu trúc qua adapter | Appearance và chi tiết không có trong control | Khi cần tách hình thức khỏi chuyển động, chấp nhận setup kỹ thuật |
| F. AI mocap → rig → render/composite | Animation curve/rig có thể sửa | Không bắt video model tái tạo asset nếu render 3D | Asset lặp, product/character cần sửa xác định |

Phân loại dựa D01–D11/P04; đánh giá phù hợp là đề xuất cho dự án. Higgsfield là nền tảng có nhiều pipeline/model; Seedance là họ model. “Higgsfield vs Seedance” không phải hai lựa chọn cùng tầng: có thể chạy Seedance ngay trong Higgsfield. Luôn ghi platform + model/version + mode + loại reference.

**Đặc biệt:** D11 có Blender nhưng vẫn quay về hai endpoint; chỉ bổ sung 3D ở khâu ảnh sẽ chưa giải được thiếu tín hiệu thời gian mà user đang gặp. Ngược lại, D02 công bố clay-render reference là hướng sát hơn với câu hỏi Blender video → AI.

### Prompt không phải toàn bộ giao diện điều khiển

D06 có mode không bắt buộc text; D08 chủ yếu điều khiển bằng inputs/settings; D10 cần đúng adapter/node. Một prompt dài không thể thay slot motion reference, mask hay pose control bị thiếu. Cú pháp @ hoặc tên file chỉ có tác dụng tham chiếu đúng nếu frontend thực sự gắn asset tương ứng.

## 5. So sánh cấu trúc prompt

| Tác vụ | Cấu trúc hợp lý để thử | Điều nên bỏ |
|---|---|---|
| Single-shot đã có ảnh tốt | Hành động → nhịp/sự kiện → camera → continuity cần giữ → audio nếu dùng | Mô tả lại cả ảnh; nhiều tính từ mâu thuẫn motion |
| Multi-shot do model dựng | Quy tắc chung + cast/location → blocking ban đầu → từng shot với action/camera/điểm cắt → audio | Một đoạn dài không phân ranh shot; one-take lẫn hard cut |
| Blender → reference video | Vai trò từng asset → cái lấy từ motion → appearance → biến đổi cho phép → thứ tự ưu tiên → sound | Yêu cầu camera khác previs; copy mannequin lẫn “photoreal” |
| Performance capture | Diễn mẫu + framing/pose đầu phù hợp + settings transfer | Mong text sửa được diễn mẫu sai nhịp |
| Object/region edit | Chỉ rõ vùng/vật cần đổi → replacement reference → phần giữ → khoảng thời gian nếu mode hỗ trợ | Viết lại toàn cảnh, vô tình yêu cầu sáng tác shot mới |
| Blender blockout | Scene scale → vị trí/đường đi → key event theo frame → camera curve → contact → export | Shader chi tiết không phục vụ blocking; ép diễn cảm xúc bằng cube |

Đây là tổng hợp ứng viên, không quy định parser hoặc thứ tự bắt buộc toàn ngành. D03 và D04 dùng cấu trúc khác vì phạm vi single-shot/multi-shot khác. Bài D04 có claim mạnh về độ ổn định; chưa có ablation công khai đủ để coi việc thiếu một heading sẽ gây một lỗi xác định.

### Ví dụ đối chiếu cùng một ý đồ — do nghiên cứu soạn, chưa thử

Ý đồ: nhân vật bước tới bàn, đặt hộp xuống, rút tay; một shot 6s. Con số chỉ minh họa, cần diễn thử/timing trước sản xuất. Ảnh đầu/cuối và video mẫu phải cùng trạng thái, hướng đi, tỷ lệ hộp; không dùng đoạn text dưới đây để bù reference mâu thuẫn. Gắn placeholder với asset ID thật của UI; không gửi nguyên placeholder chưa điền.

**A — Prompt cho hai endpoint:**

```text
One continuous six-second shot at natural walking speed. The person walks from the opening position toward the table, lowers the box onto the marked area, releases it after contact, and withdraws both hands. The box reaches the tabletop at about four seconds; the remaining time shows the release and withdrawal. The camera tracks gently to the right while keeping the box and both hands readable. Finish in the supplied ending composition. Preserve the person's identity and the box's dimensions and label layout. Footsteps and a single soft contact sound.
```

Ý nghĩa: text vẫn giao quỹ đạo và các pose giữa cho model. “About four seconds” là yêu cầu, không timer bắt buộc. Không đánh giá bằng việc prompt có đủ từ.

**B — Prompt cho video reference có timing đã đúng:**

```text
REFERENCE ROLES
[MOTION_VIDEO]: use its camera path, subject trajectory, box placement, contact timing, and hand withdrawal. Preserve the source timeline without stretching the action.
[CHARACTER_IMAGE]: use the person's identity and wardrobe.
[PRODUCT_IMAGE]: use the box's appearance and label layout.
[LOOK_IMAGE]: use the materials and lighting, not its camera angle or poses.

Create a live-action version of the supplied blocking. Replace the proxy person and proxy materials with the referenced appearance. Keep the visible contact and event order from [MOTION_VIDEO]. Allow natural clothing and facial micro-movement without changing the planned action. The product remains one rigid box. Use the source camera movement rather than introducing another move. Add footsteps and one contact sound at the placement event.
```

Prompt B mô tả phân công reference, không kể lại một chuyển động khác. Source duration và request duration phải tương thích trong settings thực. Nếu tool không hỗ trợ nhiều input/vai trò này, không dùng nguyên cấu trúc rồi kỳ vọng tính năng xuất hiện.

**C — Chỉ sửa hình hộp khi motion đã đạt:**

```text
Replace only the box with the product in [PRODUCT_IMAGE]. Keep its existing position, scale, motion, and hand contact throughout the shot. Preserve the person, camera movement, background, and timing. Match the replacement's lighting and occlusion to the existing footage.
```

C là chỉ đạo sửa cục bộ; mask/selection phải cấu hình riêng nếu tool có. Brand/text chính xác vẫn phải QA; câu “preserve” không bảo đảm tuyệt đối.

**D — Chỉ đạo tạo previs trong Blender:**

```text
Build a six-second blocking scene at 24 fps, frames 1 through 144. Use one human-scale proxy, one rigid box, and one table. Keep the product at its approved dimensions. Animate the approach, lowering, table contact near frame 97, release, and hand withdrawal. The box remains attached to the hands until contact and stays on the table after release. Use a single camera tracking to the right; keep both hands and the contact point visible. Use simple contrasting materials. Export a clean preview without labels, grids, or interface overlays. Do not add an unplanned pause at the beginning or end.
```

Giữ frame/time convention nhất quán: frame 1 là t=0, frame 97 là t=4 tại 24fps. Constraint/contact và curve phải được người làm kiểm tra; code/agent chạy xong chưa chứng minh chuyển động đúng.

## 6. Workflow đề xuất để ít retry, theo loại shot

### 6.1 Bước chung: chốt bản dựng và tiêu chí

1. Lập animatic toàn đoạn từ ảnh/proxy/diễn thử; xác định shot nào cần continuous, shot nào cut.
2. Ghi mỗi shot: thông điệp, timing sự kiện, camera, phần không được sai, source-of-truth appearance, đầu/đuôi cần để dựng.
3. Chọn nhánh điều khiển theo nguyên nhân khó, không theo tên model nổi tiếng. Một phim có thể dùng nhiều nhánh nhưng giữ chung reference/grade/continuity.
4. Xác định bản “xem được” trước run: đúng nhịp, không hỏng product/contact, đọc được ý đồ, nối được vào cut. Không đòi mọi pixel hoàn hảo nếu brief không cần; cũng không dùng cinematic để bỏ qua sai sản phẩm.

### 6.2 Nhánh mô tả/endpoint

Animatic → ảnh đúng trạng thái → prompt motion ngắn → một candidate → đặt ngay vào timeline → chẩn đoán lỗi trước retry. Phù hợp khi đường đi không cần chính xác hoặc động tác đơn giản. Nếu liên tục sai cùng quỹ đạo/timing dù input rõ, cân nhắc thêm tín hiệu motion; không kéo dài prompt vô hạn.

### 6.3 Nhánh Blender làm reference video

1. Dựng thô đúng camera/layout/contact; không làm asset đẹp hơn mức model cần để đọc chuyển động.
2. Kiểm tra curve tốc độ: easing là lựa chọn có chủ ý. Linear không mặc định tự nhiên; smooth/ease không mặc định cinematic. Foot sliding hoặc mannequin diễn cứng là lỗi nguồn cần sửa trước.
3. Khớp aspect, duration, nhịp sự kiện và phần chuyển động nhìn thấy. Dùng ánh sáng đơn giản làm silhouette/contact dễ đọc; tránh overlay, text và giao diện lọt vào source.
4. Chuẩn bị look/identity/product reference tương thích góc nhìn. Chi tiết được kiểm tra ở final framing, không chỉ portrait đẹp.
5. Chọn mode thật sự đọc video motion hoặc control sequence. Gán riêng camera, body, layout, appearance; xác định mức được phép sáng tạo.
6. Sinh một candidate rồi so với previs theo event/contact/camera và với asset chuẩn theo identity/product. Lỗi motion sửa motion/control; lỗi appearance sửa reference/edit; tránh đổi cả hai rồi không biết nguyên nhân.
7. Dựng ngay vào cut, xem cả hai seam. Chỉ chỉnh shot sai. Giữ source previs để tái sử dụng cho variant nếu nó đã đạt.

Đây là quy trình ứng viên; chưa chứng minh giảm số lượt trên case hiện tại. Nguồn P01 cho thấy cả blockout lẫn text có thể phải sửa, nên “dựng một lần rồi chắc chắn transfer đạt” không có căn cứ.

### 6.4 Nhánh diễn xuất và nhánh asset chính xác

- Với ánh mắt, phản ứng, gesture: một performance điện thoại có thể truyền đạt timing rõ hơn animation thô. D08/D07 có giới hạn framing và input; không mặc định camera/body/face đều được lấy từ cùng video.
- Với product hero hoặc cơ cấu máy: cân nhắc render asset đúng và composite phần AI quanh nó. Nhánh này có chi phí dựng/rig/composite, nhưng cho phép sửa asset xác định. Chưa đủ dữ liệu nói luôn rẻ hơn.
- AI mocap giúp lấy animation, sau đó sửa trong DCC; khác với AI tạo video hoàn chỉnh. Quyết định mức cần sửa lại sau feedback khách hàng quan trọng ngang chất lượng take đầu.

## 7. Hai lỗi đang gặp: những điều nghiên cứu mới thay đổi

### Chậm dù đã có motion reference

P02 cung cấp một giả thuyết có dấu vết thực hành: source ngắn và output dài có thể làm action bị kéo giãn. D08 cho thấy mismatch duration ở một pipeline khác gây loop/boomerang. Không gộp chúng thành một cơ chế chung. Khi audit, đo event time ở source và output rồi xem output đã stretch, loop, giữ hình hay tự thêm động tác.

Nếu source có nhịp đúng mà output chậm, cần sửa duration/mode/strength trước khi kết luận phải animate lại. Nếu source đã chậm, transfer bám tốt cũng không cứu nhịp. Nếu chỉ camera đúng nhưng người diễn sai, cân nhắc chỉ chuyển camera hoặc cung cấp performance phù hợp; quyền điều khiển riêng phải được mode hỗ trợ, text chỉ là yêu cầu.

### Seam vẫn lệch sau Blender

Một scene 3D chung có thể làm camera/layout nguồn liên tục, nhưng các lần AI tạo appearance độc lập vẫn có thể khác nhau. Cần kiểm tra riêng continuity nguồn 3D và continuity output.

Đề xuất khi phù hợp model/brief: render một timeline liên tục qua điểm nối; chia cửa sổ source có đoạn chồng nhau thay vì hai clip đều dừng tại biên. Dùng đoạn chồng để chọn điểm dựng, không mặc định crossfade. Overlap làm tăng số giây bị tính phí và không bảo đảm appearance khớp; đây là thử nghiệm chưa kiểm chứng, chỉ đáng thử khi seam là bottleneck thật.

Trước paid retry: so source/output, trim frame rác/hold, sửa màu/transform nhẹ, chọn cut hoặc patch nếu brief cho phép. P01 là lời nhắc cụ thể rằng frame cuối có thể chứa reference bị chèn; không mặc định frame cuối là frame tốt nhất để truyền tiếp.

## 8. Chi phí: điều đã biết và chưa biết

### Đơn vị đo đúng theo user

`Tổng tiền = phí chuẩn bị phát sinh + tất cả generation/edit/retry bị tính phí − refund thực nhận`

Theo dõi thêm `số lần sinh tới bản xem được`, `số lần edit trả phí`, `thời gian chuẩn bị/sửa`, `trạng thái đạt`. Batch một request trả nhiều candidate phải ghi cả số request và số output tính phí, không làm số lần thử trông nhỏ giả tạo. Trial không đạt vẫn nằm trong tổng.

So sánh clip có cùng độ dài bàn giao, độ phân giải, acceptance và số variant. Không lấy giá một clip 5s so với clip 15s hoặc tính preview đạt là final đạt.

### Snapshot giá công khai, không phải báo giá tài khoản

| Nguồn | Con số đọc được | Dùng thế nào |
|---|---|---|
| D08 Act-Two | 5 credits/giây, tối thiểu 3s | 6s = 30 credits theo bảng web; không đổi credits sang USD nếu chưa biết plan; không ngang chức năng với toàn-cảnh V2V |
| D12 Genjutsu standard | Bảng 10s/1080p: 99 credits, bài quy đổi khoảng $4.95 | Bài ghi giá kiểm tra tháng 9/2026; chưa xác minh giá hiện tại trong account |
| D12 Seedance 2.5 Edit | Bảng 10s/1080p: 90 credits, bài quy đổi khoảng $4.50 | Giá edit, không dùng làm giá sinh từ text/ảnh |
| D12 Genjutsu Lite | Bài nói khoảng một phần ba standard trên web | Không suy thành giá cố định; đọc estimate ở lần submit thực |
| D03/D06 | Một số web plan có Unlimited; API/MCP vẫn trừ credits | Phải so cùng access route; phí biên bằng 0 không đồng nghĩa subscription/chờ đợi bằng 0 |

Không có tỷ lệ đạt đo được cho các nhánh trong repo, nên chưa tính expected cost từ giá quảng cáo. Điều kiện hòa vốn cho một clip: `S + m × b < n × a`, với S là tiền chuẩn bị tăng thêm, a/b là phí mỗi lượt của hai nhánh, n/m là số lượt thực. Khi đã có log nhiều clip mới ước lượng phân phối retry; không suy tỷ lệ đạt từ showcase.

### Mâu thuẫn tài liệu cần giữ lại

- D04 có đoạn nói 50 reference images; D02 phân loại 30 ảnh + 10 video + 10 audio. Ưu tiên phân loại model từ D02 và xác nhận frontend, không chuẩn bị 50 ảnh dựa một câu blog.
- D13 entry Lite 19/10 ghi 4–15s và có mode; D06 ngày 26/10 ghi 4–30s và không chọn mode. Có thể là cập nhật sản phẩm; chưa kiểm tra account. Không coi hai trang cùng đúng cho một request.
- D09 là guide Ray3 có lưu ý keyframe 5s. Trang API Modify đời Ray2 có redirect sang API mới; không lấy giá hoặc schema Ray2 để báo cho Ray3 hiện hành.
- D03 khuyên draft thấp rồi final cao. Đối với mục tiêu ít lượt của user, bước này không luôn rẻ: đổi model/tier/resolution có thể thay output, và ít nhất thêm một lượt. Chỉ draft nếu nó kiểm tra được rủi ro đủ lớn; render cuối vẫn phải QA.

## 9. Phản biện các lời hứa thường gặp

| Lời hứa | Phản biện / điều cần kiểm chứng |
|---|---|
| Có Blender là hết prompt roulette | Chỉ đúng phần được truyền và model bám được; Blender xuất hai ảnh không truyền cả motion |
| AI là render engine thay Blender | V2V có thể tái diễn giải geometry/lighting/identity; không tương đương renderer xác định |
| Thêm reference luôn tăng consistency | Reference khác state/góc/scale có thể mâu thuẫn; cần đúng vai trò và đúng thời điểm |
| Transfer giữ nguyên camera tuyệt đối | D09 mô tả tradeoff strength; các hãng khác công bố khả năng nhưng chưa có cam kết sai số bằng 0 |
| Prompt càng chi tiết càng ít retry | Chi tiết mâu thuẫn source làm tăng khó; prompt phải theo control đang có |
| Shot đẹp chứng minh workflow production | Cần cả revision, seam, sản phẩm, fail log và tổng tiền; tác phẩm được chọn không cho biết pass-rate |
| Một lần sinh dài rẻ hơn nhiều shot | Có thể giảm seam ngoài model nhưng tăng chi phí retry cả đoạn, sai chronology/cut; phải tính phần có thể sửa cục bộ |

## 10. Kế hoạch kiểm chứng tối thiểu, chưa được chạy

Không mở benchmark mọi hãng. Chọn một model/mode đọc được video reference và một brief đúng nhu cầu user trước.

**Hai bài thử có khả năng phân biệt nguyên nhân:**

1. Camera đi quanh sản phẩm đứng yên: kiểm tra camera path, tốc độ và logo/geometry. So endpoint-only với video từ cùng scene Blender, cùng look/identity.
2. Nhân vật đặt hộp xuống: kiểm tra timing, contact, release và hình hộp. Motion source phải được duyệt trước; source sai thì không thử AI để “cứu” giả thuyết.

Nếu endpoint và video reference dùng cùng model/settings khả dụng, đây là so input-control. Nếu phải đổi model/provider, ghi là so **hai workflow**, không kết luận riêng motion reference gây cải thiện.

Mỗi nhánh bắt đầu một candidate trong budget được chốt; đặt vào cùng bản dựng và chấm theo spec. Một candidate chỉ sàng lọc, không ước lượng pass-rate. Với mục tiêu production: dừng khi có bản đạt. Chỉ tiếp tục thử độ tái lập khi user có budget nghiên cứu riêng; không hy sinh ít lần sinh để có một báo cáo thống kê đẹp.

Log cần có: source duration/frame rate/aspect, event timing, actual submitted prompt/reference role, mode/version/settings, số output, phí và trạng thái, lỗi timestamp, phần footage dùng được, loại sửa và thời gian sửa. Riêng chuỗi thực dùng cả first/last vẫn theo case/run AGENTS §7. Nghiên cứu này không tạo run giả cho các demo ngoài repo.

## 11. Quyết định đề xuất cho AI-GAN

Giữ animatic làm bước chung. Không bắt toàn bộ phim qua Blender. Chọn lớp kiểm soát đủ cho rủi ro shot:

- Hình đẹp, motion đơn giản → endpoint/reference ảnh + chỉ đạo motion.
- Camera/layout/timing không được trôi → previs video; ưu tiên nghiên cứu mode có clay/motion reference thật.
- Diễn xuất tinh tế → performance người thật làm mẫu nếu phù hợp framing.
- Asset sản phẩm và revision chính xác → cân nhắc giữ 3D/composite; đừng mặc định AI phải vẽ lại sản phẩm.
- Clip đã đúng motion chỉ sai một phần → thử sửa vùng/vật có mục tiêu trước full reroll, sau khi so giá edit với reroll.

Thứ tự triển khai đề xuất này chưa được promote thành workflow pass. Kết luận chắc hiện tại là đã có nhiều nguồn trực tiếp bàn và thực hành hướng kiểm soát bằng previs/performance, nhưng **chưa có bằng chứng công khai đủ để chọn một nhánh rẻ nhất cho mọi clip**. Cần chọn theo lỗi chi phối và đo số lượt đến acceptance trên chính sản phẩm của user.
