# Sổ từ ngữ & lọc kiểm duyệt theo nền tảng

> Ghi nhận thực nghiệm để tránh đốt request khi làm việc đa nền tảng.
> Cập nhật mỗi khi gặp cờ kiểm duyệt mới, bất kể nền tảng nào.

## Quy ước trạng thái

| Trạng thái | Nghĩa | Điều kiện ghi |
|------------|-------|---------------|
| `blocked` | Request bị chặn thật | Có `request_id` + log `failed`/`nsfw` cụ thể |
| `suspected` | Nghi ngờ, chưa cô lập | Nằm trong prompt bị chặn nhưng đổi ≥2 từ cùng lúc, chưa test đơn biến |
| `safe` | Đã qua kiểm duyệt | Xuất hiện trong request `completed` ≥1 lần (ghi rõ nền tảng) |

## Nền tảng: Higgsfield — MiniMax H3 image-to-video

| Từ/cụm | Trạng thái | Bằng chứng |
|--------|------------|------------|
| `slams down` | `suspected` | clip-1bc `7fd67d79` → nsfw; retry đổi đồng thời 2 cụm → qua (`4c91aba1`) — chưa tách đơn biến |
| `dense burst` | `suspected` | Cùng cặp trên (đổi thành `fine mist` ở bản qua) |
| `burst` (mọi dạng) | `suspected` | Chưa tách khỏi `dense burst` — test đơn biến khi cần |

Từ `safe` trên nền tảng này: `pours`, `pours gently`, `pouring stream`, `spiraling`, `vortex`, `lifts`, `levitate`, `float`, `cap pops off`, `tumbling`, `cascading`, `settling`, `simmering`, `steam`, `mist`, `fine mist`, `pull-back`, `swirling`, `circles`, `ignites`, `glowing energy ring`, `reveals`, `holding`

## Nền tảng: (mẫu cho nền tảng sau)

```markdown
## Nền tảng: <Tên> — <Model>

| Từ/cụm | Trạng thái | Bằng chứng |
|--------|------------|------------|
| ... | blocked / suspected / safe | request_id + kết quả |
```

## Quy tắc chung đa nền tảng

1. **Không mang kết luận qua nền tảng khác:** từ `safe` ở Higgsfield vẫn có thể bị chặn ở platform khác — mỗi nền tảng 1 bảng riêng.
2. **Test đơn biến khi cần kết án:** prompt bị chặn mà đổi nhiều từ cùng lúc thì tất cả chỉ ở `suspected`; muốn lên `blocked` thì giữ nguyên prompt, đổi đúng 1 từ rồi chạy lại.
3. **Khi bị chặn:** đổi từ trước, giữ nguyên frames (xem PITFALLS #13); ghi cặp rớt/qua kèm `request_id` trước khi thử tiếp.
4. Động từ mạnh bạo lực (`slam`, `burst`, `explode`, `blast`, `crash`) mặc định thay bằng từ mềm (`pour`, `mist`, `drift`, `settle`, `unfold`) ở nền tảng mới cho tới khi có bằng chứng ngược.
