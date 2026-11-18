
from analyzer import analyze_text

# Các dấu hiệu bổ sung để SO SÁNH nội dung.
# Phần này không thay đổi cách tính điểm trong analyzer.py.
SIGNAL_GROUPS = {
    "Giật gân / cường điệu": [
        "sốc", "động trời", "chấn động",
        "bó tay", "không thể tin nổi"
    ],
    "Tạo tò mò / mơ hồ": [
        "thứ này", "sự thật đằng sau",
        "bí mật", "không ai ngờ"
    ],
    "Gây hoang mang": [
        "khẩn cấp", "đáng sợ",
        "hoảng loạn", "nguy hiểm"
    ],
    "Thúc giục chia sẻ": [
        "chia sẻ ngay", "lan truyền ngay",
        "hãy chia sẻ", "gửi ngay"
    ]
}


def detect_signals(text):
    content = text.casefold()
    findings = {}

    for category, phrases in SIGNAL_GROUPS.items():
        matched = [
            phrase for phrase in phrases
            if phrase.casefold() in content
        ]
        findings[category] = matched

    return findings


def describe_signals(findings):
    descriptions = []

    for category, phrases in findings.items():
        if phrases:
            descriptions.append(
                f"{category}: {', '.join(phrases)}"
            )

    if not descriptions:
        return "Chưa phát hiện dấu hiệu bổ sung."

    return "; ".join(descriptions)


def compare_articles(text_a, text_b):
    # Giữ nguyên kết quả phân tích hiện tại
    result_a = analyze_text(text_a)
    result_b = analyze_text(text_b)

    score_a = result_a["risk_score"]
    score_b = result_b["risk_score"]

    # Giữ nguyên logic so sánh điểm
    if score_a > score_b:
        basic_conclusion = (
            "Bài A có điểm cảnh báo ngôn ngữ cao hơn "
            "theo bộ phân tích hiện tại."
        )
    elif score_b > score_a:
        basic_conclusion = (
            "Bài B có điểm cảnh báo ngôn ngữ cao hơn "
            "theo bộ phân tích hiện tại."
        )
    else:
        basic_conclusion = (
            "Hai bài có cùng điểm cảnh báo ngôn ngữ "
            "theo bộ phân tích hiện tại."
        )

    # Phân tích bổ sung để so sánh sâu hơn
    signals_a = detect_signals(text_a)
    signals_b = detect_signals(text_b)

    comparison_rows = []

    for category in SIGNAL_GROUPS:
        found_a = signals_a[category]
        found_b = signals_b[category]

        comparison_rows.append({
            "Tiêu chí": category,
            "Bài A": ", ".join(found_a) if found_a else "Chưa phát hiện",
            "Bài B": ", ".join(found_b) if found_b else "Chưa phát hiện"
        })

    # Nhận xét chi tiết, hiển thị được qua
    # trường conclusion hiện có trong app.py
    conclusion = (
        basic_conclusion
        + "\n\n**SO SÁNH DẤU HIỆU BỔ SUNG:**\n\n"
        + "- **Bài A:** "
        + describe_signals(signals_a)
        + "\n"
        + "- **Bài B:** "
        + describe_signals(signals_b)
        + "\n\n"
        + "**Gợi ý kiểm chứng:** "
        + "Xác định nguồn đăng, tìm dẫn chứng cụ thể "
        + "và đối chiếu với nguồn đáng tin cậy.\n\n"
        + "**Lưu ý:** Các dấu hiệu bổ sung chưa được "
        + "tính vào điểm số hiện tại. Điểm thấp không "
        + "có nghĩa bài viết chắc chắn đúng sự thật."
    )

    return {
        "article_a": result_a,
        "article_b": result_b,
        "score_a": score_a,
        "score_b": score_b,
        "conclusion": conclusion,
        "comparison_rows": comparison_rows
    }
