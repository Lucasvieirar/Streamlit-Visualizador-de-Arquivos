import streamlit as st 
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import io
import os
st.title("Editor de PDF")

tab1, tab2, tab3 = st.tabs([
    "Juntar PDF",
    "Divir PDF",
    "Converter"
])

with tab1:
    st.subheader("Juntar PDF")

    arquivos= st.file_uploader( 
    "Selecione vários PDFs",
    type="pdf",
    accept_multiple_files=True )

    if arquivos:
        ordem = st.multiselect(
            "Esolha a ordem",
            options=[f.name for f in arquivos],
            default=[f.name for f in arquivos]    
        )
        if st.button("Juntar PDF"):
            merger = PdfMerger()

            for nome in ordem:
                for f in arquivos:
                    if f.name == nome:
                        merger.append(f)
            
            output = io.BytesIO()
            merger.write(output)

            st.download_button(
                "Baixar PDF unido",
                data=output.getvalue(),
                file_name="pdf_unido.pdf"
            )

with tab2:
    st.subheader("Dividir PDF")

    pdf_file = st.file_uploader("Envie um PDF", type="pdf", key="split")

    if pdf_file:
        reader = PdfReader(pdf_file)
        total = len(reader.pages)

        st.write(f"Total de páginas: {total}")

        inicio = st.number_input("Página inicial", 1, total, 1)
        fim = st.number_input("Página final", 1, total, total)

        if st.button("Dividir PDF"):
            writer = PdfWriter()

            for i in range(inicio -1, fim):
                writer.add_page(reader.pages[i])
            
            output = io.BytesIO()
            writer.write(output)

            st.download_button(
                "Baixar PDF dividio",
                data=output.getvalue(),
                file_name="pdf_dividido.pdf"
            )

        if st.button("Gerar páginas separadas"):
            for i in range(total):
                writer = PdfWriter()
                writer.add_page(reader.pages[i])

                output = io.BytesIO()
                writer.write(output)

                st.download_button(
                f"Página {i+1}",
                data=output.getvalue(),
                file_name=f"pagina{i+1}.pdf" )