# -*- coding: utf-8 -*-
import os
import sys
import json
import re
import time
import subprocess
import tempfile
import imageio_ffmpeg
from gtts import gTTS
import translators as ts

FFMPEG_BIN = imageio_ffmpeg.get_ffmpeg_exe()

def clean_hallucination(text: str) -> str:
    """Loại bỏ hiện tượng Whisper lặp từ bất tận khi gặp khoảng lặng."""
    text = text.strip()
    # Loại bỏ cụm 2-25 ký tự bị lặp từ 3 lần trở lên
    pattern = re.compile(r'(.{2,25}?)\1{2,}')
    cleaned = pattern.sub(r'\1', text)
    # Nếu lặp lại tiếp
    cleaned = pattern.sub(r'\1', cleaned)
    return cleaned.strip()

def merge_segments(raw_segments):
    merged = []
    curr = None

    for seg in raw_segments:
        text = clean_hallucination(seg['ja'])
        if not text:
            continue
        
        # Bỏ qua các câu vô nghĩa do Whisper sinh ngẫu nhiên khi tĩnh
        if len(text) < 2 and text in ['はい', 'えー', 'あ', 'ん']:
            continue
            
        if not curr:
            curr = {
                'start': seg['start'],
                'end': seg['end'],
                'ja': text
            }
            continue
        
        pause = seg['start'] - curr['end']
        ends_punct = curr['ja'].endswith(('。', '？', '?', '！', '!', 'ね。', 'よ。'))
        
        if pause < 1.0 and not ends_punct and len(curr['ja']) < 90:
            curr['end'] = seg['end']
            curr['ja'] += text
        else:
            merged.append(curr)
            curr = {
                'start': seg['start'],
                'end': seg['end'],
                'ja': text
            }

    if curr:
        merged.append(curr)

    return merged

def translate_ja_to_vi(text: str) -> str:
    """Dịch tiếng Nhật sang tiếng Việt với cơ chế fallback thông minh."""
    text = text.strip()
    if not text:
        return ""
        
    # Thử Bing
    try:
        res = ts.translate_text(text, from_language='ja', to_language='vi', translator='bing')
        if res and res.strip():
            return res.strip()
    except Exception as e:
        pass
        
    # Thử MyMemory
    try:
        from deep_translator import MyMemoryTranslator
        res = MyMemoryTranslator(source='ja-JP', target='vi-VN').translate(text)
        if res and res.strip():
            return res.strip()
    except Exception as e:
        pass
        
    # Thử Google qua deep_translator nếu được
    try:
        from deep_translator import GoogleTranslator
        res = GoogleTranslator(source='ja', target='vi').translate(text)
        if res and res.strip():
            return res.strip()
    except Exception as e:
        pass

    return text

def format_time(seconds: float) -> str:
    m = int(seconds) // 60
    s = int(seconds) % 60
    return f"{m:02d}:{s:02d}"

def process_file_1():
    base_dir = r"D:\AgentAI\PublicDocument\Translate"
    segments_json = os.path.join(base_dir, "Duong_3_Thang_2_5_segments.json")
    bilingual_json = os.path.join(base_dir, "Duong_3_Thang_2_5_bilingual.json")
    bilingual_txt = os.path.join(base_dir, "Duong_3_Thang_2_5_bilingual.txt")
    output_mp3 = os.path.join(base_dir, "Duong_3_Thang_2_5_bilingual.mp3")

    print(f"=== BẮT ĐẦU XỬ LÝ VĂN BẢN VÀ DỊCH THUẬT PHẦN 1 ===", flush=True)
    with open(segments_json, "r", encoding="utf-8") as f:
        raw_segments = json.load(f)

    merged = merge_segments(raw_segments)
    print(f"Từ {len(raw_segments)} đoạn thô -> gộp thành {len(merged)} câu hoàn chỉnh.", flush=True)

    translated_list = []
    print("Đang dịch từng câu tiếng Nhật sang tiếng Việt...", flush=True)
    for idx, item in enumerate(merged, 1):
        ja_text = item['ja']
        vi_text = translate_ja_to_vi(ja_text)
        item['id'] = idx
        item['vi'] = vi_text
        translated_list.append(item)
        if idx % 5 == 0 or idx == len(merged):
            print(f"  [{idx}/{len(merged)}] [{format_time(item['start'])}] JA: {ja_text[:30]}... -> VI: {vi_text[:30]}...", flush=True)
        time.sleep(0.1) # Tránh dồn dập request

    with open(bilingual_json, "w", encoding="utf-8") as f:
        json.dump(translated_list, f, ensure_ascii=False, indent=2)

    # Xuất file text song ngữ
    lines = [
        "================================================================================",
        "BIÊN BẢN CUỘC HỌP TIẾNG NHẬT - BẢN DỊCH SONG NGỮ (NHẬT - VIỆT)",
        "Tệp âm thanh gốc: Duong_3_Thang_2_5.m4a (Thời lượng: ~13 phút 35 giây)",
        f"Tổng số phân đoạn phát biểu: {len(translated_list)}",
        "================================================================================",
        ""
    ]
    for item in translated_list:
        t_str = f"[{format_time(item['start'])} - {format_time(item['end'])}]"
        lines.append(t_str)
        lines.append(f"JA: {item['ja']}")
        lines.append(f"VI: {item['vi']}")
        lines.append("")

    with open(bilingual_txt, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Đã xuất file text song ngữ tại: {bilingual_txt}", flush=True)

    # Convert thành MP3
    print(f"=== BẮT ĐẦU TỔNG HỢP ÂM THANH MP3 (JA -> VI) CHO PHẦN 1 ===", flush=True)
    temp_dir = tempfile.mkdtemp(prefix="audio_part1_")
    concat_list_path = os.path.join(temp_dir, "concat.txt")
    
    # Tạo file silence 0.5s và 1.0s
    silence_05 = os.path.join(temp_dir, "silence_05.mp3")
    cmd_sil = [FFMPEG_BIN, "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", "0.5", "-q:a", "5", silence_05]
    subprocess.run(cmd_sil, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    silence_10 = os.path.join(temp_dir, "silence_10.mp3")
    cmd_sil = [FFMPEG_BIN, "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", "1.0", "-q:a", "5", silence_10]
    subprocess.run(cmd_sil, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    file_entries = []
    total = len(translated_list)
    for idx, item in enumerate(translated_list, 1):
        ja_file = os.path.join(temp_dir, f"seg_{idx:03d}_ja.mp3")
        vi_file = os.path.join(temp_dir, f"seg_{idx:03d}_vi.mp3")
        
        # Sinh JA
        try:
            tts_ja = gTTS(text=item['ja'], lang='ja')
            tts_ja.save(ja_file)
            file_entries.append(ja_file)
            file_entries.append(silence_05)
        except Exception as e:
            print(f"Lỗi TTS JA câu {idx}: {e}", flush=True)

        # Sinh VI
        try:
            tts_vi = gTTS(text=item['vi'], lang='vi')
            tts_vi.save(vi_file)
            file_entries.append(vi_file)
            file_entries.append(silence_10)
        except Exception as e:
            print(f"Lỗi TTS VI câu {idx}: {e}", flush=True)

        if idx % 5 == 0 or idx == total:
            print(f"  -> Đã tổng hợp audio [{idx}/{total}] câu...", flush=True)

    # Ghi file concat
    with open(concat_list_path, "w", encoding="utf-8") as f:
        for fpath in file_entries:
            clean_path = fpath.replace("\\", "/")
            f.write(f"file '{clean_path}'\n")

    print("Đang nối toàn bộ các đoạn âm thanh thành file MP3 hoàn chỉnh...", flush=True)
    cmd_concat = [
        FFMPEG_BIN, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list_path,
        "-c:a", "libmp3lame",
        "-b:a", "128k",
        output_mp3
    ]
    subprocess.run(cmd_concat, check=True)
    size_mb = os.path.getsize(output_mp3) / (1024 * 1024)
    print(f"=== XUẤT FILE MP3 PHẦN 1 THÀNH CÔNG: {output_mp3} ({size_mb:.2f} MB) ===", flush=True)

    # Dọn dẹp temp
    for root, dirs, files in os.walk(temp_dir, topdown=False):
        for f in files: os.remove(os.path.join(root, f))
        for d in dirs: os.rmdir(os.path.join(root, d))
    os.rmdir(temp_dir)

if __name__ == "__main__":
    process_file_1()
