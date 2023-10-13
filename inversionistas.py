# inversionistas

import streamlit as st
import pandas as pd

# Cargar el archivo CSV
def load_data():
    data = pd.read_csv("categoria.csv")
    return data


def app():
    # Cargar los datos desde el archivo CSV
    data = load_data()

    st.title('Opciones para inversionistas')
    st.header('Proyecto Yelp & Google Maps')
    st.subheader(' ')
    st.markdown(' ')

    # Widget ComboBox para seleccionar una categoría
    selected_category = st.selectbox("Selecciona una categoría:", data["categoria"])

    # Mostrar la categoría seleccionada
    st.write("Categoría seleccionada:", selected_category)