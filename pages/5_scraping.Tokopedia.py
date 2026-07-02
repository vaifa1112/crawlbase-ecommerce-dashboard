import streamlit as st
import pandas as pd

st.set_page_config(page_title="Metodologi Scraping",layout="wide")

st.title("📦 Metodologi Web Scraping Tokopedia")

st.markdown("---")

st.subheader("Alur Pengambilan Data")

st.graphviz_chart("""

digraph {

rankdir=LR

A[label="Tokopedia"]

B[label="Selenium"]

C[label="Auto Scroll"]

D[label="Parsing HTML"]

E[label="Extract Data"]

F[label="Data Cleaning"]

G[label="CSV / Excel"]

A->B
B->C
C->D
D->E
E->F
F->G

}

""")

st.markdown("---")

st.subheader("Penjelasan Tahapan")

col1,col2=st.columns(2)

with col1:

    st.info("""
**1. Selenium**

Membuka website Tokopedia secara otomatis menggunakan browser Chrome.
""")

    st.info("""
**2. Auto Scroll**

Melakukan scroll hingga seluruh produk pada halaman dimuat.
""")

    st.info("""
**3. Parsing HTML**

Mengambil source HTML setelah halaman selesai dimuat.
""")

with col2:

    st.success("""
**4. Extract Data**

Mengambil:

- Nama Produk
- Harga
- Lokasi
- Link Produk
""")

    st.success("""
**5. Data Cleaning**

Menghapus data kosong dan duplikat.
""")

    st.success("""
**6. Export**

Dataset disimpan menjadi CSV dan Excel.
""")

st.markdown("---")

st.subheader("Dataset")

df=pd.read_excel("tokopedia_aksesorisPengendara.xlsx")

st.dataframe(df,use_container_width=True)

st.markdown("---")

st.metric("Total Produk",len(df))

st.metric("Jumlah Kolom",len(df.columns))

st.metric("Lokasi Unik",df["Lokasi"].nunique())

st.markdown("---")

st.subheader("Distribusi Lokasi")

lokasi=df["Lokasi"].value_counts().head(10)

st.bar_chart(lokasi)

st.markdown("---")

st.subheader("Pencarian Produk")

keyword=st.text_input("Cari Nama Produk")

if keyword:

    hasil=df[df["Nama Produk"].str.contains(keyword,case=False)]

    st.dataframe(hasil,use_container_width=True)

st.markdown("---")

csv=df.to_csv(index=False).encode("utf-8-sig")

st.download_button(

"⬇ Download CSV",

csv,

file_name="tokopedia.csv",

mime="text/csv"

)

with open("tokopedia_aksesorisPengendara.xlsx","rb") as file:

    st.download_button(

        "⬇ Download Excel",

        file,

        file_name="tokopedia.xlsx"

    )