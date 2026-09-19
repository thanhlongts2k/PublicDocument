# HƯỚNG DẪN SỬ DỤNG BỘ CÔNG CỤ XUẤT ĐỀ THI & BÁO CÁO ĐÁNH GIÁ (DOC TOOLS)

Bộ công cụ tự động hóa biên soạn và kết xuất tài liệu theo quy chuẩn sư phạm và in ấn chuyên nghiệp.

> ⚠️ **QUY CHUẨN ĐỊNH DẠNG ĐẦU RA BẮT BUỘC (MANDATORY OUTPUT RULE):**
> * 🖨️ **File ĐỀ THI (Exam Paper):** **CHỈ TẠO DUY NHẤT FILE PDF** (`.pdf` Print-Ready). Sẵn sàng bấm lệnh in ấn ngay, áp dụng triệt để *Zero-Key Rule* (không lộ đáp án). File Word `.docx` trung gian sẽ được tự động xóa sau khi render xong.
> * 📝 **File ĐÁNH GIÁ (Evaluation Report):** **CHỈ TẠO DUY NHẤT FILE WORD** (`.docx`). Đạt chuẩn Microsoft Word/Google Docs để giáo viên và học viên dễ dàng đọc giải thích, ghi chú, phản hồi hoặc biên tập nội dung. Không cần xuất file PDF.

---

## 1. Danh Sách Công Cụ

| File Script | Định dạng xuất | Chức năng chính | Quy cách kỹ thuật |
| :--- | :---: | :--- | :--- |
| [`generate_exam.py`](file:///d:/AgentAI/PublicDocument/generate_exam.py) | **PDF** (Duy nhất) | Tạo Đề thi từ JSON & Tự động lưu vết vào Bank | Khổ A4, lề 2.5cm, chống gãy câu, phiếu tô, **Zero-Key Rule** |
| [`generate_evaluation.py`](file:///d:/AgentAI/PublicDocument/generate_evaluation.py) | **Word (.docx)** (Duy nhất) | Tạo Báo cáo đánh giá & Lưu vết lỗi sai vào Bank | Metadata 2x4, [ĐÚNG]/[CHƯA ĐÚNG], Callout cốt lõi, Confusion Matrix |
| [`assemble_exam.py`](file:///d:/AgentAI/PublicDocument/assemble_exam.py) | **PDF** (Duy nhất) | **Bộ gom đề thông minh từ Question Bank** | Tự động ghép đề Gateway, đề ôn lỗi sai, đề chuyên đề theo tuần |
| [`doc_tools/pdf_converter.py`](file:///d:/AgentAI/PublicDocument/doc_tools/pdf_converter.py) | Engine PDF | Chuyển đổi Word sang PDF tự động | Dùng Microsoft Word COM Automation, độ nét tối đa 100% |

---

## 2. Cách Chạy Bằng Lệnh (CLI)

### A. Gom Đề Thi Thông Minh Từ Question Bank (Mới)
```powershell
# 1. Xem thống kê dữ liệu câu hỏi trong kho:
python assemble_exam.py --stats

# 2. Gom đề thi Gateway tổng hợp theo tuần (Ví dụ: gom 60 câu từ Tuần 1 đến Tuần 4):
python assemble_exam.py --weeks 1,2,3,4 --count 60 --title "ĐỀ THI GATEWAY 1 (TUẦN 1 - 4)"

# 3. Gom đề thi ôn tập Tuần 1 (Ví dụ: bốc nhanh 30 câu từ Tuần 1):
python assemble_exam.py --weeks 1 --count 30 --title "ĐỀ THI ÔN TẬP NHANH TUẦN 01"

# 4. Gom đề "Đặc trị lỗi sai" cho từng học viên (Chỉ gom những câu học viên từng làm sai):
python assemble_exam.py --student TranVanMinh --only-errors --count 20 --title "ĐỀ ÔN TẬP LỖI SAI - TRẦN VĂN MINH"
```

### B. Tạo Đề Thi Hoàn Chỉnh Từ File JSON Cụ Thể (Xuất ra file .pdf)
```powershell
# Chạy tạo đề thi từ file JSON (Tự động nạp câu hỏi vào Bank và xuất PDF):
python generate_exam.py doc_tools/exam_week01.json --output-dir output
```

### C. Tạo Báo Cáo Đánh Giá & Phân Tích Lỗi Sai (Xuất ra file .docx)
```powershell
# Chạy tạo đánh giá từ file JSON (Tự động cập nhật lỗi sai của học viên vào Bank):
python generate_evaluation.py doc_tools/sample_evaluation.json --output-dir output
```

---

## 3. Quy Trình Làm Việc Hợp Tác Với AI (Khuyên Dùng)

Sau này, anh **không cần phải tự viết JSON thủ công**:
1. **Bước 1:** Anh chỉ cần đưa yêu cầu hoặc dữ liệu thô vào chat. Ví dụ:
   - *"Em tạo giúp anh 1 đề thi JLPT N2 phần ngữ pháp 15 câu kèm 1 bài đọc ngắn."*
   - *"Học viên Nguyễn Văn B vừa làm đề số 3 bị sai câu 2, 5, 9. Tạo giúp anh file đánh giá kèm bảng so sánh cấu trúc."*
2. **Bước 2:** Em (AI) sẽ tự động biên soạn nội dung học thuật chuẩn mực thành file JSON.
3. **Bước 3:** Em tự động kích hoạt tool chạy ngầm để xuất ra ngay file `.docx` và `.pdf` trong thư mục [`output/`](file:///d:/AgentAI/PublicDocument/output/). Anh chỉ cần mở file lên và sử dụng!

---

## 4. Cấu Trúc File Dữ Liệu Đầu Vào (JSON Schema)

### A. Cấu trúc Đề thi (`sample_exam.json`)
```json
{
  "metadata": {
    "organization": "Tên Đơn vị / Học viện",
    "program": "Tên Chương trình học",
    "subject": "Tên Môn thi",
    "exam_title": "Tên Kỳ Thi (Ví dụ: ĐỀ THI ĐÁNH GIÁ NĂNG LỰC)",
    "program_code": "JLPT_N3",
    "subject_code": "NguPhapDocHieu",
    "type_code": "DeLuyenTap",
    "exam_code": "101",
    "date_code": "20260919",
    "duration_minutes": 50,
    "total_questions": 8,
    "date": "19/09/2026"
  },
  "instructions": [
    "1. Hướng dẫn 1...",
    "2. Hướng dẫn 2..."
  ],
  "sections": [
    {
      "title": "PHẦN I: TỪ VỰNG & NGỮ PHÁP",
      "description": "Hướng dẫn làm bài...",
      "reading_passage": "Nội dung đoạn văn đọc hiểu (nếu có sẽ tự đóng khung Border Box)",
      "questions": [
        {
          "question": "Nội dung câu hỏi...",
          "type": "multiple_choice",
          "options": ["A. ...", "B. ...", "C. ...", "D. ..."]
        },
        {
          "question": "Câu ghép sao...",
          "type": "star_arrangement",
          "star_parts": ["1. ...", "2. ...", "3. ...", "4. ..."],
          "options": ["1", "2", "3", "4"]
        }
      ]
    }
  ]
}
```

### B. Cấu trúc Đánh giá (`sample_evaluation.json`)
```json
{
  "metadata": {
    "title": "BÁO CÁO ĐÁNH GIÁ, PHÂN TÍCH LỖI SAI & GIẢI THÍCH CHI TIẾT",
    "subtitle": "Phụ đề chương trình...",
    "subject_code": "JLPT_N3",
    "type_code": "DanhGia",
    "student_code": "TranVanMinh",
    "student_name": "Trần Văn Minh",
    "topic_code": "NguPhapTuan01",
    "exam_set": "Tên bộ đề",
    "score_summary": "6 / 8 (75.0%)",
    "date_code": "20260919",
    "date": "19/09/2026",
    "version": "1",
    "core_strengths": "Điểm mạnh cốt lõi...",
    "key_weaknesses": "Lỗ hổng cần khắc phục ngay..."
  },
  "summary_results": [
    {
      "question_number": 1,
      "student_choice": "B (がち)",
      "correct_answer": "A (気味)",
      "is_correct": false,
      "question_content": "Câu gốc...",
      "translation": "Dịch nghĩa...",
      "brief_explanation": "Giải thích ngắn gọn..."
    }
  ],
  "error_analyses": [
    {
      "question_number": 1,
      "question_text": "Câu hỏi...",
      "error_phenomenon": "1. Hiện tượng sai...",
      "root_cause": "2. Nguồn gốc nhầm lẫn / Bẫy tâm lý...",
      "core_rule": "3. Bản chất kiến thức cốt lõi (tự đóng khung Callout Quote)..."
    }
  ],
  "confusion_matrix": {
    "rows": [
      {
        "structure": "〜気味",
        "meaning": "Ý nghĩa...",
        "connection": "Cách kết hợp...",
        "nuance": "Sắc thái...",
        "example": "Ví dụ..."
      }
    ],
    "exam_traps": [
      { "trap_name": "Tên bẫy", "trap_description": "Mô tả bẫy đề thi..." }
    ],
    "quick_checklist": [
      "Mẹo nhận biết 3 giây..."
    ]
  },
  "drill_exercises": [
    {
      "question": "Câu bài tập mới...",
      "options": ["A. ...", "B. ...", "C. ...", "D. ..."]
    }
  ]
}
```
