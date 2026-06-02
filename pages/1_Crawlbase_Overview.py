import streamlit as st

st.set_page_config(
    page_title="Crawlbase Overview",
    page_icon="🚀"
)

st.title("🚀 Eksplorasi Crawlbase untuk Scraping Data E-Commerce Otomotif")

st.markdown("""
Dashboard ini dibuat sebagai bagian dari eksplorasi penggunaan **Crawlbase**
untuk pengambilan data e-commerce pada kategori **Motorcycle Oil**.

### Tujuan Eksplorasi

✅ Memahami penggunaan Crawlbase

✅ Menguji scraping data marketplace

✅ Mengolah hasil scraping menjadi insight bisnis

✅ Mengetahui batasan dan potensi penggunaan Crawlbase
""")

st.divider()

st.subheader("📌 Ringkasan Proyek")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Platform", "Crawlbase")

with col2:
    st.metric("Kategori", "Motorcycle Oil")

with col3:
    st.metric("Output", "JSON & CSV")

st.divider()

st.subheader("⚙️ Workflow Proyek")

st.code("""
Amazon Marketplace
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
""", language="text")

st.divider()

st.subheader("🌐 Marketplace yang Dieksplorasi")

marketplace_data = {
    "Marketplace": ["Amazon", "AliExpress", "eBay"],
    "Status": ["✅ Berhasil", "✅ Berhasil", "❌ Gagal"],
    "Keterangan": [
        "Menghasilkan data produk terstruktur",
        "Menghasilkan metadata halaman",
        "Error 520 saat scraping"
    ]
}

st.table(marketplace_data)

st.info("""
Hasil eksplorasi menunjukkan bahwa kualitas data yang diperoleh
bergantung pada jenis scraper yang tersedia dan proteksi website.
""")

st.divider()

st.subheader("💼 Use Cases Crawlbase")

st.markdown("""
- Monitoring Harga Produk
- Analisis Kompetitor
- Market Research
- Monitoring Tren Produk
- Product Intelligence
- Dataset Machine Learning
""")

st.divider()

st.subheader("⚠️ Limitasi yang Ditemukan")

st.warning("""
1. Free tier memiliki batas request.

2. Tidak semua marketplace memiliki scraper khusus.

3. Beberapa website memiliki proteksi anti-bot.

4. Data hasil scraping perlu dibersihkan sebelum dianalisis.
""")

st.divider()

st.subheader("📌 Kesimpulan")

st.success("""
Crawlbase efektif untuk mengumpulkan data e-commerce secara otomatis
dan menghasilkan data yang siap dianalisis, terutama pada website
yang didukung oleh scraper khusus seperti Amazon.
""")