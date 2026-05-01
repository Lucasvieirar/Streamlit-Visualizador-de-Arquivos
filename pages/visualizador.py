import streamlit as st 
from pandas import read_csv

st.title("Visualizador de arquivos")


file = st.file_uploader(
    label='Suba seu arquivo aqui!',
    
)

if file: 
    if file.type == 'text/plain':
        st.text(file.read().decode())
    elif file.type == 'aplication/json':
        st.json(file.read().decode())
    elif file.type == 'image/jpeg':
        st.image(file)
    elif file.type == 'text/csv':
        df = read_csv(file)
        st.dataframe(df)
    elif file.type == 'text/x-python':
        st.code(file.read().decode(), language='python')
    elif file.type == 'audio/mpeg':
        st.audio(file)
    elif file.type == 'video/mp4':
        st.video(file)
    else:
        st.error('Formato de arquivo não suportado!')

else:
    st.warning("Ainda não tenho arquivo")