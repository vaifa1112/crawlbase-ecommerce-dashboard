import streamlit as st
import pandas as pd

# ==========================
# Load Data Amazon
# ==========================

df = pd.read_csv("amazone_motorcycle_oil.csv")

st.title("📦 Hasil Scraping & Eksplorasi Marketplace")

st.markdown("""
Halaman ini menampilkan hasil eksplorasi Crawlbase pada beberapa marketplace
serta hasil scraping produk **Motorcycle Oil** menggunakan
**Amazon SERP Scraper**.
""")

# ==========================
# KPI
# ==========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Produk",
        len(df)
    )

with col2:
    st.metric(
        "Harga Rata-Rata",
        f"${df['rawPrice'].mean():.2f}"
    )

with col3:
    st.metric(
        "Rating Rata-Rata",
        f"{df['rating'].mean():.2f}"
    )

with col4:
    st.metric(
        "Review Tertinggi",
        f"{int(df['customerReviewCount'].max()):,}"
    )

st.divider()

# ==========================
# Marketplace Comparison
# ==========================

st.subheader("🌐 Perbandingan Marketplace")

comparison_df = pd.DataFrame({
    "Marketplace": [
        "Amazon",
        "AliExpress",
        "eBay"
    ],
    "Scraping Success": [
        100,
        100,
        0
    ],
    "Data Completeness": [
        100,
        70,
        0
    ]
})

st.bar_chart(
    comparison_df.set_index("Marketplace")
)

st.info("""
Amazon menghasilkan data produk yang lengkap.
AliExpress berhasil diekstrak menggunakan Generic Extractor.
eBay gagal diekstrak karena Error 520.
""")

st.divider()

# ==========================
# Marketplace Result Table
# ==========================

st.subheader("📊 Ringkasan Hasil Eksplorasi")

marketplace_result = pd.DataFrame({
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
    "Output": [
        "Nama Produk, Harga, Rating, Review",
        "Title, Description, Images, Links",
        "Error 520"
    ]
})

st.dataframe(
    marketplace_result,
    use_container_width=True
)

st.divider()

# ==========================
# Output Comparison
# ==========================

st.subheader("📑 Output yang Dihasilkan")

output_df = pd.DataFrame({
    "Marketplace": [
        "Amazon",
        "AliExpress",
        "eBay"
    ],
    "Jenis Data": [
        "Structured Product Data",
        "Page Metadata",
        "Tidak Berhasil"
    ]
})

st.dataframe(
    output_df,
    use_container_width=True
)

st.divider()

# ==========================
# Preview JSON
# ==========================

st.subheader("🧾 Contoh Output JSON Amazon")

contoh_json = {
    "name": df.iloc[0]["name"],
    "price": df.iloc[0]["rawPrice"],
    "rating": df.iloc[0]["rating"],
    "review_count": df.iloc[0]["customerReviewCount"]
}

st.json(contoh_json)

st.divider()

# ==========================
# Filter Produk
# ==========================

st.subheader("🔍 Filter Produk Amazon")

min_harga = int(df["rawPrice"].min())
max_harga = int(df["rawPrice"].max())

harga_range = st.slider(
    "Pilih Rentang Harga",
    min_harga,
    max_harga,
    (min_harga, max_harga)
)

filtered_df = df[
    (df["rawPrice"] >= harga_range[0]) &
    (df["rawPrice"] <= harga_range[1])
]

st.divider()

# ==========================
# Data Produk
# ==========================

st.subheader("📋 Data Produk Amazon")

st.dataframe(
    filtered_df,
    use_container_width=True
)

st.divider()

# ==========================
# Top Product
# ==========================

st.subheader("🏆 Top 5 Produk Berdasarkan Rating")

top_rating = filtered_df.sort_values(
    by="rating",
    ascending=False
).head(5)

st.dataframe(
    top_rating[
        [
            "name",
            "rawPrice",
            "rating",
            "customerReviewCount"
        ]
    ],
    use_container_width=True
)

st.divider()

# ==========================
# Temuan Eksplorasi
# ==========================

st.subheader("🔍 Temuan Eksplorasi")

st.success("""
1. Amazon menghasilkan data paling lengkap karena tersedia scraper khusus.

2. AliExpress berhasil dieksplorasi menggunakan Generic Extractor,
   namun output yang diperoleh masih berupa metadata halaman.

3. eBay tidak berhasil diekstrak karena Error 520 yang menunjukkan
   adanya proteksi atau keterbatasan scraper.

4. Keberhasilan scraping sangat dipengaruhi oleh jenis scraper
   dan struktur website yang digunakan.
""")

st.divider()

# ==========================
# Kesimpulan
# ==========================

st.subheader("📌 Kesimpulan")

st.success("""
Crawlbase berhasil digunakan untuk mengumpulkan data e-commerce
secara otomatis.

Amazon menjadi marketplace dengan hasil scraping terbaik karena
menghasilkan data produk yang lengkap dan siap dianalisis.

Eksplorasi ini menunjukkan bahwa Crawlbase dapat dimanfaatkan
untuk monitoring harga, analisis kompetitor, market research,
serta pengumpulan dataset untuk kebutuhan Data Analytics dan
Machine Learning.
""")