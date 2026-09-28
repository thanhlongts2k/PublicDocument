#!/usr/bin/env python
"""
generate_audio.py - CLI tool tạo file âm thanh đề thi (.mp3) từ kịch bản JSON.
Hỗ trợ Tiếng Nhật JLPT, Tiếng Việt và Tiếng Anh.
Tùy biến tốc độ, giọng đọc, thời gian chờ và chế độ xuất file.
"""

import os
import sys
import json
import argparse
import asyncio

# Đảm bảo in tiếng Việt và ký tự đặc biệt an toàn trên Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from doc_tools.audio_generator import AudioExamGenerator, DEFAULT_VOICE_REGISTRY
import edge_tts



async def print_available_voices():
    """Hiển thị danh sách các giọng đọc AI chất lượng cao cho 3 ngôn ngữ."""
    print("\n🔍 ĐANG TÌM KIẾM DANH SÁCH GIỌNG ĐỌC AI TRÊN HỆ THỐNG...\n")
    try:
        voices = await edge_tts.list_voices()
        locales = ("vi-VN", "ja-JP", "en-US")
        filtered = [v for v in voices if any(v.get("Locale", "").startswith(loc) for loc in locales)]
        
        print(f"{'Mã Ngôn Ngữ':<12} | {'Tên Giọng Đọc (Voice ID)':<35} | {'Giới tính':<10}")
        print("-" * 65)
        for v in filtered:
            loc = v.get("Locale", "")
            name = v.get("ShortName", "")
            gender = v.get("Gender", "")
            print(f"{loc:<12} | {name:<35} | {gender:<10}")
        print("\n💡 Gợi ý: Bạn có thể truyền tên giọng đọc vào kịch bản JSON (settings.narrator_voice, male_voice, female_voice).")
    except Exception as e:
        print(f"❌ Không thể tải danh sách giọng đọc: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Bộ công cụ xuất đề thi âm thanh (.mp3) từ kịch bản JSON - Hỗ trợ Tiếng Nhật JLPT, Tiếng Việt & Tiếng Anh."
    )
    parser.add_argument(
        "script",
        nargs="?",
        help="Đường dẫn đến file kịch bản JSON (ví dụ: doc_tools/sample_audio_vi.json)"
    )
    parser.add_argument(
        "--output-dir", "-o",
        default="output",
        help="Thư mục xuất file âm thanh .mp3 (mặc định: output)"
    )
    parser.add_argument(
        "--lang",
        choices=["vi-VN", "ja-JP", "en-US"],
        help="Ghi đè ngôn ngữ thi (vi-VN, ja-JP, en-US)"
    )
    parser.add_argument(
        "--speed",
        help="Ghi đè tốc độ đọc (ví dụ: '+0%%', '-10%%', '+15%%')"
    )
    parser.add_argument(
        "--pitch",
        help="Ghi đè cao độ giọng (ví dụ: '+0Hz', '+5Hz', '-5Hz')"
    )
    parser.add_argument(
        "--mode",
        choices=["combined", "split", "both"],
        help="Chế độ xuất file: 'combined' (file tổng duy nhất), 'split' (tách từng câu), 'both' (cả hai)"
    )
    parser.add_argument(
        "--pause-think",
        type=float,
        help="Ghi đè thời gian chờ suy nghĩ / làm bài cho mỗi câu (giây, ví dụ: 12.0)"
    )
    parser.add_argument(
        "--narrator-voice",
        help="Ghi đè giọng đọc người dẫn chuyện"
    )
    parser.add_argument(
        "--male-voice",
        help="Ghi đè giọng đọc nhân vật Nam"
    )
    parser.add_argument(
        "--female-voice",
        help="Ghi đè giọng đọc nhân vật Nữ"
    )
    parser.add_argument(
        "--package-name",
        help="Tên thư mục gói đề thi tùy chỉnh (mặc định lấy theo metadata hoặc title)"
    )
    parser.add_argument(
        "--no-package",
        action="store_true",
        help="Không tạo thư mục con gói đề thi, lưu thẳng vào output-dir"
    )
    parser.add_argument(
        "--pdf-exam",
        help="Đường dẫn file JSON đề thi giấy để biên soạn và xuất PDF vào cùng thư mục gói"
    )
    parser.add_argument(
        "--list-voices",
        action="store_true",
        help="Liệt kê danh sách các giọng đọc AI khả dụng (Việt, Nhật, Anh)"
    )

    args = parser.parse_args()

    # Nếu gọi lệnh --list-voices
    if args.list_voices:
        asyncio.run(print_available_voices())
        return

    # Kiểm tra kịch bản đầu vào
    if not args.script:
        parser.print_help()
        print("\n❌ LỖI: Vui lòng cung cấp đường dẫn file kịch bản JSON (hoặc dùng --list-voices để xem giọng đọc).")
        sys.exit(1)

    if not os.path.exists(args.script):
        print(f"❌ LỖI: Không tìm thấy file kịch bản tại '{args.script}'")
        sys.exit(1)

    try:
        with open(args.script, "r", encoding="utf-8") as f:
            script_data = json.load(f)
    except Exception as e:
        print(f"❌ LỖI: Không thể đọc file JSON '{args.script}': {e}")
        sys.exit(1)

    # Đóng gói các tham số ghi đè từ CLI
    overrides = {}
    if args.package_name:
        overrides["package_name"] = args.package_name
    if args.lang:
        overrides["language"] = args.lang
    if args.speed:
        overrides["speed"] = args.speed
    if args.pitch:
        overrides["pitch"] = args.pitch
    if args.mode:
        overrides["output_mode"] = args.mode
    if args.pause_think is not None:
        overrides["pause_thinking"] = args.pause_think
    if args.narrator_voice:
        overrides["narrator_voice"] = args.narrator_voice
    if args.male_voice:
        overrides["male_voice"] = args.male_voice
    if args.female_voice:
        overrides["female_voice"] = args.female_voice

    # Khởi tạo và chạy generator
    generator = AudioExamGenerator(script_data, global_overrides=overrides)
    manifest = asyncio.run(generator.generate(output_dir=args.output_dir, package=not args.no_package))

    # Nếu có yêu cầu xuất kèm đề thi giấy PDF
    if args.pdf_exam:
        pdf_json_path = os.path.abspath(args.pdf_exam)
        if os.path.exists(pdf_json_path):
            print(f"\n[INFO] Đang nạp và biên soạn kèm đề thi in ấn PDF: {pdf_json_path}...")
            with open(pdf_json_path, "r", encoding="utf-8") as f_pdf:
                pdf_exam_data = json.load(f_pdf)
            from doc_tools.exam_generator import ExamGenerator
            pdf_gen = ExamGenerator(pdf_exam_data)
            # Xuất trực tiếp vào package_directory của audio vừa tạo
            pkg_dir = manifest.get("package_directory") or args.output_dir
            res_pdf = pdf_gen.generate(output_dir=pkg_dir, package=False)
            print(f"[SUCCESS] Đã tạo thành công file ĐỀ THI (PDF) trong cùng thư mục: {res_pdf}")
        else:
            print(f"[WARNING] Không tìm thấy file đề thi PDF: {pdf_json_path}")


if __name__ == "__main__":
    main()
