import streamlit as st
import pandas as pd
 
# Cargar el archivo CSV
@st.cache  # Usamos la caché de Streamlit para evitar la recarga constante del CSV
def load_data():
    data = pd.read_csv("categoria.csv")
    return data

# Título de la aplicación
st.title('Categoria ....')

# Cargar los datos desde el archivo CSV
data = load_data()

import streamlit as st

# Configuración del título
st.title("JL3")

# Crear un menú lateral
st.sidebar.header("Alternativas")

# Opciones del menú
selected_option = st.sidebar.radio("Selecciona una opción", ["Inicio", "Para los Usuarios", "Para los Negocios","Para los Inversionistas" ])

# Contenido principal basado en la opción seleccionada
if selected_option == "Inicio":
    st.write("""
    # Proyecto de Recomendaciones  
    ## Somos JL3
    """)
elif selected_option == "Para los Usuarios":
    st.write("Aquí puedes configurar tus preferencias.")
elif selected_option == "Para los Negocios":
    st.write("Puedes obtener ayuda y soporte aquí.")
elif selected_option == "Para los Inversionistas":
    st.write("#Inversionistas")
    # Widget ComboBox para seleccionar una categoría
    selected_category = st.selectbox("Selecciona una categoría:", data["categoria"])

    # Mostrar la categoría seleccionada
    st.write("Categoría seleccionada:", selected_category)
