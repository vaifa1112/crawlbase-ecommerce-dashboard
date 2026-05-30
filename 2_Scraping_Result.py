import streamlit as st
import pandas as pd

df = pd.read_csv("motorcycle_oil_clean.csv")

st.title("📦 Scraping Result")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Total Produk", len(df))

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
        "Review Maksimum",
        f"{int(df['customerReviewCount'].max()):,}"
    )

st.divider()

st.subheader("Data Produk")

st.dataframe(
    df,
    use_container_width=True
)