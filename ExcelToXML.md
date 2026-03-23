# HƯỚNG DẪN SỬ DỤNG CHỨC NĂNG EXCELTOXML

> Đặt folder `EXCELTOXML` cung cấp với folder `xml, MQHIS` để có thể **kết nối được với hệ thống và ký số** được

## Bước 1: Chọn mẫu chuyển đổi
* Tại giao diện chính, tìm ô **Danh mục / Loại danh mục**.
* Chọn đúng loại mẫu văn bản cần làm việc (Ví dụ: *Mẫu 05/DM - DM dịch vụ KBCB...*).

## Bước 2: Chuẩn bị dữ liệu (Nếu chưa có file Excel)
* Nhấn nút **Tải file Excel mẫu**.
* Chọn vị trí lưu file `.xlsx`.
* Mở file vừa tải, nhập dữ liệu vào các dòng trống bên dưới hàng tiêu đề đã có sẵn và **Lưu (Save)** lại.
* **Lưu ý:** Đóng file `.xlsx`.

## Bước 3: Nạp dữ liệu vào phần mềm
* Nhấn nút chọn **File Excel**.
* Chọn file Excel chứa dữ liệu.
* Kiểm tra dữ liệu hiển thị trên lưới đang hiển thị để đảm bảo không lỗi font hoặc thiếu hàng.

## Bước 4: Xuất tệp XML
Tùy theo nhu cầu, chọn một trong hai phương thức sau:

### 1. Xuất XML thông thường
* Nhấn nút **Xuất XML**.
* Chọn vị trí lưu file XML trên máy tính.

### 2. Xuất và Ký số trực tiếp
* Nhấn nút **Xuất & Ký số XML**.
* Chọn vị trí lưu file. XML xuất ra sẽ được tự động chèn chữ ký số vào file.
* Khi nhận được thông báo: **"Đã ký: [đường dẫn tệp]"** là hoàn tất.

> * Nếu nhận được thông báo Ký số thất bại thì có thể kiểm tra log lỗi tại file `log_kyso/LogFile.txt` hoặc liên hệ bộ phận chuyên môn để có thể ký số được.

---

## HƯỚNG DẪN CẤU HÌNH FILE XML MẪU (Dành cho Quản trị viên)

Để phần mềm nhận diện và ánh xạ dữ liệu động từ Excel sang XML, file mẫu trong thư mục `TemplateCategory` cần tuân thủ các quy tắc sau:

### 1. Định nghĩa thuộc tính TypeNode
* **`TypeNode="isRow"`**: Đặt tại thẻ đại diện cho một dòng dữ liệu (thẻ sẽ lặp lại theo số hàng trong Excel).
* **`TypeNode="isRowDetail"`**: Đặt tại các thẻ cha bao bọc các nhóm thẻ con mà không chứa giá trị trực tiếp.

### 2. Quy tắc ánh xạ tiêu đề cột (Mapping)
* **Thẻ đơn:** Tiêu đề cột Excel đặt trùng tên với thẻ trong XML.
* **Thẻ lồng nhau:** Tiêu đề cột Excel đặt theo cấu trúc `ThẻCha.ThẻCon` (Ví dụ: `THONGTIN.QUEQUAN`).

### 3. Chỉnh sửa cấu hình
* **File `config.json`**: Phải khai báo `Key` trùng hoàn toàn với tên file XML mẫu (không bao gồm phần mở rộng `.xml`).
* **Thẻ ký số**: File XML mẫu phải khớp với thẻ `<CHUKYDONVI>` vị trí ký trong file `config.json` để có thể gắn mã Hash khi thực hiện Ký số.

---
**Lưu ý:** Mọi thay đổi trong cấu trúc file XML mẫu sẽ thay đổi cách phần mềm sinh file Excel mẫu ở **Bước 2**.
