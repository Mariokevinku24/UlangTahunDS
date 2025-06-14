import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Konversi CSV ke Excel", layout="wide")
st.title("📤 Konversi CSV ke Excel")

# Upload file CSV
uploaded_file = st.file_uploader("Unggah file CSV", type=["csv"])

if uploaded_file is not None:
    try:
        # Baca isi file
        df = pd.read_csv(uploaded_file)
        st.subheader("📄 Pratinjau Data CSV")
        st.dataframe(df, use_container_width=True)

        # Konversi ke Excel dalam memori (BytesIO)
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Data')
        output.seek(0)  # Kembali ke awal stream

        # Tombol unduh Excel
        st.download_button(
            label="⬇️ Unduh sebagai Excel",
            data=output,
            file_name="data_konversi.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")

