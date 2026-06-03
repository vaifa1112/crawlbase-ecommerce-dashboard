import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Crawlbase Overview",
    page_icon="🚀",
    layout="wide"
)

# ==========================
# HEADER
# ==========================

st.title("🚀 Eksplorasi Crawlbase untuk Scraping Data E-Commerce Otomotif")

st.markdown("""
Dashboard ini dibuat untuk mengeksplorasi penggunaan **Crawlbase**
dalam pengambilan data e-commerce kategori **Motorcycle Oil**
serta menganalisis potensi penggunaannya dalam monitoring harga,
analisis kompetitor, dan market research.
""")

st.divider()

# ==========================
# KPI
# ==========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Platform",
        "Crawlbase"
    )

with col2:
    st.metric(
        "Marketplace",
        "3"
    )

with col3:
    st.metric(
        "Output",
        "JSON & CSV"
    )

with col4:
    st.metric(
        "Kategori",
        "Motorcycle Oil"
    )

st.divider()

# ==========================
# TUJUAN
# ==========================

st.subheader("🎯 Tujuan Eksplorasi")

st.markdown("""
- Memahami penggunaan Crawlbase
- Menguji scraping data marketplace
- Mengolah hasil scraping menjadi insight bisnis
- Mengetahui batasan dan potensi penggunaan Crawlbase
""")

st.divider()

# ==========================
# WORKFLOW
# ==========================

st.subheader("⚙️ Workflow Proyek")

st.code("""
Amazon / AliExpress / eBay
            ↓
       Crawlbase API
            ↓
        JSON Output
            ↓
      Data Cleaning
            ↓
            CSV
            ↓
 Interactive Dashboard
""")

st.divider()

# ==========================
# SUCCESS RATE
# ==========================

st.subheader("📈 Tingkat Keberhasilan Eksplorasi")

success_df = pd.DataFrame({
    "Marketplace": [
        "Amazon",
        "AliExpress",
        "eBay"
    ],
    "Success Rate (%)": [
        100,
        100,
        0
    ]
})

st.bar_chart(
    success_df.set_index("Marketplace")
)

st.divider()

# ==========================
# MARKETPLACE COMPARISON
# ==========================

st.subheader("🌐 Perbandingan Marketplace")

marketplace_data = pd.DataFrame({
    "Marketplace": [
        "Amazon",
        "AliExpress",
        "eBay"
    ],
    "Status": [
        "✅ Berhasil",
        "✅ Berhasil",
        "❌ Gagal"
    ],
    "Output Data": [
        "Produk, Harga, Rating, Review",
        "Title, Description, Images, Links",
        "Error 520"
    ]
})

st.dataframe(
    marketplace_data,
    use_container_width=True
)

comparison_df = pd.DataFrame({
    "Marketplace": [
        "Amazon",
        "AliExpress",
        "eBay"
    ],
    "Data Completeness": [
        100,
        70,
        0
    ]
})

st.subheader("📊 Kelengkapan Data Hasil Scraping")

st.bar_chart(
    comparison_df.set_index("Marketplace")
)

st.info("""
Interpretasi:

✅ Amazon menghasilkan data paling lengkap karena menggunakan
Amazon SERP Scraper.

✅ AliExpress berhasil diekstrak menggunakan Generic Extractor,
namun data yang diperoleh masih berupa metadata halaman.

❌ eBay mengalami Error 520 sehingga data tidak berhasil diperoleh.
""")

st.divider()

# ==========================
# USE CASE
# ==========================

st.subheader("💼 Use Cases Crawlbase")

col1, col2 = st.columns(2)

with col1:
    st.success("""
📈 Monitoring Harga Produk

📊 Analisis Kompetitor

🔍 Market Research
""")

with col2:
    st.success("""
📉 Monitoring Tren Produk

🤖 Dataset Machine Learning

🛍 Product Intelligence
""")

st.divider()

# ==========================
# LIMITASI
# ==========================

st.subheader("⚠️ Limitasi yang Ditemukan")

st.warning("""
1. Free tier memiliki batas request.

2. Tidak semua marketplace memiliki scraper khusus.

3. Beberapa website memiliki proteksi anti-bot.

4. Data hasil scraping perlu dibersihkan sebelum dianalisis.

5. Kualitas output sangat bergantung pada jenis scraper yang tersedia.
""")

st.divider()

# ==========================
# FINDINGS
# ==========================

st.subheader("🔍 Temuan Eksplorasi")

st.success("""
1. Amazon memberikan hasil scraping terbaik karena menghasilkan
   data produk yang lengkap dan terstruktur.

2. AliExpress berhasil dieksplorasi namun hanya menghasilkan
   metadata halaman menggunakan Generic Extractor.

3. eBay tidak berhasil diekstrak karena Error 520.

4. Crawlbase sangat efektif digunakan untuk monitoring harga,
   market research, dan competitor analysis pada marketplace
   yang didukung scraper khusus.
""")

st.divider()

# ==========================
# KESIMPULAN
# ==========================

st.subheader("📌 Kesimpulan")

st.success("""
Berdasarkan hasil eksplorasi yang dilakukan, Crawlbase berhasil
digunakan untuk mengumpulkan data e-commerce secara otomatis.

Amazon menjadi marketplace dengan hasil terbaik karena menghasilkan
data produk yang lengkap (harga, rating, review, dan nama produk).

Eksplorasi ini menunjukkan bahwa Crawlbase dapat dimanfaatkan
untuk monitoring harga, analisis kompetitor, market research,
serta pengumpulan dataset untuk kebutuhan Data Analytics dan
Machine Learning.
""")