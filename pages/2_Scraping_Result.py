import streamlit as st
import pandas as pd

# ==========================
# LOAD DATA
# ==========================

df = pd.read_csv("amazone_motorcycle_oil.csv")

st.title("📦 Hasil Scraping & Perbandingan Marketplace")

st.markdown("""
Halaman ini menampilkan hasil eksplorasi Crawlbase
pada Amazon, AliExpress, dan eBay.
""")

# ==========================
# KPI EXPLORATION
# ==========================

st.subheader("📊 Ringkasan Eksplorasi")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Marketplace Diuji", "3")

with col2:
    st.metric("Berhasil", "2")

with col3:
    st.metric("Gagal", "1")

with col4:
    st.metric("Success Rate", "66.7%")

st.divider()

# ==========================
# MARKETPLACE COMPARISON
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
        60,
        0
    ]
})

st.bar_chart(
    comparison_df.set_index("Marketplace")
)

st.info("""
Amazon menghasilkan data paling lengkap.
AliExpress menghasilkan metadata halaman.
eBay gagal karena Error 520.
""")

st.divider()

# ==========================
# AMAZON ANALYSIS
# ==========================

st.header("🛒 Amazon Analysis")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Produk", len(df))

with col2:
    st.metric(
        "Avg Price",
        f"${df['rawPrice'].mean():.2f}"
    )

with col3:
    st.metric(
        "Avg Rating",
        f"{df['rating'].mean():.2f}"
    )

with col4:
    st.metric(
        "Max Review",
        f"{int(df['customerReviewCount'].max()):,}"
    )

st.subheader("🧾 Contoh Output JSON")

st.json({
    "name": df.iloc[0]["name"],
    "price": df.iloc[0]["rawPrice"],
    "rating": df.iloc[0]["rating"],
    "review_count": df.iloc[0]["customerReviewCount"]
})

st.subheader("📈 Top 10 Harga Produk")

price_chart = (
    df.sort_values(
        by="rawPrice",
        ascending=False
    )
    .head(10)
    .set_index("name")
)

st.bar_chart(price_chart["rawPrice"])

st.subheader("⭐ Distribusi Rating")

rating_chart = (
    df.groupby("rating")
    .size()
    .reset_index(name="Jumlah")
    .set_index("rating")
)

st.bar_chart(rating_chart)

st.subheader("📋 Data Produk")

st.dataframe(
    df[
        [
            "name",
            "rawPrice",
            "rating",
            "customerReviewCount"
        ]
    ],
    use_container_width=True
)

st.subheader("🏆 Top 5 Produk Berdasarkan Rating")

top_rating = (
    df.sort_values(
        by="rating",
        ascending=False
    )
    .head(5)
)

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

st.success("""
Amazon menghasilkan data paling lengkap karena
menggunakan Amazon SERP Scraper.
""")

st.divider()

# ==========================
# ALIEXPRESS ANALYSIS
# ==========================

st.header("🛍 AliExpress Analysis")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Status",
        "Berhasil"
    )

with col2:
    st.metric(
        "Data Completeness",
        "60%"
    )

ali_df = pd.DataFrame({
    "Data yang Diperoleh": [
        "Title",
        "Description",
        "Images",
        "Links"
    ],
    "Status": [
        "✅",
        "✅",
        "✅",
        "✅"
    ]
})

st.dataframe(
    ali_df,
    use_container_width=True
)

st.info("""
AliExpress berhasil diekstrak menggunakan
Generic Extractor.

Output yang diperoleh berupa metadata halaman,
bukan data produk terstruktur seperti Amazon.
""")

st.success("""
AliExpress cocok digunakan untuk eksplorasi
konten halaman dan metadata website.
""")

st.divider()

# ==========================
# EBAY ANALYSIS
# ==========================

st.header("🚫 eBay Analysis")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Status",
        "Gagal"
    )

with col2:
    st.metric(
        "Success Rate",
        "0%"
    )

st.error("""
520 Web Server Returned an Unknown Error
""")

st.warning("""
Kemungkinan penyebab:

• Website memiliki proteksi anti-bot

• Tidak tersedia scraper khusus

• Pembatasan akses dari marketplace
""")

st.divider()

# ==========================
# RANKING
# ==========================

st.header("🏆 Ranking Hasil Eksplorasi")

ranking_df = pd.DataFrame({
    "Marketplace": [
        "Amazon",
        "AliExpress",
        "eBay"
    ],
    "Exploration Score": [
        100,
        60,
        0
    ]
})

st.bar_chart(
    ranking_df.set_index("Marketplace")
)

st.divider()

# ==========================
# KESIMPULAN
# ==========================

st.header("📌 Kesimpulan")

st.success("""
Amazon menjadi marketplace dengan hasil scraping terbaik
karena menghasilkan data produk yang lengkap dan siap dianalisis.

AliExpress berhasil dieksplorasi namun hanya menghasilkan
metadata halaman.

eBay gagal diekstrak karena Error 520.

Eksplorasi ini menunjukkan bahwa keberhasilan scraping
bergantung pada jenis scraper yang tersedia serta proteksi
yang digunakan oleh masing-masing marketplace.
""")