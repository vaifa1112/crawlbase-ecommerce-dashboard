import streamlit as st

st.title("🚀 Crawlbase Overview")

st.markdown("""
## Apa itu Crawlbase?

Crawlbase adalah platform web scraping dan crawling yang membantu pengambilan data website secara otomatis.

### Cara Kerja

Website
⬇️
Crawlbase API
⬇️
JSON Output
⬇️
Analisis Data
⬇️
Dashboard

---
""")

col1,col2,col3 = st.columns(3)

with col1:
    st.metric("Platform", "Crawlbase")

with col2:
    st.metric("Data Source", "Amazon")

with col3:
    st.metric("Kategori", "Motorcycle Oil")

st.subheader("Use Cases")

st.markdown("""
- Monitoring Harga Produk
- Analisis Kompetitor
- Market Research
- Dataset Machine Learning
- Monitoring Tren Produk
""")

st.subheader("Limitasi")

st.warning("""
- Free tier memiliki batas request.
- Tidak semua website dapat discrape dengan mudah.
- Data perlu dibersihkan sebelum dianalisis.
""")