import streamlit as st 
import tempfile
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from pdf2docx import Converter
from docx2pdf import convert
import io
import os
st.title("Editor de PDF")

tab1, tab2, tab3 = st.tabs([
    "Juntar PDF",
    "Dividir PDF",
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



with tab3:
    st.subheader("Converter PDF")

    opcao = st.selectbox(
        "Escolha a conversão:",
        ["PDF → Word", "Word → PDF"]
    )

    arquivo = st.file_uploader("Envie o arquivo")

    if arquivo:

        
        extensao = arquivo.name.split('.')[-1]

        
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=f".{extensao}"
        ) as temp_input:

            temp_input.write(arquivo.read())
            input_path = temp_input.name

        try:

           
            if opcao == "PDF → Word":

                output_path = input_path.replace(".pdf", ".docx")

                cv = Converter(input_path)
                cv.convert(output_path)
                cv.close()

                with open(output_path, "rb") as f:
                    st.download_button(
                        "Baixar Word",
                        data=f,
                        file_name="convertido.docx"
                    )

           
            elif opcao == "Word → PDF":

                output_path = input_path.replace(".docx", ".pdf")

                convert(input_path, output_path)

                with open(output_path, "rb") as f:
                    st.download_button(
                        "Baixar PDF",
                        data=f,
                        file_name="convertido.pdf"
                    )

        except Exception as e:
            st.error(f"Erro: {e}")

       
        finally:

            try:
                os.remove(input_path)
            except:
                pass

            try:
                os.remove(output_path)
            except:
                pass