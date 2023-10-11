import streamlit as st
import pandas as pd
 
st.write("""
# Recomendacion de negocios 
Somos *JL3*
""")
 

# Cargar el archivo CSV
@st.cache  # Usamos la caché de Streamlit para evitar la recarga constante del CSV
def load_data():
    data = pd.read_csv("categoria.csv")
    return data

# Título de la aplicación
st.title('Categoria ....')

# Cargar los datos desde el archivo CSV
data = load_data()

# Widget ComboBox para seleccionar una categoría
selected_category = st.selectbox("Selecciona una categoría:", data["categoria"])

# Mostrar la categoría seleccionada
st.write("Categoría seleccionada:", selected_category)
