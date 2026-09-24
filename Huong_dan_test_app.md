
### 1. Tổng quan & Mục đích chung của các video

* **Hoạt động đang diễn ra**: Một chuyên viên / người có kinh nghiệm đang quay màn hình thao tác trên ứng dụng quản lý POS (dành cho quán bar, lounge, nhà hàng tại Nhật) kết nối trực tiếp với máy in nhiệt, đồng thời giảng giải và hướng dẫn một bạn tester/nhân viên mới cách thực hiện kiểm thử phần mềm (test nghiệp vụ và in ấn).


* **Mục đích**:
* Hướng dẫn quy trình kiểm thử (test case) toàn diện cho chức năng **Cài đặt máy in (印刷設定)** và **In ấn thực tế** từ các màn hình nghiệp vụ (tạo bill, order món, thanh toán, chấm công, báo cáo thu chi...).


* Hướng dẫn cách kiểm tra đối chiếu (verify) giữa thông tin hiển thị trên màn hình ứng dụng với nội dung và bố cục (layout) được in ra trên giấy nhiệt thực tế.


* Chỉ ra các trường hợp phát sinh lỗi (bug) thường gặp như: lệch ngày/giờ, sai số tiền sau điều chỉnh giá, thiếu thông tin khi chọn nhiều phương thức thanh toán, hoặc không in đúng thiết lập bật/tắt.





---

### 2. Phân tích chi tiết từng video

#### **Video 1: Cấu hình in, Chấm công, Tạo Bill, Gọi món & Thanh toán**

* **Đang làm gì**: Hướng dẫn cấu hình bật/tắt các trường thông tin trong máy in, tạo bill bàn, order món/set menu, điều chỉnh giá và in các loại hoá đơn (Guest check, Receipt, Hóa đơn đỏ).


* **Mục đích**: Kiểm tra xem các thiết lập in khi bật (ON) hoặc tắt (OFF) có tác động chính xác lên giao diện xác nhận và nội dung tờ bill được in ra hay không; đồng thời kiểm tra luồng tính tiền.


* **Chi tiết các màn hình & thao tác**:
* **Màn hình Cài đặt in (印刷設定)**:
* Bật/tắt các tuỳ chọn in cho từng loại phiếu: Hóa đơn (レシート), Bảng kê tính tiền (会計表 - Guest check), Biên lai/Hoá đơn đỏ (領収書), Phiếu bếp/order (オーダー), In báo cáo (日報印刷), Mã QR (QRコード), Chấm công (出退勤印刷).


* Thiết lập chi tiết cho từng loại: ẩn/hiện tên khách (顧客名非表示), thời gian vào quán (来店時間), thời gian tạo bill (伝票作成時間), hiển thị tiền thẻ (お会計表のクレジット表示), in khổ ngang/dọc (横レイアウト).




* **Màn hình Quản lý chấm công (勤怠管理)**:
* Thao tác bấm Chấm công vào (出勤) / Chấm công về (退勤) cho nhân viên.


* Lưu ý tính năng không cho phép chấm công ở ngày tương lai.




* **Màn hình Quản lý bill/bàn (伝票)**:
* Tạo bill mới cho bàn (chọn bàn số 4, số lượng khách, gán màu đánh dấu bàn, gán nhân viên phục vụ/đồng hành 本指名/同伴者).


* Xuất và in mã QR bàn (QRコード) để test quét order hoặc tải mã QR.




* **Màn hình Chi tiết bill & Gọi món (伝票詳細 / MENU)**:
* Thêm món lẻ (Soft drink, rượu, tháp Calpis/Champagne) và tuỳ chọn option (Nóng/Lạnh - Hot/Cold).


* Thử tính năng gọi phục vụ (呼出: khăn lạnh おしぼり, đá 氷...).


* Chọn gói Set menu (SET12, phí ngồi chỗ, gia hạn thời gian 1h, 2h, 3h...).




* **Màn hình In phiếu tạm tính (会計表) & Thanh toán (支払)**:
* In phiếu tạm tính bàn 4 trước khi thanh toán và kiểm tra cửa sổ xác nhận có hiện bước chọn thẻ hay không tùy vào cài đặt.


* Nhập giảm giá/điều chỉnh giá (価格調整: giảm 1,000 yên).


* Chọn phương thức thanh toán tiền mặt (現金), nhập tiền khách đưa và tính tiền thối.


* In hóa đơn ra giấy và đối chiếu số tiền tổng, số tiền giảm, tên khách, ngày giờ giữa app và tờ giấy in.







---

#### **Video 2: Kiểm thử Báo cáo ngày (日報) & Các khoản Thu - Chi**

* **Đang làm gì**: Hướng dẫn kiểm tra màn hình Báo cáo (日報) gồm báo cáo tổng, tạo và in các khoản Chi phí (経費), Ứng lương theo ngày (日払い), Tiền cọc (デポジット), Khấu trừ/Phạt (ペナルティー/控除額).


* **Mục đích**: Đảm bảo tất cả các chức năng có biểu tượng máy in đều in ra đúng số liệu thực tế của ngày hoặc tháng được chọn, không bị lấy nhầm số liệu của ngày khác.


* **Chi tiết các màn hình & thao tác**:
* **Màn hình Báo cáo ngày/tháng (日報 - 売上情報)**:
* Xem và chuyển đổi giữa các ngày trong lịch (ngày 22/09, ngày 23/09/2026) và xem tổng tháng (月報).


* Bấm nút biểu tượng máy in để in báo cáo doanh thu.


* Kiểm tra lỗi: App đang hiển thị ngày 22 nhưng khi in ra giấy có bị nhầm sang ngày 23 hay không.




* **Màn hình Chi phí (経費)**:
* Tạo khoản chi phí mới: Chọn danh mục (Ô tô 自動車, Internet...), tên khoản chi, nơi mua, số tiền, cách tính (tính vào tiền két キャッシュに計算, tiền tạm ứng, hay không tính).


* In phiếu chi từng mục lẻ ngay sau khi tạo.


* In phiếu tổng chi phí của cả ngày hoặc tháng.




* **Màn hình Tiền ứng trong ngày (日払い)**:
* Tạo khoản tiền ứng cho nhân viên (chọn staff, nhập số tiền, ghi chú) và in phiếu ứng tiền.


* In báo cáo tiền ứng theo danh sách nhân viên hoặc theo ngày.




* **Màn hình Tiền đặt cọc (デポジット - Deposit)**:
* Tạo khoản tiền cọc mới (chọn nhân viên, khách hàng, số tiền, hình thức nhận tiền mặt/chuyển khoản).


* In phiếu cọc lẻ và phiếu danh sách cọc.




* **Màn hình Tiền tạm ứng/Đền bù/Phạt (立替金 / ペナルティー / 控除額)**:
* Tạo mới tiền phạt/khấu trừ cho nhân viên.


* Lưu ý tester: Chỗ nào có icon máy in thì bấm in thử, chỗ nào không có icon in thì chỉ cần kiểm tra lưu số liệu đúng trên màn hình.







---

#### **Video 3: Cấu hình nhanh & In Báo cáo Ngày/Tháng**

* **Đang làm gì**: Tóm tắt lại luồng bật máy in cho module Báo cáo (日報印刷) và in trực tiếp báo cáo tổng ngày/tháng.


* **Mục đích**: Giúp tester ghi nhớ cấu hình tiên quyết trước khi test in báo cáo và quy trình in chuẩn.


* **Chi tiết các màn hình & thao tác**:
* **Màn hình Cài đặt (設定) -> Cài đặt in (印刷設定) -> In báo cáo (日報印刷)**:
* Bật toàn bộ công tắc (ON) của: Báo cáo ngày (日報), Tiền vào (入金), Tiền ứng (日払い), Tiền cọc (デポジット), Chi phí (経費).




* **Màn hình Báo cáo (日報)**:
* Mở xem báo cáo tháng (chờ tải dữ liệu xong) -> Bấm nút in -> Máy in xuất phiếu báo cáo tháng.


* Chuyển sang xem báo cáo ngày -> Bấm nút in -> Máy in xuất phiếu báo cáo ngày.


* Người hướng dẫn căn dặn luôn phải chờ dữ liệu trên app tải đầy đủ mới ấn in để tránh in ra số liệu rỗng hoặc sai lệch.







---

#### **Video 4: Test Thanh toán kết hợp nhiều phương thức & Gom bill in**

* **Đang làm gì**: Hướng dẫn mở lại bill đã có sẵn, thực hiện thanh toán kết hợp nhiều phương pháp thanh toán (Split payment) và kiểm tra tờ hóa đơn xuất ra.


* **Mục đích**: Bắt các lỗi hiển thị thông tin phương thức thanh toán trên hóa đơn và chia sẻ mẹo gom các loại bill để test nhanh, tiết kiệm thời gian.


* **Chi tiết các màn hình & thao tác**:
* **Màn hình Danh sách bill (伝票)**:
* Mở một bill bàn đang phục vụ (bàn S-2, khách Saul, staff Test6).




* **Màn hình Chi tiết bill & Thanh toán (支払)**:
* Kiểm tra giờ vào, giờ tạo bill, danh sách đồ uống.


* Chọn kết hợp 2 phương thức thanh toán (ví dụ: vừa Tiền mặt 現金 vừa Quẹt thẻ tín dụng カード).


* In hóa đơn ra giấy và kiểm tra: Trên giấy in bắt buộc phải liệt kê đầy đủ cả 2 phương thức và số tiền tương ứng từng phương thức. Nếu trên giấy chỉ in 1 phương thức hoặc thiếu là **BUG**.


* Hướng dẫn mẹo cho tester: Khi test một bàn/bill, nên in liên tiếp các loại phiếu (Guest check, Receipt, Hoá đơn đỏ) cùng lúc rồi lấy giấy ra so sánh một lượt, không nên làm rời rạc từng bước để tránh mất thời gian.







---

### 3. Tóm tắt các điểm tester cần ghi nhớ khi test theo video

1. **Kiểm tra Layout (Bố cục giấy in)**: Cần quen thuộc mẫu in của từng loại (Guest check khác Receipt, Receipt khác Hoá đơn đỏ, Hoá đơn đỏ dọc khác ngang).


2. **Đối chiếu số liệu**: Luôn so sánh từng mục: Ngày giờ, Tên khách hàng, Tên nhân viên phụ trách/đồng hành, Tiền món, Tiền thuế/phí, Tiền giảm giá (nếu có), Phương thức thanh toán và Tiền thừa.


3. **Cài đặt ON/OFF**: Khi bật chức năng nào trong Cài đặt in thì trên giấy phải xuất hiện thông tin đó, khi tắt thì giấy in không được hiển thị.