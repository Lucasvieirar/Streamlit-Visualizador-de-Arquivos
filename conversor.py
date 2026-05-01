import streamlit as st
from PIL import Image
import io
st.title('conversor de imagens')


file = st.file_uploader("Converta sua imagem",
        type=['jpg', 'jpeg', 'png', 'webp', 'jfif', 'tiff', 'vg'])

saida = st.selectbox('Escolha o formato de saída: ',
                     ['JPEG', 'PNG']
                     )
if file:
    img = Image.open(file)

    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Imagem original")
        st.image(img)

    with col_right:
        st.subheader(f"Imagem convertida ({saida})")

        convertido = img

        if saida == 'JPEG':
            if img.mode in ('RGBA', 'LA'):
                convertido = img.convert('RGB')
                
        st.image(convertido)

        img_bytes = io.BytesIO()
        convertido.save(img_bytes, format=saida)

        st.download_button(
            label=f'Baixar como {saida}',
            file_name=f'convertido.{saida.lower()}',
            data= img_bytes.getvalue(),
            mime=f'image/{saida.lower()}'
        )

else:
    st.warning('Ainda não tem arquivo')