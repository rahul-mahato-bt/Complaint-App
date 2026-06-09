import streamlit as st
import joblib

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Complaint Detection System",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------
# Premium Styling with Gradients & Animations
# ---------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
}
[data-testid="stHeader"] { background: transparent; }
[data-testid="stSidebar"] { background: rgba(15,12,41,0.95); }

.main-title {
   font-family: 'Inter', sans-serif;
   font-size: 5.5rem;
   font-weight: 900;
   text-align: center;
   margin: 0;
   line-height: 1.05;
   background: linear-gradient(
       90deg,
       #ffffff,
       #d7e1ff,
       #8fb3ff,
       #ffffff
   );
   background-size: 300% auto;
   -webkit-background-clip: text;
   -webkit-text-fill-color: transparent;
   animation: premiumGlow 8s linear infinite;
}
@keyframes premiumGlow {
   0% { background-position: 0% center; }
   100% { background-position: 300% center; }
}
@keyframes shimmer {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.8; filter: brightness(1.2); }
}

.subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 24px;
    color: rgba(255,255,255,0.6);
    letter-spacing: 1px;
    text-align: center;
}

.glass-card {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.1);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(102,126,234,0.15);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.glass-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(118,75,162,0.3);
}

.result-badge {
    background: linear-gradient(135deg, #667eea, #764ba2);
    padding: 16px 32px;
    border-radius: 50px;
    display: inline-block;
    font-size: 20px;
    font-weight: 600;
    color: white;
    box-shadow: 0 4px 20px rgba(102,126,234,0.4);
    animation: pulse 2s ease-in-out infinite;
}
@keyframes pulse {
    0%, 100% { box-shadow: 0 4px 20px rgba(102,126,234,0.4); }
    50% { box-shadow: 0 4px 30px rgba(118,75,162,0.6); }
}

.stat-label {
    color: rgba(255,255,255,0.5);
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 8px;
}

/* Style Streamlit elements */
.stTextArea textarea {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 12px !important;
    color: black !important;
    font-size: 16px !important;
}
.stTextArea textarea:focus {
    border-color: #667eea !important;
    box-shadow: 0 0 15px rgba(102,126,234,0.3) !important;
}
.stButton > button {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 12px 40px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(102,126,234,0.4) !important;
}
.stButton > button:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 6px 25px rgba(118,75,162,0.5) !important;
}
h3, .stMarkdown h3 { color: rgba(255,255,255,0.9) !important; }
label { color: rgba(255,255,255,0.7) !important; }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Load Model
# ---------------------------
@st.cache_resource
def load_model():
    return joblib.load("complaint_model.pkl")

loaded_model = load_model()

# ---------------------------
# Header
# ---------------------------
import base64

def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bt_logo_b64 = get_base64_image("BT Logo.png")

st.markdown(f"""
<div style="display:flex; align-items:center; justify-content:center; gap:30px; margin-bottom:10px;">
    <img src="data:image/png;base64,{bt_logo_b64}" height="70">
</div>
""", unsafe_allow_html=True)
st.markdown("""
<style>
[data-testid="stAppViewContainer"] h1 {
    text-align: center;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Complaint Detection Dashboard")
st.markdown('<p class="subtitle">AI-powered customer complaint classification • Real-time analysis</p>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------
# Layout
# ---------------------------
col1, col2 = st.columns([2, 1])

# ---------------------------
# Input Section
# ---------------------------
with col1:
    st.markdown("### Enter Customer Comment")
    User_Comments = st.text_area(
        "Type the customer issue:",
        placeholder="e.g. Courier marked delivered but I did not receive the package...",
        height=180
    )
    predict_btn = st.button("⚡ Analyze Comment")

# ---------------------------
# Prediction Output
# ---------------------------
with col2:
    st.markdown("### 🎯 Prediction Result")

    if predict_btn:
        if User_Comments.strip() == "":
            st.warning("⚠ Please enter a comment")
        else:
            with st.spinner("🔍 Analyzing..."):
                user_prediction = loaded_model.predict([User_Comments])

            st.markdown(f"""
<div class="glass-card" style="text-align:center;">
    <p class="stat-label">Detected Category</p>
    <div class="result-badge">{user_prediction[0]}</div>
    <p style="color:rgba(255,255,255,0.4); margin-top:16px; font-size:12px;">
        ✓ Analysis complete
    </p>
</div>
""", unsafe_allow_html=True)

    else:
        st.markdown("""
<div class="glass-card" style="text-align:center;">
    <p style="color:rgba(255,255,255,0.4); font-size:40px; margin-bottom:8px;">🎯</p>
    <p style="color:rgba(255,255,255,0.4);">Enter a comment and click Analyze</p>
</div>
""", unsafe_allow_html=True)
