
import re
import html

SIGNALS = {
    "Giật gân": [
        "chấn động", "sốc", "không thể tin nổi",
        "sự thật kinh hoàng", "bí mật động trời"
    ],
    "Gây sợ hãi": [
        "nguy hiểm chết người", "thảm họa",
        "hoảng loạn", "tất cả sẽ chết"
    ],
    "Kích động cảm xúc": [
        "phẫn nộ", "đáng căm ghét",
        "không thể tha thứ", "tẩy chay ngay"
    ],
    "Thúc giục chia sẻ": [
        "chia sẻ ngay", "lan truyền ngay",
        "gửi cho tất cả mọi người",
        "đừng để bị xóa", "chia sẻ trước khi quá muộn"
    ]
}

EXPLANATIONS = {
    "Giật gân": "Sử dụng từ ngữ gây chú ý mạnh, có thể khiến người đọc phản ứng vội vàng.",
    "Gây sợ hãi": "Có ngôn ngữ gợi cảm giác lo lắng hoặc hoảng sợ.",
    "Kích động cảm xúc": "Có cách diễn đạt dễ kích thích phản ứng cảm xúc mạnh.",
    "Thúc giục chia sẻ": "Có lời kêu gọi lan truyền thông tin nhanh chóng."
}


def analyze_text(text):
    detected = {}
    spans = []
    counts = {}

    for category, keywords in SIGNALS.items():
        matches = []

        for keyword in keywords:
            pattern = r"(?<!\w)" + re.escape(keyword) + r"(?!\w)"

            for match in re.finditer(pattern, text, re.IGNORECASE):
                matches.append(match.group())
                spans.append((match.start(), match.end()))

        if matches:
            detected[category] = list(dict.fromkeys(matches))

        counts[category] = len(matches)

    risk_score = min(len(detected) * 25, 100)

    if risk_score >= 75:
        level = "🔴 Cảnh báo cao"
    elif risk_score >= 25:
        level = "🟡 Cần thận trọng"
    else:
        level = "🟢 Chưa phát hiện dấu hiệu trong bộ từ khóa"

    return {
        "risk_score": risk_score,
        "level": level,
        "detected": detected,
        "counts": counts,
        "spans": spans
    }


def highlight_text(text, spans):
    spans = sorted(spans)
    merged = []

    for start, end in spans:
        if merged and start <= merged[-1][1]:
            old_start, old_end = merged[-1]
            merged[-1] = (old_start, max(old_end, end))
        else:
            merged.append((start, end))

    result = []
    last = 0

    for start, end in merged:
        result.append(html.escape(text[last:start]))
        result.append(
            '<mark style="background:#FF8A3D;'
            'color:#08172D;padding:2px 4px;'
            'border-radius:4px;font-weight:700;">'
            + html.escape(text[start:end])
            + '</mark>'
        )
        last = end

    result.append(html.escape(text[last:]))

    return "".join(result).replace("\n", "<br>")
