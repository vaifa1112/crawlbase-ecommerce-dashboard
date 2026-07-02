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

st.code("""
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
""", language="text")

st.divider()

# ====================================================
# KPI
# ====================================================

st.subheader("📊 Informasi Dataset")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Jumlah Produk", len(df))
c2.metric("Jumlah Kolom", len(df.columns))
c3.metric("Lokasi Unik", df["Lokasi"].nunique())
c4.metric("Link Produk", df["Link"].count())

st.divider()

# ====================================================
# PREVIEW
# ====================================================

st.subheader("📄 Preview Dataset")

st.dataframe(df, use_container_width=True, height=350)

st.divider()

# ====================================================
# SEARCH
# ====================================================

st.subheader("🔍 Cari Produk")

keyword = st.text_input("Masukkan Nama Produk")

if keyword:
    hasil = df[df["Nama Produk"].str.contains(keyword, case=False, na=False)]
    st.success(f"Ditemukan {len(hasil)} produk")
    st.dataframe(hasil, use_container_width=True)

st.divider()

# ====================================================
# GRAFIK LOKASI
# ====================================================

st.subheader("📍 Distribusi Lokasi Penjual")

lokasi = df["Lokasi"].fillna("Tidak Diketahui").value_counts().reset_index()
lokasi.columns = ["Lokasi", "Jumlah"]

fig = px.bar(
    lokasi.head(10),
    x="Lokasi",
    y="Jumlah",
    text="Jumlah",
    title="10 Lokasi Terbanyak"
)
fig.update_layout(height=450)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ====================================================
# HARGA
# ====================================================

st.subheader("💰 Distribusi Harga Produk")

harga = (
    df["Harga"]
    .astype(str)
    .str.replace("Rp", "", regex=False)
    .str.replace(".", "", regex=False)
    .str.replace(",", "", regex=False)
)
harga = pd.to_numeric(harga, errors="coerce")

df["Harga_Numeric"] = harga

fig2 = px.histogram(
    df,
    x="Harga_Numeric",
    nbins=30,
    title="Sebaran Harga Produk"
)
fig2.update_layout(height=450)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ====================================================
# PIE CHART
# ====================================================

st.subheader("🥧 Persentase Lokasi")

fig3 = px.pie(
    lokasi.head(10),
    names="Lokasi",
    values="Jumlah",
    hole=.45
)

st.plotly_chart(fig3, use_container_width=True)

st.divider()

# ====================================================
# DATASET INFO
# ====================================================

st.subheader("📋 Informasi Dataset")

info1, info2 = st.columns(2)

with info1:
    st.write("Jumlah Baris")
    st.code(len(df))
    st.write("Jumlah Kolom")
    st.code(len(df.columns))
    st.write("Kolom")
    st.write(df.columns.tolist())

with info2:
    st.write("Missing Value")
    st.dataframe(df.isnull().sum().reset_index(), use_container_width=True)

st.divider()

# ====================================================
# DATA CLEANING
# ====================================================

st.subheader("🧹 Tahapan Data Cleaning")

st.success("""
✔ Menghapus data kosong
✔ Menghapus data duplikat
✔ Membersihkan format harga
✔ Menstandarkan lokasi
✔ Menyimpan ke CSV
✔ Menyimpan ke Excel
""")

st.divider()

# ====================================================
# DOWNLOAD
# ====================================================

st.subheader("⬇ Download Dataset")

col1, col2 = st.columns(2)

csv = df.to_csv(index=False).encode("utf-8-sig")

with col1:
    st.download_button(
        "⬇ Download CSV",
        csv,
        file_name="tokopedia.csv",
        mime="text/csv"
    )

with col2:
    excel_path = Path("data/tokopedia_aksesorisPengendara.xlsx")
    if not excel_path.exists():
        excel_path = Path("tokopedia_aksesorisPengendara.xlsx")

    if excel_path.exists():
        with open(excel_path, "rb") as f:
            st.download_button(
                "⬇ Download Excel",
                data=f,
                file_name="tokopedia.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

st.divider()

# ====================================================
# FOOTER
# ====================================================

st.caption("© Dashboard Web Scraping Tokopedia | Sistem Informasi")
