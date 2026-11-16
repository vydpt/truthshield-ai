
import streamlit as st
from pathlib import Path
import base64
import html
import textwrap


# ==========================================
# BEHIND THE SHIELD
# TRUTHSHIELD AI • K7T1
# ==========================================

ASSETS_DIR = Path(__file__).parent / "assets"


def get_image_data(filename):
    """Đọc ảnh từ assets và chuyển thành data URI."""
    image_path = ASSETS_DIR / filename

    if not image_path.is_file():
        return None

    extension = image_path.suffix.lower()

    mime_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
    }

    mime_type = mime_types.get(extension)

    if not mime_type:
        return None

    image_base64 = base64.b64encode(
        image_path.read_bytes()
    ).decode("utf-8")

    return f"data:{mime_type};base64,{image_base64}"


def avatar_html(filename, size=78, featured=False):
    """Tạo ảnh đại diện hoặc biểu tượng mặc định."""
    image_data = get_image_data(filename)

    border_color = "#FFB45B" if featured else "#355A75"

    if image_data:
        return f"""
        <img
            src="{image_data}"
            alt="Ảnh thành viên"
            style="
                width:{size}px;
                height:{size}px;
                object-fit:cover;
                border-radius:16px;
                border:1px solid {border_color};
                flex-shrink:0;
            "
        >
        """

    return f"""
    <div style="
        width:{size}px;
        height:{size}px;
        min-width:{size}px;
        border-radius:16px;
        background:#24445F;
        border:1px solid {border_color};
        display:flex;
        align-items:center;
        justify-content:center;
        color:#B8D4E6;
        font-size:30px;
        box-sizing:border-box;
    ">
        ◈
    </div>
    """

def render_html(content):
    cleaned_html = textwrap.dedent(content).strip()

    # Gộp HTML thành một dòng để Streamlit hiển thị đúng
    cleaned_html = " ".join(
        line.strip()
        for line in cleaned_html.splitlines()
    )

    st.markdown(
        cleaned_html,
        unsafe_allow_html=True
    )
def render_behind_the_shield():

    # --------------------------------------
    # HEADER
    # --------------------------------------

    render_html(
        """
        <div style="
            text-align:center;
            padding:20px 12px 14px;
        ">
            <div style="
                color:#22D3EE;
                font-size:12px;
                font-weight:700;
                letter-spacing:2px;
                margin-bottom:10px;
            ">
                TRUTHSHIELD AI · K7T1
            </div>

            <h2 style="
                color:#FFFFFF;
                font-size:clamp(26px, 5vw, 36px);
                letter-spacing:1px;
                margin:0 0 10px;
            ">
                BEHIND THE SHIELD
            </h2>

            <p style="
                color:#AFC7DA;
                font-size:14px;
                margin:0;
            ">
                Những người kiến tạo TRUTHSHIELD AI
            </p>

            <p style="
                color:#88A9C2;
                font-size:12px;
                margin-top:8px;
            ">
                Trường Trung học Phổ thông FPT Cần Thơ
            </p>
        </div>
        """,
    )

    # --------------------------------------
    # PRODUCT LEAD — TOBI
    # --------------------------------------

    tobi_avatar = avatar_html(
        "tobi.jpg",
        size=78,
        featured=True
    )

    render_html(
        f"""
        <div style="
            max-width:460px;
            margin:24px auto 30px;
            padding:22px;
            background:linear-gradient(
                135deg,
                #173451 0%,
                #102640 100%
            );
            border:1px solid #42617A;
            border-radius:18px;
            box-shadow:0 12px 30px rgba(0,0,0,0.18);
            box-sizing:border-box;
        ">

            <div style="
                display:flex;
                align-items:center;
                gap:18px;
            ">

                {tobi_avatar}

                <div style="min-width:0;">

                    <div style="
                        color:#FFB45B;
                        font-size:11px;
                        font-weight:700;
                        letter-spacing:1px;
                        margin-bottom:7px;
                    ">
                        ✦ PRODUCT LEAD
                    </div>

                    <div style="
                        color:#FFFFFF;
                        font-size:clamp(16px, 3.5vw, 19px);
                        font-weight:700;
                        line-height:1.45;
                    ">
                        Đào Phạm Tường Vy
                    </div>

                    <div style="
                        color:#22D3EE;
                        font-size:12px;
                        margin-top:6px;
                    ">
                        Tobi · Lead Developer
                    </div>

                </div>
            </div>

            <div style="
                height:1px;
                background:#294763;
                margin:18px 0 14px;
            "></div>

            <p style="
                color:#C4D6E6;
                font-size:13px;
                line-height:1.75;
                margin:0;
            ">
                Định hướng sản phẩm, thiết kế trải nghiệm
                và phụ trách phát triển chính TRUTHSHIELD AI.
            </p>

        </div>
        """,
    )

    # --------------------------------------
    # TEAM MEMBERS
    # --------------------------------------

    render_html(
        """
        <h3 style="
            color:#FFFFFF;
            font-size:19px;
            text-align:center;
            margin:18px 0 20px;
        ">
            THE CREATIVE TEAM
        </h3>
        """,
    )

    members = [
        {
            "name": "Trương Bảo Thiên Ân",
            "image": "thien_an.jpg",
        },
        {
            "name": "Quách Gia Linh",
            "image": "gia_linh.jpg",
        },
        {
            "name": "Nguyễn Đức Thiện Mỷ",
            "image": "thien_my.jpg",
        },
    ]

    columns = st.columns(3, gap="small")

    for column, member in zip(columns, members):

        avatar = avatar_html(
            member["image"],
            size=76
        )

        safe_name = html.escape(member["name"])

        with column:
            render_html(
                f"""
                <div style="
                    background:#142C48;
                    border:1px solid #294763;
                    border-radius:16px;
                    padding:18px 10px;
                    min-height:200px;
                    text-align:center;
                    box-sizing:border-box;
                ">

                    <div style="
                        display:flex;
                        justify-content:center;
                        margin-bottom:14px;
                    ">
                        {avatar}
                    </div>

                    <div style="
                        color:#FFFFFF;
                        font-size:13px;
                        font-weight:700;
                        line-height:1.5;
                        min-height:42px;
                    ">
                        {safe_name}
                    </div>

                    <div style="
                        color:#91B3CB;
                        font-size:11px;
                        letter-spacing:1px;
                        margin-top:10px;
                    ">
                        TEAM MEMBER
                    </div>

                </div>
                """,

            )

    # --------------------------------------
    # MENTOR
    # --------------------------------------

    render_html(
        """
        <div style="
            text-align:center;
            margin:38px 0 18px;
        ">
            <div style="
                color:#22D3EE;
                font-size:11px;
                font-weight:700;
                letter-spacing:2px;
                margin-bottom:8px;
            ">
                PROJECT ADVISOR
            </div>

            <h3 style="
                color:#FFFFFF;
                font-size:21px;
                margin:0;
            ">
                OUR MENTOR
            </h3>
        </div>
        """,
    )

    mentor_avatar = avatar_html(
        "mentor.jpg",
        size=76
    )

    render_html(
        f"""
        <div style="
            max-width:520px;
            margin:0 auto;
            padding:22px;
            background:linear-gradient(
                135deg,
                #173451,
                #112B46
            );
            border:1px solid #35536D;
            border-radius:18px;
            box-sizing:border-box;
        ">

            <div style="
                display:flex;
                align-items:center;
                gap:18px;
            ">

                {mentor_avatar}

                <div style="min-width:0;">

                    <div style="
                        color:#22D3EE;
                        font-size:11px;
                        font-weight:700;
                        letter-spacing:1px;
                        margin-bottom:7px;
                    ">
                        GIÁO VIÊN HƯỚNG DẪN
                    </div>

                    <div style="
                        color:#FFFFFF;
                        font-size:19px;
                        font-weight:700;
                        line-height:1.4;
                    ">
                        Cô Tiêu Ngọc Tươi
                    </div>

                    <div style="
                        color:#AFC7DA;
                        font-size:12px;
                        margin-top:6px;
                    ">
                        Project Mentor
                    </div>

                </div>
            </div>

            <div style="
                height:1px;
                background:#294763;
                margin:18px 0 14px;
            "></div>

            <p style="
                color:#C4D6E6;
                font-size:13px;
                line-height:1.75;
                margin:0;
            ">
                Đồng hành, định hướng và cố vấn cho nhóm
                trong quá trình thực hiện dự án TRUTHSHIELD AI.
            </p>

        </div>
        """,
    )

    # --------------------------------------
    # CLOSING SLOGAN
    # --------------------------------------

    render_html(
        """
        <div style="
            max-width:760px;
            margin:42px auto 16px;
            padding:24px 12px;
            text-align:center;
        ">

            <div style="
                width:48px;
                height:2px;
                background:#FFB45B;
                border-radius:10px;
                margin:0 auto 22px;
            "></div>

            <p style="
                color:#FFFFFF;
                font-size:clamp(18px, 4vw, 23px);
                font-weight:600;
                line-height:1.6;
                letter-spacing:0.3px;
                margin:0 0 12px;
            ">
                Four People. One Dream.<br>
                One Legacy.
            </p>

            <p style="
                color:#B6CDDF;
                font-size:13px;
                line-height:1.8;
                margin:0 0 20px;
            ">
                Bốn con người. Một giấc mơ.<br>
                Một dấu ấn.
            </p>

            <div style="
                color:#22D3EE;
                font-size:11px;
                font-weight:700;
                letter-spacing:2px;
            ">
                THE TRUTHSHIELD TEAM · K7T1
            </div>

        </div>
        """,
    )
