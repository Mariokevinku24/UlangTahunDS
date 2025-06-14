import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Konversi CSV ke Excel")

# Upload file CSV
uploaded_file = st.file_uploader("Unggah file CSV", type=["csv"])

if uploaded_file is not None:
    # Tampilkan isi file
    df = pd.read_csv(uploaded_file)
    st.subheader("Pratinjau Data")
    st.dataframe(df)

    # Konversi ke Excel dalam memori
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Data')
        writer.save()
    processed_data = output.getvalue()

    # Tombol untuk mengunduh file Excel
    st.download_button(
        label="Unduh sebagai Excel",
        data=processed_data,
        file_name="data_konversi.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
