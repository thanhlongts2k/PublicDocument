
# HƯỚNG DẪN DÀNH CHO NGƯỜI TRÁI NGÀNH: BÓC TÁCH & HIỂU TRỌN VẸN LOGIC CÔNG VIỆC

---

## 1. KỸ THUẬT "DỊCH NGƯỢC TỪ THỰC TẾ" (THE PHYSICAL WALKTHROUGH)
*Tránh xa các khái niệm trừu tượng; quy đổi toàn bộ logic về hành vi thực tế ngoài đời.*

- **Hỏi về dòng chảy vật lý:** 
  "Anh/chị mô tả giúp em trên thực tế ngoài đời, một quy trình chuẩn từ lúc phát sinh đến lúc kết thúc sẽ diễn ra như thế nào (ai làm gì, đi đâu, cầm giấy tờ/thao tác gì)?"
- **Xin một case study thực tế gần nhất:** 
  "Cho em xin một trường hợp khách hàng/sự vụ thực tế gần nhất vừa gặp phải vấn đề này được không ạ?"
- **Nguyên lý cốt lõi:** Con người rất khó giải thích lý thuyết trừu tượng cho người ngoài ngành, nhưng kể lại một câu chuyện thực tế vừa xảy ra thì ai cũng làm được. Bạn hãy lắng nghe câu chuyện đó để tự rút ra logic xử lý.

---

## 2. BỘ 4 CÂU HỎI GIẢI MÃ NGHIỆP VỤ (DOMAIN DECODER)

### Câu hỏi 1: Đối tượng trung tâm (Core Entity) là gì?
*Xác định "vật thể" mà mọi quy trình và thao tác đang xoay quanh (phiếu bảo trì, hồ sơ bệnh án, lô hàng, hợp đồng, hóa đơn...).*
- **Cách hỏi:** "Trong bài toán này, thực thể chính mà em cần theo dõi và xử lý từ đầu đến cuối là gì?"

### Câu hỏi 2: Vòng đời trạng thái (Life-cycle & Status) ra sao?
*Mọi logic nghiệp vụ thực chất là việc một đối tượng chuyển từ trạng thái này sang trạng thái khác.*
- **Cách hỏi:** "Đối tượng này sinh ra khi nào? Nó sẽ đi qua những trạng thái nào (ví dụ: Tạo mới -> Chờ duyệt -> Đang xử lý -> Hoàn thành/Hủy)? Điều kiện gì kích hoạt nó nhảy sang bước tiếp theo?"

### Câu hỏi 3: Luật ngầm & Ràng buộc bắt buộc (Hard Constraints & Compliance) là gì?
*Các quy chuẩn, thói quen ngành hoặc quy định pháp lý bất di bất dịch mà người ngoài không thể tự suy luận.*
- **Cách hỏi:** "Trong mảng này, có quy định, tiêu chuẩn hoặc điều luật nào bắt buộc phải tuân thủ mà không được phép làm tắt không ạ?"

### Câu hỏi 4: Khi xảy ra sự cố ngoài đời, người ta xử lý tay thế nào (Exception Handling)?
*Nắm bắt toàn bộ các kịch bản ngoại lệ (edge cases) mà không cần 5-10 năm kinh nghiệm.*
- **Cách hỏi:** "Nếu ngoài đời thực tế gặp trường hợp bất khả kháng [ví dụ: mất mạng, thiết bị hỏng, khách đổi ý], hiện tại mọi người đang xử lý tay bằng cách nào?"

---

## 3. KỸ THUẬT HỎI KHÔN NGOAN CHO NGƯỜI MỚI

Tận dụng "Lợi thế của người mới" (Beginner's Advantage) để hỏi sâu mà vẫn thể hiện tư duy bài bản:

### Kỹ thuật 1: Paraphrase bằng ngôn ngữ đời thường
Ngay sau khi nghe giải thích một tràng thuật ngữ chuyên môn, hãy tóm gọn lại bằng logic đời sống:
> "Em chưa quen với thuật ngữ [Thuật ngữ A] của ngành mình, nhưng theo cách em hiểu logic đời thường thì nó giống như việc [Ví dụ tương đương: như đi đăng kiểm xe / ký nhận bưu tá], đoạn này cần [Điều kiện B] xong thì mới được làm [Điều kiện C]. Em hiểu bản chất như vậy đã chuẩn chưa ạ?"

### Kỹ thuật 2: Thừa nhận vị thế để hỏi sâu
Đặt câu hỏi với tâm thế người muốn hiểu bản chất để bảo vệ an toàn cho hệ thống:
> "Vì em mới tiếp cận mảng [Tên lĩnh vực] nên em muốn làm rõ bản chất ngay từ đầu để tránh làm sai lệch dữ liệu/nghiệp vụ của team. Chỗ [Khái niệm X] này trong ngành mình được định nghĩa dựa trên tiêu chí nào vậy anh/chị?"

---

## 4. VŨ KHÍ SINH TỒN: SỔ TAY "THUẬT NGỮ & NGHIỆP VỤ" (DOMAIN GLOSSARY)

Trong 2–4 tuần đầu, tạo một bảng ghi chú cá nhân để tra cứu và tích lũy:

| Thuật ngữ / Từ viết tắt | Nghĩa đời thường (Dễ hiểu) | Bắt nguồn từ đâu / Ai dùng | Lưu ý sống còn / Luật cấm kỵ |
| :--- | :--- | :--- | :--- |
| *Ví dụ: SKU, SLA, HSD...* | *Dịch ra ngôn ngữ bạn hiểu* | *Bộ phận vận hành / Khách hàng* | *Sai lệch trường này sẽ phạt tiền / lỗi luồng* |

**Quy tắc:** Nghe thấy từ viết tắt/thuật ngữ lạ -> Ghi lại ngay -> Tra cứu hoặc hỏi đồng nghiệp ngang cấp sau buổi họp -> Đưa vào bảng. Sau 2 tuần, bạn sẽ làm chủ 80% từ vựng cốt lõi của ngành.

---

# CẨM NANG BÓC TÁCH YÊU CẦU & ỨNG BIẾN KHI NHẬN VIỆC TỪ QUẢN LÝ

---

## PHẦN 1: KHUNG 4 TẦNG BÓC TÁCH NHIỆM VỤ (THE 4-LAYER BRIEFING)
*Chuyển từ tâm thế "người ghi chép thụ động" sang "người đồng thuận giải pháp".*

### 1. Tầng 1: Mục đích & Bối cảnh (Why & Context)
*Hiểu lý do thực sự đằng sau yêu cầu để tự chủ động xử lý các chi tiết phát sinh mà không cần hỏi lại từng li từng tí.*
- Nguồn gốc bài toán: "Vấn đề này phát sinh từ đâu ạ (phản ánh từ khách hàng, định hướng từ ban giám đốc, hay tối ưu nội bộ)?"
- Giá trị kỳ vọng: "Nếu task này xong đúng hạn và chuẩn chỉnh, chỉ số hoặc quy trình nào của phòng ban/dự án sẽ được cải thiện rõ nhất?"
- Tác động nếu không làm: "Mức độ khẩn cấp của việc này thế nào? Nếu chưa làm ngay trong tuần này thì rủi ro lớn nhất là gì?"

### 2. Tầng 2: Tiêu chuẩn hoàn thành (Definition of Done - DoD)
*Đóng đinh kết quả đầu ra, tránh trường hợp bạn nghĩ đã xong nhưng quản lý thấy chưa đạt.*
- Hình thái kết quả: "Kết quả cuối cùng sếp muốn nhận là gì: một tài liệu phân tích, một bản demo chạy thử, một báo cáo số liệu, hay tính năng đưa thẳng lên môi trường production?"
- Tiêu chí nghiệm thu: "Dấu hiệu hoặc kịch bản cụ thể nào cho thấy task này đã đạt chuẩn 100% để bàn giao?"
- Người thụ hưởng trực tiếp: "Ai sẽ là người dùng cuối hoặc người kiểm tra kết quả này (sếp, team nghiệp vụ, hay khách hàng)?"

### 3. Tầng 3: Ranh giới phạm vi & Ràng buộc (Scope & Constraints)
*Chặn đứng nguy cơ phình to yêu cầu (scope creep) và lãng phí thời gian vào chi tiết ngoài lề.*
- Phạm vi loại trừ (Out-of-scope): "Trong phiên bản/giai đoạn này, có phần nào ta tuyệt đối chưa cần chạm vào để ưu tiên tốc độ không ạ?"
- Ràng buộc tài nguyên & hệ thống: "Task này có phụ thuộc vào dữ liệu, API, hoặc sự phối hợp của ai/bộ phận nào khác không?"
- Mốc kiểm tra giữa chặng (Checkpoint): "Em dự kiến mốc [thời gian cụ thể] sẽ gửi bản phác thảo/bản nháp đầu tiên để sếp liếc qua trước khi chốt toàn bộ, như vậy có hợp lý không?"

### 4. Tầng 4: Thứ tự ưu tiên & Đánh đổi (Trade-offs)
*Xác định rõ yếu tố cần hy sinh khi xảy ra xung đột về thời gian hoặc nguồn lực.*
- Cân bằng tải: "Hiện tại em đang chạy task X và Y. Khi nhận thêm task này, thứ tự ưu tiên của nó đứng trước hay sau task X?"
- Tiêu chí đánh đổi: "Nếu phải chọn giữa chất lượng hoàn hảo/tính bao quát cao nhưng cần thêm thời gian, và phiên bản rút gọn hoàn thành nhanh để giải quyết việc gấp trước mắt, sếp muốn ưu tiên hướng nào hơn?"

---

## PHẦN 2: KỸ THUẬT HỎI CHỦ ĐỘNG (PROACTIVE INQUIRY)

Tuyệt đối không hỏi câu hỏi mở chung chung khiến quản lý phải mất thời gian suy nghĩ và giải thích từ đầu. Hãy luôn đưa ra giả định hoặc đề xuất có sẵn:

| Cách hỏi bị động (Gây tốn thời gian, thiếu chủ động) | Cách hỏi chủ động (Thể hiện tư duy làm chủ bài toán) |
| :--- | :--- |
| "Em phải làm tính năng này như thế nào?" | "Dựa trên bài toán này, em thấy có 2 hướng tiếp cận: Hướng A (nhanh, giải quyết tức thì) và Hướng B (chuẩn hóa lâu dài). Em đề xuất đi theo hướng A trước, sếp thấy sao?" |
| "Deadline là khi nào?" | "Để hoàn thành trọn vẹn kèm test kỹ, em ước tính cần 2 ngày (chốt thứ Năm). Nếu sếp cần gấp bản xem trước vào chiều thứ Tư, em sẽ tập trung hoàn thiện luồng chính trước." |
| "Sếp giải thích lại đoạn này được không?" | "Theo cách em hiểu thì luồng xử lý sẽ là [Bước 1 -> Bước 2], dữ liệu trả về cần loại trừ trường hợp X. Em hiểu như vậy đã đúng trọng tâm sếp dặn chưa ạ?" |

---

## PHẦN 3: XỬ LÝ LỆNH GIAO VIỆC VẮN TẮT, MƠ HỒ (1–2 DÒNG)

### 1. Nguyên tắc cốt lõi
Không bao giờ dùng câu hỏi mở. Chuyển toàn bộ nghi vấn thành câu hỏi trắc nghiệm A/B kèm phương án mặc định để sếp chỉ cần gõ 1 chữ cái hoặc 1 từ ngắn để duyệt.

### 2. Quy trình phản xạ 3 bước
- Bước 1 - Tự điều tra nhanh (Internal Triangulation) trong 5–10 phút: Rà soát lại email, log hệ thống, ticket gần nhất hoặc ngữ cảnh cuộc họp gần đây để định vị điểm vấp của sếp trước khi phản hồi.
- Bước 2 - Đóng khung giả định (Framed Assumption): Gửi lại thông điệp theo công thức: Hiểu hiện tại + Đề xuất phương án + Hỏi chọn A/B.
- Bước 3 - Chốt chặn im lặng (Negative Confirmation): Đưa ra mốc thời gian cụ thể: nếu sếp không phản hồi, bạn sẽ tự động chạy theo phương án mặc định đã đề xuất.

### 3. Kịch bản ứng biến theo 3 tình huống thực tế

Tình huống A: Lệnh kiểm tra mơ hồ ("Check lại cái X giúp anh / Xem lại số liệu tuần này")
> "Em vừa liếc nhanh qua [Module/Bảng số liệu X]:
> - Có phải sếp đang thấy lệch ở chỗ [Vấn đề A - ví dụ: số liệu ngày hôm qua chưa nhảy]?
> - Hay sếp cần em rà soát tổng thể toàn bộ chuỗi dữ liệu tuần qua?
> 
> Nếu là điểm A, em xử lý xong trong 30 phút. Nếu là tổng thể, em sẽ gửi báo cáo đối soát trước [Giờ/Buổi]. Sếp định hướng giúp em để em tập trung đúng chỗ nhé."

Tình huống B: Yêu cầu tính năng/tác vụ mới không có spec ("Làm thêm nút xuất Excel / Thêm báo cáo này")
> "Dạ để ra được bản dùng được ngay, em định làm theo hướng tối giản trước:
> - Nội dung: Xuất theo đúng các trường [Trường A, B, C] đang hiển thị trên màn hình hiện tại.
> - Định dạng: File .xlsx chuẩn không cần tạo màu hay công thức phức tạp.
> 
> Em lên bản này trước để sếp dùng trong chiều nay, còn các bộ lọc nâng cao em sẽ bổ sung ở phiên bản tiếp theo. Sếp thấy hướng này ổn chưa ạ?"

Tình huống C: Quăng việc gấp đè lên việc cũ ("Ưu tiên cái này trước nhé / Xử lý gấp cái này")
> "Dạ em nhận việc này. Hiện em đang hoàn thiện nốt [Task cũ X] (dự kiến xong lúc 15h):
> - Nếu task mới này cần đẩy lên trước: Em sẽ tạm dừng [Task X] và bàn giao task mới trước 16h, [Task X] dời sang sáng mai.
> - Nếu [Task X] vẫn quan trọng hơn: Em chốt xong lúc 15h rồi dồn toàn lực xử lý việc mới này đến cuối ngày.
> 
> Sếp duyệt giúp em hướng nào để em sắp xếp timeline luôn nhé."

---

## PHẦN 4: KHÓA CHẶT KỲ VỌNG (THE CONFIRMATION LOOPS)

### 1. Mẫu tin nhắn chốt việc sau 15 phút nhận lệnh
(Dùng để gửi lại ngay sau khi nhận việc qua lời nói hoặc tin nhắn vắn tắt, tạo bằng chứng văn bản tránh sai lệch):

--------------------------------------------------
Em xin xác nhận lại các điểm cốt lõi của task [Tên việc]:
1. Mục tiêu: [1 câu tóm gọn bài toán cần giải quyết]
2. Đầu ra bàn giao: [Báo cáo / Code / File đối soát / Bản demo...]
3. Ranh giới: Tập trung vào [Tính năng/Phần chính], chưa xử lý [Phần mở rộng].
4. Tiến độ: Gửi sếp bản nháp/demo vào [Giờ, Ngày] và nghiệm thu vào [Giờ, Ngày].

Nếu không có gì cần điều chỉnh, em sẽ tiến hành theo đúng khung này nhé sếp!
--------------------------------------------------

### 2. Mẫu kích hoạt tiến độ khi sếp "Seen" không phản hồi
(Biến sự im lặng thành sự đồng thuận ngầm để công việc không bị tắc, giữ thế chủ động an toàn):

--------------------------------------------------
"Sếp ơi, để kịp tiến độ bàn giao trong hôm nay, em xin phép triển khai theo phương án A (làm luồng chuẩn trước). 

Đến [Giờ cụ thể], em sẽ gửi bản kết quả đầu tiên. Nếu có điểm nào cần uốn nắn lại, sếp nhắn em chỉnh ngay nhé!"
--------------------------------------------------