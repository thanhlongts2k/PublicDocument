# -*- coding: utf-8 -*-
import os
import sys
import json
import re
import time
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
import imageio_ffmpeg
from gtts import gTTS
import translators as ts

FFMPEG_BIN = imageio_ffmpeg.get_ffmpeg_exe()
BASE_DIR = r"D:\AgentAI\PublicDocument\Translate"

def clean_hallucination(text: str) -> str:
    """Loại bỏ hiện tượng Whisper lặp từ bất tận khi gặp khoảng lặng."""
    text = text.strip()
    pattern = re.compile(r'(.{2,25}?)\1{2,}')
    cleaned = pattern.sub(r'\1', text)
    cleaned = pattern.sub(r'\1', cleaned)
    return cleaned.strip()

def merge_segments(raw_segments):
    merged = []
    curr = None

    for seg in raw_segments:
        text = clean_hallucination(seg['ja'])
        if not text:
            continue
        
        # Bỏ qua các âm phụ ngắn vô nghĩa khi tĩnh
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

def translate_single_text(text: str) -> str:
    """Dịch tiếng Nhật sang tiếng Việt với cơ chế fallback tự động."""
    text = text.strip()
    if not text:
        return ""
    
    # Danh sách các engine dịch dự phòng
    engines = ['bing', 'alibaba', 'google', 'myMemory']
    for engine in engines:
        try:
            res = ts.translate_text(text, from_language='ja', to_language='vi', translator=engine)
            if res and res.strip():
                return res.strip()
        except Exception:
            continue

    # Fallback deep_translator MyMemory
    try:
        from deep_translator import MyMemoryTranslator
        res = MyMemoryTranslator(source='ja-JP', target='vi-VN').translate(text)
        if res and res.strip():
            return res.strip()
    except Exception:
        pass

    return text

def format_time(seconds: float) -> str:
    m = int(seconds) // 60
    s = int(seconds) % 60
    return f"{m:02d}:{s:02d}"

def synthesize_audio_task(text: str, lang: str, out_path: str, max_retries: int = 3):
    """Tạo audio mp3 qua gTTS với retry."""
    if os.path.exists(out_path) and os.path.getsize(out_path) > 200:
        return True
    for attempt in range(max_retries):
        try:
            tts = gTTS(text=text, lang=lang)
            tts.save(out_path)
            if os.path.exists(out_path) and os.path.getsize(out_path) > 200:
                return True
        except Exception as e:
            time.sleep(0.5 * (attempt + 1))
    return False

def process_file_2():
    segments_json = os.path.join(BASE_DIR, "Duong_3_Thang_2_6_segments.json")
    bilingual_json = os.path.join(BASE_DIR, "Duong_3_Thang_2_6_bilingual.json")
    bilingual_txt = os.path.join(BASE_DIR, "Duong_3_Thang_2_6_bilingual.txt")
    output_mp3 = os.path.join(BASE_DIR, "Duong_3_Thang_2_6_bilingual.mp3")
    cache_dir = os.path.join(BASE_DIR, "audio_cache_part2")
    os.makedirs(cache_dir, exist_ok=True)

    print(f"=== BẮT ĐẦU XỬ LÝ VĂN BẢN VÀ DỊCH THUẬT PHẦN 2 ===", flush=True)
    if not os.path.exists(segments_json):
        print(f"LỖI: Chưa tìm thấy tệp {segments_json}!", flush=True)
        return

    with open(segments_json, "r", encoding="utf-8") as f:
        raw_segments = json.load(f)

    merged = merge_segments(raw_segments)
    total_items = len(merged)
    print(f"Từ {len(raw_segments)} đoạn thô -> gộp thành {total_items} câu phát biểu.", flush=True)

    # 1. DỊCH THUẬT SONG SONG
    translated_map = {}
    if os.path.exists(bilingual_json):
        try:
            with open(bilingual_json, "r", encoding="utf-8") as f:
                old_data = json.load(f)
                for item in old_data:
                    if 'ja' in item and 'vi' in item and item['vi']:
                        translated_map[item['ja']] = item['vi']
            print(f"Đã nạp {len(translated_map)} câu dịch từ cache.", flush=True)
        except Exception:
            pass

    items_to_translate = [item for item in merged if item['ja'] not in translated_map]
    print(f"Đang tiến hành dịch {len(items_to_translate)} câu với đa luồng...", flush=True)

    def do_trans(idx_item):
        idx, item = idx_item
        vi = translate_single_text(item['ja'])
        return idx, item['ja'], vi

    if items_to_translate:
        with ThreadPoolExecutor(max_workers=6) as executor:
            futures = [executor.submit(do_trans, (i, it)) for i, it in enumerate(items_to_translate)]
            completed = 0
            for future in as_completed(futures):
                try:
                    _, ja, vi = future.result()
                    translated_map[ja] = vi
                except Exception as e:
                    pass
                completed += 1
                if completed % 25 == 0 or completed == len(items_to_translate):
                    print(f"  -> Đã dịch {completed}/{len(items_to_translate)} câu...", flush=True)

    # Tạo danh sách hoàn chỉnh
    final_list = []
    for idx, item in enumerate(merged, 1):
        vi_trans = translated_map.get(item['ja'], item['ja'])
        final_list.append({
            'id': idx,
            'start': item['start'],
            'end': item['end'],
            'ja': item['ja'],
            'vi': vi_trans
        })

    with open(bilingual_json, "w", encoding="utf-8") as f:
        json.dump(final_list, f, ensure_ascii=False, indent=2)

    # 2. XUẤT TỆP VĂN BẢN SONG NGỮ
    lines = [
        "================================================================================",
        "BIÊN BẢN CUỘC HỌP TIẾNG NHẬT - BẢN DỊCH SONG NGỮ (NHẬT - VIỆT)",
        "Tệp âm thanh gốc: Duong_3_Thang_2_6.m4a (Thời lượng: ~51 phút 28 giây)",
        f"Tổng số phân đoạn phát biểu: {len(final_list)}",
        "================================================================================",
        ""
    ]
    for item in final_list:
        t_str = f"[{format_time(item['start'])} - {format_time(item['end'])}]"
        lines.append(t_str)
        lines.append(f"JA: {item['ja']}")
        lines.append(f"VI: {item['vi']}")
        lines.append("")

    with open(bilingual_txt, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Đã xuất file text song ngữ tại: {bilingual_txt}", flush=True)

    # 3. TỔNG HỢP ÂM THANH MP3 (JA -> SILENCE 0.5s -> VI -> SILENCE 1.0s)
    print(f"=== BẮT ĐẦU TỔNG HỢP ÂM THANH MP3 (JA -> VI) CHO PHẦN 2 ===", flush=True)
    silence_05 = os.path.join(cache_dir, "silence_05.mp3")
    if not os.path.exists(silence_05):
        cmd_sil = [FFMPEG_BIN, "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", "0.5", "-q:a", "5", silence_05]
        subprocess.run(cmd_sil, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    silence_10 = os.path.join(cache_dir, "silence_10.mp3")
    if not os.path.exists(silence_10):
        cmd_sil = [FFMPEG_BIN, "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", "1.0", "-q:a", "5", silence_10]
        subprocess.run(cmd_sil, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    tts_tasks = []
    for item in final_list:
        idx = item['id']
        ja_file = os.path.join(cache_dir, f"seg_{idx:04d}_ja.mp3")
        vi_file = os.path.join(cache_dir, f"seg_{idx:04d}_vi.mp3")
        tts_tasks.append((item['ja'], 'ja', ja_file))
        tts_tasks.append((item['vi'], 'vi', vi_file))

    print(f"Đang sinh {len(tts_tasks)} đoạn audio qua gTTS với đa luồng...", flush=True)
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(synthesize_audio_task, text, lang, path) for text, lang, path in tts_tasks]
        done_count = 0
        for future in as_completed(futures):
            done_count += 1
            if done_count % 50 == 0 or done_count == len(tts_tasks):
                print(f"  -> Đã sinh {done_count}/{len(tts_tasks)} tệp audio...", flush=True)

    # 4. GHÉP NỐI CONCAT
    concat_list_path = os.path.join(cache_dir, "concat.txt")
    file_entries = []
    for item in final_list:
        idx = item['id']
        ja_file = os.path.join(cache_dir, f"seg_{idx:04d}_ja.mp3")
        vi_file = os.path.join(cache_dir, f"seg_{idx:04d}_vi.mp3")
        if os.path.exists(ja_file):
            file_entries.append(ja_file)
            file_entries.append(silence_05)
        if os.path.exists(vi_file):
            file_entries.append(vi_file)
            file_entries.append(silence_10)

    with open(concat_list_path, "w", encoding="utf-8") as f:
        for fpath in file_entries:
            clean_path = fpath.replace("\\", "/")
            f.write(f"file '{clean_path}'\n")

    print(f"Đang nối {len(file_entries)} đoạn âm thanh thành file MP3 hoàn chỉnh...", flush=True)
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
    print(f"=== XUẤT FILE MP3 PHẦN 2 THÀNH CÔNG: {output_mp3} ({size_mb:.2f} MB) ===", flush=True)

if __name__ == "__main__":
    process_file_2()
