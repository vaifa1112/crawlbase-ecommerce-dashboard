import streamlit as st
import pandas as pd

# ==========================
# Load Data
# ==========================

df = pd.read_csv("amazone_motorcycle_oil.csv")

st.title("📊 Business Insight & Analytics")

st.markdown("""
Analisis ini dibuat berdasarkan hasil scraping produk
**Motorcycle Oil** menggunakan Crawlbase.
""")

# ==========================
# Summary Cards
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Harga Rata-rata",
        f"${df['rawPrice'].mean():.2f}"
    )

with col2:
    st.metric(
        "Rating Rata-rata",
        f"{df['rating'].mean():.2f}"
    )

with col3:
    st.metric(
        "Total Produk",
        len(df)
    )

st.divider()

# ==========================
# Marketplace Comparison
# ==========================

st.subheader("🌐 Marketplace Comparison")

comparison_df = pd.DataFrame({
    "Marketplace": [
        "Amazon",
        "AliExpress",
        "eBay"
    ],
    "Data Structure Score": [
        100,
        70,
        0
    ],
    "Scraping Success Rate": [
        100,
        100,
        0
    ]
})

st.bar_chart(
    comparison_df.set_index("Marketplace")
)

st.info("""
Hasil eksplorasi menunjukkan bahwa:

✅ Amazon menghasilkan data produk yang lengkap
(nama produk, harga, rating, review).

✅ AliExpress berhasil discrape menggunakan
Generic Extractor namun hanya menghasilkan
metadata halaman.

❌ eBay gagal diekstrak karena Error 520
sehingga tidak menghasilkan data yang dapat
digunakan untuk analisis.
""")

st.divider()

# ==========================
# Tabs
# ==========================

tab1, tab2, tab3 = st.tabs(
    [
        "💰 Harga",
        "⭐ Rating",
        "📝 Review"
    ]
)

# ==========================
# Harga
# ==========================

with tab1:

    st.subheader("Top 10 Produk Termahal")

    chart = (
        df.sort_values(
            "rawPrice",
            ascending=False
        )
        .head(10)
        .set_index("name")
    )

    st.bar_chart(chart["rawPrice"])

# ==========================
# Rating
# ==========================

with tab2:

    st.subheader("Top 10 Rating Produk")

    chart = (
        df.sort_values(
            "rating",
            ascending=False
        )
        .head(10)
        .set_index("name")
    )

    st.bar_chart(chart["rating"])

# ==========================
# Review
# ==========================

with tab3:

    st.subheader("Top 10 Produk dengan Review Terbanyak")

    chart = (
        df.sort_values(
            "customerReviewCount",
            ascending=False
        )
        .head(10)
        .set_index("name")
    )

    st.bar_chart(chart["customerReviewCount"])

st.divider()

# ==========================
# Key Findings
# ==========================

st.subheader("🔍 Key Findings")

produk_termahal = df.loc[df["rawPrice"].idxmax()]
produk_termurah = df.loc[df["rawPrice"].idxmin()]
produk_rating = df.loc[df["rating"].idxmax()]
produk_review = df.loc[df["customerReviewCount"].idxmax()]

col1, col2 = st.columns(2)

with col1:

    st.success(f"""
🏆 Produk Termahal

**{produk_termahal['name']}**

Harga: ${produk_termahal['rawPrice']:.2f}
""")

    st.info(f"""
💰 Produk Termurah

**{produk_termurah['name']}**

Harga: ${produk_termurah['rawPrice']:.2f}
""")

with col2:

    st.success(f"""
⭐ Rating Tertinggi

**{produk_rating['name']}**

Rating: {produk_rating['rating']}
""")

    st.info(f"""
📝 Review Terbanyak

**{produk_review['name']}**

Review: {int(produk_review['customerReviewCount']):,}
""")

st.divider()

# ==========================
# Business Insights
# ==========================

st.subheader("💡 Business Insights")

st.warning(f"""
1. Rata-rata harga produk berada di kisaran
${df['rawPrice'].mean():.2f}.

2. Mayoritas produk memiliki rating tinggi
dengan rata-rata {df['rating'].mean():.2f}.

3. Produk dengan jumlah review terbesar
cenderung memiliki tingkat kepercayaan
pelanggan yang lebih tinggi.

4. Amazon menghasilkan data paling lengkap
dibanding marketplace lain yang diuji.

5. Crawlbase sangat cocok digunakan untuk
price monitoring, competitor analysis,
dan market research.
""")

st.success("""
Kesimpulan:

Berdasarkan hasil eksplorasi, Amazon merupakan
marketplace yang menghasilkan data paling optimal
karena tersedia scraper khusus yang mampu
menghasilkan data produk terstruktur.

Crawlbase terbukti mampu membantu proses
pengumpulan data e-commerce secara otomatis
dan menghasilkan insight yang dapat digunakan
untuk mendukung pengambilan keputusan bisnis.
""")