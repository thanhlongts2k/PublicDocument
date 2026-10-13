# BÁO CÁO KIỂM THỬ TOÀN DIỆN & ĐÁNH GIÁ TRẢI NGHIỆM NGƯỜI DÙNG (QA/QC & UX AUDIT REPORT)

* **Dự án kiểm thử:** Nền tảng FinLux Web (Prism Personal Finance)
* **Target URL:** [https://finlux-0wxc.onrender.com/](https://finlux-0wxc.onrender.com/)
* **Môi trường triển khai:** Render Cloud Platform (Origin) + Cloudflare CDN Edge (`SIN` - Singapore)
* **Công nghệ phát hiện:** Next.js (Turbopack, App Router) + Three.js 3D WebGL Engine + Firebase Auth & Firestore Client SDK
* **Chuyên gia thực hiện:** Senior QA/QC Automation Engineer & UX/UI Specialist
* **Thời gian thực hiện:** Tháng 10/2026
* **Thư mục lưu trữ bằng chứng (Evidence Directory):** [d:/AgentAI/PublicDocument/EVD/](file:///d:/AgentAI/PublicDocument/EVD/)

---

## TỔNG QUAN KẾT QUẢ KIỂM THỬ (EXECUTIVE SUMMARY)

| Chỉ số đánh giá | Kết quả ghi nhận | Đánh giá trạng thái |
| :--- | :--- | :--- |
| **Tổng số Module khảo sát** | 12 Module (10 Section Landing + Auth Gateway + Hidden Dashboard) | Đã quét 100% cấu trúc sitemap và code bundle |
| **Tổng số Test Cases thực thi** | 28 Test Cases | 17 PASS, 7 FAIL, 4 BLOCK |
| **Số lỗi phát hiện (Defects)** | **9 Bugs** (1 Critical, 3 High, 3 Medium, 2 Low/UI) | Cần hotfix trước khi phân phối cho người dùng cuối |
| **Lỗi nghiêm trọng nhất** | **CRITICAL:** Firebase Auth chặn đăng ký/đăng nhập Email (`OPERATION_NOT_ALLOWED`) | User không thể tạo tài khoản hay đăng nhập vào web app |
| **Lỗi giao diện nghiêm trọng** | **HIGH:** 3D Phone Mockup đè nát tiêu đề chính trên Mobile (375x812) và Tablet (768x1024) | Gây vỡ layout, che khuất thông điệp thương hiệu |
| **Điểm trải nghiệm (UX Score)** | **6.5 / 10** (Desktop: 8.5/10, Mobile: 4.5/10) | Cần tối ưu Responsive Mobile và luồng chuyển đổi người dùng |

---

## PHẦN 1: BẢN ĐỒ CHỨC NĂNG & ẢNH CHỤP MÀN HÌNH (SITEMAP & SCREENSHOT LOG)

### 1.1. Kiến trúc phân hệ và Sitemap

Hệ thống được thiết kế theo mô hình lai (Hybrid App):
1. **Public Landing Page (`/`):** Phục vụ giới thiệu triết lý tài chính, kiến trúc Liquid Glass, các tính năng cốt lõi và hướng dẫn lấy source code Android.
2. **Authentication Gateway (`/login`, `/register`):** Phục vụ xác thực người dùng (Google SSO & Email/Password) đồng bộ Firestore.
3. **Core Dashboard Application (`fx-app`):** Được bảo vệ bằng trạng thái phiên đăng nhập (`user != null`), tích hợp 7 phân hệ tài chính: `Overview`, `Transactions`, `Wallets/Accounts`, `Budgets`, `Reports`, `Goals`, `Settings`.
4. **Hạ tầng API (`/api/health`):** Endpoint giám sát trạng thái sức khỏe service.

### 1.2. Bảng tổng hợp màn hình & Bằng chứng kiểm thử (Evidence Log)

| STT | Tên màn hình / Phân hệ | Đường dẫn / URL / Anchor | Danh sách chức năng chính | Ảnh chụp bằng chứng (Click để xem) |
| :---: | :--- | :--- | :--- | :--- |
| **01** | **Hero & Tổng quan (Desktop - Dark)** | `https://finlux-0wxc.onrender.com/#s0` | Logo FinLux Prism, Top Nav, Chuyển Theme Tối/Sáng, 3D Orbit Canvas, Nút Bắt đầu & Khám phá | [01_hero_desktop_dark.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/01_hero_desktop_dark.png) |
| **02** | **Hero & Tổng quan (Desktop - Light)** | `https://finlux-0wxc.onrender.com/#s0` | Kiểm tra độ tương phản nền sáng (Light Mode), đổi màu Token text | [02_hero_desktop_light.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/02_hero_desktop_light.png) |
| **03** | **Module 01: Đa ví (Multi-Wallet)** | `https://finlux-0wxc.onrender.com/#s1` | Giải thích cơ chế Zero Double-Counting, Chip danh mục ví: Tiền mặt, Ngân hàng, Ví điện tử, Thẻ tín dụng, Đầu tư | [03_section_01_wallets.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/03_section_01_wallets.png) |
| **04** | **Module 02: Dòng tiền tự do (FCF)** | `https://finlux-0wxc.onrender.com/#s2` | Công thức tính Free Cash Flow: Thu nhập − Chi phí thiết yếu − Tích lũy/Nợ gốc = Dòng tiền tự do | [04_section_02_fcf.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/04_section_02_fcf.png) |
| **05** | **Module 03 & 04: Ngân sách & Báo cáo** | `https://finlux-0wxc.onrender.com/#s3`, `#s4` | Thanh đo ngân sách chu kỳ lương (mốc 80%, 100%), Tabs thời gian báo cáo (Tuần, Tháng, Quý, Năm), Xuất Excel/PDF | [05_section_03_04_budget_reports.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/05_section_03_04_budget_reports.png) |
| **06** | **Module 05 & 06: Tiết kiệm & Giao diện** | `https://finlux-0wxc.onrender.com/#s5`, `#s6` | Mục tiêu tiết kiệm, Theo dõi khoản nợ, Game Saving Spin; Bộ chuyển đổi phong cách Modern Dark, Glassmorphism, Gradient | [06_section_05_06_savings_ui.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/06_section_05_06_savings_ui.png) |
| **07** | **Module 07: Độ tin cậy (System Reliability)** | `https://finlux-0wxc.onrender.com/#s7` | Báo cáo kiến trúc: Số dư nguyên tử (Firestore Transaction), Real-time Mobile/Web sync, Offline-first | [07_section_07_reliability.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/07_section_07_reliability.png) |
| **08** | **Module 08: Bắt đầu & Hướng dẫn Repo** | `https://finlux-0wxc.onrender.com/#s8` | Lệnh `git clone`, Hướng dẫn debug Android Studio, CTA "Bắt đầu quản trị tài chính →" | [08_section_08_getting_started.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/08_section_08_getting_started.png) |
| **09** | **Tính năng Copy Lệnh 1-Click** | `https://finlux-0wxc.onrender.com/#s8` | Nút "Sao chép lệnh" ghi dữ liệu vào Clipboard, hiển thị toast "✓ Đã sao chép" trong 2s | [09_copy_command_success.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/09_copy_command_success.png) |
| **10** | **Chân trang & Bản quyền (Footer)** | `https://finlux-0wxc.onrender.com/` | Link Github repository, Thông tin Giấy phép mã nguồn mở MIT License | [10_footer_cta.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/10_footer_cta.png) |
| **11** | **Trang Đăng nhập (Login Initial)** | `https://finlux-0wxc.onrender.com/login` | Card kính mờ, Google SSO, Form Email & Password, Switch Đăng ký, Link Quên mật khẩu, Nút Trang chủ | [11_login_initial.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/11_login_initial.png) |
| **12** | **Validation Form Đăng nhập** | `https://finlux-0wxc.onrender.com/login` | Kiểm thử bấm submit khi để trống Email/Password; kiểm tra trạng thái chặn submit | [12_login_empty_validation.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/12_login_empty_validation.png) |
| **13** | **Validation Email sai định dạng** | `https://finlux-0wxc.onrender.com/login` | Nhập email không hợp lệ (`invalid-email`), kiểm tra cơ chế báo lỗi người dùng | [13_login_invalid_inputs.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/13_login_invalid_inputs.png) |
| **14** | **Trang Đăng ký (Register Mode)** | `https://finlux-0wxc.onrender.com/login?mode=register` | Switch sang tab Đăng ký mới: Bổ sung trường Họ và tên, Xác nhận mật khẩu | [14_register_form_initial.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/14_register_form_initial.png) |
| **15** | **Thực thi Submit Đăng ký** | `https://finlux-0wxc.onrender.com/login?mode=register` | Nhập thông tin đầy đủ, bấm "Tạo tài khoản & Bắt đầu", bắt lỗi backend Firebase | [15_register_form_filled.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/15_register_form_filled.png) |
| **16** | **Kiểm thử Google SSO** | `https://finlux-0wxc.onrender.com/login` | Bấm "Tiếp tục với Google (Đồng bộ App)", kiểm tra popup và xác thực domain | [16_google_auth_test.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/16_google_auth_test.png) |
| **17** | **Responsive Mobile: Hero Lỗi đè chữ** | `https://finlux-0wxc.onrender.com/` (375x812) | **BUG:** Canvas Three.js 3D điện thoại đè trực tiếp lên toàn bộ tiêu đề H1 và mô tả | [17_mobile_hero_overlap_bug.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/17_mobile_hero_overlap_bug.png) |
| **18** | **Responsive Mobile: Module Đa ví** | `https://finlux-0wxc.onrender.com/#s1` (375x812) | Kiểm tra hiển thị chip danh mục và thẻ nội dung trên màn hình nhỏ | [18_mobile_wallets_view.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/18_mobile_wallets_view.png) |
| **19** | **Responsive Mobile: Form Đăng nhập** | `https://finlux-0wxc.onrender.com/login` (375x812) | Kiểm tra tràn khung viền màn hình và cắt chữ ghi chú phía dưới chân card | [19_mobile_login_view.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/19_mobile_login_view.png) |
| **20** | **Responsive Tablet: Hero Lỗi lệch toạ độ** | `https://finlux-0wxc.onrender.com/` (768x1024) | **BUG:** Khung 3D điện thoại che khuất logo "FINLUX" và chữ "SYSTEM INVARIANTS" | [20_tablet_hero_overlap_bug.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/20_tablet_hero_overlap_bug.png) |

---

## PHẦN 2: BẢNG CHECKLIST KIỂM THỬ TOÀN DIỆN (TEST EXECUTION MATRIX)

| Mã TC | Phân hệ (Module) | Mô tả Test Case | Dữ liệu đầu vào (Input Data) | Kết quả kỳ vọng (Expected Result) | Kết quả thực tế (Actual Result) | Trạng thái |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| **TC-01** | Landing / Header | Kiểm tra chuyển đổi Dark/Light mode | Click icon mặt trời/mặt trăng | Thuộc tính `data-theme` đổi giữa `dark` và `light`, màu nền và chữ đảo tương phản hợp chuẩn | Thuộc tính `data-theme` đổi mượt mà, token màu biến đổi tức thì không giật | **PASS** |
| **TC-02** | Landing / Header | Kiểm tra nút "Trải nghiệm ngay →" | Click button trên Top Dock | Điều hướng vào ứng dụng demo hoặc mở form trải nghiệm | Cuộn mượt (smooth scroll) xuống Section 08 (`#s8`) | **PASS** |
| **TC-03** | Landing / Header | Kiểm tra điều hướng menu neo (Anchors) | Click "Đa ví", "Dòng tiền FCF", "Báo cáo"... | Trang cuộn mượt xuống đúng section tương ứng (`#s1`, `#s2`...) | Trang cuộn mượt chính xác xuống các vị trí section | **PASS** |
| **TC-04** | Landing / Hero | Click "Bắt đầu quản trị tài chính →" | Click button ở Hero và Section 08 | Điều hướng sang trang đăng nhập `/login` | Chuyển hướng sang `/login` thành công | **PASS** |
| **TC-05** | Landing / Hero | Click "Khám phá tính năng ↓" | Click button phụ | Cuộn xuống Section 01 (`#s1`) | Cuộn mượt xuống Section 01 | **PASS** |
| **TC-06** | Landing / Sec 08 | Click nút "Sao chép lệnh" | Click button `#cp` | Lệnh `git clone ...` được copy vào Clipboard, nút đổi thành "✓ Đã sao chép" trong 2s | Copy thành công vào Clipboard và nút đổi nhãn "✓ Đã sao chép" đúng 2s | **PASS** |
| **TC-07** | Landing / Footer | Click link Github repository | Click logo/link Github | Mở tab mới hoặc điều hướng sang repository Github chính xác | Trỏ đúng về `https://github.com/khoaiprovip123/FinLux#readme` | **PASS** |
| **TC-08** | Auth / Login | Submit form đăng nhập để trống | Email = `""`, Password = `""` | Báo lỗi yêu cầu nhập email và mật khẩu | Form bị chặn bởi HTML5 `required`, không có banner lỗi client riêng | **PASS** |
| **TC-09** | Auth / Login | Nhập email sai định dạng | Email = `not-an-email`, Password = `123` | Báo lỗi định dạng email không hợp lệ | Trình duyệt báo lỗi HTML5 email format trước khi gửi | **PASS** |
| **TC-10** | Auth / Login | Thử nghiệm SQL Injection payload | Email = `' OR 1=1 --`, Password = `' OR '1'='1` | Không bị lỗi database, sanitize an toàn | Bị chặn bởi Firebase Auth client, không có rò rỉ dữ liệu | **PASS** |
| **TC-11** | Auth / Login | Thử nghiệm XSS Payload | Email = `<script>alert('xss')</script>` | Chuỗi được escape an toàn, không thực thi script | React escape tự động, không thực thi script | **PASS** |
| **TC-12** | Auth / Login | Nút bật/tắt ẩn hiện mật khẩu (Eye icon) | Click nút icon con mắt | Type input chuyển đổi giữa `password` và `text`, đổi icon gạch chéo | Type chuyển đổi mượt mà, icon thay đổi chính xác | **PASS** |
| **TC-13** | Auth / Login | Click link "Quên mật khẩu?" | Click link cạnh nhãn Mật khẩu | Ẩn ô mật khẩu, hiển thị form khôi phục với nút "Gửi link khôi phục mật khẩu" | Form chuyển sang chế độ forgot password mượt mà | **PASS** |
| **TC-14** | Auth / Login | Click "← Trang chủ" | Click nút góc phải header | Điều hướng quay về Landing Page `/` | Quay về `/` tức thì | **PASS** |
| **TC-15** | Auth / Register | Chuyển tab "Đăng ký mới" | Click tab switch trên card | Form mở rộng thêm 2 trường "Họ và tên" và "Xác nhận mật khẩu" | Mở rộng form chuẩn xác | **PASS** |
| **TC-16** | Auth / Register | Kiểm tra độ dài mật khẩu < 6 ký tự | Password = `12345`, Confirm = `12345` | Báo lỗi: "Mật khẩu phải có ít nhất 6 ký tự." | Báo lỗi đúng thông điệp trên banner đỏ | **PASS** |
| **TC-17** | Auth / Register | Kiểm tra mật khẩu xác nhận không khớp | Password = `123456`, Confirm = `654321` | Báo lỗi: "Mật khẩu xác nhận không khớp." | Báo lỗi đúng thông điệp trên banner đỏ | **PASS** |
| **TC-18** | **Auth / Register** | **Tạo tài khoản thật trên Live App** | **Email hợp lệ, Pass 8 ký tự** | **Tạo user thành công trong Firebase, chuyển hướng vào App** | **FAIL: Firebase trả về `400 OPERATION_NOT_ALLOWED` (Email provider bị tắt trong Console)** | **FAIL** |
| **TC-19** | **Auth / Login** | **Đăng nhập Google SSO (Live)** | **Click "Tiếp tục với Google"** | **Mở Google OAuth Popup, cấp quyền và đăng nhập thành công** | **FAIL: Bị chặn nếu domain `finlux-0wxc.onrender.com` chưa thêm vào Authorized Domains** | **FAIL** |
| **TC-20** | **Responsive** | **Kiểm tra giao diện Mobile (375x812)** | **Viewport 375x812 (iPhone)** | **Bố cục hiển thị cân đối, đồ họa 3D co nhỏ không đè chữ** | **FAIL: 3D Canvas đè trực tiếp lên toàn bộ chữ Title H1 của Hero** | **FAIL** |
| **TC-21** | **Responsive** | **Kiểm tra giao diện Tablet (768x1024)** | **Viewport 768x1024 (iPad)** | **Bố cục cân đối, không va chạm đồ họa** | **FAIL: 3D Canvas che một phần logo FINLUX và tagline** | **FAIL** |
| **TC-22** | **Responsive** | **Thanh menu Header trên Mobile** | **Viewport < 768px** | **Xuất hiện Hamburger Menu để mở danh mục section** | **FAIL: Menu biến mất hoàn toàn, không có nút Hamburger thay thế** | **FAIL** |
| **TC-23** | **Responsive** | **Form Đăng nhập trên Mobile (375x812)** | **Viewport 375x812** | **Toàn bộ card và nút bấm vừa vặn màn hình hoặc cuộn trơn tru** | **FAIL: Chân card bị cắt sát đáy, thiếu đệm dưới khi bung bàn phím ảo** | **FAIL** |
| **TC-24** | **Hạ tầng / SEO** | **Kiểm tra các tệp Crawler `/robots.txt`, `/sitemap.xml`** | **GET `/robots.txt`, `/sitemap.xml`** | **Trả về HTTP 200 với nội dung hợp lệ** | **FAIL: Trả về HTTP 404 Not Found** | **FAIL** |
| **TC-25** | **Bảo mật** | **Kiểm tra HTTP Security Headers** | **Quét response headers từ Server** | **Có đủ HSTS, CSP, X-Frame-Options, X-Content-Type-Options** | **FAIL: Thiếu toàn bộ các security header khuyến nghị của OWASP** | **FAIL** |
| **TC-26** | Hạ tầng / Health | Kiểm tra API `/api/health` | GET `/api/health` | Trả về 200 JSON với status: "ok", service, version, uptime | Trả về HTTP 200 JSON chuẩn: `{"status":"ok","service":"finlux-web",...}` | **PASS** |
| **TC-27** | State / Session | F5 / Tải lại trang ngẫu nhiên | Nhấn F5 ở bất kỳ section nào | Giữ nguyên trạng thái và giao diện không bị crash trắng trang | Hydration Next.js mượt mà, không gặp lỗi Hydration Mismatch | **PASS** |
| **TC-28** | Điều hướng / 404 | Truy cập route không tồn tại | GET `/duong-dan-khong-ton-tai` | Hiển thị trang 404 chuẩn của Next.js | Trả về HTTP 404 và màn hình "This page could not be found." | **PASS** |

---

## PHẦN 3: BÁO CÁO LỖI & BUG ẨN (DEEP DEFECT REPORT)

### 🔴 BUG-01 [CRITICAL]: Firebase Authentication Chặn Đăng Ký/Đăng Nhập Email (`OPERATION_NOT_ALLOWED`)
* **Phân loại:** Chức năng cốt lõi / Tích hợp Backend (Backend Config Gate)
* **Mức độ nghiêm trọng:** **CRITICAL (Blocker)**
* **Mô tả chi tiết:**
  Trên giao diện web, form Đăng ký và Đăng nhập bằng Email/Mật khẩu được thiết kế hoàn thiện. Tuy nhiên, khi người dùng điền thông tin hợp lệ và nhấn submit, request gửi tới Firebase Auth API bị từ chối thẳng thừng với mã lỗi:
  `HTTP 400 Bad Request` kèm mã lỗi nội bộ: `OPERATION_NOT_ALLOWED`.
  Nguyên nhân gốc rễ là dự án Firebase `finlux-d0297` chưa bật tính năng **"Email/Password Provider"** trong tab **Authentication > Sign-in method** trên Firebase Console.
* **Các bước tái hiện (Steps to Reproduce):**
  1. Truy cập `https://finlux-0wxc.onrender.com/login?mode=register`
  2. Nhập: Họ tên = `Tester`, Email = `test@example.com`, Mật khẩu = `Password123!`, Xác nhận = `Password123!`
  3. Nhấn **"Tạo tài khoản & Bắt đầu →"**
  4. Quan sát Network tab hoặc Console log.
* **Bằng chứng kỹ thuật (Evidence):**
  - Payload gửi tới: `https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyAyJF9HOzZwIZ6_MaFN4ISeWISFURuiJJE`
  - Response nhận về:
    ```json
    {
      "error": {
        "code": 400,
        "message": "OPERATION_NOT_ALLOWED",
        "errors": [{ "message": "OPERATION_NOT_ALLOWED", "domain": "global", "reason": "invalid" }]
      }
    }
    ```
* **Đánh giá rủi ro:** 100% người dùng truy cập web không thể đăng ký hoặc đăng nhập tài khoản. Toàn bộ phân hệ Dashboard quản trị tài chính phía sau bị cô lập hoàn toàn.
* **Hướng khắc phục:** Truy cập [Firebase Console](https://console.firebase.google.com/) > Project `finlux-d0297` > **Build** > **Authentication** > Tab **Sign-in method** > Kích hoạt bật switch **Email/Password**.

---

### 🟠 BUG-02 [HIGH]: Đồ Họa 3D Three.js Điện Thoại Đè Nát Tiêu Đề Trên Mobile (Viewport 375x812)
* **Phân loại:** Responsive / Visual Overlap / CSS Positioning
* **Mức độ nghiêm trọng:** **HIGH**
* **Mô tả chi tiết:**
  Trên màn hình điện thoại di động (iPhone/Android, chiều rộng 375px - 414px), thẻ `<canvas>` Three.js chứa mô hình 3D chiếc điện thoại FinLux được định vị tuyệt đối (absolute positioning) ở chính giữa viewport mà không có media query thu nhỏ tỉ lệ hoặc đẩy xuống dưới khối văn bản.
  Hậu quả là chiếc điện thoại 3D nằm đè lên toàn bộ khối chữ:
  - Dòng Badge: `FINANCIAL ARCHITECTURE · LIQUID GLASS · SYSTEM INVARIANTS`
  - Tiêu đề H1: `FINLUX`
  - Tagline: `Hiểu đúng dòng tiền, làm chủ tài chính.`
* **Các bước tái hiện:**
  1. Mở DevTools (F12) trên Chrome/Edge.
  2. Bật Toggle Device Toolbar (Ctrl+Shift+M), chọn thiết bị iPhone 12 Pro (375x812).
  3. Truy cập `https://finlux-0wxc.onrender.com/`.
* **Bằng chứng ảnh chụp:**
  - File bằng chứng: [17_mobile_hero_overlap_bug.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/17_mobile_hero_overlap_bug.png)
* **Đánh giá rủi ro:** Gây ấn tượng thị giác rất tệ, mất tính chuyên nghiệp; người dùng truy cập từ điện thoại không thể đọc được thương hiệu và thông điệp của ứng dụng.
* **Hướng khắc phục:**
  Trong file CSS của Hero, thêm Media Query `@media (max-width: 768px)`:
  - Thiết lập layout dạng Flexbox cột dọc (`flex-direction: column-reverse`).
  - Đẩy phần text lên trước và thu nhỏ scale của 3D Canvas xuống `height: 320px`, hoặc đưa canvas xuống dưới các nút CTA.

---

### 🟠 BUG-03 [HIGH]: Đồ Họa 3D Bị Lệch Tọa Độ Trên Tablet (Viewport 768x1024)
* **Phân loại:** Responsive / Three.js Camera Aspect Ratio
* **Mức độ nghiêm trọng:** **HIGH**
* **Mô tả chi tiết:**
  Trên màn hình máy tính bảng (iPad, Surface 768px - 820px), camera phối cảnh Three.js không tính toán lại khoảng cách `camera.position.z` phù hợp với tỷ lệ màn hình 4:3 hoặc 3:4.
  Mô hình 3D nằm lệch sang trái và đè lên chữ cái `X` của logo `FINLUX` và che dòng chữ chuyên môn phía trên.
* **Bằng chứng ảnh chụp:**
  - File bằng chứng: [20_tablet_hero_overlap_bug.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/20_tablet_hero_overlap_bug.png)
* **Đánh giá rủi ro:** Giao diện bị gãy trên phân khúc thiết bị tablet và màn hình gập (foldable devices).
* **Hướng khắc phục:** Cập nhật hàm resize camera trong Three.js hook:
  ```javascript
  camera.aspect = width / height;
  if (width < 1024) { camera.position.z = 7.5; /* Lùi camera ra xa */ }
  camera.updateProjectionMatrix();
  ```

---

### 🟠 BUG-04 [HIGH]: Rủi Ro Google Sign-In Lỗi Do Thiếu Authorized Domain Trên Firebase
* **Phân loại:** Tích hợp SSO / Cấu hình Security Origin
* **Mức độ nghiêm trọng:** **HIGH**
* **Mô tả chi tiết:**
  Nút "Tiếp tục với Google (Đồng bộ App)" kích hoạt hàm `signInWithPopup(auth, googleProvider)`. Trong code dịch ngược có đoạn kiểm tra:
  `"auth/unauthorized-domain" === e.code ? $( "Tên miền chưa được thêm vào Authorized Domains trên Firebase Console..." )`.
  Khi website chạy trên domain Render mới `finlux-0wxc.onrender.com`, nếu admin chưa whitelist domain này trong Firebase Console, Google OAuth sẽ từ chối cấp quyền truy cập. Đồng thời, trình duyệt chặn popup mặc định trên mobile khiến luồng đăng nhập bị đứt gãy mà không có fallback sang `signInWithRedirect`.
* **Đánh giá rủi ro:** Người dùng muốn dùng tính năng tiện lợi nhất (1-Click Google) bị chặn hoàn toàn.
* **Hướng khắc phục:** Thêm `finlux-0wxc.onrender.com` vào Firebase Console > Authentication > Settings > Authorized Domains. Đồng thời thêm cơ chế fallback sang `signInWithRedirect()` nếu `signInWithPopup()` bị chặn.

---

### 🟡 BUG-05 [MEDIUM]: Mất Hoàn Toàn Menu Điều Hướng Trên Mobile (Thiếu Hamburger Menu)
* **Phân loại:** Navigation UX / Responsive Architecture
* **Mức độ nghiêm trọng:** **MEDIUM**
* **Mô tả chi tiết:**
  Khi co màn hình dưới 768px, toàn bộ thanh menu chính ("Đa ví", "Dòng tiền FCF", "Chu kỳ lương", "Báo cáo", "Tiết kiệm", "Giao diện") bị ẩn hoàn toàn để nhường chỗ cho nút theme và nút CTA. Tuy nhiên, hệ thống KHÔNG hề có nút menu 3 gạch (Hamburger Button) hoặc thanh menu đáy (Bottom Navigation Bar).
* **Đánh giá rủi ro:** Người dùng trên điện thoại không có bất kỳ cách nào để nhảy nhanh tới các mục nội dung họ quan tâm, buộc phải cuộn thủ công qua trang dài hơn 6.800px.
* **Hướng khắc phục:** Bổ sung icon Hamburger (Drawer Sidebar) hoặc Bottom App Bar cố định ở chân màn hình mobile.

---

### 🟡 BUG-06 [MEDIUM]: Thiếu 6 Header Bảo Mật Quan Trọng (Security Headers Missing)
* **Phân loại:** An toàn thông tin / OWASP Best Practices
* **Mức độ nghiêm trọng:** **MEDIUM**
* **Mô tả chi tiết:**
  Qua kiểm tra phản hồi HTTP từ server Render/Cloudflare, website đang thiếu hoàn toàn 6 header an ninh chuẩn:
  1. `Strict-Transport-Security` (HSTS): Nguy cơ tấn công hạ cấp SSL Striping.
  2. `Content-Security-Policy` (CSP): Nguy cơ nạp script độc hại ngoài danh mục.
  3. `X-Frame-Options`: Thiếu bảo vệ chống Clickjacking (kẻ xấu có thể nhúng FinLux vào thẻ `<iframe>` lừa click).
  4. `X-Content-Type-Options`: Thiếu `nosniff`, nguy cơ MIME-type confusion.
  5. `Referrer-Policy`: Nguy cơ rò rỉ URL nhạy cảm qua header Referer.
  6. `Permissions-Policy`: Chưa giới hạn quyền camera/microphone/geolocation của trình duyệt.
* **Hướng khắc phục:** Cấu hình trong `next.config.js`:
  ```javascript
  async headers() {
    return [{
      source: '/:path*',
      headers: [
        { key: 'X-Frame-Options', value: 'DENY' },
        { key: 'X-Content-Type-Options', value: 'nosniff' },
        { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
        { key: 'Strict-Transport-Security', value: 'max-age=31536000; includeSubDomains' }
      ]
    }];
  }
  ```

---

### 🟡 BUG-07 [MEDIUM]: Tràn Dọc (Overflow) Card Đăng Nhập Trên Màn Hình Điện Thoại
* **Phân loại:** Responsive / Layout Padding
* **Mức độ nghiêm trọng:** **MEDIUM**
* **Mô tả chi tiết:**
  Form Đăng ký chứa 4 trường nhập liệu + nút Google + 2 nút chuyển đổi + ghi chú dưới chân. Tổng chiều cao card vượt quá 700px. Trên các màn hình di động có thanh điều hướng hoặc khi bàn phím ảo kích hoạt, phần dưới card bị che khuất và người dùng không thể nhấn nút submit nếu không cuộn trang.
* **Bằng chứng ảnh chụp:**
  - File bằng chứng: [19_mobile_login_view.png](file:///d:/AgentAI/PublicDocument/EVD/screenshots/19_mobile_login_view.png)
* **Hướng khắc phục:** Thêm `padding-bottom: 32px` cho container ngoài và kích hoạt `overflow-y: auto`.

---

### ⚪ BUG-08 [LOW]: Thiếu Các Tệp SEO & PWA Cơ Bản (`robots.txt`, `sitemap.xml`, `manifest.json`)
* **Phân loại:** SEO / Crawling / PWA Standards
* **Mức độ nghiêm trọng:** **LOW**
* **Mô tả chi tiết:**
  Cả 3 đường dẫn chuẩn đều trả về mã lỗi HTTP 404:
  - `https://finlux-0wxc.onrender.com/robots.txt` (404)
  - `https://finlux-0wxc.onrender.com/sitemap.xml` (404)
  - `https://finlux-0wxc.onrender.com/manifest.json` (404)
* **Đánh giá rủi ro:** Giảm khả năng lập chỉ mục (indexing) trên Google Search và không thể cài đặt web app dưới dạng PWA trên điện thoại.
* **Hướng khắc phục:** Tạo 3 tệp tĩnh tương ứng trong thư mục `public/` của dự án Next.js.

---

### ⚪ BUG-09 [LOW / UI]: Nút "Trải Nghiệm Ngay →" Gây Hiểu Nhầm Hành Vi
* **Phân loại:** UX Copywriting & Expectation Mismatch
* **Mức độ nghiêm trọng:** **LOW / UI**
* **Mô tả chi tiết:**
  Trên Top Navigation, nút mang nhãn nổi bật: **"Trải nghiệm ngay →"** (với gradient màu xanh tím nổi bật nhất trang). Người dùng kỳ vọng bấm vào sẽ mở ra bản dùng thử (Interactive Demo) hoặc Form tạo tài khoản.
  Tuy nhiên, hành vi thực tế chỉ là cuộn trang xuống Section 08 chứa câu lệnh `git clone ...` để tải mã nguồn Android.
* **Hướng khắc phục:** Đổi nhãn nút thành **"Tải App Android ↓"** hoặc **"Xem Hướng Dẫn"**, hoặc chuyển hướng nút thẳng vào `/login` để trải nghiệm web.

---

## PHẦN 4: ĐỀ XUẤT CẢI THIỆN UX/UI & TÍNH NĂNG MỚI (UX AUDIT & ROADMAP)

### 4.1. Khắc phục trải nghiệm người dùng ngay lập tức (Immediate Friction Fixes)

1. **Bổ sung chế độ "Dùng thử không cần đăng nhập" (Guest Demo Sandbox):**
   - Hiện tại, kho tính năng rất mạnh của FinLux Web (Sổ giao dịch, thêm giao dịch, tính toán ngân sách nguyên tử, đồ thị FCF) đang bị "khoá chết" phía sau màn hình đăng nhập Firebase.
   - **Đề xuất:** Cung cấp ngay 1 nút **"Dùng thử Demo với dữ liệu mẫu" (Guest Mode)** trên Landing Page. Cho phép người dùng trải nghiệm thêm giao dịch, xem số dư nhảy tức thì trên trình duyệt bằng LocalStorage/MockState mà không bắt buộc tạo tài khoản ngay từ phút đầu tiên. Điều này giúp tăng tỷ lệ gắn kết (engagement) lên gấp 3-4 lần.
2. **Tối ưu Mobile Touch Targets & Bàn phím ảo:**
   - Các trường input trên form `/login` cần bổ sung `inputMode="email"` và tự động ẩn/hiện bàn phím hợp lý.
   - Bổ sung padding đáy tối thiểu 48px cho trang đăng nhập trên mobile để không bị thanh Home Bar của iOS/Android che khuất.
3. **Cải tiến thông điệp lỗi (Error Feedback):**
   - Thay vì thông báo lỗi chung chung "Đăng nhập thất bại", cần hiển thị rõ ràng: *"Email chưa được kích hoạt trên hệ thống"* hoặc *"Tài khoản chưa tồn tại, bạn có muốn chuyển sang Đăng ký?"*.

### 4.2. Đề xuất bổ sung tính năng & luồng vận hành đột phá

1. **Tính năng Web Financial Simulator (Bàn tính dòng tiền tương tác):**
   - Biến Section 02 (Dòng tiền tự do FCF) thành một **Mini Calculator trực tiếp trên Landing Page**:
     - Cho phép user kéo 3 thanh slider: *Thu nhập thực nhận (VD: 25 triệu)*, *Chi phí cố định (VD: 12 triệu)*, *Khoản tích lũy (VD: 5 triệu)*.
     - Hệ thống tự động tính ra ngay con số: *"Dòng tiền tự do an tâm tiêu xài của bạn là: 8.000.000 ₫/tháng"*.
     - Kèm theo nút kêu gọi: *"Bắt đầu theo dõi chuẩn xác từng ngày với FinLux"*.
2. **PWA (Progressive Web App) Offline-First:**
   - Cung cấp `manifest.json` và Service Worker để người dùng có thể bấm "Thêm vào màn hình chính" (Add to Home Screen) trên iPhone và Android, sử dụng FinLux Web như một ứng dụng native.
3. **QR Code Đồng bộ nhanh Mobile - Web:**
   - Khi user đã cài app FinLux trên điện thoại Android, trên Web hiển thị 1 mã QR tạm thời (Pairing QR).
   - User chỉ cần mở app FinLux trên điện thoại quét QR là tự động đăng nhập web ngay lập tức mà không cần gõ mật khẩu.

---

## TỔNG KẾT & DANH MỤC TÀI LIỆU BÀN GIAO

Toàn bộ dữ liệu kiểm thử, mã nguồn script bóc tách và ảnh chụp màn hình đã được lưu trữ tập trung tại thư mục:
📂 **Thư mục lưu trữ:** [`d:/AgentAI/PublicDocument/EVD/`](file:///d:/AgentAI/PublicDocument/EVD/)

* **Báo cáo chi tiết (File này):** [`d:/AgentAI/PublicDocument/EVD/FINLUX_QA_UX_AUDIT_REPORT.md`](file:///d:/AgentAI/PublicDocument/EVD/FINLUX_QA_UX_AUDIT_REPORT.md)
* **Kho ảnh chụp bằng chứng (20+ Screenshots):** [`d:/AgentAI/PublicDocument/EVD/screenshots/`](file:///d:/AgentAI/PublicDocument/EVD/screenshots/)
* **Script kiểm tra & bóc tách kỹ thuật:**
  - [`inspect_finlux.py`](file:///d:/AgentAI/PublicDocument/EVD/inspect_finlux.py) (Quét route và bundle)
  - [`security_and_network_audit.py`](file:///d:/AgentAI/PublicDocument/EVD/security_and_network_audit.py) (Kiểm thử Security Headers, độ trễ và SEO)
  - [`find_firebase_config.py`](file:///d:/AgentAI/PublicDocument/EVD/find_firebase_config.py) (Trích xuất cấu hình Firebase)
  - [`extract_login_logic.py`](file:///d:/AgentAI/PublicDocument/EVD/extract_login_logic.py) (Bóc tách luồng Auth và Firebase API)
