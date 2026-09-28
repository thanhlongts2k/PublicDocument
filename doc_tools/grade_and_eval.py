"""
Module: grade_and_eval.py
Tự động phân tích và chấm điểm danh sách câu trả lời của học viên từ tin nhắn chat thô.
Ví dụ đầu vào: "kết quả đề tổng hợp tuần 1: 1d 2b 3a 4c 5a..."
"""

import os
import re
import json
from typing import Dict, Any, List, Tuple

KEYS_FILE = os.path.join(os.path.dirname(__file__), "bank", "exam_keys.json")

def parse_user_answers(raw_text: str) -> Dict[int, str]:
    """
    Phân tích chuỗi đáp án học viên gửi dạng:
    'kết quả đề tổng hợp tuần 1: 1d 2b 3a 4c...' hoặc '1. D, 2. B...'
    """
    answers = {}

    # Nếu có dấu hai chấm phân tách tiêu đề, ưu tiên lấy phần sau dấu hai chấm
    if ":" in raw_text:
        parts = raw_text.split(":", 1)
        # Kiểm tra xem phần sau dấu hai chấm có chứa nhiều đáp án không
        if re.search(r'\d+[a-zA-Z]', parts[1]) or re.search(r'[a-zA-Z]', parts[1]):
            text_to_parse = parts[1]
        else:
            text_to_parse = raw_text
    else:
        text_to_parse = raw_text

    # Tìm mẫu: Số thứ tự + chữ cái đáp án: 1d, 1b, 1-d, 1:d, 1.d, câu 1 d, 1 D
    pattern = r'(?:câu\s*)?(\d{1,3})[\s.:=/-]*([a-dA-D1-4])(?![a-zA-Z0-9])'
    matches = re.findall(pattern, text_to_parse, re.IGNORECASE)
    for q_num_str, ans in matches:
        q_num = int(q_num_str)
        answers[q_num] = ans.upper()

    # Nếu không tìm thấy dạng 1d 2b, thử tách danh sách chữ cái liên tiếp
    if not answers:
        tokens = re.split(r'[\s,;]+', text_to_parse.strip())
        valid_letters = [t.upper() for t in tokens if t.upper() in ["A", "B", "C", "D", "1", "2", "3", "4"]]
        if len(valid_letters) >= 3:
            for idx, ans in enumerate(valid_letters):
                answers[idx + 1] = ans

    return answers

def grade_answers(exam_code: str, student_answers: Dict[int, str]) -> Dict[str, Any]:
    """
    Chấm điểm dựa trên mã đề thi và danh sách đáp án học viên gửi.
    """
    if not os.path.exists(KEYS_FILE):
        raise FileNotFoundError(f"Không tìm thấy file đáp án: {KEYS_FILE}")

    with open(KEYS_FILE, "r", encoding="utf-8") as f:
        all_keys = json.load(f)

    # Tìm mã đề tương ứng (hỗ trợ tìm kiếm linh hoạt)
    matched_key_data = None
    if exam_code in all_keys:
        matched_key_data = all_keys[exam_code]
    else:
        for code, data in all_keys.items():
            if exam_code.lower() in code.lower() or code.lower() in exam_code.lower():
                matched_key_data = data
                break

    if not matched_key_data:
        # Mặc định lấy W01_60Q nếu có từ khóa tuần 1 / w01
        if "1" in exam_code or "tuần 1" in exam_code.lower() or "w01" in exam_code.lower():
            matched_key_data = all_keys.get("W01_60Q")
        else:
            raise ValueError(f"Chưa có đáp án chuẩn cho mã đề: '{exam_code}'. Danh sách có sẵn: {list(all_keys.keys())}")

    keys = matched_key_data["keys"]
    total_q = matched_key_data.get("total_questions", len(keys))

    correct_count = 0
    wrong_count = 0
    results_list = []
    wrong_questions = []

    for i in range(1, total_q + 1):
        str_i = str(i)
        correct_ans = keys.get(str_i, "")
        student_ans = student_answers.get(i, "Chưa làm")

        is_correct = (student_ans == correct_ans)
        if is_correct:
            correct_count += 1
        else:
            wrong_count += 1
            wrong_questions.append({
                "question_number": i,
                "student_choice": student_ans,
                "correct_answer": correct_ans
            })

        results_list.append({
            "question_number": i,
            "student_choice": student_ans,
            "correct_answer": correct_ans,
            "is_correct": is_correct
        })

    score_pct = round((correct_count / total_q) * 100, 1) if total_q > 0 else 0

    return {
        "exam_code": matched_key_data.get("exam_code", exam_code),
        "exam_title": matched_key_data.get("title", ""),
        "total_questions": total_q,
        "answered_count": len(student_answers),
        "correct_count": correct_count,
        "wrong_count": wrong_count,
        "score_percentage": score_pct,
        "score_str": f"{correct_count} / {total_q} ({score_pct}%)",
        "wrong_questions": wrong_questions,
        "results_list": results_list
    }

if __name__ == "__main__":
    test_str = "kết quả đề tổng hợp tuần 1: 1d 2b 3a 4c 5a 6a 7a 8a 9a 10a 21a 22a 23c"
    parsed = parse_user_answers(test_str)
    print("Parsed:", parsed)
    graded = grade_answers("W01_60Q", parsed)
    print("Score:", graded["score_str"])
    print("Wrong:", len(graded["wrong_questions"]))
