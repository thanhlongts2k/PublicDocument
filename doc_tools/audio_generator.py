"""
audio_generator.py - Bộ công cụ tạo file âm thanh đề thi (.mp3) từ kịch bản có sẵn.
Hỗ trợ đa ngôn ngữ (Tiếng Nhật JLPT, Tiếng Việt, Tiếng Anh) với công nghệ AI Neural Voice.
Tùy biến 100%: tốc độ, cao độ, thời gian chờ, phân vai nhân vật, lặp lại đoạn nghe.
Đặc biệt: Xử lý khoảng lặng bằng encoder LAME MP3 chuẩn xác 100%, triệt tiêu hoàn toàn lỗi đọc 'break time'.
"""

import os
import sys
import json
import asyncio
from typing import Dict, List, Any, Optional

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import edge_tts

# Hỗ trợ nạp an toàn lameenc (tránh lỗi IDE cảnh báo unresolved module trên môi trường thiếu type stub)
try:
    import lameenc  # type: ignore
    HAVE_LAMEENC = True
except ImportError:
    lameenc = None  # type: ignore
    HAVE_LAMEENC = False


# Bảng giọng đọc chuẩn mặc định cho 3 ngôn ngữ mục tiêu
DEFAULT_VOICE_REGISTRY = {
    "vi-VN": {
        "narrator": "vi-VN-NamMinhNeural",  # Người dẫn chuyện (Nam - chuẩn, truyền cảm, trang trọng)
        "male": "vi-VN-NamMinhNeural",      # Nhân vật Nam
        "female": "vi-VN-HoaiMyNeural",     # Nhân vật Nữ (Nữ - nhẹ nhàng, tự nhiên)
        "default": "vi-VN-NamMinhNeural"
    },
    "ja-JP": {
        "narrator": "ja-JP-NanamiNeural",   # Người dẫn chuyện (Chuẩn Tokyo)
        "male": "ja-JP-KeitaNeural",        # Nhân vật Nam JLPT
        "female": "ja-JP-NanamiNeural",     # Nhân vật Nữ JLPT
        "default": "ja-JP-NanamiNeural"
    },
    "en-US": {
        "narrator": "en-US-JennyNeural",    # Người dẫn chuyện (Giọng chuẩn thi quốc tế)
        "male": "en-US-GuyNeural",          # Nhân vật Nam
        "female": "en-US-JennyNeural",      # Nhân vật Nữ
        "default": "en-US-JennyNeural"
    }
}

# Câu thông báo lặp lại đoạn nghe theo ngôn ngữ
REPEAT_ANNOUNCEMENTS = {
    "vi-VN": "Hãy lắng nghe lại một lần nữa.",
    "ja-JP": "もう一度聞きます。",
    "en-US": "Listen again."
}

# Frame MP3 im lặng chuẩn xác tuyệt đối (MPEG-2 Layer III, 24000 Hz, 48kbps, Mono, 144 bytes/frame)
# 1 frame = 576 mẫu PCM âm thanh = 0.024 giây (24ms). Biên độ âm thanh = 0 (tuyệt đối im lặng).
# Không phụ thuộc thư viện C ngoài, tương thích chuẩn 100% với định dạng đầu ra của Edge-TTS.
MP3_SILENCE_FRAME_24K_48KBPS = bytes.fromhex("fff364c47c0000034800000000" + "55" * 131)


def create_mp3_silence(seconds: float, sample_rate: int = 24000, bitrate: int = 48) -> bytes:
    """
    Tạo đoạn MP3 im lặng (pure PCM silence) chuẩn xác 100%.
    - Chuẩn 24000 Hz / 48 kbps (chuẩn của Edge-TTS): Dùng Pure MP3 Silence Frame trực tiếp cực nhanh,
      hoàn toàn không phụ thuộc thư viện C ngoài, triệt tiêu 100% lỗi đọc nhầm tag XML 'break time'.
    - Các tần số khác: Tự động dùng lameenc nếu có sẵn trên máy.
    """
    if seconds <= 0:
        return b""

    # 1. Tối ưu cho định dạng chuẩn Edge-TTS (24000 Hz, 48kbps Mono)
    if sample_rate == 24000 and bitrate == 48:
        num_frames = max(1, int(round(seconds / 0.024)))
        return MP3_SILENCE_FRAME_24K_48KBPS * num_frames

    # 2. Sử dụng lameenc nếu được cài đặt cho các cấu hình custom khác
    if HAVE_LAMEENC and lameenc is not None:
        try:
            num_samples = int(sample_rate * seconds)
            pcm_silence = b"\x00\x00" * num_samples
            encoder = lameenc.Encoder()
            encoder.set_channels(1)
            encoder.set_in_sample_rate(sample_rate)
            encoder.set_out_sample_rate(sample_rate)
            encoder.set_bit_rate(bitrate)
            encoder.set_quality(2)
            mp3_data = encoder.encode(pcm_silence)
            mp3_data += encoder.flush()
            return mp3_data
        except Exception:
            pass

    # 3. Fallback chuẩn frame
    num_frames = max(1, int(round(seconds / 0.024)))
    return MP3_SILENCE_FRAME_24K_48KBPS * num_frames


class AudioExamGenerator:
    """
    Trình khởi tạo âm thanh đề thi tự động từ cấu trúc kịch bản JSON.
    """

    def __init__(self, script_data: Dict[str, Any], global_overrides: Optional[Dict[str, Any]] = None):
        self.script = script_data
        self.overrides = global_overrides or {}
        
        # 1. Cấu hình ngôn ngữ (Language)
        self.language = self.overrides.get("language") or self.script.get("language", "vi-VN")
        
        # 2. Cấu hình giọng đọc (Voice Mapping)
        script_settings = self.script.get("settings", {})
        default_voices = DEFAULT_VOICE_REGISTRY.get(self.language, DEFAULT_VOICE_REGISTRY["vi-VN"])
        
        self.voice_map = {
            "narrator": self.overrides.get("narrator_voice") or script_settings.get("narrator_voice", default_voices["narrator"]),
            "male": self.overrides.get("male_voice") or script_settings.get("male_voice", default_voices["male"]),
            "female": self.overrides.get("female_voice") or script_settings.get("female_voice", default_voices["female"]),
            "default": default_voices["default"]
        }
        if "custom_voices" in script_settings:
            self.voice_map.update(script_settings["custom_voices"])
            
        # 3. Cấu hình tốc độ (Speed / Rate), Cao độ (Pitch), Âm lượng (Volume)
        self.rate = self.overrides.get("speed") or script_settings.get("rate", "+0%")
        self.pitch = self.overrides.get("pitch") or script_settings.get("pitch", "+0Hz")
        self.volume = self.overrides.get("volume") or script_settings.get("volume", "+0%")
        
        # 4. Cấu hình các khoảng chờ (Pauses in seconds)
        self.pause_after_intro = script_settings.get("pause_after_intro", 2.0)
        self.pause_after_instruction = script_settings.get("pause_after_instruction", 1.5)
        self.pause_between_dialogue = script_settings.get("pause_between_dialogue", 0.8)
        self.pause_before_question = script_settings.get("pause_before_question", 1.5)
        self.pause_repeat = script_settings.get("pause_repeat", 2.0)
        
        # Thời gian chờ suy nghĩ (làm bài): ưu tiên override -> script -> default 10s
        self.pause_thinking_default = (
            self.overrides.get("pause_thinking") 
            if self.overrides.get("pause_thinking") is not None 
            else script_settings.get("pause_thinking_default", 10.0)
        )
        self.pause_between_questions = script_settings.get("pause_between_questions", 3.0)
        
        # Chế độ xuất: 'combined' (file tổng duy nhất), 'split' (chia từng câu), 'both' (cả hai)
        self.output_mode = self.overrides.get("output_mode") or self.script.get("output_mode", "both")

        # Bộ nhớ cache lưu các đoạn im lặng đã render để dùng lại siêu tốc
        self._silence_cache: Dict[float, bytes] = {}

    def _resolve_voice(self, speaker_key: str, explicit_voice: Optional[str] = None, lang: Optional[str] = None) -> str:
        """
        Tìm voice tương ứng với vai nói, hỗ trợ kết hợp đa ngôn ngữ (Việt, Nhật, Anh) linh hoạt.
        """
        # 1. Nếu có voice chỉ định trực tiếp (ví dụ: 'ja-JP-NanamiNeural')
        if explicit_voice and explicit_voice.strip():
            return explicit_voice.strip()
            
        clean = (speaker_key or "default").strip()
        
        # 2. Nếu speaker_key chính là tên một voice AI đầy đủ
        if "Neural" in clean:
            return clean
            
        clean_lower = clean.lower()
        
        # 3. Hỗ trợ các từ khóa song ngữ nhanh (male_ja, female_ja, male_vi, female_vi, male_en, female_en...)
        multilang_shortcuts = {
            "male_vi": "vi-VN-NamMinhNeural",
            "female_vi": "vi-VN-HoaiMyNeural",
            "narrator_vi": "vi-VN-NamMinhNeural",
            "male_ja": "ja-JP-KeitaNeural",
            "female_ja": "ja-JP-NanamiNeural",
            "narrator_ja": "ja-JP-NanamiNeural",
            "male_en": "en-US-GuyNeural",
            "female_en": "en-US-JennyNeural",
            "narrator_en": "en-US-JennyNeural"
        }
        if clean_lower in multilang_shortcuts:
            return multilang_shortcuts[clean_lower]
            
        # 4. Nếu có chỉ định ngôn ngữ phụ cụ thể (lang = 'ja-JP', 'vi-VN', 'en-US')
        if lang and lang in DEFAULT_VOICE_REGISTRY:
            lang_voices = DEFAULT_VOICE_REGISTRY[lang]
            if clean_lower in ("man", "nam", "male"):
                return lang_voices["male"]
            if clean_lower in ("woman", "nu", "nữ", "female"):
                return lang_voices["female"]
            if clean_lower in ("narrator", "mc", "dan_chuyen", "nguoi_dan"):
                return lang_voices["narrator"]
            return lang_voices.get("default", lang_voices["narrator"])
            
        # 5. Tra cứu trong bảng voice_map mặc định của kịch bản
        if clean_lower in self.voice_map:
            return self.voice_map[clean_lower]
        if clean_lower in ("man", "nam", "male"):
            return self.voice_map["male"]
        if clean_lower in ("woman", "nu", "nữ", "female"):
            return self.voice_map["female"]
        if clean_lower in ("narrator", "mc", "dan_chuyen", "nguoi_dan"):
            return self.voice_map["narrator"]
            
        return self.voice_map.get("default", self.voice_map["narrator"])

    def _get_silence_bytes(self, seconds: float) -> bytes:
        """Lấy đoạn MP3 khoảng lặng tuyệt đối, cache trong RAM."""
        if seconds <= 0:
            return b""
        sec_key = round(seconds, 1)
        if sec_key not in self._silence_cache:
            self._silence_cache[sec_key] = create_mp3_silence(sec_key)
        return self._silence_cache[sec_key]

    async def _synthesize_text(self, text: str, voice: str, rate: Optional[str] = None, pitch: Optional[str] = None, max_retries: int = 4) -> bytes:
        """
        Tổng hợp chuỗi văn bản thuần túy thành âm thanh MP3.
        TUYỆT ĐỐI không chèn tag XML/SSML vào văn bản để tránh lỗi đọc thành lời.
        """
        clean_text = text.strip()
        if not clean_text:
            return b""
            
        rate_val = rate or self.rate
        pitch_val = pitch or self.pitch
        volume_val = self.volume
        
        for attempt in range(max_retries):
            try:
                comm = edge_tts.Communicate(
                    text=clean_text,
                    voice=voice,
                    rate=rate_val,
                    pitch=pitch_val,
                    volume=volume_val
                )
                audio_data = b""
                async for chunk in comm.stream():
                    if chunk["type"] == "audio":
                        audio_data += chunk["data"]
                if audio_data:
                    # Giãn cách 250ms giữa các lệnh gọi để duy trì kết nối ổn định
                    await asyncio.sleep(0.25)
                    return audio_data
            except Exception as e:
                wait_time = 1.0 * (attempt + 1)
                if attempt == max_retries - 1:
                    print(f"⚠️ Cảnh báo lỗi tổng hợp âm thanh (lần {attempt+1}/{max_retries}): {e}")
                    raise e
                await asyncio.sleep(wait_time)
        return b""

    async def _render_question_track(self, q_data: Dict[str, Any], q_index: int) -> bytes:
        """
        Render toàn bộ âm thanh của 1 câu hỏi thành mảng bytes MP3.
        Hỗ trợ kịch bản song ngữ kết hợp (ví dụ: Lời dẫn tiếng Việt + Hội thoại tiếng Nhật).
        """
        track_parts: List[bytes] = []
        narrator_voice = self._resolve_voice(
            "narrator",
            explicit_voice=q_data.get("narrator_voice"),
            lang=q_data.get("narrator_lang")
        )
        
        # 1. Tiêu đề câu hỏi (Ví dụ: "Câu hỏi số 1" / "第1問")
        q_title = q_data.get("title") or f"Câu hỏi số {q_index + 1}"
        if q_data.get("speak_title", True):
            t_bytes = await self._synthesize_text(q_title, narrator_voice)
            track_parts.append(t_bytes)
            track_parts.append(self._get_silence_bytes(1.0))
            
        # 2. Lời dẫn đề bài (Instruction)
        instruction = q_data.get("instruction", "")
        if instruction:
            ins_voice = self._resolve_voice(
                "narrator",
                explicit_voice=q_data.get("instruction_voice"),
                lang=q_data.get("instruction_lang")
            )
            ins_bytes = await self._synthesize_text(instruction, ins_voice)
            track_parts.append(ins_bytes)
            track_parts.append(self._get_silence_bytes(self.pause_after_instruction))
            
        # 3. Nội dung hội thoại (Dialogue) hoặc Đoạn văn đọc (Passage)
        repeat_count = q_data.get("repeat", 1)
        dialogue = q_data.get("dialogue", [])
        passage = q_data.get("passage")
        
        for r in range(repeat_count):
            if r > 0:
                ann_lang = q_data.get("repeat_lang", self.language)
                announcement = q_data.get("repeat_announcement") or REPEAT_ANNOUNCEMENTS.get(ann_lang, "Lắng nghe lại một lần nữa.")
                ann_voice = self._resolve_voice("narrator", explicit_voice=q_data.get("repeat_voice"), lang=ann_lang)
                ann_bytes = await self._synthesize_text(announcement, ann_voice)
                track_parts.append(self._get_silence_bytes(self.pause_repeat))
                track_parts.append(ann_bytes)
                track_parts.append(self._get_silence_bytes(1.2))
                
            if dialogue:
                for line in dialogue:
                    speaker = line.get("speaker", "default")
                    explicit_voice = line.get("voice")
                    line_lang = line.get("lang")
                    text = line.get("text", "")
                    line_rate = line.get("rate") or self.rate
                    line_pitch = line.get("pitch") or self.pitch
                    
                    voice = self._resolve_voice(speaker, explicit_voice=explicit_voice, lang=line_lang)
                    line_bytes = await self._synthesize_text(text, voice, rate=line_rate, pitch=line_pitch)
                    track_parts.append(line_bytes)
                    track_parts.append(self._get_silence_bytes(self.pause_between_dialogue))
            elif passage:
                speaker = q_data.get("speaker", "narrator")
                explicit_voice = q_data.get("passage_voice")
                passage_lang = q_data.get("passage_lang")
                voice = self._resolve_voice(speaker, explicit_voice=explicit_voice, lang=passage_lang)
                pass_bytes = await self._synthesize_text(passage, voice)
                track_parts.append(pass_bytes)
                track_parts.append(self._get_silence_bytes(self.pause_between_dialogue))
                
        # 4. Khoảng nghỉ trước câu hỏi
        track_parts.append(self._get_silence_bytes(self.pause_before_question))
        
        # 5. Câu hỏi chính (Question prompt)
        question_text = q_data.get("question", "")
        if question_text:
            q_voice = self._resolve_voice(
                "narrator",
                explicit_voice=q_data.get("question_voice"),
                lang=q_data.get("question_lang")
            )
            q_bytes = await self._synthesize_text(question_text, q_voice)
            track_parts.append(q_bytes)
            track_parts.append(self._get_silence_bytes(1.2))
            
        # 6. Đọc phương án trắc nghiệm A-B-C-D (nếu có yêu cầu)
        if q_data.get("read_options", False) and "options" in q_data:
            opt_voice = self._resolve_voice(
                "narrator",
                explicit_voice=q_data.get("options_voice"),
                lang=q_data.get("options_lang")
            )
            for opt in q_data["options"]:
                opt_bytes = await self._synthesize_text(opt, opt_voice)
                track_parts.append(opt_bytes)
                track_parts.append(self._get_silence_bytes(1.0))
                
        # 7. Khoảng lặng suy nghĩ / tô đáp án (Thinking Time)
        thinking_time = q_data.get("thinking_time", self.pause_thinking_default)
        if thinking_time > 0:
            track_parts.append(self._get_silence_bytes(thinking_time))
            
        return b"".join(track_parts)

    async def generate(self, output_dir: str = "output", package: bool = True) -> Dict[str, Any]:
        """
        Thực thi quy trình tạo âm thanh toàn bộ đề thi và xuất file MP3.
        Nếu package=True (mặc định), tự động gom file vào thư mục định danh chuẩn: output_dir/[safe_title]/
        """
        meta = self.script.get("metadata", {})
        custom_base = (
            self.overrides.get("package_name")
            or self.script.get("package_name")
            or meta.get("package_name")
            or meta.get("base_filename")
        )
        if custom_base:
            safe_title = "".join(c if c.isalnum() or c in ("-", "_") else "_" for c in custom_base).strip("_")
        elif meta and "program_code" in meta and "subject_code" in meta:
            exam_prog = meta.get("program_code", "EXAM")
            subject_code = meta.get("subject_code", "SUBJ")
            exam_type = meta.get("type_code", "DeLuyenTap")
            exam_code = meta.get("exam_code", "101")
            from datetime import datetime
            date_str = meta.get("date_code", datetime.now().strftime("%Y%m%d"))
            safe_title = f"{exam_prog}_{subject_code}_{exam_type}_{exam_code}_{date_str}"
        else:
            exam_title = self.script.get("title", "Audio_Exam").strip()
            safe_title = "".join(c if c.isalnum() or c in ("-", "_") else "_" for c in exam_title).strip("_")
            
        if not safe_title:
            safe_title = "Audio_Exam"

        exam_title = self.script.get("title", safe_title).strip()

        # Xác định thư mục lưu trữ: Gói đề thi vào folder riêng biệt theo format chuẩn
        norm_out = os.path.normpath(os.path.abspath(output_dir))
        if package and os.path.basename(norm_out) != safe_title:
            target_dir = os.path.join(norm_out, safe_title)
        else:
            target_dir = norm_out

        os.makedirs(target_dir, exist_ok=True)
            
        print(f"\n========================================================")
        print(f"🎧 BẮT ĐẦU TẠO ĐỀ THI ÂM THANH: {exam_title}")
        print(f"   - Thư mục gói đề: {target_dir}")
        print(f"   - Ngôn ngữ: {self.language}")
        print(f"   - Tốc độ: {self.rate} | Cao độ: {self.pitch}")
        print(f"   - Giọng dẫn chuyện: {self.voice_map['narrator']}")
        print(f"   - Giọng Nam: {self.voice_map['male']} | Giọng Nữ: {self.voice_map['female']}")
        print(f"   - Chế độ xuất: {self.output_mode}")
        print(f"========================================================\n")
        
        generated_files = []
        master_parts: List[bytes] = []
        
        # 1. Đoạn giới thiệu đầu bài thi (Intro)
        intro_text = self.script.get("intro")
        if intro_text:
            print("🔊 Đang xử lý: Lời giới thiệu mở đầu đề thi...")
            intro_bytes = await self._synthesize_text(intro_text, self.voice_map["narrator"])
            master_parts.append(intro_bytes)
            master_parts.append(self._get_silence_bytes(self.pause_after_intro))
            
        # 2. Xử lý từng câu hỏi
        questions = self.script.get("questions", [])
        total_q = len(questions)
        print(f"📋 Tổng số câu hỏi: {total_q}")
        
        # Thư mục chứa từng câu lẻ: 'tracks' bên trong thư mục gói
        split_dir = os.path.join(target_dir, "tracks")
        if self.output_mode in ("split", "both"):
            os.makedirs(split_dir, exist_ok=True)
            
        for i, q in enumerate(questions):
            q_id = q.get("id", i + 1)
            q_title = q.get("title") or f"Câu {q_id}"
            print(f"   [Câu {i+1}/{total_q}] Đang tổng hợp âm thanh: {q_title}...")
            
            q_audio_bytes = await self._render_question_track(q, i)
            
            # Lưu file tách riêng cho từng câu (nếu mode là split hoặc both)
            if self.output_mode in ("split", "both"):
                q_filename = f"Q{q_id:02d}_{safe_title}.mp3"
                q_path = os.path.join(split_dir, q_filename)
                with open(q_path, "wb") as f_q:
                    f_q.write(q_audio_bytes)
                generated_files.append(q_path)
                
            # Đưa vào file tổng master
            master_parts.append(q_audio_bytes)
            
            # Khoảng nghỉ giữa các câu hỏi
            if i < total_q - 1:
                master_parts.append(self._get_silence_bytes(self.pause_between_questions))
                
        # 3. Đoạn kết thúc bài thi (Outro)
        outro_text = self.script.get("outro")
        if outro_text:
            print("🔊 Đang xử lý: Lời kết thúc bài thi...")
            outro_bytes = await self._synthesize_text(outro_text, self.voice_map["narrator"])
            master_parts.append(self._get_silence_bytes(1.5))
            master_parts.append(outro_bytes)
            
        # 4. Xuất file tổng hợp (Master File)
        master_path = None
        if self.output_mode in ("combined", "both"):
            master_filename = f"{safe_title}_FULL.mp3"
            master_path = os.path.join(target_dir, master_filename)
            total_master_bytes = b"".join(master_parts)
            with open(master_path, "wb") as f_m:
                f_m.write(total_master_bytes)
            generated_files.insert(0, master_path)
            master_size_mb = len(total_master_bytes) / (1024 * 1024)
            print(f"\n✅ ĐÃ XUẤT FILE TỔNG HỢP: {master_path} ({master_size_mb:.2f} MB)")
            
        if self.output_mode in ("split", "both"):
            print(f"✅ ĐÃ XUẤT THƯ MỤC CÁC CÂU LẺ: {split_dir} ({total_q} files)")
            
        # 5. Xuất metadata JSON tóm tắt
        manifest = {
            "title": exam_title,
            "package_name": safe_title,
            "package_directory": target_dir,
            "language": self.language,
            "rate": self.rate,
            "pitch": self.pitch,
            "total_questions": total_q,
            "output_mode": self.output_mode,
            "master_file": master_path,
            "split_directory": split_dir if self.output_mode in ("split", "both") else None,
            "generated_files": generated_files
        }
        manifest_path = os.path.join(target_dir, f"{safe_title}_manifest.json")
        with open(manifest_path, "w", encoding="utf-8") as f_man:
            json.dump(manifest, f_man, ensure_ascii=False, indent=2)
            
        print(f"📄 Đã lưu thông tin kiểm tra tại: {manifest_path}\n")
        return manifest
