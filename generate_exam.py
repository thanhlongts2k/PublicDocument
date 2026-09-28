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
    parser = argparse.ArgumentParser(description="Tự động tạo Đề Thi Chuẩn Hóa (Exam Paper) - Đóng gói PDF & MP3 vào thư mục riêng biệt")
    parser.add_argument("input", nargs="?", default="doc_tools/sample_exam.json", help="Đường dẫn file JSON chứa dữ liệu đề thi")
    parser.add_argument("--output-dir", "-o", default="output", help="Thư mục lưu file kết quả (mặc định: output/)")
    parser.add_argument("--keep-docx", action="store_true", help="Giữ lại file Word .docx tạm thời (mặc định sẽ xóa, chỉ giữ PDF)")
    parser.add_argument("--no-package", action="store_true", help="Không tạo thư mục con gói đề thi, lưu thẳng vào output-dir")
    parser.add_argument("--audio-script", "-a", help="Đường dẫn file kịch bản JSON âm thanh để xuất MP3 vào cùng thư mục gói đề thi")

    args = parser.parse_args()

    input_path = os.path.abspath(args.input)
    if not os.path.exists(input_path):
        print(f"[ERROR] Không tìm thấy file dữ liệu: {input_path}")
        sys.exit(1)

    print(f"[INFO] Đang đọc dữ liệu đề thi từ: {input_path}")
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Nếu truyền file audio script rời rạc từ CLI, gắn vào data nếu chưa có
    if args.audio_script:
        audio_path = os.path.abspath(args.audio_script)
        if os.path.exists(audio_path):
            with open(audio_path, "r", encoding="utf-8") as f_a:
                data["audio"] = json.load(f_a)
            print(f"[INFO] Đã nạp kịch bản âm thanh đính kèm từ: {audio_path}")
        else:
            print(f"[WARNING] Không tìm thấy file âm thanh: {audio_path}")

    generator = ExamGenerator(data)
    out_dir = os.path.abspath(args.output_dir)
    print(f"[INFO] Đang biên soạn và kết xuất tài liệu PDF Print-Ready...")
    
    result_path = generator.generate(output_dir=out_dir, keep_docx=args.keep_docx, package=not args.no_package)

    if result_path.endswith(".pdf"):
        print(f"[SUCCESS] Đã tạo thành công file ĐỀ THI (PDF): {result_path}")
        print(f"[SUCCESS] Thư mục gói đề thi: {os.path.dirname(result_path)}")
    else:
        print(f"[SUCCESS] Đã tạo file: {result_path}")

if __name__ == "__main__":
    main()
