# -*- coding: utf-8 -*-
import os
import sys
import json
import time
from faster_whisper import WhisperModel

def main():
    audio_path = r"D:\AgentAI\PublicDocument\Translate\Duong_3_Thang_2_5.m4a"
    json_out = r"D:\AgentAI\PublicDocument\Translate\Duong_3_Thang_2_5_segments.json"
    
    print(f"=== BẮT ĐẦU QUÉT FILE 1: {os.path.basename(audio_path)} ===")
    t0 = time.time()
    print("Khởi tạo Whisper Model 'base' (CPU int8)...")
    model = WhisperModel('base', device='cpu', compute_type='int8')
    print(f"Model đã nạp xong trong {time.time()-t0:.2f}s")
    
    t_start = time.time()
    print("Đang nhận diện giọng nói tiếng Nhật (ASR)...")
    segments, info = model.transcribe(
        audio_path,
        language='ja',
        beam_size=5,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=500)
    )
    print(f"Ngôn ngữ phát hiện: {info.language} ({info.language_probability*100:.1f}%), Thời lượng: {info.duration:.2f}s")
    
    data = []
    for seg in segments:
        text = seg.text.strip()
        if not text:
            continue
        data.append({
            "id": len(data) + 1,
            "start": round(seg.start, 2),
            "end": round(seg.end, 2),
            "ja": text
        })
        if len(data) % 10 == 0:
            print(f"  -> Đã quét {len(data)} đoạn ({seg.end:.1f}s / {info.duration:.1f}s)...")
            
    with open(json_out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"=== HOÀN TẤT FILE 1! Tổng số đoạn: {len(data)}, Thời gian xử lý: {time.time()-t_start:.2f}s ===")
    print(f"Lưu kết quả tại: {json_out}")

if __name__ == "__main__":
    main()
