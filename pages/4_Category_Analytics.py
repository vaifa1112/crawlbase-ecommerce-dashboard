import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Category Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Category Analytics Tokopedia")

# =====================
# Load Data
# =====================

files = [
    "Aksesoris_Motor.csv",
    "Helm_Motor.csv",
    "Oli_Motor.csv",
    "Perkakas_Kendaraan.csv",
    "sparepart_motor.csv"
]

df = pd.concat(
    [pd.read_csv(file) for file in files],
    ignore_index=True
)

# =====================
# KPI
# =====================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Kategori",
        len(df)
    )

with col2:
    st.metric(
        "Total Gambar",
        int(df["Image_Count"].sum())
    )

with col3:
    st.metric(
        "Total Link",
        int(df["Link_Count"].sum())
    )

with col4:
    st.metric(
        "Rata-rata Gambar",
        round(df["Image_Count"].mean(), 2)
    )

st.divider()

# =====================
# Grafik Gambar
# =====================

st.subheader("🖼️ Jumlah Gambar per Kategori")

chart1 = (
    df.set_index("Title")
)

st.bar_chart(
    chart1["Image_Count"]
)

# =====================
# Grafik Link
# =====================

st.subheader("🔗 Jumlah Link per Kategori")

st.bar_chart(
    chart1["Link_Count"]
)

st.divider()

# =====================
# Top Category
# =====================

top_img = df.loc[df["Image_Count"].idxmax()]
top_link = df.loc[df["Link_Count"].idxmax()]

col1, col2 = st.columns(2)

with col1:
    st.success(f"""
🏆 Kategori dengan Gambar Terbanyak

**{top_img['Title']}**

Jumlah Gambar: {top_img['Image_Count']}
""")

with col2:
    st.success(f"""
🔥 Kategori dengan Link Terbanyak

**{top_link['Title']}**

Jumlah Link: {top_link['Link_Count']}
""")

st.divider()

# =====================
# Data Table
# =====================

st.subheader("📋 Dataset Kategori")

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

st.info("""
Saat ini data yang berhasil diperoleh dari Tokopedia masih berupa
metadata halaman (title, description, image count, dan link count).

Untuk menghasilkan analisis harga, rating, produk termahal,
dan kategori paling populer diperlukan data produk yang lebih detail.
""")