
import streamlit as st
from behind_the_shield import render_behind_the_shield
from styles import CSS, CSS_NAV, CSS_FIX
from analyzer import analyze_text, highlight_text, EXPLANATIONS

st.set_page_config(
    page_title="TRUTHSHIELD AI",
    page_icon="🛡️",
    layout="wide"
)

st.markdown(
    CSS + CSS_NAV + CSS_FIX,
    unsafe_allow_html=True
)

# Logo + tên ứng dụng
st.markdown("""
<div class="topbar">
<svg width="38" height="38" viewBox="0 0 24 24" fill="none">
<path d="M12 2L4 5v6c0 5 3.4 9.4 8 11 4.6-1.6 8-6 8-11V5l-8-3z"
fill="#22D3EE" fill-opacity="0.2"
stroke="#22D3EE" stroke-width="1.6"
stroke-linejoin="round"/>
<path d="M8.5 12l2.5 2.5 4.5-5"
stroke="#FF8A3D" stroke-width="1.8"
stroke-linecap="round" stroke-linejoin="round"/>
</svg>
<div class="brand-name">TRUTHSHIELD <span>AI</span></div>
</div>
""", unsafe_allow_html=True)

# Thanh điều hướng
tab_home, tab_check, tab_lab, tab_about = st.tabs(
    ["Trang chủ", "Kiểm tra bài viết", "🔬 TRUTH LAB", "Giới thiệu"]
)

# TRANG CHỦ
with tab_home:
    st.markdown("""
    <div class="hero">
        <div class="hero-tag">
            NHẬN DIỆN THAO TÚNG THÔNG TIN
        </div>
        <div class="hero-title">
            Đừng chia sẻ khi chưa <span>kiểm chứng</span>
        </div>
        <div class="hero-sub">
            TRUTHSHIELD AI giúp bạn nhận ra những dấu hiệu
            giật gân, gây sợ hãi và thao túng cảm xúc
            trong nội dung trên mạng xã hội.
        </div>
    </div>
    """, unsafe_allow_html=True)


# TRANG KIỂM TRA
with tab_check:
    st.markdown("## 🔎 Kiểm tra nội dung bài viết")

    st.write(
        "Dán bài viết hoặc tin nhắn để phát hiện "
        "một số dấu hiệu thao túng thông tin."
    )

    content = st.text_area(
        "Nội dung cần kiểm tra",
        height=220,
        placeholder="Dán nội dung bài viết vào đây...",
        key="article_input"
    )

    if st.button(
        "🛡️ PHÂN TÍCH NGAY",
        use_container_width=True
    ):
        if not content.strip():
            st.warning("Bạn chưa nhập nội dung để phân tích!")

        else:
            result = analyze_text(content)

            # SHIELD SCAN
            st.markdown("### 🛡️ SHIELD SCAN")

            st.write(
                "Các cụm từ màu cam là những dấu hiệu "
                "cần chú ý trong bài viết."
            )

            highlighted = highlight_text(
                content,
                result["spans"]
            )

            st.markdown(
                '<div style="background:#172B48;'
                'padding:24px;border-radius:16px;'
                'border:1px solid #22D3EE;'
                'color:white;line-height:2;">'
                + highlighted +
                '</div>',
                unsafe_allow_html=True
            )

            # ĐIỂM RỦI RO
            st.markdown("### 📊 Kết quả phân tích")

            st.metric(
                "Điểm rủi ro ngôn ngữ (thử nghiệm)",
                f"{result['risk_score']}/100"
            )

            st.progress(result["risk_score"] / 100)

            st.markdown(
                f"**Mức cảnh báo:** {result['level']}"
            )

            # EMOTION RADAR
            
            st.markdown("### 🔬 SHIELD X-RAY")

            st.caption(
                "Chọn một nhóm dấu hiệu để hiểu "
                "vì sao nội dung được cảnh báo."
            )

            detected_categories = list(result["detected"].keys())

            if detected_categories:
                selected_category = st.selectbox(
                    "Chọn nhóm dấu hiệu",
                    detected_categories,
                    key="xray_category"
                )

                st.info(
                    "🧠 " + EXPLANATIONS.get(
                        selected_category,
                        "Chưa có giải thích cho nhóm này."
                    )
                )

                keywords = result["detected"][selected_category]

                st.write("**Cụm từ được phát hiện:**")
                st.write(", ".join(keywords))

                st.warning(
                    "Dấu hiệu ngôn ngữ không đồng nghĩa "
                    "với việc nội dung là tin giả."
                )
            else:
                st.success(
                    "Chưa phát hiện dấu hiệu trong "
                    "bộ từ khóa thử nghiệm."
                )
            st.markdown("### 📡 EMOTION RADAR")
            counts = result["counts"]
            total = sum(counts.values())

            for category, count in counts.items():
                percentage = count / total if total > 0 else 0

                st.write(
                    f"**{category}** – {count} lượt phát hiện"
                )
                st.progress(percentage)

            st.caption(
                "Biểu đồ thể hiện tỷ lệ lượt khớp từ khóa, "
                "không phải xác suất thao túng."
            )

            # CÁC DẤU HIỆU
            st.markdown("### 🚨 Dấu hiệu được phát hiện")

            if result["detected"]:
                for category, keywords in result["detected"].items():
                    st.warning(
                        f"**{category}:** "
                        + ", ".join(keywords)
                    )
            else:
                st.success(
                    "Không phát hiện dấu hiệu trong "
                    "bộ từ khóa hiện tại."
                )

            # GIẢI THÍCH
            st.markdown("### 🧠 VÌ SAO BỊ CẢNH BÁO?")

            if result["detected"]:
                for category in result["detected"]:
                    st.info(
                        f"**{category}:** "
                        + EXPLANATIONS[category]
                    )
            else:
                st.info(
                    "Chưa có dấu hiệu cần giải thích "
                    "theo bộ quy tắc hiện tại."
                )

            # GỢI Ý KIỂM CHỨNG
            st.markdown("### 💡 Gợi ý kiểm chứng")

            st.info(
                "1. Kiểm tra nguồn đăng bài.\n\n"
                "2. Tìm thông tin từ các nguồn đáng tin cậy.\n\n"
                "3. Kiểm tra ngày đăng và bối cảnh.\n\n"
                "4. Không vội chia sẻ khi chưa xác minh."
            )

            st.caption(
                "Đây là bộ phân tích từ khóa thử nghiệm. "
                "Kết quả không khẳng định nội dung đúng hay sai."
            )


# THINK BEFORE SHARE - Tram kiem chung
with tab_check:
    st.markdown("---")
    st.markdown("## 🧠 THINK BEFORE SHARE")
    st.write(
        "Trước khi chia sẻ một thông tin, "
        "hãy dành vài giây tự kiểm chứng!"
    )

    with st.container(border=True):
        st.markdown("### 🛡️ Thử thách 3 câu hỏi")

        q1 = st.checkbox(
            "Tôi đã kiểm tra nguồn đăng bài.",
            key="verify_source"
        )

        q2 = st.checkbox(
            "Tôi đã tìm được bằng chứng đáng tin cậy.",
            key="verify_evidence"
        )

        q3 = st.checkbox(
            "Tôi đã kiểm tra ngày đăng và bối cảnh.",
            key="verify_context"
        )

        score = sum([q1, q2, q3])

        st.progress(score / 3)
        st.write(f"Đã hoàn thành: {score}/3 bước")

        if st.button(
            "🔍 KIỂM TRA MỨC ĐỘ SẴN SÀNG",
            use_container_width=True,
            key="check_readiness"
        ):
            if score == 3:
                st.success(
                    "Bạn đã hoàn thành 3 bước tự kiểm chứng! "
                    "Hãy tiếp tục đánh giá độ tin cậy "
                    "của các bằng chứng trước khi chia sẻ."
                )
                st.balloons()

            elif score >= 1:
                st.warning(
                    "Bạn đã bắt đầu kiểm chứng! "
                    "Hãy hoàn thành các bước còn thiếu "
                    "trước khi chia sẻ."
                )

            else:
                st.error(
                    "Đừng vội chia sẻ! "
                    "Bạn chưa hoàn thành bước kiểm chứng nào."
                )

        st.caption(
            "Đây là bảng tự kiểm tra, không tự động "
            "xác nhận thông tin là đúng hay sai."
        )

# TRANG GIỚI THIỆU
with tab_about:
    st.write(
        "TRUTHSHIELD AI là dự án giúp người dùng "
        "nhận biết nội dung dễ gây hiểu lầm "
        "trên mạng xã hội."
    )
    render_behind_the_shield()

# TRUTH LAB - So sánh hai bài viết
with tab_lab:
    st.markdown("## 🔬 TRUTH LAB")

    st.write(
        "So sánh dấu hiệu ngôn ngữ trong hai bài viết "
        "để nhận biết cách truyền tải thông tin."
    )

    col_a, col_b = st.columns(2)

    with col_a:
        text_a = st.text_area(
            "🅰️ Bài viết A",
            height=200,
            key="lab_article_a"
        )

    with col_b:
        text_b = st.text_area(
            "🅱️ Bài viết B",
            height=200,
            key="lab_article_b"
        )

    if st.button(
        "🔬 SO SÁNH NGAY",
        use_container_width=True,
        key="compare_lab"
    ):
        if not text_a.strip() or not text_b.strip():
            st.warning("Hãy nhập đủ hai bài viết!")
        else:
            from truth_lab import compare_articles

            result = compare_articles(text_a, text_b)

            st.markdown("### 📊 Kết quả so sánh")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Bài A - Điểm ngôn ngữ",
                    f"{result['score_a']}/100"
                )
                st.progress(result["score_a"] / 100)

            with col2:
                st.metric(
                    "Bài B - Điểm ngôn ngữ",
                    f"{result['score_b']}/100"
                )
                st.progress(result["score_b"] / 100)

            st.info(result["conclusion"])
            st.markdown("### 🔬 COMPARISON MATRIX")
            st.table(result["comparison_rows"])
            st.caption("So sánh dấu hiệu ngôn ngữ, không xác minh tin thật hay giả.")
            # TRUTH LAB 3.0 - BẢNG SO SÁNH CHI TIẾT
            st.markdown("### 🔬 COMPARISON MATRIX")

            st.write(
                "Đối chiếu các dấu hiệu ngôn ngữ "
                "được phát hiện trong hai bài viết."
            )

            st.table(result["comparison_rows"])

            st.caption(
                "Bảng sử dụng bộ dấu hiệu bổ sung. "
                "Các dấu hiệu này chưa được cộng vào "
                "điểm ngôn ngữ hiện tại."
            )

            # TRUTH LAB 2.0 - DUAL SHIELD SCAN
            st.markdown("### 🛡️ DUAL SHIELD SCAN")

            st.write(
                "Các cụm từ màu cam là những dấu hiệu "
                "ngôn ngữ cần chú ý trong mỗi bài viết."
            )

            from analyzer import highlight_text

            scan_a = highlight_text(
                text_a,
                result["article_a"]["spans"]
            )

            scan_b = highlight_text(
                text_b,
                result["article_b"]["spans"]
            )

            col_scan_a, col_scan_b = st.columns(2)

            with col_scan_a:
                st.markdown("#### 🅰️ Bài viết A")
                st.markdown(
                    '<div class="scan-box">'
                    + scan_a
                    + '</div>',
                    unsafe_allow_html=True
                )

            with col_scan_b:
                st.markdown("#### 🅱️ Bài viết B")
                st.markdown(
                    '<div class="scan-box">'
                    + scan_b
                    + '</div>',
                    unsafe_allow_html=True
                )

            st.caption(
                "Từ khóa được tô sáng không chứng minh "
                "nội dung là tin giả."
            )

            # TRUTH LAB 2.0 - SHIELD EXPLAIN
            st.markdown("### 🧠 SHIELD EXPLAIN")

            st.write(
                "Giải thích các dấu hiệu ngôn ngữ "
                "được phát hiện trong từng bài viết."
            )

            explain_a, explain_b = st.columns(2)

            with explain_a:
                st.markdown("#### 🅰️ Phân tích bài A")

                detected_a = result["article_a"]["detected"]

                if detected_a:
                    for category, keywords in detected_a.items():
                        st.warning(
                            f"**{category}**: "
                            + ", ".join(keywords)
                        )
                        st.info(
                            EXPLANATIONS.get(
                                category,
                                "Chưa có giải thích cho nhóm này."
                            )
                        )
                else:
                    st.success(
                        "Chưa phát hiện dấu hiệu trong "
                        "bộ từ khóa thử nghiệm."
                    )

            with explain_b:
                st.markdown("#### 🅱️ Phân tích bài B")

                detected_b = result["article_b"]["detected"]

                if detected_b:
                    for category, keywords in detected_b.items():
                        st.warning(
                            f"**{category}**: "
                            + ", ".join(keywords)
                        )
                        st.info(
                            EXPLANATIONS.get(
                                category,
                                "Chưa có giải thích cho nhóm này."
                            )
                        )
                else:
                    st.success(
                        "Chưa phát hiện dấu hiệu trong "
                        "bộ từ khóa thử nghiệm."
                    )

            st.markdown("#### 💡 Câu hỏi kiểm chứng")
            st.info(
                "1. Hai bài viết lấy thông tin từ nguồn nào?\n\n"
                "2. Có bằng chứng hoặc tài liệu gốc không?\n\n"
                "3. Thông tin được đăng vào thời điểm nào?\n\n"
                "4. Có nguồn độc lập nào xác nhận không?"
            )

            st.caption(
                "SHIELD EXPLAIN sử dụng quy tắc và bộ từ khóa "
                "thử nghiệm, không tự động xác minh tính chính xác."
            )

            st.caption(
                "Điểm số dựa trên bộ từ khóa thử nghiệm, "
                "không xác định bài viết đúng hay sai."
                                   )

