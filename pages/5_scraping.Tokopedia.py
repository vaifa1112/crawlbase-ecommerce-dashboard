import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="Scraping Tokopedia",
    page_icon="🛒",
    layout="wide"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
}

.kpi{
    background:#0F172A;
    padding:18px;
    border-radius:15px;
    color:white;
    text-align:center;
}

.title{
    font-size:42px;
    font-weight:bold;
}

.sub{
    color:gray;
    font-size:17px;
}

</style>
""",unsafe_allow_html=True)

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():

    possible_files = [

        "tokopedia_produk.csv",

        "Tokopedia_produk.csv",

        "tokopedia_produk(percobaan)(1).csv",

        "data/tokopedia_produk.csv"

    ]

    for file in possible_files:

        if Path(file).exists():

            return pd.read_csv(file)

    st.error("CSV tidak ditemukan.")

    st.stop()

df = load_data()

# =====================================================
# CLEANING
# =====================================================

df["Harga_Numeric"] = (

    df["Harga"]

    .astype(str)

    .str.replace("Rp","",regex=False)

    .str.replace(".","",regex=False)

    .str.replace(",","",regex=False)

)

df["Harga_Numeric"] = pd.to_numeric(

    df["Harga_Numeric"],

    errors="coerce"

)

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class='title'>
🛒 Scraping Tokopedia Menggunakan Selenium
</div>

<div class='sub'>
Dashboard ini menampilkan hasil scraping produk Tokopedia
menggunakan Selenium dan BeautifulSoup.
</div>
""",unsafe_allow_html=True)

st.divider()

# =====================================================
# WORKFLOW
# =====================================================

st.subheader("🔄 Workflow Scraping")

c1,c2,c3,c4,c5,c6,c7 = st.columns(7)

with c1:
    st.success("🛒\n\nTokopedia")

with c2:
    st.markdown("<h1 style='text-align:center;'>➡️</h1>",unsafe_allow_html=True)

with c3:
    st.success("🤖\n\nSelenium")

with c4:
    st.markdown("<h1 style='text-align:center;'>➡️</h1>",unsafe_allow_html=True)

with c5:
    st.success("📜\n\nHTML")

with c6:
    st.markdown("<h1 style='text-align:center;'>➡️</h1>",unsafe_allow_html=True)

with c7:
    st.success("💾\n\nCSV")

st.info("""

Tahapan scraping:

1. Membuka halaman Tokopedia menggunakan Selenium.

2. Melakukan auto scroll agar seluruh produk muncul.

3. Mengambil source HTML halaman.

4. Mengekstrak Nama Produk, Harga, Lokasi, Rating,
Terjual, dan Link Produk.

5. Membersihkan data.

6. Menyimpan hasil ke CSV.

""")

st.divider()

# =====================================================
# KPI
# =====================================================

st.subheader("📊 Ringkasan Dataset")

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.metric(

        "Jumlah Produk",

        len(df)

    )

with c2:

    st.metric(

        "Lokasi",

        df["Lokasi"].nunique()

    )

with c3:

    st.metric(

        "Harga Rata-rata",

        f"Rp {int(df['Harga_Numeric'].mean()):,}"

    )

with c4:

    st.metric(

        "Harga Maksimum",

        f"Rp {int(df['Harga_Numeric'].max()):,}"

    )

st.divider()

# =====================================================
# GRAFIK HARGA
# =====================================================

st.subheader("💰 Distribusi Harga Produk")

fig_harga = px.histogram(

    df,

    x="Harga_Numeric",

    nbins=30,

    title="Sebaran Harga Produk"

)

fig_harga.update_layout(

    template="plotly_dark",

    height=450

)

st.plotly_chart(

    fig_harga,

    use_container_width=True

)

st.divider()

# =====================================================
# LOKASI
# =====================================================

st.subheader("📍 Top 10 Lokasi Penjual")

lokasi = (

    df["Lokasi"]

    .fillna("Tidak Diketahui")

    .value_counts()

    .reset_index()

)

lokasi.columns=[

    "Lokasi",

    "Jumlah"

]

fig_lokasi = px.bar(

    lokasi.head(10),

    x="Lokasi",

    y="Jumlah",

    color="Jumlah",

    text="Jumlah"

)

fig_lokasi.update_layout(

    template="plotly_dark",

    height=450,

    showlegend=False

)

st.plotly_chart(

    fig_lokasi,

    use_container_width=True

)

st.divider()

# =====================================================
# PIE LOKASI
# =====================================================

st.subheader("🥧 Persentase Lokasi")

fig_pie = px.pie(

    lokasi.head(10),

    names="Lokasi",

    values="Jumlah",

    hole=.5

)

fig_pie.update_layout(

    template="plotly_dark",

    height=500

)

st.plotly_chart(

    fig_pie,

    use_container_width=True

)

st.divider()

# =====================================================
# PRODUK TERMAHAL
# =====================================================

st.subheader("🏆 Top 10 Produk Termahal")

top_mahal = (

    df

    .sort_values(

        "Harga_Numeric",

        ascending=False

    )

    .head(10)

)

st.dataframe(

    top_mahal[

        [

            "Nama Produk",

            "Harga",

            "Lokasi",

            "Rating",

            "Terjual"

        ]

    ],

    use_container_width=True

)

st.divider()

# =====================================================
# PRODUK TERMURAH
# =====================================================

st.subheader("💸 Top 10 Produk Termurah")

top_murah=(

    df

    .sort_values(

        "Harga_Numeric"

    )

    .head(10)

)

st.dataframe(

    top_murah[

        [

            "Nama Produk",

            "Harga",

            "Lokasi",

            "Rating",

            "Terjual"

        ]

    ],

    use_container_width=True

)

st.divider()

# =====================================================
# RATING
# =====================================================

if "Rating" in df.columns:

    st.subheader("⭐ Distribusi Rating")

    rating=(

        df["Rating"]

        .fillna("-")

        .value_counts()

        .reset_index()

    )

    rating.columns=[

        "Rating",

        "Jumlah"

    ]

    fig_rating = px.bar(

        rating,

        x="Rating",

        y="Jumlah",

        color="Jumlah",

        text="Jumlah"

    )

    fig_rating.update_layout(

        template="plotly_dark",

        height=450,

        showlegend=False

    )

    st.plotly_chart(

        fig_rating,

        use_container_width=True

    )

st.divider()

# =====================================================
# TERJUAL
# =====================================================

if "Terjual" in df.columns:

    st.subheader("🔥 Top 10 Produk Terlaris")

    top_laris = df.copy()

    top_laris["Terjual"] = (

        top_laris["Terjual"]

        .astype(str)

        .str.replace("rb","000")

        .str.replace("+","")

    )

    st.dataframe(

        top_laris.head(10),

        use_container_width=True

    )

st.divider()

# =====================================================
# SEARCH PRODUK
# =====================================================

st.subheader("🔍 Pencarian Produk")

keyword = st.text_input(
    "Masukkan nama produk yang ingin dicari"
)

if keyword:

    hasil = df[
        df["Nama Produk"]
        .astype(str)
        .str.contains(
            keyword,
            case=False,
            na=False
        )
    ]

    st.success(f"Ditemukan {len(hasil)} produk")

    st.dataframe(
        hasil,
        use_container_width=True
    )

st.divider()

# =====================================================
# FILTER LOKASI
# =====================================================

st.subheader("📍 Filter Berdasarkan Lokasi")

lokasi_option = st.selectbox(

    "Pilih Lokasi",

    ["Semua"] +

    sorted(df["Lokasi"].fillna("-").unique())

)

if lokasi_option != "Semua":

    tampil = df[
        df["Lokasi"] == lokasi_option
    ]

else:

    tampil = df

st.dataframe(

    tampil,

    use_container_width=True,

    height=450

)

st.divider()

# =====================================================
# DATASET PREVIEW
# =====================================================

st.subheader("📄 Preview Dataset")

st.dataframe(

    df,

    use_container_width=True,

    height=500

)

st.divider()

# =====================================================
# MISSING VALUE
# =====================================================

st.subheader("📋 Kualitas Dataset")

missing = pd.DataFrame({

    "Kolom":df.columns,

    "Missing Value":df.isnull().sum().values

})

st.dataframe(

    missing,

    use_container_width=True

)

st.divider()

# =====================================================
# DOWNLOAD
# =====================================================

st.subheader("⬇ Download Dataset")

c1,c2 = st.columns(2)

csv = df.to_csv(

    index=False

).encode(

    "utf-8-sig"

)

with c1:

    st.download_button(

        "⬇ Download CSV",

        csv,

        file_name="tokopedia_produk.csv",

        mime="text/csv"

    )

with c2:

    excel = df.to_excel(
        "tokopedia_export.xlsx",
        index=False
    )

    with open(
        "tokopedia_export.xlsx",
        "rb"
    ) as file:

        st.download_button(

            "⬇ Download Excel",

            file,

            file_name="tokopedia_export.xlsx",

            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        )

st.divider()

# =====================================================
# INSIGHT
# =====================================================

st.subheader("💡 Insight Hasil Scraping")

produk_termahal = df.loc[
    df["Harga_Numeric"].idxmax()
]

produk_termurah = df.loc[
    df["Harga_Numeric"].idxmin()
]

c1,c2 = st.columns(2)

with c1:

    st.success(f"""

🏆 Produk Termahal

**{produk_termahal['Nama Produk']}**

Harga : {produk_termahal['Harga']}

Lokasi : {produk_termahal['Lokasi']}

""")

with c2:

    st.info(f"""

💸 Produk Termurah

**{produk_termurah['Nama Produk']}**

Harga : {produk_termurah['Harga']}

Lokasi : {produk_termurah['Lokasi']}

""")

st.divider()

st.subheader("📌 Kesimpulan")

st.success("""

Scraping berhasil dilakukan menggunakan Selenium
dan BeautifulSoup.

Dataset yang diperoleh terdiri dari informasi
Nama Produk, Harga, Lokasi, Rating, Terjual,
serta Link Produk.

Data telah dibersihkan kemudian disimpan
ke dalam format CSV sehingga siap digunakan
untuk proses analisis maupun visualisasi
pada dashboard Streamlit.

Dashboard ini dapat membantu proses
monitoring harga produk, analisis lokasi
penjual, pencarian produk, serta eksplorasi
hasil scraping secara interaktif.

""")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "© 2026 | Web Scraping Tokopedia Dashboard | v"
)