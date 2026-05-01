import streamlit as st
from PIL import Image, ImageEnhance
import io
st.title('Editor e Conversor de Imagem')


file = st.file_uploader("Converta e edite sua imagem",
        type=['jpg', 'jpeg', 'png', 'webp', 'jfif', 'tiff'])

saida = st.selectbox('Escolha o formato de saída: ',
                     ['JPEG', 'PNG']
                     )
if file:
    img = Image.open(file)

    st.sidebar.header(" ⚙️ Edição")

    largura = st.sidebar.number_input("Largura", value=img.width)
    altura = st.sidebar.number_input("Altura", value=img.height)

    qualidade = st.sidebar.slider("Qualidade (JPEG)", 10, 100, 90)

    preto_branco = st.sidebar.checkbox('Preto e Branco')

    brilho = st.sidebar.slider('Brilho', 0.5, 2.0, 1.0)

    contraste  = st.sidebar.slider('Contraste', 0.5, 2.0, 1.0)

    rotacao = st.sidebar.selectbox('Rotação', [0, 90, 180, 270])


    editada = img

    editada = editada.resize((largura, altura))

    if rotacao != 0:

        editada = editada.rotate(rotacao, expand=True)

    if preto_branco: 
        editada = editada.convert('L')

    enhacer = ImageEnhance.Contrast(editada)
    editada = enhacer.enhance(brilho)

    enhacer = ImageEnhance.Contrast(editada)
    editada = enhacer.enhance(contraste)

    if saida == 'JPEG' and editada.mode in ('RGBA', 'LA'):
        fundo = Image.new("RGB", editada.size, (255, 255, 255))
        fundo.paste(editada, mask=editada.split()[3])
        editada = fundo

    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Imagem original")
        st.image(img)

    with col_right:
        st.subheader(f"Imagem Editada ({saida})")

        
                
        st.image(editada)

        img_bytes = io.BytesIO()
        if saida == 'JPEG':
            editada.save(img_bytes, format='JPEG', quality=qualidade)
        else:
            editada.save(img_bytes, format='PNG')


        st.download_button(
            label=f'Baixar como {saida}',
            file_name=f'convertido.{saida.lower()}',
            data= img_bytes.getvalue(),
            mime=f'image/{saida.lower()}'
        )

else:
    st.warning('Ainda não tem arquivo')