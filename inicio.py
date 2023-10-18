# inicio

import streamlit as st

def app():
    # Título de la aplicación
    st.title('Inicio')
    st.title("Demo de Machine Learning")    
    st.header('Proyecto Yelp & Google Maps')

    # Cargar la imagen desde el archivo "mapa.png"
    imagen = "src/mapa.png"

    # URL del video que deseas enlazar
    video_url = "https://jl3.ntx360.net/mapa.mp4"

    # Mostrar el video en la página
    st.video(video_url)

    # Enlace al mapa
    url = "https://jl3.ntx360.net/MapaML_Grupo07_01.html"
    st.markdown("<div style='text-align: center;'><a href='{}' target='_blank'>MAPA</a></div>".format(url), unsafe_allow_html=True)