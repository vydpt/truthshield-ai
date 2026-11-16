
from analyzer import analyze_text


def compare_articles(text_a, text_b):
    # Phân tích từng bài viết
    result_a = analyze_text(text_a)
    result_b = analyze_text(text_b)

    score_a = result_a["risk_score"]
    score_b = result_b["risk_score"]

    # So sánh điểm rủi ro ngôn ngữ
    if score_a > score_b:
        conclusion = (
            "Bài A có nhiều dấu hiệu ngôn ngữ "
            "đáng chú ý hơn theo thang điểm thử nghiệm."
        )
    elif score_b > score_a:
        conclusion = (
            "Bài B có nhiều dấu hiệu ngôn ngữ "
            "đáng chú ý hơn theo thang điểm thử nghiệm."
        )
    else:
        conclusion = (
            "Hai bài có cùng điểm rủi ro ngôn ngữ "
            "theo thang điểm thử nghiệm."
        )

    return {
        "article_a": result_a,
        "article_b": result_b,
        "score_a": score_a,
        "score_b": score_b,
        "conclusion": conclusion
    }
