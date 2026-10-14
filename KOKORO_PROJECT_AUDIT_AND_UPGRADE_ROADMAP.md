# 🌸 KOKORO (心) — ĐẠI DỰ ÁN RÀ SOÁT TOÀN DIỆN & LỘ TRÌNH NÂNG CẤP CHIẾN LƯỢC TOÀN NĂNG (v1.8.0 – v3.0.0+)

> **Dự án:** Kokoro (心) — Personal Diary, Photo Journal & Mindfulness Platform  
> **Kiến trúc cốt lõi:** Starlette ASGI + PostgreSQL 18 + Mobile-First Liquid Glass PWA  
> **Phiên bản hiện tại:** `v1.7.7` *(Single Source of Truth từ `VERSION`)*  
> **Trạng thái kiểm thử:** 102/102 Test Cases PASS (100%), Playwright E2E Browser Testing Ready  
> **Ngày cập nhật rà soát:** 14/10/2026  
> **Tầm nhìn sản phẩm:** Nâng tầm Kokoro từ một ứng dụng PWA nhật ký cá nhân hoàn thiện thành một **Nền tảng Quản lý Kỷ niệm, Sức khỏe Tinh thần & Lưu trữ Cuộc đời Đa giác quan (All-in-One Life Journaling & Mindfulness Platform)** sánh ngang hoặc vượt trội hơn các ứng dụng hàng đầu thế giới (Day One, Journey, Apple Journal, Stoic, Rosebud).

---

## 🧭 PHẦN I: TẦM NHÌN SẢN PHẨM & MA TRẬN 10 TRỤ CỘT TÍNH NĂNG TOÀN DIỆN

Sau khi rà soát sâu sắc toàn bộ hành trình trải nghiệm người dùng (User Journey) và các chuẩn mực quốc tế về lưu trữ ký ức cá nhân, một cuốn nhật ký đích thực của tâm hồn không chỉ dừng lại ở việc gõ chữ và tải ảnh. Nó cần chạm đến mọi giác quan, đồng hành cùng thói quen sống, bảo vệ bí mật tuyệt đối và có khả năng đúc kết thành những di sản kỷ niệm hữu hình.

Dưới đây là **Ma trận 10 Trụ Cột Tính Năng Toàn Diện** được quy hoạch đồng bộ:

```
┌───────────────────────────────────────────────────────────────────────────────────┐
│                    KOKORO — HỆ SINH THÁI NHẬT KÝ & CHỮA LÀNH (心)                 │
├─────────────────────────┬─────────────────────────┬───────────────────────────────┤
│ 1. SOẠN THẢO ĐA PHƯƠNG TIỆN│ 2. MẪU BÀI & LIỆU PHÁP   │ 3. LỐI SỐNG & CHỈ SỐ CUỘC ĐỜI │
│ • Voice Journal & STT   │ • Morning/Evening Zen   │ • Habit Tracker tích hợp      │
│ • Floating Markdown     │ • Stoic Reflection      │ • Tự động Thời tiết & Tuần trăng│
│ • Video ngắn & Doodle vẽ│ • Catharsis "Hóa tro"   │ • Đếm ngày kỷ niệm D-Day      │
├─────────────────────────┼─────────────────────────┼───────────────────────────────┤
│ 4. BẢN ĐỒ & DẤU CHÂN    │ 5. TRÍ TUỆ NHÂN TẠO AI  │ 6. CHIÊM NGHIỆM & THỜI GIAN   │
│ • Trích xuất EXIF GPS   │ • AI Zen Companion      │ • Thư gửi tương lai (Capsule) │
│ • Bản đồ ký ức Leaflet  │ • Sóng cảm xúc Circumplex│ • Chiếc lọ biết ơn (Jar)      │
│ • Địa điểm & Check-in   │ • Weekly AI Digest      │ • Box Breathing thiền hít thở │
├─────────────────────────┼─────────────────────────┼───────────────────────────────┤
│ 7. KHÁM PHÁ & THƯ VIỆN  │ 8. IN ẤN & XUẤT BẢN     │ 9. BẢO MẬT & QUYỀN RIÊNG TƯ   │
│ • Full-Text Search FTS  │ • Xuất sách Photobook PDF│ • WebAuthn FaceID/Vân tay     │
│ • Lọc đa tầng phức hợp  │ • Kokoro Wrapped năm    │ • Mã hóa đầu cuối E2EE AES-256│
│ • Nhận diện màu sắc ảnh │ • Social Card Studio    │ • Thùng rác tạm thời (30 ngày)│
├─────────────────────────┴─────────────────────────┴───────────────────────────────┤
│                   10. TỰ CHỦ DỮ LIỆU, ĐỒNG BỘ ĐA THIẾT BỊ & NỀN TẢNG              │
│ • Đồng bộ 2 chiều (Conflict Resolver) • Auto-backup Google Drive / WebDAV         │
│ • PWA Web Push Notification • Đóng gói Desktop Tauri v2 & Mobile Store Apps       │
└───────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔍 PHẦN II: CHI TIẾT 10 TRỤ CỘT TÍNH NĂNG CẦN BỔ SUNG

### 1. Trình Soạn Thảo Đa Phương Tiện & Nghệ Thuật (Creative Multimedia & Rich Editor)
- **Voice Journaling & Speech-to-Text (STT):**
  - Ghi âm trực tiếp qua Web Audio API; hiển thị sóng âm thanh nước chảy/sóng biển mượt mà phong cách Soft Sakura.
  - Tự động phiên âm giọng nói tiếng Việt thành văn bản (chế độ Web Speech API trên máy client + tùy chọn backend `faster-whisper` cho độ chuẩn xác 100%).
  - Audio player mini bo góc gắn liền với thẻ bài viết ngoài Timeline.
- **Floating Markdown Toolbar:**
  - Thanh công cụ nổi thông minh: **In đậm**, *In nghiêng*, `> Trích dẫn`, `- Danh sách`, `[ ] Hộp kiểm việc cần làm`, `--- Đường phân cách`.
  - Bộ đếm số từ (Word Count) và ước tính thời gian đọc (Reading Time).
- **Video Kỷ Niệm Ngắn & Live Photo / GIF:**
  - Hỗ trợ tải lên video ngắn (< 30 giây, nén tự động WebM/MP4) để lưu lại nụ cười, tiếng gió, khung cảnh chuyển động.
  - Hỗ trợ ảnh động GIF nhẹ và hiển thị mượt mà.
- **Khung Vẽ Phác Thảo & Chữ Ký Số (Doodle Canvas):**
  - Khung vẽ tay mini bằng nét cọ nước màu pastel ngay trên màn hình cảm ứng: vẽ hoa, vẽ trái tim, ký tên lưu bút.
- **Digital Scrapbooking & Stickers:**
  - Bộ sticker hoa lá, trà đạo, mèo con, origami phong cách Nhật Bản.
  - Cho phép gắn sticker trang trí lên góc thẻ bài viết hoặc góc ảnh.

### 2. Mẫu Nhật Ký Theo Ngữ Cảnh & Liệu Pháp Viết (Contextual Templates & Therapeutic Writing)
- **Kho Mẫu Nhật Ký Đa Dạng (Diary Template Studio):**
  - *5-Minute Morning Journal:* 3 điều biết ơn hôm nay, điều gì sẽ làm ngày hôm nay tuyệt vời, lời khẳng định tích cực.
  - *Evening Stoic Reflection:* Điều gì mình đã làm tốt hôm nay? Điều gì còn thiếu sót? Tâm trí có an yên không?
  - *Travel Diary (Nhật ký xê dịch):* Lịch trình, tọa độ, điểm nhấn ẩm thực, chi phí đáng nhớ.
  - *Cafe & Chill Corner:* Tên quán, bản nhạc đang nghe, đồ uống, đánh giá không gian (1-5 sao).
  - *Book & Movie Review:* Tựa đề, trích dẫn tâm đắc, bài học nhân sinh rút ra.
- **Chế Độ Giải Tỏa "Hóa Tro Muộn Phiền" (Catharsis Venting Burn Mode):**
  - Một ô viết dành riêng cho những cơn giận dữ, ấm ức hay nỗi đau cần giải phóng.
  - Sau khi viết hết tâm can, người dùng bấm nút **[ 🔥 Đốt Cháy Muộn Phiền ]**: hiệu ứng tro tàn tan biến sinh động, bài viết lập tức bị tiêu hủy vĩnh viễn không lưu lại vết tích trong CSDL, giúp tâm lý được xả van an toàn.

### 3. Theo Dõi Lối Sống, Chu Kỳ & Thói Quen (Life Tracking, Astro & Habit Integration)
- **Habit Tracker Tích Hợp Thẻ Nhật Ký (Micro Habit Check-in):**
  - Cho phép người dùng theo dõi 3-5 thói quen cốt lõi mỗi ngày ngay dưới bài viết: Uống đủ 2L nước, Ngủ $\ge 7\text{h}$, Đọc sách 15 phút, Tập thể dục / Đi dạo, Thiền định 10 phút.
  - Tự động phân tích tương quan giữa thói quen và cảm xúc (Ví dụ: Những ngày hoàn thành đủ thói quen thì tâm trạng có tỷ lệ "Năng lượng" cao hơn 40%).
- **Tự Động Lấy Thời Tiết Thực Tế & Chu Kỳ Tuần Trăng (Auto Weather & Moon Phases):**
  - Tự động lấy nhiệt độ, độ ẩm, biểu tượng thời tiết thực tế qua tọa độ IP/GPS thay vì chỉ chọn thủ công.
  - Hiển thị chu kỳ tuần trăng (Moon Phase: Trăng non 🌑, Trăng khuyết 🌓, Trăng tròn 🌕) — chi tiết phong thủy & thiên văn gắn liền với chu kỳ cảm xúc của con người.
- **Bộ Đếm Ngày Kỷ Niệm & D-Day Milestones:**
  - Đếm xuôi: "Đã 520 ngày yêu nhau", "365 ngày kể từ ngày chuyển việc", "100 ngày kiên trì viết nhật ký".
  - Đếm ngược: "Còn 25 ngày đến Tết", "Còn 10 ngày đến chuyến du lịch Nhật Bản".
  - Tự động hiển thị huy hiệu đếm ngày trên đầu thẻ nhật ký tương ứng.

### 4. Bản Đồ Ký Ức, Không Gian & Dấu Chân Địa Lý (Geotagging, Places & Memory Map)
- **Trích Xuất Vị Trí EXIF & Check-in Tùy Chọn:**
  - Tự động đọc tọa độ GPS từ ảnh chụp qua thư viện Pillow (có popup xin quyền để bảo vệ riêng tư).
  - Cho phép gõ tên địa điểm thủ công (Ví dụ: "Hồ Tây, Hà Nội", "Góc phố cổ", "Đỉnh Fansipan").
- **Giao Diện Bản Đồ Ký Ức (Interactive Memory Map View):**
  - Tích hợp bản đồ Leaflet.js phong cách Pastel Soft Sakura với các cụm ghim hoa anh đào.
  - Thu phóng bản đồ thế giới/Việt Nam: chạm vào một tỉnh/thành phố để mở bung danh sách các bài viết và album ảnh đã chụp tại nơi đó.
- **Hành Trình Du Lịch (Trip Album Timeline):**
  - Khả năng gom các bài viết theo chuyến đi (Ví dụ: "Chuyến đi Đà Lạt 4 ngày 3 đêm") thành một dòng thời gian con liền mạch.

### 5. Trí Tuệ Nhân Tạo Chữa Lành & Phân Tích Cảm Xúc (AI Companion, Mood Analytics & Insights)
- **Mô Hình Ma Trận Cảm Xúc 2 Trục (Russell's Mood Circumplex Model):**
  - Nâng cấp từ 5 mood cố định thành ma trận khoa học tâm lý: Trục X (Mức độ Dễ chịu / Thoải mái) $\times$ Trục Y (Mức độ Kích hoạt / Năng lượng), giúp nắm bắt chính xác các trạng thái vi mô: "Thanh thản" khác "Hào hứng", "U sầu" khác "Căng thẳng".
- **Biểu Đồ Sóng Cảm Xúc & Phân Tích Tương Quan (Emotional Journey Analytics):**
  - Biểu đồ đường cong cảm xúc biến thiên theo tuần/tháng/năm.
  - Phân tích giờ viết nhiều nhất, ngày trong tuần có tâm trạng tích cực nhất.
- **Người Bạn Tri Kỷ Chánh Niệm (Kokoro AI Zen Companion):**
  - Tích hợp trợ lý AI cục bộ qua **Ollama API (Offline 100%)** hoặc Cloud LLM (DeepSeek / Gemini).
  - Chế độ "Tâm Sự Đêm Khuya": Hộp thoại kính mờ riêng tư, người dùng có thể chia sẻ khúc mắc cuộc sống và nhận lại những lời hồi đáp ân cần, ấm áp dựa trên triết lý Chánh niệm (Mindfulness) và Khắc kỷ (Stoicism).
- **Bản Tin Đúc Kết Tuần (Weekly Mindfulness Digest):**
  - Tự động tổng kết vào 21:00 tối Chủ Nhật: Số từ đã viết, từ khóa lặp lại nhiều nhất, khoảnh khắc sáng nhất trong tuần và lời khích lệ cho tuần mới.

### 6. Cỗ Máy Thời Gian, Chiêm Nghiệm & Gửi Tương Lai (Time Machine, Gratitude Jar & Therapy)
- **Hộp Thư Gửi Tương Lai (Time Capsule / Letter to Future Self):**
  - Cho phép viết một lá thư gửi chính mình trong tương lai: hẹn ngày mở sau 1 tháng, 6 tháng, 1 năm hoặc sinh nhật năm sau.
  - Lá thư được niêm phong với biểu tượng phong bì sáp hồng; đúng ngày hẹn, ứng dụng sẽ gửi thông báo và mở khóa lá thư để người đọc chiêm nghiệm lại sự trưởng thành của bản thân.
- **Chiếc Lọ Biết Ơn (Gratitude Jar / Three Good Things):**
  - Widget tương tác chiếc lọ thủy tinh ảo: Mỗi ngày thả vào lọ 3 mẩu giấy nhỏ ghi lại 3 điều may mắn trong ngày.
  - Vào ngày cuối năm (31/12), có nút "Mở nắp lọ biết ơn" để mở bung tất cả mẩu giấy như một bữa tiệc pháo hoa kỷ niệm.
- **Liệu Pháp Thở Điều Hòa & Thiền Định Mini (Box Breathing & Singing Bowl):**
  - Widget hít thở nhịp nhàng 4-4-4-4 (Hít vào - Giữ hơi - Thở ra - Giữ hơi) với đồ họa cánh hoa anh đào nở ra / khép lại kèm tiếng chuông xoay Tây Tạng ngân vang giúp tĩnh tâm trước khi đặt bút viết.
- **Cỗ Máy Thời Gian — "Ngày Này Năm Xưa" (On This Day Flashback):**
  - Tự động hiển thị thẻ hoài niệm trên đầu feed khi có bài viết đúng ngày này của 1 năm, 2 năm hoặc 5 năm trước.

### 7. Khám Phá, Thư Viện Kỷ Niệm & Tìm Kiếm Đa Chiều (Smart Vault & Search Engine)
- **Tìm Kiếm Toàn Văn Tiếng Việt Thông Minh (PostgreSQL FTS + Unaccent + Trigram):**
  - Tìm kiếm bài viết không dấu ("mua dong" tìm ra "mùa đông"), tìm kiếm mờ khi gõ sai lỗi chính tả nhẹ.
- **Bộ Lọc Phức Hợp Đa Tầng (Multi-criteria Query Builder):**
  - Cho phép kết hợp nhiều điều kiện: `[Tâm trạng: Chiêm nghiệm] AND [Thời tiết: Mưa] AND [Thẻ: #cafe] AND [Năm: 2025]`.
- **Tìm Kiếm Theo Màu Sắc Ảnh Chủ Đạo (Color Palette Search):**
  - Tự động phân tích bảng màu chính (Dominant Colors) của ảnh khi nén; cho phép người dùng bấm vào màu "Hồng pastel", "Xanh lá matcha", "Vàng nắng" để tìm các bài viết mang gam màu đó.
- **Chế Độ Thu Phóng Dòng Thời Gian Theo Mùa & Thập Kỷ:**
  - Nhìn toàn cảnh cuộc đời theo năm (2024, 2025, 2026) hoặc theo 4 mùa Xuân - Hạ - Thu - Đông với hình nền chuyển sắc theo mùa.

### 8. Xuất Bản Kỷ Yếu Chuẩn In Ấn & Tổng Kết Năm (Photobook PDF & Kokoro Wrapped)
- **Xuất Sách Ảnh Kỷ Yếu PDF Chuẩn In Ấn (Print-Ready Photobook PDF Exporter):**
  - Tự động dàn trang toàn bộ bài viết và ảnh thành cuốn sách kỷ yếu hoàn chỉnh khổ A5/A4: Trang bìa hoa anh đào nghệ thuật, trang mục lục tự động, từng trang bài viết có ảnh bo góc và typography thanh lịch, số trang chân trang.
  - Người dùng có thể mang file PDF này ra nhà in để đóng thành cuốn sách vật lý để đời!
- **Báo Cáo Tổng Kết Năm (Kokoro Wrapped — Year in Review):**
  - Trình diễn dạng Story tương tác (như Spotify Wrapped): Tổng số ngày viết, bức ảnh đẹp nhất năm, từ khóa xuất hiện nhiều nhất, chuỗi streak dài nhất, bản nhạc thiền được nghe nhiều nhất.
  - Xuất thẻ tóm tắt năm để chia sẻ lên mạng xã hội.

### 9. Bảo Mật Tuyệt Đối, Sinh Trắc Học & Mã Hóa E2EE (Zero-Knowledge Privacy)
- **Sinh Trắc Học Bản Địa WebAuthn FIDO2:**
  - Mở khóa 1 chạm bằng **Face ID / Touch ID** (iOS/Mac) hoặc **Vân tay / Mở khóa khuôn mặt** (Android / Windows Hello).
- **Két Sắt Kỷ Niệm Tuyệt Mật — Mã Hóa Đầu Cuối (Client-side E2EE):**
  - Bật cờ "Nhật ký bí mật" cho bài viết nhạy cảm.
  - Sử dụng WebCrypto API mã hóa AES-256-GCM với khóa bí mật do người dùng tự nắm giữ; PostgreSQL chỉ lưu ciphertext vô nghĩa. Kể cả quản trị viên máy chủ hay hacker can thiệp CSDL cũng không thể giải mã.
- **Thùng Rác Kỷ Niệm Tạm Thời (Soft-Delete Trash Bin 30 Ngày):**
  - Bài viết bị xóa sẽ nằm trong thùng rác 30 ngày trước khi bị thanh trừng vĩnh viễn, giúp khôi phục dễ dàng khi xóa nhầm.

### 10. Tự Chủ Dữ Liệu, Đồng Bộ Đa Nền Tảng & Kết Nối (Data Sovereignty & Ecosystem)
- **Đồng Bộ Hai Chiều & Giải Quyết Xung Đột (Bi-directional Sync & Conflict Resolver):**
  - Đồng bộ mượt mà giữa điện thoại và máy tính; modal so sánh 2 phiên bản song song khi có xung đột offline.
- **Tự Động Sao Lưu Đám Mây Cá Nhân (Personal Cloud Auto-Backup):**
  - Tự động nén và đẩy tệp `.kokoro.zip` (gồm JSON + toàn bộ ảnh WebP gốc) lên Google Drive cá nhân, WebDAV hoặc Nextcloud hàng tuần.
- **Nhập Dữ Liệu Từ Các Ứng Dụng Khác (One-click Importers):**
  - Nhập trơn tru từ Day One, Journey, Apple Notes, Google Keep, Notion.
- **Thông Báo Đẩy Nhắc Nhở Chăm Sóc Bản Thân (PWA Web Push Notifications):**
  - Nhắc nhở viết nhật ký dịu dàng mỗi tối vào khung giờ người dùng chọn.
- **Đóng Gói Desktop Native Siêu Nhẹ Bằng Tauri v2:**
  - Ứng dụng chạy trên Windows (.exe), macOS (.dmg), Linux (.AppImage) với dung lượng < 15MB, RAM < 50MB, biểu tượng khay hệ thống.
- **Tích Hợp Phím Tắt Tự Động Hóa (iOS Shortcuts & Android Quick Tiles):**
  - Hỗ trợ Siri Shortcut ("Hey Siri, viết nhật ký Kokoro") hoặc nút bấm Quick Settings trên thanh trạng thái Android.

---

## 🚀 PHẦN III: LỘ TRÌNH TRIỂN KHAI CHI TIẾT THEO 12 PHIÊN BẢN (v1.8.0 – v3.0.0+)

Lộ trình được thiết kế bài bản theo từng cột mốc rõ ràng, đảm bảo nguyên tắc Zero Regression:

```
  v1.7.7 (Hiện tại: PWA Hoàn Thiện & Mobile-First Liquid Glass)
     │
     ├── 🎙️ SPRINT A: SOẠN THẢO SÁNG TẠO & CẢM XÚC
     │    ├── Giai đoạn 23 (v1.8.0): Voice Journaling & Floating Markdown Toolbar
     │    └── Giai đoạn 24 (v1.8.5): Diary Templates Studio & Scrapbook Stickers
     │
     ├── 🔐 SPRINT B: BẢO MẬT TUYỆT ĐỐI & HIỆU NĂNG LÕI
     │    ├── Giai đoạn 25 (v1.9.0): WebAuthn Biometrics & E2EE Privacy Vault
     │    └── Giai đoạn 26 (v2.0.0): Async Psycopg3 Engine & Vietnamese Full-Text Search
     │
     ├── 🗺️ SPRINT C: KHÔNG GIAN, THÓI QUEN & CHIÊM NGHIỆM
     │    ├── Giai đoạn 27 (v2.1.0): Auto Weather/Moon Phase & Interactive Memory Map
     │    ├── Giai đoạn 28 (v2.2.0): Habit Tracker Tích Hợp & Mood Circumplex Model
     │    └── Giai đoạn 29 (v2.3.0): Time Capsule (Thư tương lai), Gratitude Jar & Box Breathing
     │
     ├── 🍵 SPRINT D: TRÍ TUỆ NHÂN TẠO & ĐỒNG BỘ ĐA NỀN TẢNG
     │    ├── Giai đoạn 30 (v2.4.0): AI Zen Companion & Emotional Journey Analytics
     │    └── Giai đoạn 31 (v2.5.0): Bi-directional Multi-device Sync & Conflict Resolver
     │
     └── 📦 SPRINT E: XUẤT BẢN KỶ YẾU, ĐA VĂN HÓA & NỀN TẢNG TOÀN NĂNG
          ├── Giai đoạn 32 (v2.6.0): Print-Ready Photobook PDF & Kokoro Wrapped
          ├── Giai đoạn 33 (v2.7.0): Couple/Circle Shared Memories & Secret QR Capsules
          ├── Giai đoạn 34 (v2.8.0): i18n Multi-Language (VI, JA, EN) & Theme Studio 2.0
          └── Giai đoạn 35 (v3.0.0): Tauri Desktop Apps & Personal Cloud Auto-Backup
```

---

### 🔹 GIAI ĐOẠN 23 (v1.8.0) — VOICE JOURNALING & TRÌNH SOẠN THẢO THÔNG MINH
1. **Voice Journal Recorder:** Thu âm Web Audio API, visualizer sóng nước Soft Sakura trong Bottom Sheet, nén file `.m4a` / `.opus` < 500KB đính kèm bài viết, player mini ngoài feed.
2. **Speech-to-Text (STT):** Nhận diện giọng nói tiếng Việt thời gian thực (Web Speech API) và backend Whisper fallback cho bản ghi âm dài.
3. **Floating Markdown Toolbar:** In đậm, In nghiêng, Trích dẫn, Danh sách gạch đầu dòng, Hộp kiểm checkbox; Widget đếm từ & thời gian đọc.

### 🔹 GIAI ĐOẠN 24 (v1.8.5) — MẪU NHẬT KÝ THEO NGỮ CẢNH & NHÃN DÁN SCRAPBOOK
1. **Kho Mẫu Nhật Ký (Template Studio):** Mẫu 5-Minute Morning Journal, Evening Stoic Reflection, Travel Log, Cafe Review, Book & Movie Journal.
2. **Liệu Pháp "Hóa Tro Muộn Phiền" (Catharsis Venting Burn Mode):** Ô viết xả van tâm lý kèm hiệu ứng tro tàn tan biến và tự hủy bài viết an toàn.
3. **Digital Scrapbook Stickers:** Bộ sticker phong cách Nhật Bản gắn trang trí lên góc thẻ bài viết và ảnh.

### 🔹 GIAI ĐOẠN 25 (v1.9.0) — SINH TRẮC HỌC WEBAUTHN & KÉT SẮT E2EE
1. **WebAuthn FIDO2 Biometrics:** Mở khóa 1 chạm bằng Face ID / Touch ID (iOS/Mac) và Vân tay / Mở khóa khuôn mặt (Android / Windows Hello).
2. **Mã Hóa Đầu Cuối (Client-side E2EE):** Mã hóa AES-256-GCM cho bài viết bí mật ngay tại máy client; CSDL PostgreSQL chỉ lưu bản mã.
3. **Thùng Rác Tạm Thời (Soft-delete Trash Bin):** Giữ bài viết đã xóa trong 30 ngày trước khi xóa vĩnh viễn.

### 🔹 GIAI ĐOẠN 26 (v2.0.0) — ĐẠI PHẪU BACKEND ASYNC PSYCOPG3 & FULL-TEXT SEARCH
1. **Async Psycopg3 Engine:** Chuyển đổi 6 Repositories sang `psycopg` v3 native `AsyncConnectionPool`, non-blocking I/O 100%, tăng 500% throughput.
2. **Full-Text Search Tiếng Việt:** Kích hoạt PostgreSQL `unaccent` và `pg_trgm`, tìm kiếm không dấu ("mua dong" -> "mùa đông") và tìm kiếm gần đúng khi gõ nhầm chính tả.
3. **Cursor-based Pagination:** Tải dòng thời gian mượt mà với hàng chục nghìn bài viết mà không suy giảm hiệu năng.

### 🔹 GIAI ĐOẠN 27 (v2.1.0) — THỜI TIẾT TỰ ĐỘNG, TUẦN TRĂNG & BẢN ĐỒ KÝ ỨC
1. **Tự Động Lấy Thời Tiết & Tuần Trăng:** Lấy nhiệt độ, độ ẩm thời gian thực qua tọa độ IP/GPS; hiển thị chu kỳ tuần trăng (Moon Phases 🌑 🌓 🌕).
2. **Bản Đồ Ký Ức (Interactive Memory Map):** Tích hợp Leaflet.js pastel, các cụm ghim hoa anh đào theo địa danh/thành phố đã đi qua.
3. **Chuyến Đi & Album Du Lịch:** Gom các bài viết cùng hành trình thành dòng thời gian du lịch liền mạch.

### 🔹 GIAI ĐOẠN 28 (v2.2.0) — THEO DÕI THÓI QUEN & MA TRẬN TÂM TRẠNG CIRCUMPLEX
1. **Habit Tracker Tích Hợp:** Theo dõi 3-5 thói quen mỗi ngày (Uống nước, Ngủ đủ, Đọc sách, Đi bộ, Thiền định) ngay dưới bài viết.
2. **Russell's Mood Circumplex Model:** Nâng cấp chọn tâm trạng theo ma trận 2 trục: Dễ chịu $\times$ Năng lượng.
3. **Đếm Ngày Kỷ Niệm & D-Day:** Huy hiệu đếm ngày yêu nhau, ngày bắt đầu lối sống mới, đếm ngược sự kiện quan trọng.

### 🔹 GIAI ĐOẠN 29 (v2.3.0) — THƯ GỬI TƯƠNG LAI, LỌ BIẾT ƠN & THIỀN HÍT THỞ
1. **Hộp Thư Gửi Tương Lai (Time Capsule):** Niêm phong thư gửi chính mình sau 1 tháng, 6 tháng, 1 năm hoặc sinh nhật tiếp theo.
2. **Chiếc Lọ Biết Ơn (Gratitude Jar):** Mỗi ngày thả 3 mẩu giấy may mắn; cuối năm mở nắp đọc lại toàn bộ điều kỳ diệu.
3. **Bài Tập Thở Box Breathing & Chuông Thiền:** Đồ họa cánh hoa nở/khép nhịp 4-4-4-4 kèm âm thanh chuông xoay Tây Tạng giúp tĩnh tâm trước khi viết.
4. **Cỗ Máy Thời Gian "Ngày Này Năm Xưa":** Tự động gợi nhắc kỷ niệm đúng ngày này của các năm trước.

### 🔹 GIAI ĐOẠN 30 (v2.4.0) — BẠN ĐỒNG HÀNH AI ZEN & PHÂN TÍCH CẢM XÚC
1. **Kokoro AI Zen Companion:** Kết nối Local Ollama (Offline 100%) hoặc Cloud LLM; chế độ trò chuyện lắng nghe, phản hồi dịu dàng theo triết lý Chánh niệm.
2. **Emotional Journey Charts:** Biểu đồ sóng cảm xúc biến thiên theo tuần/tháng/năm; nhận diện quy luật tâm trạng.
3. **Bản Tin Suy Ngẫm Tuần (Mindfulness Digest):** Tổng kết tự động tối Chủ Nhật về những khoảnh khắc và bài học quý giá trong tuần.

### 🔹 GIAI ĐOẠN 31 (v2.5.0) — ĐỒNG BỘ ĐA THIẾT BỊ NÂNG CAO & GIẢI QUYẾT XUNG ĐỘT
1. **Đồng Bộ Hai Chiều & Vector Clock:** Đồng bộ dữ liệu liền mạch giữa điện thoại và máy tính; PWA Background Sync gửi bài ngầm.
2. **Conflict Resolution UI:** Modal so sánh song song 2 phiên bản (Side-by-side Diff) khi có chỉnh sửa offline xung đột giữa 2 thiết bị.

### 🔹 GIAI ĐOẠN 32 (v2.6.0) — XUẤT BẢN SÁCH ẢNH KỶ YẾU & KOKORO WRAPPED
1. **Xuất Sách Ảnh Photobook PDF In Ấn:** Dàn trang tự động toàn bộ bài viết và ảnh thành file PDF khổ A5/A4 hoàn chỉnh (Bìa hoa anh đào, mục lục, số trang) sẵn sàng mang ra tiệm in thành sách thật.
2. **Kokoro Wrapped (Tổng Kết Năm):** Slide tương tác dạng Story đúc kết 1 năm hành trình cảm xúc và xuất thẻ chia sẻ mạng xã hội.

### 🔹 GIAI ĐOẠN 33 (v2.7.0) — SỔ KỶ NIỆM GHÉP ĐÔI & THẺ KỶ NIỆM MÃ QR
1. **Sổ Kỷ Niệm Ghép Đôi / Nhóm Kín:** Nhật ký viết chung cho 2 người (Người yêu / Vợ chồng / Bạn thân) với bài viết chung và bài viết riêng biệt.
2. **Thẻ Kỷ Niệm Bí Mật Mã QR:** Tạo liên kết ẩn danh hoặc mã QR có mật khẩu chia sẻ 1 khoảnh khắc kỷ niệm duy nhất (tự hủy sau 24h hoặc sau 1 lần xem).

### 🔹 GIAI ĐOẠN 34 (v2.8.0) — QUỐC TẾ HÓA I18N & THEME STUDIO 2.0
1. **Đa Ngôn Ngữ i18n:** Hỗ trợ 3 ngôn ngữ: Tiếng Việt, Tiếng Nhật (日本語), Tiếng Anh (English).
2. **Bộ Giao Diện Thiên Nhiên Mở Rộng:** Thêm 3 giao diện chữa lành: *Matcha Serenity* (Xanh trà), *Autumn Maple* (Lá phong), *Lavender Mist* (Oải hương).
3. **Âm Thanh Zen 2.0:** Bổ sung âm thanh gõ bàn phím gỗ mộc, lật trang sách giấy thô, lửa trại tí tách trong đêm.

### 🔹 GIAI ĐOẠN 35 (v3.0.0) — ĐÓNG GÓI ĐA NỀN TẢNG & TỰ ĐỘNG SAO LƯU ĐÁM MÂY
1. **Đóng Gói Desktop Native Tauri v2:** Ứng dụng chạy mượt mà trên Windows (.exe), macOS (.dmg), Linux (.AppImage) với dung lượng < 15MB, RAM < 50MB.
2. **Tự Động Sao Lưu Đám Mây Cá Nhân:** Tự động đẩy file nén `.kokoro.zip` lên Google Drive cá nhân, WebDAV hoặc Nextcloud hàng tuần.
3. **Nhập Dữ Liệu Từ Các Ứng Dụng Khác:** Nhập 1-click từ Day One, Journey, Apple Notes, Google Keep, Notion.
4. **Tích Hợp Phím Tắt Tự Động Hóa:** iOS Shortcuts ("Hey Siri, viết nhật ký Kokoro") & Android Quick Settings Tile.

---

## 📊 PHẦN IV: BẢNG SO SÁNH NĂNG LỰC KOKORO VỚI CÁC ỨNG DỤNG HÀNG ĐẦU

| Tiêu chí / Tính năng | Day One ($35/năm) | Apple Journal | Notion | **Kokoro (心) Lộ Trình Mới** |
|:---|:---:|:---:|:---:|:---:|
| **Giao diện Liquid Glass Chữa Lành** | ❌ (Chuẩn phẳng) | ❌ (Chuẩn iOS) | ❌ (Cơ sở dữ liệu) | ✅ **Soft Sakura / Frosted Glass Độc bản** |
| **Ghi âm giọng nói & Phiên âm STT** | ✅ | ✅ | ❌ | ✅ **Voice Journaling + Visualizer sóng nước** |
| **Gợi ý chánh niệm & Triết lý sống** | ⚠️ (Nhắc nhở cơ bản) | ⚠️ (Gợi ý máy tính) | ❌ | ✅ **Daily Zen 36 câu + AI Stoic/Zen Companion** |
| **Âm thanh thư giãn Zen Ambient** | ❌ | ❌ | ❌ | ✅ **Tích hợp sẵn 4+ cảnh âm tự nhiên & Lofi** |
| **Mẫu nhật ký & "Hóa tro muộn phiền"** | ⚠️ (Templates đơn giản) | ❌ | ✅ (Templates) | ✅ **Đa dạng templates + Liệu pháp xả stress** |
| **Habit Tracker & Tuần trăng / Thời tiết** | ❌ | ⚠️ (Thời tiết) | ⚠️ (Tự dựng DB) | ✅ **Tự động thời tiết, trăng sao & Habit check-in** |
| **Bản đồ ký ức (Memory Map)** | ✅ | ⚠️ (Cơ bản) | ❌ | ✅ **Bản đồ Leaflet Pastel + Cụm ghim hoa anh đào** |
| **Thư gửi tương lai & Chiếc lọ biết ơn** | ❌ | ❌ | ❌ | ✅ **Time Capsule phong bì sáp & Gratitude Jar** |
| **Bài tập thở & Chuông xoay Tây Tạng** | ❌ | ❌ | ❌ | ✅ **Box Breathing 4-4-4-4 + Singing Bowl** |
| **Xuất thẻ ảnh nghệ thuật Canvas 1080p** | ❌ | ❌ | ❌ | ✅ **Memory Studio 5 themes (Scrapbook, Music..)** |
| **Xuất sách ảnh PDF in ấn (Photobook)** | ✅ (Trả phí in cao) | ❌ | ❌ | ✅ **Xuất PDF chuẩn in ấn A5/A4 miễn phí** |
| **Bảo mật sinh trắc học & E2EE** | ✅ (FaceID) | ✅ (FaceID) | ❌ (Không E2EE) | ✅ **WebAuthn FaceID + Két sắt E2EE AES-256** |
| **Tự chủ dữ liệu & Lưu trữ máy chủ riêng** | ❌ (Lưu cloud hãng) | ❌ (Lưu iCloud) | ❌ (Lưu cloud hãng) | ✅ **100% Tự chủ dữ liệu (Self-hosted/Drive/WebDAV)** |
| **Hỗ trợ Offline & PWA Đa nền tảng** | ⚠️ (Native App) | ⚠️ (Chỉ iOS) | ⚠️ (Yêu cầu mạng) | ✅ **Offline-First PWA + Tauri Desktop siêu nhẹ** |

---

## 🎯 PHẦN V: KẾ HOẠCH BẮT ĐẦU THỰC HIỆN NGAY

Để biến đại lộ trình này thành hiện thực mà không bị quá tải, em đề xuất triển khai theo **Sprint A (Giai đoạn 23 - v1.8.0)** ngay:
1. **Xây dựng Voice Journaling:** Bộ thu âm Web Audio API với visualizer sóng nước Soft Sakura trong Bottom Sheet, lưu file audio nhẹ vào `/uploads/audio/`.
2. **Tích hợp Web Speech API:** Nói tiếng Việt tới đâu chữ tự động chạy vào khung soạn thảo tới đó.
3. **Thanh công cụ Markdown nổi:** Cung cấp đầy đủ công cụ format chữ in đậm, in nghiêng, trích dẫn, checklist công việc.
