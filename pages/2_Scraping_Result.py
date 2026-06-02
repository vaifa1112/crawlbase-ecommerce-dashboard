import streamlit as st
import pandas as pd

# ==========================
# Load Data
# ==========================

df = pd.read_csv("amazone_motorcycle_oil.csv")

st.title("📦 Hasil Scraping Amazon Marketplace")

st.markdown("""
Halaman ini menampilkan hasil scraping produk **Motorcycle Oil**
menggunakan **Crawlbase Amazon SERP Scraper**.
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
        "Harga Rata-rata",
        f"${df['rawPrice'].mean():.2f}"
    )

with col3:
    st.metric(
        "Rating Rata-rata",
        f"{df['rating'].mean():.2f}"
    )

with col4:
    st.metric(
        "Review Tertinggi",
        f"{int(df['customerReviewCount'].max()):,}"
    )

st.divider()

# ==========================
# Preview JSON
# ==========================

st.subheader("🧾 Contoh Output Crawlbase")

contoh_json = {
    "name": df.iloc[0]["name"],
    "price": df.iloc[0]["rawPrice"],
    "rating": df.iloc[0]["rating"],
    "review_count": df.iloc[0]["customerReviewCount"]
}

st.json(contoh_json)

st.divider()

# ==========================
# Filter
# ==========================

st.subheader("🔍 Filter Produk")

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

# ==========================
# Data Table
# ==========================

st.subheader("📋 Data Produk")

st.dataframe(
    filtered_df,
    use_container_width=True
)

st.divider()

# ==========================
# Top Products
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

st.success("""
Data berhasil diperoleh menggunakan Crawlbase Amazon SERP Scraper
dan telah dikonversi ke format CSV untuk analisis lebih lanjut.
""")