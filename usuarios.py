# usuarios

import streamlit as st
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax

# Cargar el modelo y el tokenizador
tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
model = BertForSequenceClassification.from_pretrained('bert-base-cased')

# Definir la función para la clasificación de sentimiento
def classifySentiment(review_text):

    # Tokenizar el texto
    encoding_review = tokenizer(review_text, return_tensors="pt")


    # Realizar la inferencia en el modelo
    with torch.no_grad():
        output = model(**encoding_review)

    # Calcular las probabilidades y la etiqueta de sentimiento
    probabilities = softmax(output.logits, dim=1)
    sentiment_label = "Positivo" if probabilities[0][1] > probabilities[0][0] else "Negativo"

    sentiment_label
    
def app():
    # Cargar y mostrar la imagen
    st.title('Opciones para usuarios')
    st.header('Proyecto Yelp & Google Maps')
    st.subheader('Machine Learning - BERT')
    st.subheader('Demo de Análisis de Sentimientos - Review')
    
    # Interfaz de usuario
    user_input = st.text_area('Ingrese un comentario en inglés:')
    if st.button('Analizar'):
        with st.spinner('Analizando...'):
            prediction = classifySentiment(user_input)
            st.markdown(f'El sentimiento del comentario es **{prediction}**.')

