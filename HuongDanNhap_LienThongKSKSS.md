# Hướng dẫn Nhập và Liên thông Khám Sức Khỏe Sinh Sản (e-MCH) [KSKSS]

---

## 1. Quy trình Nhập KSKSS (Điền dữ liệu lâm sàng)

### 📌 Điều kiện cần và đủ
Bệnh nhân phải có tối thiểu **1 trong 2** thông tin bắt buộc sau:
* `Số CCCD` (Căn cước công dân)
* `Thẻ BHYT` (Bảo hiểm y tế)

### 💻 Thao tác nhập liệu trên HIS (Có 3 cách)

Hệ thống HIS hỗ trợ 3 phân hệ để người dùng nhập thông tin KSKSS tùy theo luồng tiếp đón:

* **Cách 1: Khám sức khỏe**
    * **Đường dẫn:** `Khám sức khỏe` ➡️ `Khám sức khỏe` ➡️ `Khám sức khỏe sinh sản (e-MCH)` *(hoặc Khám sức khỏe bà mẹ & trẻ em)*
* **Cách 2: Khám bệnh (Ngoại trú)**
    * **Đường dẫn:** `Khám bệnh` ➡️ `Phiếu khám bệnh` ➡️ Click chọn nút mũi tên xuống `⬇️` ➡️ `Khám sức khỏe sinh sản (e-MCH)` *(hoặc Khám sức khỏe bà mẹ & trẻ em)*
* **Cách 3: Điều trị Nội trú**
    * **Đường dẫn:** `Nội trú` ➡️ `Hiện diện` ➡️ `Tiện ích` ➡️ `Khám sức khỏe sinh sản (e-MCH)` *(hoặc Khám sức khỏe bà mẹ & trẻ em)*

---

## 2. Quy trình Liên thông KSKSS (Đẩy dữ liệu lên cổng e-MCH quốc gia)

### 🧭 Thao tác trên giao diện liên thông
* **Truy cập Menu:** `Tiện ích` ➡️ `Quản lý dữ liệu liên thông` ➡️ `Liên thông khám sức khỏe sinh sản`
* **Thực hiện gửi:** Chọn bệnh nhân từ danh sách cần đẩy dữ liệu ➡️ Bấm **Gửi liên thông**.

### 🔍 Phản hồi từ hệ thống e-MCH
* **Gửi thành công:** Hệ thống sẽ hiển thị thông báo kèm theo thông tin `Mã giao dịch` và `Thời gian tiếp nhận`.
* **Tra cứu trạng thái:** Hồ sơ sẽ được Cổng e-MCH quốc gia tiếp nhận và trả kết quả phê duyệt dựa vào `Mã giao dịch` đã được cấp.

---

## 3. Cấu hình Liên thông KSKSS (Dành cho Quản trị viên hệ thống)

Để chức năng liên thông hoạt động, quản trị viên cần cấu hình chính xác **2 tham số** sau trên hệ thống **MQHIS**:

### 🔑 Tham số 1600204 - TaiKhoanLienThongKSKSS
*Dùng để cấu hình tài khoản và endpoint đăng nhập lấy token.*

```json
{
  "urlLogin": "[https://skss.tkyt.vn/api/lien-thong/tai-khoan/dang-nhap](https://skss.tkyt.vn/api/lien-thong/tai-khoan/dang-nhap)",
  "method": "POST",
  "contentType": "application/x-www-form-urlencoded",
  "params": {
    "tenDangNhap": "NHẬP_TÊN_ĐĂNG_NHẬP_TẠI_ĐÂY",
    "matKhau": "NHẬP_MẬT_KHẨU_TẠI_ĐÂY"
  }
}
```

### 🛰️ Tham số 1600205 - GuiDuLieuLienThongKSKSS
*Dùng để cấu hình đường dẫn API tiếp nhận gói tin XML dữ liệu lâm sàng.*
```json
{
  "Url": "[https://skss.tkyt.vn/api/lien-thong/tiep-nhan](https://skss.tkyt.vn/api/lien-thong/tiep-nhan)",
  "Method": "POST",
  "Headers": {
    "Content-Type": "application/xml"
  }
}
```

