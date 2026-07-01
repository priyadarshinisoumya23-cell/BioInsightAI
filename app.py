import streamlit as st
import base64


# -----------------------------
# Background Image Function
# -----------------------------
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="BioInsight AI",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)


# -----------------------------
# Background Theme
# -----------------------------
bg = get_base64("assets/bio_background.jpg")

st.markdown(
    f"""
    <style>

    .stApp {{
        background-image: url("data:image/jpeg;base64,{bg}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* Dark overlay */
    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background: rgba(5,10,20,0.78);
        z-index: -1;
    }}

    /* Sidebar */
    section[data-testid="stSidebar"] {{
        background: rgba(15,23,42,0.95);
    }}

    /* Main container */
    .block-container {{
        background: rgba(20,20,30,0.55);
        border-radius:20px;
        padding:2rem;
    }}

    /* Text */
    h1,h2,h3,h4,h5,h6,p,label,li {{
        color:white !important;
    }}

    /* Metric Cards */
    div[data-testid="metric-container"] {{
        background: rgba(25,35,55,0.90);
        border:1px solid #00E5FF;
        border-radius:15px;
        padding:15px;
    }}

    /* Buttons */
    .stButton > button {{
        background:#00BCD4;
        color:white;
        border:none;
        border-radius:10px;
    }}

    .stButton > button:hover {{
        background:#0097A7;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🧬 BioInsight AI")
st.sidebar.success("Gene Expression Analysis Dashboard")


# -----------------------------
# Header
# -----------------------------
st.title("🧬 BioInsight AI")
st.subheader("AI-Powered Gene Expression Analysis Dashboard")

st.markdown("""
Welcome to **BioInsight AI**, a web-based bioinformatics platform for exploring gene expression datasets using data science and machine learning.
""")

st.divider()


# -----------------------------
# Dashboard Metrics
# -----------------------------
st.header("📊 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🧬 Genes", "54,675")

with col2:
    st.metric("🧪 Samples", "130")

with col3:
    st.metric("📄 Reports", "PDF + CSV")

with col4:
    st.metric("🤖 ML Models", "3")

st.divider()


# -----------------------------
# Features
# -----------------------------
st.header("🚀 Features")

col1, col2 = st.columns(2)

with col1:
    st.info("""
### 📂 Data Explorer
- View Dataset
- Gene Search
- Summary Statistics
- Dataset Preview
""")

    st.success("""
### 📊 Visualizations
- Correlation Heatmap
- Box Plot
- Violin Plot
- Interactive Charts
""")

    st.warning("""
### 🤖 Machine Learning
- PCA
- K-Means Clustering
- Random Forest
- Feature Importance
""")

with col2:
    st.info("""
### 🧬 Differential Expression
- Top Genes
- Plotly Charts
- CSV Download
""")

    st.success("""
### 📄 Report Generation
- PDF Report
- CSV Export
- Summary Report
""")

    st.warning("""
### ℹ️ About
- Dataset Information
- Technologies Used
- Developer Profile
""")

st.divider()


# -----------------------------
# Workflow
# -----------------------------
st.header("🔬 Analysis Workflow")

st.code("""
GEO Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Data Exploration
      │
      ▼
Visualization
      │
      ▼
Machine Learning
      │
      ▼
Differential Expression
      │
      ▼
Reports
""")

st.divider()


# -----------------------------
# Technologies
# -----------------------------
st.header("🛠 Technologies Used")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
- Python
- Streamlit
- Pandas
- NumPy
""")

with c2:
    st.markdown("""
- Plotly
- Matplotlib
- Seaborn
- Scikit-learn
""")

with c3:
    st.markdown("""
- FPDF2
- Git
- GitHub
- Streamlit Cloud
""")

st.divider()


# -----------------------------
# Dataset
# -----------------------------
st.header("🧬 Dataset")

st.success("""
**Dataset:** GSE45827

**Source:** Gene Expression Omnibus (GEO)

Breast cancer gene expression dataset used for bioinformatics analysis.
""")

st.divider()


# -----------------------------
# Developer
# -----------------------------
st.header("👩‍💻 Developer")

st.info("""
**Soumya Priyadarshini**

BioInsight AI is a bioinformatics dashboard built using Python and Streamlit for gene expression analysis, visualization, machine learning, and report generation.
""")

st.divider()


# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <div style="text-align:center;padding:20px;">
        <h3>🧬 BioInsight AI</h3>
        <p>AI-Powered Gene Expression Analysis Dashboard</p>
        <p><b>Developed by Soumya Priyadarshini</b></p>
        <p>Built with Python • Streamlit • Plotly • Scikit-learn</p>
    </div>
    """,
    unsafe_allow_html=True
)