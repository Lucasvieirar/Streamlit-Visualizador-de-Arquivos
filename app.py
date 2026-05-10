import streamlit as st

st.set_page_config(page_title="Arquivos", page_icon="📁")
st.title("Bem-Vindo ao seu Editor e Conversor de arquivos")


col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("Visualizador de arquivos")
        st.write("Visualize seus arquivos de maneira limpa")
        if st.button("Visualize", key="visualizar"):
            st.switch_page("pages/visualizador.py")
        

with col2:
    with st.container(border=True):
        st.subheader("Editor e Conversão de imagens")
        st.write("Edite suas imagens e converta para JPG e PNG")
        if st.button("Editar", key="editar_img"):
            st.switch_page("pages/image.py")

col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        st.subheader("Editor e Conversão de vídeos")
        st.write("Edite seus vídeos e converta para MP3 e MP4")
        if st.button("Editar", key="editar_video"):
            st.switch_page("pages/video.py")

with col4:
    with st.container(border=True):
        st.subheader("Editor de PDF")
        st.write("Edite seus PDFs")
        if st.button("Editar", key="editar_pdf"):
            st.switch_page("pages/pdf.py")