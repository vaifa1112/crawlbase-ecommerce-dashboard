import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ====================================================
# CONFIG
# ====================================================

st.set_page_config(
    page_title="Metodologi Web Scraping",
    page_icon="🛒",
    layout="wide"
)

# ====================================================
# CSS
# ====================================================

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.card{
    background:#1e293b;
    padding:18px;
    border-radius:15px;
    text-align:center;
    color:white;
    border:1px solid #334155;
}

.title{
    font-size:38px;
    font-weight:bold;
}

.sub{
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# ====================================================
# LOAD DATA
# ====================================================

@st.cache_data
def load_data():
    csv_path = Path("data/tokopedia_aksesorisPengendara.csv")
    if not csv_path.exists():
        csv_path = Path("tokopedia_aksesorisPengendara.csv")
    return pd.read_csv(csv_path)

df = load_data()

# ====================================================
# HEADER
# ====================================================

st.markdown("""
<div class='title'>
🛒 Metodologi Web Scraping Tokopedia
</div>

<div class='sub'>
Dataset hasil scraping menggunakan Selenium
</div>
""", unsafe_allow_html=True)

st.divider()

# ====================================================
# WORKFLOW
# ====================================================

st.subheader("🔄 Workflow Web Scraping")

st.markdown("""
```text
🛒 Tokopedia
      │
      ▼
🤖 Selenium
      │
      ▼
📜 Auto Scroll
      │
      ▼
📄 Parsing HTML
      │
      ▼
🧹 Data Cleaning
      │
      ▼
📊 Dataset
      │
      ▼
💾 CSV & Excelimport streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ====================================================
# CONFIG
# ====================================================

st.set_page_config(
    page_title="Metodologi Web Scraping",
    page_icon="🛒",
    layout="wide"
)

# ====================================================
# CSS
# ====================================================

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.card{
    background:#1e293b;
    padding:18px;
    border-radius:15px;
    text-align:center;
    color:white;
    border:1px solid #334155;
}

.title{
    font-size:38px;
    font-weight:bold;
}

.sub{
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# ====================================================
# LOAD DATA
# ====================================================

@st.cache_data
def load_data():
    csv_path = Path("data/tokopedia_aksesorisPengendara.csv")
    if not csv_path.exists():
        csv_path = Path("tokopedia_aksesorisPengendara.csv")
    return pd.read_csv(csv_path)

df = load_data()

# ====================================================
# HEADER
# ====================================================

st.markdown("""
<div class='title'>
🛒 Metodologi Web Scraping Tokopedia
</div>

<div class='sub'>
Dataset hasil scraping menggunakan Selenium
</div>
""", unsafe_allow_html=True)

st.divider()

# ====================================================
# WORKFLOW
# ====================================================

st.subheader("🔄 Workflow Web Scraping")

st.markdown("""
```text
🛒 Tokopedia
      │
      ▼
🤖 Selenium
      │
      ▼
📜 Auto Scroll
      │
      ▼
📄 Parsing HTML
      │
      ▼
🧹 Data Cleaning
      │
      ▼
📊 Dataset
      │
      ▼
💾 CSV & Excelimport streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ====================================================
# CONFIG
# ====================================================

st.set_page_config(
    page_title="Metodologi Web Scraping",
    page_icon="🛒",
    layout="wide"
)

# ====================================================
# CSS
# ====================================================

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.card{
    background:#1e293b;
    padding:18px;
    border-radius:15px;
    text-align:center;
    color:white;
    border:1px solid #334155;
}

.title{
    font-size:38px;
    font-weight:bold;
}

.sub{
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# ====================================================
# LOAD DATA
# ====================================================

@st.cache_data
def load_data():
    csv_path = Path("data/tokopedia_aksesorisPengendara.csv")
    if not csv_path.exists():
        csv_path = Path("tokopedia_aksesorisPengendara.csv")
    return pd.read_csv(csv_path)

df = load_data()

# ====================================================
# HEADER
# ====================================================

st.markdown("""
<div class='title'>
🛒 Metodologi Web Scraping Tokopedia
</div>

<div class='sub'>
Dataset hasil scraping menggunakan Selenium
</div>
""", unsafe_allow_html=True)

st.divider()

# ====================================================
# WORKFLOW
# ====================================================

st.subheader("🔄 Workflow Web Scraping")

st.markdown("""
```text
🛒 Tokopedia
      │
      ▼
🤖 Selenium
      │
      ▼
📜 Auto Scroll
      │
      ▼
📄 Parsing HTML
      │
      ▼
🧹 Data Cleaning
      │
      ▼
📊 Dataset
      │
      ▼
💾 CSV & Excelimport streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ====================================================
# CONFIG
# ====================================================

st.set_page_config(
    page_title="Metodologi Web Scraping",
    page_icon="🛒",
    layout="wide"
)

# ====================================================
# CSS
# ====================================================

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.card{
    background:#1e293b;
    padding:18px;
    border-radius:15px;
    text-align:center;
    color:white;
    border:1px solid #334155;
}

.title{
    font-size:38px;
    font-weight:bold;
}

.sub{
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# ====================================================
# LOAD DATA
# ====================================================

@st.cache_data
def load_data():
    csv_path = Path("data/tokopedia_aksesorisPengendara.csv")
    if not csv_path.exists():
        csv_path = Path("tokopedia_aksesorisPengendara.csv")
    return pd.read_csv(csv_path)

df = load_data()

# ====================================================
# HEADER
# ====================================================

st.markdown("""
<div class='title'>
🛒 Metodologi Web Scraping Tokopedia
</div>

<div class='sub'>
Dataset hasil scraping menggunakan Selenium
</div>
""", unsafe_allow_html=True)

st.divider()

# ====================================================
# WORKFLOW
# ====================================================

st.subheader("🔄 Workflow Web Scraping")

st.markdown("""
```text
🛒 Tokopedia
      │
      ▼
🤖 Selenium
      │
      ▼
📜 Auto Scroll
      │
      ▼
📄 Parsing HTML
      │
      ▼
🧹 Data Cleaning
      │
      ▼
📊 Dataset
      │
      ▼
💾 CSV & Excel
