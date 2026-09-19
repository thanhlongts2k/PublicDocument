"""
Script: generate_exam.py
CLI runner để tạo đề thi từ file JSON.
Sử dụng: python generate_exam.py [input_file.json] [--output-dir OUTPUT_DIR] [--no-pdf]
"""

import sys
import os
import json
import argparse

# Đảm bảo UTF-8 cho stdout trên Windows
try:
    if sys.stdout.encoding.lower() != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    if sys.stderr.encoding.lower() != 'utf-8':
        sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

# Đảm bảo import được doc_tools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doc_tools.exam_generator import ExamGenerator

def main():
    parser = argparse.ArgumentParser(description="Tự động tạo Đề Thi Chuẩn Hóa (Exam Paper) - Quy chuẩn CHỈ TẠO FILE PDF")
    parser.add_argument("input", nargs="?", default="doc_tools/sample_exam.json", help="Đường dẫn file JSON chứa dữ liệu đề thi")
    parser.add_argument("--output-dir", "-o", default="output", help="Thư mục lưu file kết quả (mặc định: output/)")
    parser.add_argument("--keep-docx", action="store_true", help="Giữ lại file Word .docx tạm thời (mặc định sẽ xóa, chỉ giữ PDF)")

    args = parser.parse_args()

    input_path = os.path.abspath(args.input)
    if not os.path.exists(input_path):
        print(f"[ERROR] Không tìm thấy file dữ liệu: {input_path}")
        sys.exit(1)

    print(f"[INFO] Đang đọc dữ liệu đề thi từ: {input_path}")
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    generator = ExamGenerator(data)
    out_dir = os.path.abspath(args.output_dir)
    print(f"[INFO] Đang biên soạn và kết xuất tài liệu PDF Print-Ready...")
    
    result_path = generator.generate(output_dir=out_dir, keep_docx=args.keep_docx)

    if result_path.endswith(".pdf"):
        print(f"[SUCCESS] Đã tạo thành công file ĐỀ THI (PDF): {result_path}")
    else:
        print(f"[SUCCESS] Đã tạo file: {result_path}")

if __name__ == "__main__":
    main()
