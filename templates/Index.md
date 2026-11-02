# Index — template tái dùng

> Source of truth để tìm template. Template chưa test fill → giữ `drafts/`, không list ở đây.

## Agent (`agents/` — setup prompt gắn đầu phiên)

| Template | Dùng cho | Nguồn digest | Biến |
|----------|----------|--------------|------|
| `agents/agent-setup-measure-compute-ask.md` | Setup agent chuỗi edit định lượng: đo → tính → mơ hồ thì hỏi → verify bằng số (người giữ ý đồ, agent giữ con số) | `research/images/digests/muse-ai-logo-gen-chain-of-agents.md` (fill-test case Prompt 4 `giảm 40%` → nhánh ASK) | `[TASK_GOAL]`, `[STATE_IMAGE]`, `[MEASURE_CMD]`, `[ASK_CHANNEL]` |
| `agents/session-init-measure-ask.md` | Prompt init paste đầu session chat mới: bắt agent đọc 3 tài liệu + tuân thủ 6 quy tắc đo-tính-hỏi-verify | cùng digest trên (luật phiên, không cần fill-test biến) | (paste nguyên khối, không biến) |

## Ảnh (`images/`)

> Từ khóa theo 4 trục: NHÂN VẬT (`giữ-mặt`, `1-người`, `tĩnh-vật`) · HÀNH ĐỘNG (`đặt`, `trở`, `nêm`, `trình-bày`, `thay-nền`) · GÓC MÁY EN (`low-angle`, `top-down`, `fisheye`) · BỐI CẢNH (`bếp-tối`, `bao-bì`). Tối đa 8 tag/template.

| Template | Dùng cho | Nguồn digest | Biến | Từ khóa | Ref/Cost |
|----------|----------|--------------|------|---------|----------|
| `images/sk-sales-hero-9x16.md` | Ảnh hero bán hàng 9:16 (fisheye + nguyên liệu sống + bao bì) | production `.local/work/higgsfield/2026-09-29-soche/s1-master-final/` (ngoại lệ, chưa có digest) | `[PRODUCT]`, `[FISH]`, `[TRAY]`, `[PROPS]`, `[PACK]`, `[STYLE]` | `tĩnh-vật, top-down, fisheye, bao-bì` | `≥2-ref` |
| `images/bg-replace-video-opening.md` | Ảnh nền chuyển cảnh/mở đầu video từ vật thể bất kỳ (giữ vật, thay nền, khớp sáng) | `research/images/digests/bg-replace-greenscreen.md` (test fill chuỗi cart 2026-09-29) | `[SUBJECT_LOCK]`, `[ENVIRONMENT_DETAILS]`, `[LIGHT_DIRECTION]`, `[LIGHT_COLOR_TEMP]`, `[LIGHT_INTENSITY]`, `[AMBIENT_FILL]`, `[RIM_LIGHT]`, `[SHADOW_GROUNDING]`, `[ATMOSPHERE]`, `[LENS_TYPE]`, `[DEPTH_OF_FIELD]`, `[COLOR_GRADE]` | `giữ-vật, thay-nền, khớp-sáng` | `1-ref` |
| `images/kitchen-stock-continuity-16x9.md` | Stock bếp 16:9 chuỗi hành động liên tục (giữ mặt + prop + bếp) | production `.local/work/openrouter/2026-10-06-pan-*-1k/` + pack char (5 runs đạt; retro `journal/2026-10-06-iqf-kitchen-stock-retro.md`) | `[CHARACTER]`, `[ACTION]`, `[FOOD_STATE]`, `[CAMERA]`, `[FOCUS]`, `[PROPS]`, `[KITCHEN]`, `[LOCK_NEGATIVE]` | `giữ-mặt, 1-người, đặt, trở, nêm, trình-bày, low-angle, bếp-tối` | `3-ref-768 · $0.024` |

## Nháp (`drafts/` — chưa dùng được, không index ở đây)

> Draft video đã xóa khi compact image-only (D-010, 2026-10-09). Draft ảnh (nếu có) giữ trong `drafts/` tới khi fill-test pass.

Quy tắc merge: `.context/modules/templates.md`.
