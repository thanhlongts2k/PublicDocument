# -*- coding: utf-8 -*-
"""
Script: build_exam_w01_de05.py
Tạo bộ dữ liệu Đề số 05 Tuần 1 (JLPT N3 - Tuần 01 - Đề 05).
Bao quát 4 kỹ năng: Từ vựng, Ngữ pháp, Đọc hiểu và Nghe hiểu Choukai (có tích hợp kịch bản Audio AI).
"""

import json
import os
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

exam_data = {
    "metadata": {
        "organization": "HỌC VIỆN NGÔN NGỮ QUỐC TẾ TOKYO - BAN KHẢO THÍ",
        "program": "CHIẾN LƯỢC TOÀN DIỆN CHINH PHỤC JLPT N3 (24 TUẦN)",
        "subject": "TIẾNG NHẬT TỔNG HỢP & NGHE HIỂU (TUẦN 01)",
        "exam_title": "ĐỀ THI LUYỆN TẬP TUẦN 01 - ĐỀ SỐ 05",
        "program_code": "JLPT_N3",
        "subject_code": "Tuan01",
        "type_code": "De05",
        "exam_code": "W01_De05",
        "date_code": "20260928",
        "package_name": "JLPT_N3_Tuan01_De05_20260928",
        "duration_minutes": 45,
        "total_questions": 25,
        "date": "28/09/2026"
    },
    "package_name": "JLPT_N3_Tuan01_De05_20260928",
    "instructions": [
        "1. Đề thi gồm 25 câu hỏi được biên soạn theo trọng tâm kiến thức Tuần 01: Từ vựng, Ngữ pháp, Đọc hiểu và Nghe hiểu.",
        "2. Thời gian làm bài là 45 phút. Mỗi câu chỉ có DUY NHẤT một đáp án đúng.",
        "3. Phần thi Nghe hiểu được tiếp nhận 100% qua file âm thanh. Thí sinh chú ý lắng nghe và đánh dấu vào PHIẾU TRẢ LỜI NHANH ở trang cuối.",
        "4. Tuyệt đối không sử dụng tài liệu, từ điển hay thiết bị điện tử trong phòng thi."
    ],
    "sections": [
        {
            "title": "PHẦN I: TỪ VỰNG & CHỮ HÁN (MONDAI 1 & 2 - CÂU 1 ĐẾN 8)",
            "description": "Hãy chọn phương án đúng nhất (A, B, C hoặc D) cho các câu hỏi từ vựng dưới đây:",
            "questions": [
                {
                    "question": "他人の立場への【配慮】を欠いた発言は慎むべきだ。",
                    "type": "multiple_choice",
                    "options": ["はいりょ", "ばいりょ", "はいろ", "ばいろ"]
                },
                {
                    "question": "両社は互いに譲り合い、ようやく【妥協】点を見出した。",
                    "type": "multiple_choice",
                    "options": ["だきょう", "たいきょう", "だこう", "たいこう"]
                },
                {
                    "question": "状況の変化に応じた適切な【措置】を講じる必要がある。",
                    "type": "multiple_choice",
                    "options": ["そち", "しょち", "さち", "そうち"]
                },
                {
                    "question": "お客様からのクレームに対しては【迅速】な対応が最も重要である。",
                    "type": "multiple_choice",
                    "options": ["じんそく", "しんそく", "じんぞく", "しんぞく"]
                },
                {
                    "question": "事故の再発を防ぐため、作業の【　　】をもう一度最初から見直した。",
                    "type": "multiple_choice",
                    "options": ["手順", "手法", "手段", "手際"]
                },
                {
                    "question": "現状の課題を正確に【　　】していなければ、正しい解決策は導き出せない。",
                    "type": "multiple_choice",
                    "options": ["把握", "掌握", "把持", "拘束"]
                },
                {
                    "question": "激しい運動を終えた直後、正常な呼吸を【　　】するのが難しかった。",
                    "type": "multiple_choice",
                    "options": ["維持", "継続", "保存", "保留"]
                },
                {
                    "question": "先輩たちの成功例に【　　】、新しいマーケティング手法を試してみた。",
                    "type": "multiple_choice",
                    "options": ["ならって", "なぞらえて", "かたどって", "そろえて"]
                }
            ]
        },
        {
            "title": "PHẦN II: NGỮ PHÁP THỰC CHIẾN (MONDAI 3 & 4 - CÂU 9 ĐẾN 18)",
            "description": "Hãy chọn đáp án đúng hoặc sắp xếp các cụm từ theo đúng trật tự ngữ pháp:",
            "questions": [
                {
                    "question": "当社の就業規則（　　）、今回の特別手当を支給いたします。",
                    "type": "multiple_choice",
                    "options": ["に基づいて", "を通して", "を契機に", "にしたがって"]
                },
                {
                    "question": "昨年の海外出張（　　）、彼は英会話の勉強を本格的に始めた。",
                    "type": "multiple_choice",
                    "options": ["を契機に", "に基づいて", "にかんして", "をもとに"]
                },
                {
                    "question": "新製品の開発計画（　　）詳しいご説明をさせていただきます。",
                    "type": "multiple_choice",
                    "options": ["に関して", "に対して", "にこたえて", "にそって"]
                },
                {
                    "question": "朝から少し熱（　　）で体がだるいので、今日は無理をせず早く寝よう。",
                    "type": "multiple_choice",
                    "options": ["気味", "っぽい", "がち", "だらけ"]
                },
                {
                    "question": "冬の時期は寒さのあまり、どうしても運動不足に（　　）になる。",
                    "type": "multiple_choice",
                    "options": ["なりがち", "なり気味", "っぽく", "だらけ"]
                },
                {
                    "question": "このスープは調味料が足りないのか、まるで水（　　）ね。",
                    "type": "multiple_choice",
                    "options": ["っぽい", "気味だ", "がちだ", "だらけだ"]
                },
                {
                    "question": "アンケート調査の （　）（　）（ ★ ）（　） 改善案を作成した。",
                    "type": "star_arrangement",
                    "star_parts": [
                        "1. に基づいて",
                        "2. 結果",
                        "3. 業務の",
                        "4. 社員からの"
                    ]
                },
                {
                    "question": "病気で入院した （　）（　）（ ★ ）（　） 健康管理に気をつかうようになった。",
                    "type": "star_arrangement",
                    "star_parts": [
                        "1. を契機に",
                        "2. 毎日の",
                        "3. 自分の",
                        "4. ことを"
                    ]
                },
                {
                    "question": "今回の不祥事 （　）（　）（ ★ ）（　） 記者会見が開かれた。",
                    "type": "star_arrangement",
                    "star_parts": [
                        "1. 説明を行う",
                        "2. 事実関係の",
                        "3. に関して",
                        "4. ために"
                    ]
                },
                {
                    "question": "彼の部屋の中は （　）（　）（ ★ ）（　） 掃除する気が起きない。",
                    "type": "star_arrangement",
                    "star_parts": [
                        "1. ゴミ",
                        "2. 散らかっていて",
                        "3. だらけで",
                        "4. ひどく"
                    ]
                }
            ]
        },
        {
            "title": "PHẦN III: ĐỌC HIỂU ĐOẢN VĂN (DOKKAI - CÂU 19 ĐẾN 21)",
            "description": "Đọc văn bản thông báo nội bộ dưới đây và trả lời các câu hỏi 19, 20, 21:",
            "questions": [
                {
                    "reading_passage": "【社内通知：テレワーク勤務ガイドラインの改定について】\n全社員へ\n総務部よりお知らせいたします。先月実施した全社アンケートの結果に基づいて、テレワーク勤務に関する規定を一部改定いたしました。\nこれまで週2日までとしていた在宅勤務の上限を、業務の進捗状況を適切に把握することを条件に、週3日まで拡大いたします。また、社員の健康維持への配慮として、長時間の連続作業を避けるための定期的な休憩取得を推奨します。本改定に関する詳細な手順につきましては、社内ポータルサイトの案内をご確認ください。",
                    "question": "テレワーク勤務の上限日数について、改定後はどうなりましたか。",
                    "type": "multiple_choice",
                    "options": [
                        "週2日から週3日へ拡大された",
                        "週3日から週2日へ減らされた",
                        "日数の上限が完全に撤廃された",
                        "条件なしで毎日在宅勤務が可能になった"
                    ]
                },
                {
                    "question": "テレワークの上限を拡大するための条件として、本文で挙げられているものはどれですか。",
                    "type": "multiple_choice",
                    "options": [
                        "業務の進捗状況を適切に把握すること",
                        "総務部に毎日出社して報告すること",
                        "アンケートに全員が回答すること",
                        "週に1回健康診断を受けること"
                    ]
                },
                {
                    "question": "改定に関する詳細な手順を確認するにはどうすればよいですか。",
                    "type": "multiple_choice",
                    "options": [
                        "社内ポータルサイトの案内を確認する",
                        "総務部へ直接電話で問い合わせる",
                        "全社アンケートに再度回答する",
                        "次回の全体会議で質問する"
                    ]
                }
            ]
        },
        {
            "title": "PHẦN IV: NGHE HIỂU PHẢN XẠ (CHOUKAI - CÂU 22 ĐẾN 25)",
            "description": "Lắng nghe băng âm thanh và chọn phương án trả lời đúng nhất (Zero-Script Rule: không in nội dung nghe trên đề):",
            "questions": [
                {
                    "question": "【問題１・課題理解】女の人はこれからまず何をしますか。",
                    "type": "multiple_choice",
                    "options": [
                        "1. 会議室のプロジェクターを点検する",
                        "2. 参加者名簿の変更箇所を修正する",
                        "3. 部長に資料の最終確認をもらう",
                        "4. 修正後の資料を印刷する"
                    ]
                },
                {
                    "question": "【問題２・課題理解】男の人は明日何を持参しなければなりませんか。",
                    "type": "multiple_choice",
                    "options": [
                        "1. 学生証と写真2枚",
                        "2. 受験票と筆記用具",
                        "3. 卒業証明書の原本",
                        "4. 健康保険証のコピー"
                    ]
                },
                {
                    "question": "【問題３・即時応答】（メモ：........................................................................）",
                    "type": "multiple_choice",
                    "options": [
                        "1. はい、すぐにお持ちいたします。",
                        "2. いいえ、まだ受け取っていません。",
                        "3. それなら、あちらに置いてあります。",
                        "4. いえ、結構でございます。"
                    ]
                },
                {
                    "question": "【問題４・即時応答】（メモ：........................................................................）",
                    "type": "multiple_choice",
                    "options": [
                        "1. ええ、少し熱気味でだるいんです。",
                        "2. いえ、全く忙しくありませんよ。",
                        "3. これから病院へ見学に行きます。",
                        "4. はい、とても元気そうですね。"
                    ]
                }
            ]
        }
    ],
    "audio": {
        "title": "JLPT_N3_Tuan01_De05_20260928",
        "package_name": "JLPT_N3_Tuan01_De05_20260928",
        "language": "ja-JP",
        "output_mode": "both",
        "settings": {
            "narrator_voice": "ja-JP-NanamiNeural",
            "male_voice": "ja-JP-KeitaNeural",
            "female_voice": "ja-JP-NanamiNeural",
            "rate": "+0%",
            "pitch": "+0Hz",
            "pause_after_intro": 2.0,
            "pause_after_instruction": 1.5,
            "pause_between_dialogue": 0.8,
            "pause_before_question": 1.5,
            "pause_thinking_default": 12.0,
            "pause_between_questions": 3.0
        },
        "intro": "日本語能力試験、N3、第1週実戦テスト、第5回聴解試験。これから聴解試験を始めます。問題用紙を開けてください。問題用紙にメモをとっても構いません。問題用紙の１から４の中から、最もよいものを一つ選んでください。",
        "questions": [
            {
                "id": 22,
                "title": "第1問（通し番号22）",
                "instruction": "会社で男の人と女の人が話しています。女の人はこれからまず何をしますか。",
                "dialogue": [
                    {
                        "speaker": "male",
                        "text": "田中さん、明日の役員会議の資料、さっき急な変更が入ったよ。"
                    },
                    {
                        "speaker": "female",
                        "text": "えっ、もう印刷を始めてしまったんですが、どうしましょう。"
                    },
                    {
                        "speaker": "male",
                        "text": "まだ5部しか刷ってないなら大丈夫。まず名簿の変更箇所をデータ上で直して、それから印刷をやり直してほしいんだ。"
                    },
                    {
                        "speaker": "female",
                        "text": "わかりました。すぐに名簿の修正データを直してきます。"
                    },
                    {
                        "speaker": "male",
                        "text": "頼むね。会議室のプロジェクター点検は僕がやっておくから。"
                    }
                ],
                "question": "質問：女の人はこれからまず何をしますか。",
                "read_options": False,
                "repeat": 1,
                "thinking_time": 12
            },
            {
                "id": 23,
                "title": "第2問（通し番号23）",
                "instruction": "大学の事務室で留学生と職員の人が話しています。男の人は明日何を持参しなければなりませんか。",
                "dialogue": [
                    {
                        "speaker": "male",
                        "text": "すみません、明日の奨学金の面接試験ですが、何か持っていくものはありますか。"
                    },
                    {
                        "speaker": "female",
                        "text": "受験票と筆記用具は必須です。学生証や写真は今日すでに提出いただいたので、明日は持参不要ですよ。"
                    },
                    {
                        "speaker": "male",
                        "text": "わかりました。受験票と筆記用具ですね。忘れずに持ってきます。"
                    }
                ],
                "question": "質問：男の人は明日何を持参しなければなりませんか。",
                "read_options": False,
                "repeat": 1,
                "thinking_time": 12
            },
            {
                "id": 24,
                "title": "第3問（通し番号24）",
                "instruction": "問題３では、質問を聞いて、正しい答えを１から４の中から一つ選んでください。",
                "dialogue": [
                    {
                        "speaker": "female",
                        "text": "山田さん、先週頼んでおいた企画書のコピー、もうできてる？"
                    }
                ],
                "question": "",
                "read_options": True,
                "options": [
                    "１　はい、すぐにお持ちいたします。",
                    "２　いいえ、まだ受け取っていません。",
                    "３　それなら、あちらに置いてあります。",
                    "４　いえ、結構でございます。"
                ],
                "repeat": 1,
                "thinking_time": 8
            },
            {
                "id": 25,
                "title": "第4問（通し番号25）",
                "instruction": "問題４では、質問を聞いて、正しい答えを１から４の中から一つ選んでください。",
                "dialogue": [
                    {
                        "speaker": "male",
                        "text": "顔色がずいぶん悪いようだけど、体調は大丈夫ですか。"
                    }
                ],
                "question": "",
                "read_options": True,
                "options": [
                    "１　ええ、少し熱気味でだるいんです。",
                    "２　いえ、全く忙しくありませんよ。",
                    "３　これから病院へ見学に行きます。",
                    "４　はい、とても元気そうですね。"
                ],
                "repeat": 1,
                "thinking_time": 8
            }
        ],
        "outro": "これで第1週実戦テスト、第5回の聴解試験を終わります。解答用紙のマークを確認してください。"
    }
}

out_path = r"d:\AgentAI\PublicDocument\doc_tools\exam_week01_de05.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print(f"[SUCCESS] Đã tạo file kịch bản Đề số 05 Tuần 1: {out_path}")
