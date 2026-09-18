# BỘ QUY TẮC THIẾT KẾ PHẦN MỀM: OUTSIDE-IN FIRST

> **Tôn chỉ cốt lõi:**  
> *Đừng xây móng cho một ngôi nhà khi chưa biết công năng từng phòng. Kiến trúc và cơ sở dữ liệu sinh ra để phục vụ trải nghiệm người dùng, không phải ngược lại.*

---

## 1. NGUYÊN TẮC TƯ DUY (MINDSET RULES)

### Rule 1: Outside-In thay vì Inside-Out
* **Sai lầm phổ biến:** DB Schema $\rightarrow$ Service/Logic $\rightarrow$ API Contract $\rightarrow$ UI/Screen.
* **Tư duy đúng:** User Flow $\rightarrow$ UI/Wireframe $\rightarrow$ API Contract $\rightarrow$ Business Logic $\rightarrow$ DB Schema.
* *Ý nghĩa:* Đi từ những gì người dùng tương tác ngược vào hệ thống lưu trữ bên trong.

### Rule 2: API Driven by UI (UI định hình dữ liệu, không phải DB)
* Màn hình cần gì thì API trả về đúng cái đó.
* Tránh thiết kế API phản chiếu 100% cấu trúc các bảng trong DB (Entity-based API) khiến Frontend phải gọi nhiều request rời rạc hoặc tự ghép dữ liệu phức tạp.

### Rule 3: Tránh Tối ưu hóa Sớm (No Premature Optimization)
* Không tốn thời gian tối ưu hóa hiệu năng, tách microservices, hoặc chuẩn hóa DB quá mức cho những tính năng mà màn hình và luồng nghiệp vụ còn chưa chốt.
* Ưu tiên tính linh hoạt và dễ thay đổi trong giai đoạn đầu.

---

## 2. QUY TRÌNH THIẾT KẾ & TRIỂN KHAI 5 BƯỚC

```text
[BƯỚC 1] User Flow & Lo-fi UI
       │
       ▼
[BƯỚC 2] Data Flow & State Machine
       │
       ▼
[BƯỚC 3] API Contract (Mock JSON)
       │
       ▼
[BƯỚC 4] High-level Architecture
       │
       ▼
[BƯỚC 5] DB Schema & Core Logic
```

---

### BƯỚC 1: Phác thảo Wireframe & User Flow (Lo-fi UI)
* **Mục tiêu:** Xác định người dùng thấy gì và bấm vào đâu trước khi viết code.
* **Thực hiện:**
  * Dùng Excalidraw, Figma hoặc giấy bút vẽ nhanh màn hình dạng khung xương (Lo-fi).
  * Làm rõ: Màn hình này có những trường dữ liệu nào? Nút bấm dẫn tới đâu? Có các trạng thái (Loading, Success, Empty, Error) ra sao?
* **Đầu ra:** Screen Flow rõ ràng để chốt nghiệp vụ với Stakeholder / PM / Client.

---

### BƯỚC 2: Định hình Luồng Dữ liệu (Data Flow & State)
* **Mục tiêu:** Xác định vòng đời dữ liệu trên giao diện.
* **Thực hiện:**
  * Dữ liệu nào cần load ngay khi mở trang?
  * Dữ liệu nào chỉ load khi bấm xem chi tiết / tìm kiếm?
  * Hành động nào kích hoạt ghi nhận dữ liệu (Submit form, Auto-save...)?

---

### BƯỚC 3: Thiết kế API Contract (Giao ước Dữ liệu)
* **Mục tiêu:** Tách rời Frontend và Backend, giúp cả hai làm việc song song mà không bị phụ thuộc.
* **Thực hiện:** Định nghĩa mẫu payload JSON cho Request và Response.
* **Ví dụ Contract:**
  ```json
  // GET /api/v1/orders/123
  {
    "order_id": "ORD-123",
    "status": "DELIVERING",
    "customer": {
      "name": "Nguyễn Văn A",
      "phone": "0901234567"
    },
    "items": [
      { "product_id": "P1", "title": "Bàn phím cơ", "price": 1200000, "qty": 1 }
    ],
    "total_amount": 1200000
  }
  ```
* **Lợi ích:** Frontend có thể dùng Mock Data để code UI ngay lập tức; Backend chỉ việc code logic để trả ra đúng JSON này.

---

### BƯỚC 4: Thiết kế Kiến trúc Tổng thể (High-Level Architecture)
* **Mục tiêu:** Lựa chọn giải pháp kỹ thuật phù hợp với yêu cầu thực tế.
* **Thực hiện:**
  * Xác định các module, service hoặc layer cần có.
  * Lựa chọn hạ tầng phụ trợ (Caching bằng Redis, Queue/Worker cho tác vụ nặng, Storage cho file...).

---

### BƯỚC 5: Thiết kế DB Schema & Core Business Logic
* **Mục tiêu:** Lưu trữ và xử lý dữ liệu để phục vụ API Contract đã định nghĩa ở Bước 3.
* **Thực hiện:**
  * Tạo ERD (Entity Relationship Diagram) dựa trên các trường dữ liệu API thực sự cần.
  * Viết Repository, Service Logic, và Controller.
  * Tối ưu index, ràng buộc quan hệ (FK), transaction logic.

---

## 3. BẢNG KIỂM TRA NHANH (CHECKLIST TRƯỚC KHI CODE)

- [ ] Đã có phác thảo màn hình (Wireframe/Mockup) hay chưa?
- [ ] Đã hình dung được các trạng thái lỗi/rỗng (Empty state, Validation error) trên giao diện chưa?
- [ ] Đã thống nhất cấu trúc API Request/Response (Contract) với Frontend chưa?
- [ ] DB Schema thiết kế ra có trường nào bị thừa hoặc thiếu so với UI không?
- [ ] Tính năng này đã thực sự cần tối ưu scale/microservice ngay bây giờ chưa?
