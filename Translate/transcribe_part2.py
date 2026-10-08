# -*- coding: utf-8 -*-
import os
import sys
import json
import time
from faster_whisper import WhisperModel

def main():
    audio_path = r"D:\AgentAI\PublicDocument\Translate\Duong_3_Thang_2_6.m4a"
    json_out = r"D:\AgentAI\PublicDocument\Translate\Duong_3_Thang_2_6_segments.json"
    
    print(f"=== BẮT ĐẦU QUÉT FILE 2: {os.path.basename(audio_path)} ===", flush=True)
    t0 = time.time()
    print("Khởi tạo Whisper Model 'base' (CPU int8)...", flush=True)
    model = WhisperModel('base', device='cpu', compute_type='int8')
    print(f"Model đã nạp xong trong {time.time()-t0:.2f}s", flush=True)
    
    t_start = time.time()
    print("Đang nhận diện giọng nói tiếng Nhật (ASR)...", flush=True)
    segments, info = model.transcribe(
        audio_path,
        language='ja',
        beam_size=5,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=500)
    )
    print(f"Ngôn ngữ phát hiện: {info.language} ({info.language_probability*100:.1f}%), Thời lượng: {info.duration:.2f}s", flush=True)
    
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
        if len(data) % 25 == 0:
            print(f"  -> Đã quét {len(data)} đoạn ({seg.end:.1f}s / {info.duration:.1f}s - {seg.end/info.duration*100:.1f}%)...", flush=True)
            
    with open(json_out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"=== HOÀN TẤT FILE 2! Tổng số đoạn: {len(data)}, Thời gian xử lý: {time.time()-t_start:.2f}s ===", flush=True)
    print(f"Lưu kết quả tại: {json_out}", flush=True)

if __name__ == "__main__":
    main()
