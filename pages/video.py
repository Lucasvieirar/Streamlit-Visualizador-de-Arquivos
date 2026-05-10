import streamlit as st 
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import tempfile
import os

st.title("Editor e conversor de video")

st.subheader("Converter arquivos de vídeo e áudio")

arquivo = st.file_uploader(
    "Envie seu arquivo",
    type=['mp4',
        'mp3',
        'avi',
        'mov',
        'mkv',
        'wav',
        'webm'
        ]
)

formato_saida = st.selectbox(
    "Escolha o formato de saída",
    ['MP4', 'MP3']
)
if arquivo:
    st.success(f"Arquivo carregado: {arquivo.name}")

    extensao = arquivo.name.split('.')[-1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=f".{extensao}"
    ) as temp_input:
        
        temp_input.write(arquivo.read())
        input_path = temp_input.name

    
    output_path= input_path.split('.')[0]

    try : 
        if formato_saida == 'MP3':
            
            output_path += ".mp3"

            video = VideoFileClip(input_path)

            video.audio.write_audiofile(output_path)

            with open(output_path, "rb") as f:
                st.download_button(
                    "Bixar mp3",
                    data=f,
                    file_name="convertido.mp3",
                    mime="audio/mp3"
                )
        elif formato_saida == "MP4":
            output_path += ".mp4"

            if extensao in ['mp3', 'wav']:
                audio = AudioFileClip(input_path)

                from moviepy.video.VideoClip import ColorClip

                video = ColorClip(
                    size=(1280, 720),
                    color = (0,0,0),
                    duration=audio.duration
                )

                video = video.set_audio(audio)

                video.write_videofile(
                    output_path,
                    fps=24
                )
            else:
                video = VideoFileClip(input_path)

                video.write_videofile(output_path)

            with open(output_path, "rb") as f:
                st.download_button(
                    "baixar mp4",
                    data=f,
                    file_name="convertido.mp4",
                    mime="video/mp4"
                )
                
    
    except Exception as e:
        st.error(f"Erro na conversão: {e}")
    
    finally:
        try:
            os.remove(input_path)

        except:
            pass

        try:
            os.remove(output_path)
        
        except:
            pass

