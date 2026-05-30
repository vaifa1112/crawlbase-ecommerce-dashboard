import streamlit as st
import pandas as pd

df = pd.read_csv("motorcycle_oil_clean.csv")

st.title("📊 Business Insight")

tab1,tab2,tab3 = st.tabs(
    [
        "Harga",
        "Rating",
        "Review"
    ]
)

with tab1:

    st.subheader("Top 10 Harga Produk")

    chart = (
        df.sort_values(
            "rawPrice",
            ascending=False
        )
        .head(10)
        .set_index("name")
    )

    st.bar_chart(chart["rawPrice"])

with tab2:

    st.subheader("Top Rating Produk")

    chart = (
        df.sort_values(
            "rating",
            ascending=False
        )
        .head(10)
        .set_index("name")
    )

    st.bar_chart(chart["rating"])

with tab3:

    st.subheader("Produk dengan Review Terbanyak")

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

st.subheader("Key Insights")

produk_termahal = df.loc[df["rawPrice"].idxmax()]
produk_termurah = df.loc[df["rawPrice"].idxmin()]
produk_rating = df.loc[df["rating"].idxmax()]

st.success(f"""
🏆 Produk dengan harga tertinggi:
{produk_termahal['name']}

💰 Produk dengan harga terendah:
{produk_termurah['name']}

⭐ Produk dengan rating tertinggi:
{produk_rating['name']}
""")