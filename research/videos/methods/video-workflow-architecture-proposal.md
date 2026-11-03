# Ghi chú trước triển khai: workflow video và cấu trúc file

Ngày: 2026-11-03. Trạng thái: **đề xuất đã được yêu cầu ghi lại; chưa triển khai, chưa kiểm chứng production**.

Nguồn: trao đổi trực tiếp với user trong phiên ngày 2026-11-03. User yêu cầu “note lại workflow và cấu trúc file trước khi chỉnh sửa”. Ghi chú này lưu phương án để đối chiếu khi triển khai; không tự cấp quyền generation trả phí, không khôi phục runner/API hay di chuyển hồ sơ hiện hữu.

## 1. Phạm vi và nguyên tắc

- Workflow hiện tại không dùng video tham chiếu. Animatic/timeline nội bộ dùng để xét nhịp và dựng, không upload làm video conditioning. Nhánh có video tham chiếu sẽ được bàn riêng sau.
- Mục tiêu là video cinematic dùng được cho B2B/B2C với ít lần sinh nhất. Chi phí generation tính tổng mọi lần thử, gồm retry; công dựng/sửa theo dõi riêng. Không mặc định model nhiều chức năng hơn luôn đắt hơn trên mỗi sản phẩm đạt.
- Phân loại model theo năng lực; nhà cung cấp là chiều riêng. Một model có nhiều năng lực nên không sao chép hồ sơ vào các thư mục chức năng khác nhau.
- Tách “hỗ trợ input” khỏi “input bắt buộc trong mode”; ảnh đầu/cuối khác ảnh reference nhân vật, vật thể hoặc phong cách.
- Đơn vị lựa chọn và tính phí là tổ hợp model/version + provider + mode (offering). Năng lực công bố của model có thể khác phần provider đang cung cấp.
- `delta-analysis/` là phương pháp đối chiếu output thực tế với spec, phân tích lỗi và đề xuất thay đổi cho retry. Không coi cả thư mục là kho legacy chỉ vì nó chứa case cũ. Sửa có thể ở prompt, input, settings hoặc cấu trúc dựng; không mặc định mọi lỗi do prompt.
- Workflow Python chia theo nhiệm vụ; logic đặc thù model và kết nối provider nằm trong adapter riêng. Không nhân bản toàn bộ workflow theo từng model.

## 2. Cấu trúc dự kiến

Đây là cây thiết kế, không phải yêu cầu tạo scaffold rỗng. Giữ nguyên file và đường dẫn hiện hữu cho đến khi thực hiện thay đổi được chốt.

```text
workflows/
  INDEX.md
  ...                                  # Workflow research hiện hữu
  video/
    README.md                          # Quy trình vận hành
    no-video-reference.md

src/
  video/
    contracts.py                       # ShotSpec, GenerationRequest, RunResult
    registry.py                        # Tra model/provider/mode theo yêu cầu
    workflows/
      generate_shot.py                  # Điều phối một lần sinh shot
      retry_shot.py                     # Áp dụng phương án sửa đã chọn
    analysis/
      delta.py                         # Hỗ trợ thu bằng chứng và tổ chức phân tích
    models/
      <model_family>/
        <version_id>/
          capabilities.yaml            # Năng lực model, nguồn, ngày kiểm tra
          prompting.md                 # Quy tắc prompt theo model
          adapter.py                   # Ánh xạ yêu cầu chung sang ngữ nghĩa model
          validation.py                # Kiểm tra input/settings và tổ hợp hợp lệ
    providers/
      <provider_id>/
        client.py                      # Auth, upload, submit, poll, download
        offerings/
          <model_version_id>/
            config.yaml                # Các mode, giới hạn, giá tại provider
            adapter.py                 # Mapping request/response endpoint
    runs/
      recorder.py                      # Ghi run, trạng thái, phí, thay đổi

scripts/
  video.py                             # CLI mỏng gọi workflow chung

research/videos/
  INDEX.md
  delta-analysis/
    protocol.md                        # Phương pháp phân tích lỗi hiện hữu
    ...                                # Hồ sơ hiện hữu giữ nguyên
  methods/
    ...                                # Research và đề xuất chưa promote
  cases/
    <case-slug>/
      case.md
      runs/<run-id>.md

.local/video-runs/
  <case-slug>/<run-id>/
    ...                                # Media, request, response, log
```

Tên thư mục Python dùng identifier hợp lệ; tên case/run tiếp tục kebab-case. Layout này thay cho ý tưởng chỉ thêm catalog tài liệu mà chưa giải quyết code thực thi. Không tạo thêm một bộ catalog thủ công chứa bản sao capabilities/config; bảng tra cứu sau này nên được tạo từ metadata gốc hoặc chỉ liên kết tới nguồn đó.

### Ranh giới trách nhiệm

| Thành phần | Trách nhiệm |
|---|---|
| Workflow | Spec → chọn cấu hình → validate → sinh → ghi run → bàn giao QA/retry |
| Model adapter | Ngữ nghĩa input, cách chuẩn hóa yêu cầu và quy tắc riêng của model/version |
| Provider offering adapter | Tên trường, endpoint, payload và response thực của provider cho model/mode |
| Provider client | Giao tiếp dùng chung, xác thực và vòng đời job; không chứa logic sáng tạo |
| Delta Analysis | So expected/actual, ghi bằng chứng, giả thuyết, thay đổi và tiêu chí kiểm tra |
| Recorder | Liên kết case/run và artifact; lưu chi phí/trạng thái kể cả fail hoặc chưa rõ |

Chỉ tạo adapter có logic thật; không buộc một model phải có code riêng nếu metadata và adapter dùng chung đã đủ. Không nhân bản kiểm tra chung giữa model và provider: giới hạn model thuộc model, giới hạn bổ sung tại provider thuộc offering; validator kiểm tra cả hai.

`analysis/delta.py` không mặc định là máy tự chẩn đoán nguyên nhân. Nó có thể hỗ trợ lấy frame, gắn timestamp và lưu báo cáo; đánh giá hình ảnh/diễn xuất cần người hoặc công cụ có năng lực phù hợp. API completed không chứng minh video đạt spec.

### Metadata tối thiểu

- Model/version, provider và mode có ID rõ ràng.
- Mỗi input: hỗ trợ/không hỗ trợ/chưa rõ; bắt buộc/tùy chọn/không áp dụng theo mode; vai trò và giới hạn kết hợp.
- Duration, resolution, FPS, aspect ratio, audio và điều kiện khác nếu đã xác minh.
- Nguồn, ngày kiểm tra, mức bằng chứng: tài liệu/giao diện/run thực tế. Thiếu dữ liệu ghi chưa rõ.
- Giá niêm yết kèm đơn vị, điều kiện và ngày; phí thực lưu ở run. Không suy giá của provider này sang provider khác.
- Prompt hướng dẫn theo model viết tiếng Việt, prompt mẫu/kết quả viết tiếng Anh. Prompt chưa thử không gọi là template đạt.

Schema cụ thể của metadata và CLI chưa triển khai trong ghi chú này.

## 3. Walkthrough: “Từ hai ảnh sau tạo video”

Đây là mô phỏng luồng, không có ảnh hoặc run thực để kết luận. Hai ảnh không tự động đồng nghĩa hai endpoint.

### Bước 1 — Xác định vai trò input

Xác định A là start và B là end, hay hai ảnh chỉ làm reference. Hỏi khi vai trò không rõ. Các bước tiếp theo giả định user xác định cặp A → B là first/last frame.

### Bước 2 — Lập ShotSpec

Đọc A/B, ghi phần phải giữ, phần thay đổi, hành động nối, camera, nhịp/duration, mức cho phép cut/morph và tiêu chí acceptance. Tách quan sát khỏi suy đoán ý định. Nếu ảnh khác số lượng vật, chưa tự kết luận phải xuất hiện bằng morph hay đi vào cảnh. Hỏi những điểm mâu thuẫn ảnh hưởng trực tiếp hành động; mặc định nhỏ cần được nêu rõ.

Đầu ra là spec; so A/B ở bước này là delta mong muốn, chưa phải chẩn đoán lỗi video.

### Bước 3 — Kiểm tra tính khả thi và nhịp

Xét số thay đổi, contact, occlusion, camera và thời lượng. Với shot đơn giản, dùng timeline hai ảnh và các mốc hành động; không bắt buộc dựng animatic cầu kỳ. Ví dụ giả định: cầm hộp → hạ hộp → tiếp xúc bàn → buông → rút tay. Không kéo động tác ngắn ra hết clip chỉ để lấp thời gian.

Nếu spec và endpoint xung đột, đề xuất chỉnh input hoặc thiết kế shot trước khi sinh. Không lặng lẽ sửa ý định user.

### Bước 4 — Chọn offering và kiểm tra ngân sách

Lọc cấu hình thực sự nhận first/last frame, không video reference, đáp ứng settings cần thiết. Ưu tiên bằng chứng đạt trên loại shot tương tự và tổng phí gồm retry; chưa có benchmark thì ghi chưa rõ. Kiểm tra khả năng kết hợp các input, không chỉ từng tính năng riêng lẻ.

Chốt cấu hình, phí dự kiến và giới hạn thử theo quyền generation/ngân sách đã có. Không tự cấp quyền trả phí từ yêu cầu nghiên cứu hoặc ghi chú kiến trúc.

### Bước 5 — Prompt và request

Viết prompt EN mô tả chuyển động, trình tự contact, nhịp, camera và invariants. Gắn A/B vào trường first/last thật của request. Lưu prompt cuối cùng và settings thực đã gửi để truy vết; nhắc ảnh cuối trong text không thay thế conditioning.

### Bước 6 — Sinh một candidate, ghi run

Validate → submit → lưu job ID → poll → lấy output → ghi trạng thái và phí. Chưa batch nhiều biến thể ngay. Timeout sau submit phải kiểm tra job trước khi gửi lại; retry vận chuyển/API khác retry vì chất lượng. Không giả định request fail/cancelled là miễn phí.

### Bước 7 — Delta Analysis

So output với spec ở cùng giai đoạn/thời điểm và vùng hình. Ghi timestamp, expected/actual, bằng chứng và provenance, giả thuyết, phương án sửa, tiêu chí pass. Xem nhịp toàn clip và continuity, không chỉ frame cuối. Nếu chưa xem media, ghi user-reported thay vì directly-observed.

### Bước 8 — Dùng, dựng sửa, retry hoặc dừng

- Đạt spec: đưa vào dựng và dừng sinh thêm cho shot đó.
- Sửa được bằng dựng trong phạm vi spec: sửa và kiểm tra lại; không mặc định tăng tốc toàn clip.
- Cần sinh lại: chọn thay đổi có căn cứ, ưu tiên giữ các yếu tố còn lại ổn định; ghi biến đổi và dùng `retry_shot.py` tạo run mới cùng case.
- Hết ngân sách hoặc hướng sửa không hiệu quả: dừng hướng đó, xem lại input/shot; không tự retry vô hạn.

Với nhiều shot, kiểm tra trong bản dựng và kiểm tra seam theo hình lẫn chuyển động; endpoint chung không bảo đảm nối liền hoàn hảo. Tham khảo phương pháp nhịp/continuity ở liên kết bên dưới.

### Bước 9 — Bàn giao và tích lũy bằng chứng

Bàn giao video, kết luận theo acceptance và tổng phí tất cả lần sinh. Case giữ toàn bộ lịch sử run, kể cả fail; không tạo case mới chỉ vì đổi prompt/model/duration. Nếu chưa có sản phẩm đạt, báo “chưa có sản phẩm đạt; đã tốn X”, không tính ra chi phí/shot đạt giả định. Công hậu kỳ được ghi riêng nếu có dữ liệu.

## 4. Trạng thái trước chỉnh sửa

- Đã ghi nhận workflow và kiến trúc ở mức đề xuất.
- Chưa tạo `src/video/`, `workflows/video/`, CLI hoặc schema cấu hình; chưa di chuyển hồ sơ.
- Chưa chạy generation, benchmark hoặc kiểm chứng tỷ lệ pass/chi phí của kiến trúc.
- Khi triển khai cần đối chiếu capability/provider thực, xác định schema tối thiểu và thực hiện kiểm tra phù hợp; không biến ví dụ minh họa thành dữ liệu thật.

## Tham chiếu trong repo

- [Workflow không video tham chiếu](no-video-reference-workflow.md).
- [Nhịp, continuity và chi phí](cinematic-tempo-continuity-cost.md).
- [Delta Analysis: protocol hiện hữu](../delta-analysis/protocol.md).
- [Index research video](../INDEX.md).

Ghi chú này lưu thiết kế phần mềm và quyết định trao đổi, không đưa ra claim mới về khả năng của model/provider cụ thể.
