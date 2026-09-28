"""
Module: question_bank.py
Quản lý Ngân hàng Câu hỏi số hóa (Question Bank) và lịch sử lỗi sai của học viên.
Hỗ trợ lưu vết tự động (Auto-Ingestion) và trích xuất câu hỏi để ghép đề tổng hợp.
"""

import os
import json
import hashlib
from datetime import datetime
from typing import List, Dict, Optional, Any

BANK_DIR = os.path.join(os.path.dirname(__file__), "bank")
BANK_FILE = os.path.join(BANK_DIR, "question_bank.json")

class QuestionBank:
    def __init__(self, bank_path: str = BANK_FILE):
        self.bank_path = bank_path
        self.bank_dir = os.path.dirname(bank_path)
        os.makedirs(self.bank_dir, exist_ok=True)
        self.data: Dict[str, Any] = self._load()

    def _load(self) -> Dict[str, Any]:
        if os.path.exists(self.bank_path):
            try:
                with open(self.bank_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"[WARNING] Không thể đọc question_bank.json, khởi tạo mới: {e}")
        return {
            "version": "1.0",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "questions": {}
        }

    def save(self):
        self.data["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.bank_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def _generate_question_hash(self, question_text: str, options: List[str]) -> str:
        """Tạo mã băm MD5 duy nhất dựa trên nội dung câu hỏi và các lựa chọn"""
        raw = question_text.strip() + "".join(sorted([opt.strip() for opt in options]))
        return hashlib.md5(raw.encode("utf-8")).hexdigest()[:12]

    def add_or_update_question(self, q_item: Dict[str, Any], exam_code: Optional[str] = None, week: Optional[int] = None, level: str = "N3") -> str:
        """
        Thêm hoặc cập nhật một câu hỏi vào Bank.
        """
        q_text = q_item.get("question", "").strip()
        opts = q_item.get("options", [])
        if not q_text:
            return ""

        q_hash = self._generate_question_hash(q_text, opts)
        q_id = q_item.get("id") or f"Q_{level}_{q_hash}"

        now_str = datetime.now().strftime("%Y-%m-%d")

        if q_hash in self.data["questions"]:
            # Cập nhật lịch sử
            record = self.data["questions"][q_hash]
            if exam_code and exam_code not in record["history"]["exams"]:
                record["history"]["exams"].append(exam_code)
            if week and week not in record.get("weeks", []):
                record.setdefault("weeks", []).append(week)
            # Cập nhật tags nếu có mới
            for tag in q_item.get("tags", []):
                if tag not in record.get("tags", []):
                    record["tags"].append(tag)
        else:
            # Tạo bản ghi mới
            record = {
                "id": q_id,
                "hash": q_hash,
                "level": q_item.get("level", level),
                "weeks": [week] if week else q_item.get("weeks", []),
                "skill": q_item.get("skill", "general"),
                "type": q_item.get("type", "multiple_choice"),
                "star_parts": q_item.get("star_parts", []),
                "reading_passage": q_item.get("reading_passage", ""),
                "tags": q_item.get("tags", []),
                "question": q_text,
                "options": opts,
                "correct_answer": q_item.get("correct_answer", ""),
                "explanation": q_item.get("explanation", ""),
                "history": {
                    "first_added": now_str,
                    "exams": [exam_code] if exam_code else [],
                    "error_count": 0,
                    "failed_students": []
                }
            }
            self.data["questions"][q_hash] = record

        return q_hash

    def record_student_error(self, question_text: str, student_identifiers: List[str], correct_ans: str = "", explanation: str = ""):
        """
        Ghi nhận khi một học viên làm sai câu hỏi này.
        student_identifiers có thể gồm cả student_name ("Trần Văn Minh") và student_code ("TranVanMinh").
        """
        # Tìm câu hỏi theo text
        found_hash = None
        for q_hash, record in self.data["questions"].items():
            if record["question"].strip() == question_text.strip():
                found_hash = q_hash
                break

        if found_hash:
            rec = self.data["questions"][found_hash]
            rec["history"]["error_count"] += 1
            for s in student_identifiers:
                if s and s not in rec["history"]["failed_students"]:
                    rec["history"]["failed_students"].append(s)
            if correct_ans and not rec.get("correct_answer"):
                rec["correct_answer"] = correct_ans
            if explanation and not rec.get("explanation"):
                rec["explanation"] = explanation
        else:
            # Nếu câu hỏi chưa có trong bank (ví dụ từ bài tập bên ngoài)
            q_hash = hashlib.md5(question_text.strip().encode("utf-8")).hexdigest()[:12]
            rec = {
                "id": f"Q_ERROR_{q_hash}",
                "hash": q_hash,
                "level": "N3",
                "weeks": [],
                "skill": "error_log",
                "type": "multiple_choice",
                "star_parts": [],
                "reading_passage": "",
                "tags": ["from_evaluation"],
                "question": question_text.strip(),
                "options": [],
                "correct_answer": correct_ans,
                "explanation": explanation,
                "history": {
                    "first_added": datetime.now().strftime("%Y-%m-%d"),
                    "exams": [],
                    "error_count": 1,
                    "failed_students": [s for s in student_identifiers if s]
                }
            }
            self.data["questions"][q_hash] = rec

    def ingest_exam(self, exam_data: Dict[str, Any]) -> int:
        """
        Nạp toàn bộ câu hỏi từ 1 file đề thi vào Bank.
        Trả về số lượng câu hỏi được thêm/cập nhật.
        """
        meta = exam_data.get("metadata", {})
        exam_code = meta.get("exam_code", "UNKNOWN")
        level = meta.get("program_code", "N3")
        
        # Suy luận tuần từ subject_code hoặc title
        week = None
        code_str = (meta.get("subject_code", "") + meta.get("exam_title", "")).lower()
        if "tuan01" in code_str or "tuần 01" in code_str or "week01" in code_str or "w01" in code_str:
            week = 1
        elif "tuan02" in code_str or "tuần 02" in code_str or "w02" in code_str:
            week = 2

        count = 0
        for sec in exam_data.get("sections", []):
            sec_title = sec.get("title", "").lower()
            passage = sec.get("reading_passage", "")

            # Xác định skill
            if "từ vựng" in sec_title or "chữ hán" in sec_title or "moji" in sec_title or "goi" in sec_title:
                skill = "moji_goi"
            elif "ngữ pháp" in sec_title or "bunpou" in sec_title or "sao" in sec_title:
                skill = "bunpou"
            elif "đọc hiểu" in sec_title or "dokkai" in sec_title or passage:
                skill = "dokkai"
            else:
                skill = "general"

            for q in sec.get("questions", []):
                q_item = dict(q)
                q_item["skill"] = skill
                if passage and not q_item.get("reading_passage"):
                    q_item["reading_passage"] = passage
                self.add_or_update_question(q_item, exam_code=exam_code, week=week, level=level)
                count += 1

        self.save()
        return count

    def ingest_evaluation(self, eval_data: Dict[str, Any]) -> int:
        """
        Nạp dữ liệu từ file đánh giá: cập nhật các câu sai và nạp các câu Drill Exercises.
        """
        meta = eval_data.get("metadata", {})
        student_name = meta.get("student_name", "")
        student_code = meta.get("student_code", "")
        student_identifiers = [s for s in [student_name, student_code] if s]
        level = meta.get("subject_code", "N3")

        # 1. Ghi nhận các câu sai
        for item in eval_data.get("summary_results", []):
            if not item.get("is_correct", True):
                self.record_student_error(
                    question_text=item.get("question_content", ""),
                    student_identifiers=student_identifiers,
                    correct_ans=item.get("correct_answer", ""),
                    explanation=item.get("brief_explanation", "")
                )

        # 2. Nạp các câu Drill Exercises vào Bank
        drill_count = 0
        for drill in eval_data.get("drill_exercises", []):
            q_item = {
                "question": drill.get("question", ""),
                "options": drill.get("options", []),
                "type": "multiple_choice",
                "skill": "bunpou",
                "level": level,
                "tags": ["drill_exercise", "remedy"]
            }
            self.add_or_update_question(q_item, level=level)
            drill_count += 1

        self.save()
        return drill_count

    @staticmethod
    def _normalize_name(name: str) -> str:
        """Chuẩn hóa tên để so sánh (không phân biệt hoa thường, dấu tiếng Việt)"""
        import unicodedata
        s = name.lower().replace(" ", "").replace("_", "")
        nfkd = unicodedata.normalize('NFKD', s)
        return "".join([c for c in nfkd if not unicodedata.combining(c)])

    def _student_matches(self, query: str, failed_students: List[str]) -> bool:
        if not query:
            return True
        q_norm = self._normalize_name(query)
        for s in failed_students:
            s_norm = self._normalize_name(s)
            if q_norm in s_norm or s_norm in q_norm:
                return True
        return False

    def filter_questions(
        self,
        weeks: Optional[List[int]] = None,
        skills: Optional[List[str]] = None,
        tags: Optional[List[str]] = None,
        student_name: Optional[str] = None,
        only_errors: bool = False,
        limit: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Lọc danh sách câu hỏi theo các tiêu chí linh hoạt.
        """
        results = []
        for q_hash, rec in self.data["questions"].items():
            # Lọc theo tuần
            if weeks:
                q_weeks = rec.get("weeks", [])
                if not any(w in weeks for w in q_weeks):
                    continue

            # Lọc theo kỹ năng
            if skills:
                if rec.get("skill") not in skills:
                    continue

            # Lọc theo tags
            if tags:
                rec_tags = rec.get("tags", [])
                if not any(t in rec_tags for t in tags):
                    continue

            # Lọc câu sai
            if only_errors:
                if rec["history"]["error_count"] <= 0:
                    continue
                if student_name and not self._student_matches(student_name, rec["history"]["failed_students"]):
                    continue

            # Lọc theo học viên
            if student_name and not only_errors:
                if not self._student_matches(student_name, rec["history"]["failed_students"]):
                    continue

            results.append(rec)

        if limit and len(results) > limit:
            results = results[:limit]

        return results

    def get_stats(self) -> Dict[str, Any]:
        """Thống kê tổng quan về Ngân hàng câu hỏi"""
        total = len(self.data["questions"])
        by_skill = {}
        by_week = {}
        error_questions = 0

        for q in self.data["questions"].values():
            s = q.get("skill", "general")
            by_skill[s] = by_skill.get(s, 0) + 1

            for w in q.get("weeks", []):
                by_week[w] = by_week.get(w, 0) + 1

            if q["history"]["error_count"] > 0:
                error_questions += 1

        return {
            "total_questions": total,
            "by_skill": by_skill,
            "by_week": by_week,
            "questions_with_errors": error_questions,
            "last_updated": self.data.get("last_updated", "")
        }
