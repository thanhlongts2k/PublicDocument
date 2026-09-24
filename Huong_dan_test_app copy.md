# BÁO CÁO PHÂN TÍCH QUY TRÌNH KIỂM THỬ ỨNG DỤNG POS & MÁY IN NHIỆT

---

## I. TỔNG QUAN & MỤC ĐÍCH CHUNG

* **Nội dung thực hiện**: Hướng dẫn thực tế luồng kiểm thử (testing) hệ thống POS quản lý bàn/quán chuyên biệt cho thị trường Nhật kết nối máy in nhiệt[cite: 1, 2, 4].
* **Mục đích cốt lõi**:
  * Kiểm tra tính toàn vẹn của chức năng **Cài đặt in (印刷設定)** khi tương tác với các màn hình nghiệp vụ thực tế[cite: 1, 2, 3].
  * Hướng dẫn phương pháp đối soát dữ liệu (cross-check) giữa giao diện hiển thị và giấy in nhiệt[cite: 1, 2, 4].
  * Phát hiện và phòng ngừa các lỗi điển hình: sai lệch múi giờ, rớt thông tin đa phương thức thanh toán, sai lệch số tiền điều chỉnh[cite: 1, 2, 4].

---

## II. CHI TIẾT NGHIỆP VỤ & THAO TÁC THEO TỪNG VIDEO

### 1. Video 1: Cấu hình in, Chấm công, Tạo Bill, Gọi món & Thanh toán
* **Nghiệp vụ**: Thiết lập thông số in, tạo đơn, quản lý giờ làm, chọn món và thanh toán cơ bản[cite: 1].
* **Mục đích**: Xác minh các cờ cấu hình (Flags ON/OFF) phản hồi chính xác ra phiếu in và giao diện xác nhận[cite: 1].

| Màn hình | Thao tác chính | Chi tiết kiểm thử / Điểm cần lưu ý |
| :--- | :--- | :--- |
| **Cài đặt in (印刷設定)** | Cấu hình bật/tắt các loại phiếu và trường dữ liệu | • Bật/tắt các phiếu: Hóa đơn (`レシート`), Tạm tính (`会計表`), Biên lai (`領収書`), Order (`オーダー`), Báo cáo (`日報`), QR (`QRコード`), Chấm công (`出退勤`)[cite: 1].<br>• Cấu hình hiển thị: Ẩn/hiện tên khách (`顧客名非表示`), giờ vào (`来店時間`), giờ tạo đơn (`伝票作成時間`), phí thẻ (`お会計表のクレジット表示`), in dọc/ngang (`横レイアウト`)[cite: 1]. |
| **Chấm công (勤怠管理)** | Chấm công nhân viên | • Thao tác: Bấm Chấm công vào (`出勤`) / Chấm công về (`退勤`)[cite: 1].<br>• **Quy tắc**: Không cho phép chấm công cho ngày trong tương lai[cite: 1]. |
| **Quản lý bàn (伝票)** | Mở bàn và khởi tạo đơn hàng | • Chọn bàn (bàn số 4), nhập số khách, gán màu quản lý, gán nhân viên chỉ định/đồng hành (`本指名`/`同伴者`)[cite: 1].<br>• Xuất mã QR bàn để phục vụ quét order[cite: 1]. |
| **Gọi món (伝票詳細 / MENU)** | Nhập danh sách đồ ăn/uống | • Thêm món lẻ, cấu hình thuộc tính món (`Hot`/`Cold`)[cite: 1].<br>• Gọi phục vụ nhanh (`呼出`: khăn lạnh `おしぼり`, đá `氷`)[cite: 1].<br>• Đặt gói Set menu (`SET12`, tiền phụ thu bàn, gia hạn giờ 1h/2h/3h)[cite: 1]. |
| **Tạm tính & Thanh toán (支払)** | In bill tạm tính và tất toán đơn | • In phiếu tạm tính bàn 4; kiểm tra popup xác nhận thanh toán thẻ có hiện theo cài đặt hay không[cite: 1].<br>• Nhập giảm giá/điều chỉnh giá (`価格調整`: -1,000 yên)[cite: 1].<br>• Chọn thanh toán Tiền mặt (`現金`), tính tiền thối[cite: 1].<br>• In phiếu và đối soát: tổng tiền, giảm giá, tên khách, mốc thời gian[cite: 1]. |

---

### 2. Video 2: Kiểm thử Báo cáo ngày (日報) & Các khoản Thu - Chi
* **Nghiệp vụ**: Thống kê doanh thu ca/ngày/tháng và quản lý dòng tiền chi tiết[cite: 2].
* **Mục đích**: Đảm bảo toàn bộ các điểm chạm có chức năng in báo cáo đều lấy chuẩn dữ liệu theo mốc thời gian truy vấn[cite: 2].

| Màn hình | Thao tác chính | Chi tiết kiểm thử / Điểm cần lưu ý |
| :--- | :--- | :--- |
| **Báo cáo (日報 - 売上情報)** | Truy vấn doanh thu ngày & tháng | • Chuyển đổi giữa các ngày (22/09, 23/09/2026) và xem tổng tháng (`月報`)[cite: 2].<br>• **Điểm kiểm tra lỗi**: Đang chọn ngày 22 nhưng in ra số liệu ngày 23[cite: 2]. |
| **Chi phí (経費)** | Quản lý các khoản chi ngoài | • Thêm khoản chi: Phân loại danh mục (`自動車`, `Internet`), đơn vị nhận, số tiền, nguồn trừ tiền (két tiền `キャッシュに計算`, tiền tạm ứng, không tính)[cite: 2].<br>• In phiếu chi lẻ ngay khi lập và in tổng hợp chi phí ngày/tháng[cite: 2]. |
| **Ứng lương (日払い)** | Quản lý tiền ứng theo ngày của staff | • Lập khoản ứng theo nhân viên, nhập số tiền và nội dung ghi chú[cite: 2].<br>• In phiếu ứng lẻ và in báo cáo danh sách ứng tiền theo ngày/tháng[cite: 2]. |
| **Tiền đặt cọc (デポジット)** | Quản lý tiền cọc giữ bàn/dịch vụ | • Nhập thông tin cọc: Nhân viên tiếp nhận, tên khách, số tiền, hình thức nhận tiền[cite: 2].<br>• In phiếu cọc chi tiết và phiếu tổng hợp[cite: 2]. |
| **Khoản khấu trừ (立替金 / ペナルティー)** | Quản lý tiền phạt & tạm ứng khác | • Lập phiếu phạt/khấu trừ (`ペナルティー`/`控除額`) cho nhân viên[cite: 2].<br>• Chức năng nào có icon máy in thì in test, không có thì chỉ kiểm tra lưu dữ liệu trên app[cite: 2]. |

---

### 3. Video 3: Cấu hình nhanh & In Báo cáo Ngày/Tháng
* **Nghiệp vụ**: Chuẩn hóa điều kiện tiên quyết (Prerequisites) cho module Báo cáo[cite: 3].
* **Mục đích**: Nắm vững luồng bật công tắc máy in và quy trình in báo cáo chuẩn xác[cite: 3].

* **Màn hình Cài đặt in báo cáo (`設定` -> `印刷設定` -> `日報印刷`)**:
  * Kích hoạt toàn bộ công tắc (ON): Báo cáo ngày (`日報`), Tiền vào (`入金`), Tiền ứng (`日払い`), Tiền cọc (`デポジット`), Chi phí (`経費`)[cite: 3].
* **Màn hình Báo cáo (`日報`)**:
  * Xem báo cáo tháng -> Chờ dữ liệu tải hoàn tất -> Bấm in ra phiếu tháng[cite: 3].
  * Chuyển sang xem báo cáo ngày -> Bấm in ra phiếu ngày[cite: 3].
  * > **Lưu ý quan trọng**: Tuyệt đối không bấm in khi thanh tiến trình (loading) chưa hoàn tất để tránh in ra số rỗng hoặc sai lệch[cite: 3].

---

### 4. Video 4: Thanh toán tách phương thức (Split Payment) & Gom Bill
* **Nghiệp vụ**: Thanh toán đơn hàng bằng nhiều hình thức kết hợp và tối ưu quy trình kiểm thử bill[cite: 4].
* **Mục đích**: Bắt lỗi thiếu thông tin dòng tiền trên hóa đơn và rút ngắn thời gian test[cite: 4].

* **Màn hình Danh sách bàn (`伝票`) & Chi tiết thanh toán (`支払`)**:
  * Mở đơn sẵn có (bàn S-2, khách Saul, staff phụ trách Test6)[cite: 4].
  * Chọn kết hợp 2 phương thức thanh toán cùng lúc: Tiền mặt (`現金`) + Thẻ tín dụng (`カード`)[cite: 4].
  * **Tiêu chuẩn kiểm thử (Acceptance Criteria)**:
    * Phiếu in ra giấy bắt buộc phải hiển thị chi tiết số tiền của từng phương thức thanh toán[cite: 4].
    * Nếu chỉ hiển thị 1 trong 2 hoặc không hiển thị số tiền tương ứng -> **Xác định lỗi (BUG)**[cite: 4].
* **Mẹo tối ưu quy trình (Testing Tip)**:
  * Khi test một đơn, nên in liên tục cả 3 loại phiếu (Tạm tính, Hóa đơn thanh toán, Hóa đơn đỏ) cùng lúc rồi gom giấy lại đối chiếu một lượt, tránh in lẻ tẻ từng thao tác[cite: 4].

---

## III. NGUYÊN TẮC CỐT LÕI CHO TESTER KHI TEST IN ẤN

1. **Chuẩn hóa Layout**: Phân biệt rõ mẫu in của từng loại phiếu (phiếu Guest check, Receipt, Hóa đơn đỏ khổ dọc và khổ ngang)[cite: 1].
2. **Kiểm tra tính nhất quán (Consistency)**: Đối chiếu 1:1 giữa App và Giấy in về các trường: Mốc thời gian, Tên khách hàng, Tên nhân viên chỉ định/đồng hành, Tiền món, Thuế/Phí dịch vụ, Tiền điều chỉnh giảm, Phương thức thanh toán và Tiền thối[cite: 1, 4].
3. **Kiểm tra cơ chế Bật/Tắt (Toggle Logic)**: Khi Cài đặt = ON thì giấy in bắt buộc phải có trường đó; khi Cài đặt = OFF thì giấy in tuyệt đối không được xuất hiện trường đó[cite: 1].