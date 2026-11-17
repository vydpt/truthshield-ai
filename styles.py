CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap');

.stApp, .stApp p, .stApp label, .stApp button, .stApp textarea {
    font-family: 'Be Vietnam Pro', sans-serif;
}

.stApp {
    background: radial-gradient(circle at top right, #12284A 0%, #0A1A33 55%);
    color: #FFFFFF;
}

/* Ẩn thanh công cụ mặc định của Streamlit */
#MainMenu, footer, [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] {
    display: none;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

/* Khối giới thiệu */
.hero {
    padding: 3rem 2rem;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(34,211,238,0.12), rgba(255,138,61,0.08));
    border: 1px solid rgba(34,211,238,0.35);
}

.hero-tag {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 999px;
    background: rgba(34,211,238,0.15);
    color: #22D3EE;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 1px;
}

.hero-title {
    font-size: 2.6rem;
    font-weight: 800;
    line-height: 1.25;
    margin: 1rem 0 0.8rem 0;
    color: #FFFFFF;
}

.hero-title span {
    color: #FF8A3D;
}

.hero-sub {
    font-size: 1.1rem;
    color: #C7D6EA;
    max-width: 640px;
}

/* Điện thoại: chữ nhỏ lại cho vừa màn hình */
@media (max-width: 640px) {
    .hero { padding: 2rem 1.2rem; }
    .hero-title { font-size: 1.8rem; }
}
</style>
"""

CSS_NAV = """
<style>
.topbar {
    display: flex;
    align-items: center;
    gap: 12px;
    padding-bottom: 1.2rem;
}

.brand-name {
    font-size: 1.3rem;
    font-weight: 800;
    letter-spacing: 0.5px;
    color: #FFFFFF;
}

.brand-name span {
    color: #22D3EE;
}

/* Thanh điều hướng (các tab) */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    border-bottom: 1px solid rgba(255,255,255,0.12);
}

.stTabs [data-baseweb="tab"] {
    color: #C7D6EA;
    font-weight: 600;
    padding: 10px 18px;
    background: transparent;
}

.stTabs [aria-selected="true"] {
    color: #22D3EE;
}

.stTabs [data-baseweb="tab-highlight"] {
    background-color: #22D3EE;
}

.stTabs [data-baseweb="tab-border"] {
    display: none;
}

.stTabs [data-baseweb="tab"] p {
    color: #C7D6EA !important;
    font-weight: 600;
}

.stTabs [aria-selected="true"] p {
    color: #22D3EE !important;
}

.stTabs [data-baseweb="tab-highlight"] {
    background-color: #22D3EE !important;
}

.stTabs [data-baseweb="tab-border"] {
    background-color: rgba(255,255,255,0.12) !important;
}
</style>
"""

CSS_FIX = """
<style>
button[role="tab"],
button[role="tab"] p,
button[role="tab"] div,
[data-testid="stTab"],
[data-testid="stTab"] p {
    color: #C7D6EA !important;
}

button[role="tab"][aria-selected="true"],
button[role="tab"][aria-selected="true"] p,
button[role="tab"][aria-selected="true"] div,
[data-testid="stTab"][aria-selected="true"],
[data-testid="stTab"][aria-selected="true"] p {
    color: #22D3EE !important;
}

[data-baseweb="tab-highlight"] {
    background-color: #22D3EE !important;
    background: #22D3EE !important;
}

[data-baseweb="tab-border"] {
    background-color: rgba(255,255,255,0.15) !important;
    background: rgba(255,255,255,0.15) !important;
}
/* FIX: Chữ trên nút chức năng */
div.stButton > button,
div.stButton > button p {
    color: #102640 !important;
    font-weight: 700 !important;
}

/* FIX: Nhãn ô nhập trên Streamlit */
[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] *,
[data-testid="stTextArea"] label,
[data-testid="stTextArea"] label *,
[data-testid="stTextInput"] label,
[data-testid="stTextInput"] label * {
    color: #D8E9F5 !important;
}
</style>
"""
