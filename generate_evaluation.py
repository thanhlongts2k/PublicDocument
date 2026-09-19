"""
Script: generate_evaluation.py
CLI runner để tạo Báo Cáo Đánh Giá & Phân Tích Lỗi Sai từ file JSON.
Sử dụng: python generate_evaluation.py [input_file.json] [--output-dir OUTPUT_DIR] [--no-pdf]
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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doc_tools.evaluation_generator import EvaluationGenerator

def main():
    parser = argparse.ArgumentParser(description="Tự động tạo Báo Cáo Đánh Giá & Phân Tích Lỗi Sai - Quy chuẩn CHỈ TẠO FILE WORD (.docx)")
    parser.add_argument("input", nargs="?", default="doc_tools/sample_evaluation.json", help="Đường dẫn file JSON chứa dữ liệu đánh giá")
    parser.add_argument("--output-dir", "-o", default="output", help="Thư mục lưu file kết quả (mặc định: output/)")
    parser.add_argument("--pdf", action="store_true", help="Tùy chọn xuất thêm file PDF nếu cần")

    args = parser.parse_args()

    input_path = os.path.abspath(args.input)
    if not os.path.exists(input_path):
        print(f"[ERROR] Không tìm thấy file dữ liệu: {input_path}")
        sys.exit(1)

    print(f"[INFO] Đang đọc dữ liệu đánh giá từ: {input_path}")
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    generator = EvaluationGenerator(data)
    out_dir = os.path.abspath(args.output_dir)
    print(f"[INFO] Đang biên soạn và kết xuất tài liệu Word (.docx)...")

    docx_path = generator.generate(output_dir=out_dir, export_pdf=args.pdf)

    print(f"[SUCCESS] Đã tạo thành công file ĐÁNH GIÁ (Word): {docx_path}")

if __name__ == "__main__":
    main()
