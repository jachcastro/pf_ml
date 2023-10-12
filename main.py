import streamlit as st
import pandas as pd
 
# Cargar el archivo CSV
@st.cache  # Usamos la caché de Streamlit para evitar la recarga constante del CSV
def load_data():
    data = pd.read_csv("categoria.csv")
    return data
# Cargar los datos desde el archivo CSV
data = load_data()

# Título de la aplicación
st.title('Protecto de Recomendaciones')

# Agregar un logotipo en el menú lateral
# logo_path = "scr/LogoJL3.png"  # Reemplaza con la ruta a tu imagen de logotipo
# st.sidebar.image(logo_path, use_container_width=True)

# Crear un menú lateral
st.sidebar.header("Alternativas")
st.sidebar.markdown("### Menú Lateral")

# Opciones del menú
selected_option = st.sidebar.radio("Selecciona una opción", ["Inicio", "Para los Usuarios", "Para los Negocios","Para los Inversionistas" ])

# Contenido principal basado en la opción seleccionada
if selected_option == "Inicio":
    st.write("""
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
