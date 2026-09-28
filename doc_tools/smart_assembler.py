"""
Module: smart_assembler.py
Bộ tổng hợp đề thi thông minh (Smart Exam Assembler) từ Ngân hàng câu hỏi.
Hỗ trợ tạo đề Gateway theo tuần, đề ôn tập lỗi sai học viên, và đề chuyên đề.
"""

import os
from datetime import datetime
from typing import List, Dict, Optional, Any
from .question_bank import QuestionBank
from .exam_generator import ExamGenerator

class SmartAssembler:
    def __init__(self, bank: Optional[QuestionBank] = None):
        self.bank = bank or QuestionBank()

    def assemble(
        self,
        weeks: Optional[List[int]] = None,
        skills: Optional[List[str]] = None,
        tags: Optional[List[str]] = None,
        student_name: Optional[str] = None,
        only_errors: bool = False,
        count: int = 60,
        title: Optional[str] = None,
        exam_code: Optional[str] = None,
        program_code: str = "JLPT_N3",
        subject_code: str = "TongHop"
    ) -> Dict[str, Any]:
        """
        Gom và cấu trúc hóa đề thi từ Ngân hàng câu hỏi theo tiêu chí.
        """
        # Lấy câu hỏi từ Bank
        questions = self.bank.filter_questions(
            weeks=weeks,
            skills=skills,
            tags=tags,
            student_name=student_name,
            only_errors=only_errors,
            limit=count
        )

        if not questions:
            raise ValueError("Không tìm thấy câu hỏi nào phù hợp với tiêu chí lọc trong Question Bank!")

        # Phân loại câu hỏi vào các Section
        moji_goi_qs = []
        bunpou_qs = []
        dokkai_qs = []
        other_qs = []

        for q in questions:
            skill = q.get("skill", "general")
            # Format lại câu hỏi theo chuẩn exam
            q_formatted = {
                "question": q.get("question", ""),
                "type": q.get("type", "multiple_choice"),
                "options": q.get("options", []),
                "star_parts": q.get("star_parts", [])
            }
            if skill == "moji_goi":
                moji_goi_qs.append(q_formatted)
            elif skill == "bunpou":
                bunpou_qs.append(q_formatted)
            elif skill == "dokkai":
                q_formatted["reading_passage"] = q.get("reading_passage", "")
                dokkai_qs.append(q_formatted)
            else:
                other_qs.append(q_formatted)

        sections = []

        # Dựng Sections
        if moji_goi_qs:
            sections.append({
                "title": f"PHẦN I: TỪ VỰNG & CHỮ HÁN ({len(moji_goi_qs)} CÂU)",
                "description": "Hãy chọn phương án đúng nhất cho các câu hỏi sau:",
                "questions": moji_goi_qs
            })

        if bunpou_qs:
            sec_num = "II" if moji_goi_qs else "I"
            sections.append({
                "title": f"PHẦN {sec_num}: NGỮ PHÁP THỰC CHIẾN ({len(bunpou_qs)} CÂU)",
                "description": "Hãy chọn đáp án hoặc sắp xếp đúng ngữ pháp để hoàn thành câu:",
                "questions": bunpou_qs
            })

        if dokkai_qs:
            sec_num = "III" if (moji_goi_qs and bunpou_qs) else ("II" if (moji_goi_qs or bunpou_qs) else "I")
            sections.append({
                "title": f"PHẦN {sec_num}: ĐỌC HIỂU THỰC CHIẾN ({len(dokkai_qs)} CÂU)",
                "description": "Đọc các văn bản và trả lời câu hỏi tương ứng:",
                "questions": dokkai_qs
            })

        if other_qs:
            sections.append({
                "title": f"CÂU HỎI BỔ SUNG & ÔN TẬP ({len(other_qs)} CÂU)",
                "description": "Chọn phương án đúng nhất:",
                "questions": other_qs
            })

        # Thiết lập Metadata đề thi
        now = datetime.now()
        date_str = now.strftime("%d/%m/%Y")
        date_code = now.strftime("%Y%m%d")

        if not title:
            if only_errors and student_name:
                title = f"ĐỀ ÔN TẬP ĐẶC TRỊ LỖI SAI - HỌC VIÊN {student_name.upper()}"
            elif weeks:
                w_str = "-".join(str(w) for w in weeks)
                title = f"ĐỀ THI TỔNG HỢP GATEWAY (TUẦN {w_str})"
            else:
                title = "ĐỀ THI KIỂM TRA TỔNG HỢP NĂNG LỰC"

        if not exam_code:
            exam_code = f"GW_{date_code}" if weeks else f"REV_{date_code}"

        exam_data = {
            "metadata": {
                "organization": "HỌC VIỆN NGÔN NGỮ QUỐC TẾ - QUESTION BANK",
                "program": f"CHƯƠNG TRÌNH ĐÀO TẠO TIẾNG NHẬT CHUẨN HOÁ {program_code}",
                "subject": f"BÀI THI TỔNG HỢP ({len(questions)} CÂU HỎI)",
                "exam_title": title,
                "program_code": program_code,
                "subject_code": subject_code,
                "type_code": "DeTongHop",
                "exam_code": exam_code,
                "date_code": date_code,
                "duration_minutes": max(30, int(len(questions) * 1.25)),
                "total_questions": len(questions),
                "date": date_str
            },
            "instructions": [
                f"1. Đề thi gồm {len(questions)} câu hỏi được tổng hợp tự động từ Ngân hàng câu hỏi.",
                "2. Mỗi câu chỉ có DUY NHẤT một đáp án đúng. Thí sinh tô đen vào phiếu trả lời ở trang cuối.",
                "3. Tuyệt đối không sử dụng tài liệu hay từ điển trong quá trình làm bài."
            ],
            "sections": sections
        }

        return exam_data

    def assemble_and_generate_pdf(
        self,
        output_dir: str = "output",
        weeks: Optional[List[int]] = None,
        skills: Optional[List[str]] = None,
        tags: Optional[List[str]] = None,
        student_name: Optional[str] = None,
        only_errors: bool = False,
        count: int = 60,
        title: Optional[str] = None,
        exam_code: Optional[str] = None
    ) -> str:
        """
        Gom đề và xuất thẳng ra file PDF Print-Ready duy nhất.
        """
        exam_data = self.assemble(
            weeks=weeks,
            skills=skills,
            tags=tags,
            student_name=student_name,
            only_errors=only_errors,
            count=count,
            title=title,
            exam_code=exam_code
        )

        gen = ExamGenerator(exam_data)
        # Theo quy chuẩn: Chỉ tạo file PDF
        pdf_path = gen.generate(output_dir=output_dir, keep_docx=False)
        return pdf_path
