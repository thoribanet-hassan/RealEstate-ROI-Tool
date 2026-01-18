import streamlit as st

# Configure the page - MUST be the first streamlit command
st.set_page_config(
    page_title="حاسبة العائد العقاري الذكية",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for RTL and styling
st.markdown("""
    <style>
    /* Import a nice Arabic font */
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Cairo', sans-serif;
    }

    /* Main container styling for RTL */
    .stApp {
        direction: rtl;
    }

    /* Adjust container padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Input widgets styling */
    .stNumberInput > label {
        font-size: 1rem;
        font-weight: 600;
        text-align: right;
        display: block;
        margin-bottom: 0.5rem;
    }

    /* Fix alignment for numbers in inputs */
    input[type="number"] {
        direction: ltr; /* Numbers are usually LTR */
        text-align: right; /* But aligned to the right in the box */
    }

    /* Metric card styling */
    .metric-card {
        background: linear-gradient(135deg, #f6f8fd 0%, #f1f4f9 100%);
        border: 1px solid #d1d5db;
        border-radius: 16px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        margin: 20px auto;
        max-width: 600px;
        border-right: 8px solid #2563eb; /* Accent on the right */
    }

    .metric-title {
        color: #4b5563;
        font-size: 1.5rem;
        margin-bottom: 10px;
        font-weight: 600;
    }

    .metric-value {
        color: #1e40af; /* Darker blue */
        font-size: 4rem;
        font-weight: 800;
        direction: ltr;
        display: inline-block;
        line-height: 1;
    }

    /* Header styling */
    h1 {
        text-align: center;
        color: #111827;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }

    p.subtitle {
        text-align: center;
        color: #6b7280;
        margin-bottom: 2rem;
    }

    </style>
    """, unsafe_allow_html=True)

# Application Header
st.title("حاسبة العائد العقاري الذكية")
st.markdown("<p class='subtitle'>أداة احترافية لحساب العائد السنوي على الاستثمار العقاري</p>", unsafe_allow_html=True)

st.markdown("---")

# Input Section
# Using columns for layout
col1, col2, col3 = st.columns(3)

# Note: In RTL, the visual order might depend on browser rendering of flexbox.
# Streamlit columns are defined 1, 2, 3.
# We will define them typically.

with col1:
    price = st.number_input("سعر العقار (ر.س)", min_value=0.0, value=1000000.0, step=10000.0, format="%.2f")

with col2:
    rent = st.number_input("الإيجار السنوي (ر.س)", min_value=0.0, value=80000.0, step=1000.0, format="%.2f")

with col3:
    maintenance = st.number_input("تكلفة الصيانة (ر.س)", min_value=0.0, value=5000.0, step=500.0, format="%.2f")

# Calculation Logic
roi = 0.0
if price > 0:
    roi = ((rent - maintenance) / price) * 100

st.markdown("---")

# Display Result
st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">صافي العائد السنوي (ROI)</div>
        <div class="metric-value">{roi:,.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

# Footer or extra info could go here
