"""
Script: assemble_exam.py
CLI runner để gom và tạo Đề thi tổng hợp từ Ngân hàng câu hỏi (Question Bank).
Tự động xuất DUY NHẤT file PDF Print-Ready.

Ví dụ:
  python assemble_exam.py --weeks 1 --count 30 --title "ĐỀ THI ÔN TẬP TUẦN 1"
  python assemble_exam.py --student TranVanMinh --only-errors --count 20
  python assemble_exam.py --stats
"""

import sys
import os
import argparse

# Đảm bảo UTF-8 cho stdout trên Windows
try:
    if sys.stdout.encoding.lower() != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    if sys.stderr.encoding.lower() != 'utf-8':
        sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doc_tools.question_bank import QuestionBank
from doc_tools.smart_assembler import SmartAssembler

def main():
    parser = argparse.ArgumentParser(description="Bộ gom đề thông minh (Smart Assembler) từ Ngân hàng câu hỏi - Xuất file PDF Print-Ready")
    parser.add_argument("--weeks", "-w", type=str, help="Danh sách tuần cần gom, cách nhau bởi dấu phẩy (Ví dụ: 1,2,3,4)")
    parser.add_argument("--skills", "-s", type=str, help="Kỹ năng cần lọc: moji_goi, bunpou, dokkai (cách nhau bởi dấu phẩy)")
    parser.add_argument("--tags", "-t", type=str, help="Tags kiến thức (Ví dụ: 〜気味,hau_to_tinh_tu)")
    parser.add_argument("--student", type=str, help="Tên học viên cần lọc lịch sử làm sai")
    parser.add_argument("--only-errors", action="store_true", help="Chỉ gom các câu hỏi học viên từng làm sai")
    parser.add_argument("--count", "-c", type=int, default=60, help="Số lượng câu hỏi cần gom (mặc định: 60)")
    parser.add_argument("--title", type=str, help="Tiêu đề đề thi tùy chỉnh")
    parser.add_argument("--exam-code", type=str, help="Mã đề thi tùy chỉnh")
    parser.add_argument("--output-dir", "-o", default="output", help="Thư mục lưu file PDF kết quả (mặc định: output/)")
    parser.add_argument("--stats", action="store_true", help="Hiển thị thống kê dữ liệu hiện có trong Question Bank")

    args = parser.parse_args()

    bank = QuestionBank()

    if args.stats:
        stats = bank.get_stats()
        print("\n=======================================================")
        print("          THỐNG KÊ NGÂN HÀNG CÂU HỎI (QUESTION BANK)")
        print("=======================================================")
        print(f"Tổng số câu hỏi trong kho : {stats['total_questions']} câu")
        print(f"Số câu hỏi có lịch sử sai : {stats['questions_with_errors']} câu")
        print(f"Cập nhật lần cuối         : {stats['last_updated']}")
        print("\n--- Phân loại theo Kỹ năng ---")
        for sk, cnt in stats["by_skill"].items():
            print(f"  • {sk:<15}: {cnt} câu")
        print("\n--- Phân loại theo Tuần ---")
        for wk, cnt in stats["by_week"].items():
            print(f"  • Tuần {wk:<10}: {cnt} câu")
        print("=======================================================\n")
        return

    weeks_list = [int(w.strip()) for w in args.weeks.split(",")] if args.weeks else None
    skills_list = [s.strip() for s in args.skills.split(",")] if args.skills else None
    tags_list = [t.strip() for t in args.tags.split(",")] if args.tags else None

    assembler = SmartAssembler(bank=bank)

    print(f"[INFO] Đang tìm kiếm và gom câu hỏi từ Question Bank...")
    try:
        pdf_path = assembler.assemble_and_generate_pdf(
            output_dir=os.path.abspath(args.output_dir),
            weeks=weeks_list,
            skills=skills_list,
            tags=tags_list,
            student_name=args.student,
            only_errors=args.only_errors,
            count=args.count,
            title=args.title,
            exam_code=args.exam_code
        )
        print(f"[SUCCESS] Đã tạo thành công Đề thi tổng hợp PDF Print-Ready: {pdf_path}")
    except Exception as e:
        print(f"[ERROR] Thất bại khi gom đề: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
