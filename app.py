import streamlit as st

st.set_page_config(
    page_title="Crawlbase E-Commerce Analytics",
    page_icon="🏍️",
    layout="wide"
)

st.title("🏍️ Crawlbase E-Commerce Analytics Dashboard")

st.markdown("""
### Eksplorasi Platform Crawlbase untuk Scraping Data E-Commerce Otomotif

Dashboard ini dibuat untuk menunjukkan:

✅ Eksplorasi penggunaan Crawlbase

✅ Hasil scraping data e-commerce

✅ Analisis dan insight bisnis

---

Silakan pilih halaman pada sidebar.
""")

st.image(
    "https://images.unsplash.com/photo-1558981806-ec527fa84c39",
    use_container_width=True
)

st.info(
    "Data diperoleh menggunakan Crawlbase API dari hasil pencarian produk Motorcycle Oil pada marketplace Amazon."
)