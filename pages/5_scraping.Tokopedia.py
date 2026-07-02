import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ==========================================
# CONFIG
# ==========================================

st.set_page_config(
    page_title="Scraping Tokopedia",
    page_icon="🛒",
    layout="wide"
)

# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>
.block-container{
    padding-top:1rem;
}
.metric-card{
    background-color:#0F172A;
    border-radius:12px;
    padding:15px;
}
.title{
    font-size:42px;
    font-weight:bold;
}
.subtitle{
    color:#9CA3AF;
    font-size:17px;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# LOAD DATA
# ==========================================

@st.cache_data
def load_data():
    files = [
        "tokopedia_produk.csv",
        "Tokopedia_produk.csv",
        "data/tokopedia_produk.csv"
    ]
    for f in files:
        if Path(f).exists():
            return pd.read_csv(f)
    st.error("❌ File tokopedia_produk.csv tidak ditemukan")
    st.stop()

df = load_data()

# ==========================================
# CLEAN DATA
# ==========================================

if "Harga" in df.columns:
    df["Harga_Numeric"] = (
        df["Harga"]
        .astype(str)
        .str.replace("Rp", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace(",", "", regex=False)
    )
    df["Harga_Numeric"] = pd.to_numeric(
        df["Harga_Numeric"],
        errors="coerce"
    )

# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class='title'>
🛒 Scraping Tokopedia
</div>
<div class='subtitle'>
Analisis hasil scraping menggunakan Selenium & BeautifulSoup
</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================================
# WORKFLOW
# ==========================================

st.subheader("🔄 Workflow")

c1, c2, c3, c4, c5, c6, c7 = st.columns(7)

with c1:
    st.success("🛒\nTokopedia")
with c2:
    st.markdown("<h2 style='text-align:center;'>➡️</h2>", unsafe_allow_html=True)
with c3:
    st.success("🤖\nSelenium")
with c4:
    st.markdown("<h2 style='text-align:center;'>➡️</h2>", unsafe_allow_html=True)
with c5:
    st.success("📄\nHTML")
with c6:
    st.markdown("<h2 style='text-align:center;'>➡️</h2>", unsafe_allow_html=True)
with c7:
    st.success("💾\nCSV")

st.info("""
Tahapan scraping:
• Membuka halaman Tokopedia
• Auto Scroll
• Mengambil HTML
• Parsing BeautifulSoup
• Extract Data
• Cleaning
• Export CSV
""")

st.divider()

# ==========================================
# KPI
# ==========================================

st.subheader("📊 Ringkasan Dataset")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Jumlah Produk", len(df))

if "Lokasi" in df.columns:
    c2.metric("Jumlah Lokasi", df["Lokasi"].nunique())

if "Harga_Numeric" in df.columns:
    c3.metric(
        "Harga Rata-rata",
        f"Rp {int(df['Harga_Numeric'].mean()):,}"
    )
    c4.metric(
        "Harga Maksimum",
        f"Rp {int(df['Harga_Numeric'].max()):,}"
    )

st.divider()

# ==========================================
# GRAFIK HARGA
# ==========================================

if "Harga_Numeric" in df.columns:
    st.subheader("💰 Distribusi Harga")

    fig = px.histogram(
        df,
        x="Harga_Numeric",
        nbins=30,
        color_discrete_sequence=["#00C853"]
    )
    fig.update_layout(height=450)
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================
# LOKASI
# ==========================================

if "Lokasi" in df.columns:
    st.subheader("📍 Top Lokasi Penjual")

    lokasi = (
        df["Lokasi"]
        .fillna("-")
        .value_counts()
        .head(10)
        .reset_index()
    )
    lokasi.columns = ["Lokasi", "Jumlah"]

    fig = px.bar(
        lokasi,
        x="Lokasi",
        y="Jumlah",
        text="Jumlah",
        color="Jumlah"
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================
# RATING
# ==========================================

if "Rating" in df.columns:
    st.subheader("⭐ Distribusi Rating")

    rating = (
        df["Rating"]
        .fillna("-")
        .astype(str)
        .value_counts()
        .reset_index()
    )
    rating.columns = ["Rating", "Jumlah"]

    fig = px.bar(
        rating,
        x="Rating",
        y="Jumlah",
        color="Jumlah",
        text="Jumlah"
    )
    fig.update_layout(height=450)
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================
# PRODUK TERLARIS  ← BAGIAN INI YANG DIPERBAIKI
# ==========================================

if "Terjual" in df.columns:
    st.subheader("🔥 Top 10 Produk Terlaris")

    top_laris = df.copy()
    top_laris["Terjual_Angka"] = (
        top_laris["Terjual"]
        .astype(str)
        .str.extract(r'(\d+)')[0]
    )
    top_laris["Terjual_Angka"] = pd.to_numeric(
        top_laris["Terjual_Angka"],
        errors="coerce"
    ).fillna(0)

    top_laris = top_laris.sort_values(
        "Terjual_Angka",
        ascending=False
    )

    kolom = [
        "Nama Produk", "Harga", "Lokasi",
        "Toko", "Rating", "Terjual", "Link"
    ]
    kolom = [k for k in kolom if k in top_laris.columns]

    st.dataframe(
        top_laris[kolom].head(10),
        use_container_width=True
    )

st.divider()

# ==========================================
# PRODUK TERMAHAL
# ==========================================

st.subheader("🏆 Top 10 Produk Termahal")

top_mahal = (
    df
    .sort_values("Harga_Numeric", ascending=False)
    .head(10)
)

kolom = [
    "Nama Produk", "Harga", "Lokasi",
    "Toko", "Rating", "Terjual", "Link"
]
kolom = [k for k in kolom if k in top_mahal.columns]

st.dataframe(
    top_mahal[kolom],
    use_container_width=True
)

st.divider()

# ==========================================
# PRODUK TERMURAH
# ==========================================

st.subheader("💸 Top 10 Produk Termurah")

top_murah = (
    df
    .sort_values("Harga_Numeric")
    .head(10)
)

st.dataframe(
    top_murah[kolom],
    use_container_width=True
)

st.divider()

# ==========================================
# SEARCH
# ==========================================

st.subheader("🔍 Cari Produk")

keyword = st.text_input("Masukkan Nama Produk")

if keyword:
    hasil = df[
        df["Nama Produk"]
        .astype(str)
        .str.contains(keyword, case=False, na=False)
    ]
    st.success(f"Ditemukan {len(hasil)} Produk")
    st.dataframe(hasil, use_container_width=True)

st.divider()

# ==========================================
# FILTER LOKASI
# ==========================================

if "Lokasi" in df.columns:
    st.subheader("📍 Filter Lokasi")

    lokasi_list = st.selectbox(
        "Pilih Lokasi",
        ["Semua"] + sorted(df["Lokasi"].dropna().unique().tolist())
    )

    if lokasi_list != "Semua":
        tampil = df[df["Lokasi"] == lokasi_list]
    else:
        tampil = df
else:
    tampil = df

st.dataframe(tampil, use_container_width=True, height=450)

st.divider()

# ==========================================
# DATASET
# ==========================================

st.subheader("📋 Preview Dataset")
st.dataframe(df, use_container_width=True, height=450)

st.divider()

# ==========================================
# DOWNLOAD
# ==========================================

st.subheader("⬇ Download Dataset")

csv = df.to_csv(index=False).encode("utf-8-sig")

st.download_button(
    "⬇ Download CSV",
    csv,
    "tokopedia_produk.csv",
    "text/csv"
)

st.divider()

# ==========================================
# INSIGHT
# ==========================================

st.subheader("💡 Insight")

c1, c2 = st.columns(2)

produk_mahal = df.loc[df["Harga_Numeric"].idxmax()]
produk_murah = df.loc[df["Harga_Numeric"].idxmin()]

with c1:
    st.success(f"""
🏆 **Produk Termahal**

**{produk_mahal['Nama Produk']}**

Harga: **{produk_mahal['Harga']}**

Lokasi: **{produk_mahal['Lokasi']}**
""")

with c2:
    st.info(f"""
💸 **Produk Termurah**

**{produk_murah['Nama Produk']}**

Harga: **{produk_murah['Harga']}**

Lokasi: **{produk_murah['Lokasi']}**
""")

st.divider()

# ==========================================
# KESIMPULAN
# ==========================================

st.subheader("📌 Kesimpulan")

st.success("""
Web Scraping berhasil dilakukan menggunakan Selenium.

Dataset berhasil memperoleh informasi:
✅ Nama Produk
✅ Harga
✅ Lokasi
✅ Toko
✅ Rating
✅ Terjual
✅ Link Produk

Dataset kemudian dibersihkan sebelum disimpan ke CSV
untuk dianalisis menggunakan Streamlit Dashboard.
""")

st.divider()

# ==========================================
# DATA QUALITY
# ==========================================

st.subheader("📊 Data Quality")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Missing Value", int(df.isnull().sum().sum()))
with c2:
    st.metric("Duplicate Data", int(df.duplicated().sum()))
with c3:
    st.metric("Jumlah Kolom", len(df.columns))

st.divider()

st.caption("© 2026 | Dashboard Scraping Tokopedia")