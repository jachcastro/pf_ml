#Negocios 2

# negocios

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, explained_variance_score
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge

prom_final_y_one_hot = pd.read_parquet('data/Datasets_ML_ML_Luca_prom_final_y_one_hot.parquet')

### Aplicacion Cosine Similarity:
def cosine_similaritys(random_state_cs):
    # Seleccionar un restaurante aleatorio del conjunto de datos
    restaurante_aleatorio = prom_final_y_one_hot.sample(random_state=random_state_cs)

    # Seleccionar solo las columnas numéricas relevantes para el cálculo de similitud
    columnas_numericas_relevantes = restaurante_aleatorio.select_dtypes(include='number').values

    # Calcular la similitud del coseno con respecto a todos los restaurantes
    similitud_coseno = cosine_similarity(columnas_numericas_relevantes, prom_final_y_one_hot.select_dtypes(include='number'))

    # Obtener los índices de los 10 restaurantes más similares, incluyendo el índice 0
    indices_similares = np.argsort(similitud_coseno[0])[::-1][:10]

    # Prepare the output for the top 10 similar restaurants
    top_10_similar_restaurants_output = "Restaurantes Más Similares (Top 10):\n"
    for i, indice in enumerate(indices_similares):
        similitud = similitud_coseno[0][indice]  # Obtener la similitud del coseno para el restaurante en el índice
        porcentaje_similitud = (similitud * 100).round(2)  # Convertir a porcentaje y redondear a 2 decimales
        top_10_similar_restaurants_output += f"Porcentaje de similitud con restaurante {indice}: {porcentaje_similitud}%\n"

    # Obtener los índices de los restaurantes más similares (top 10)
    indices_10_similares = np.argsort(similitud_coseno[0])[::-1][1:11]  # Tomamos los primeros 10

    # Crear un DataFrame con los 10 restaurantes más similares
    restaurantes_similares = prom_final_y_one_hot.iloc[indices_10_similares]
    # Mostrar el DataFrame con los 10 restaurantes más similares
    print("Restaurante aleatorio seleccionado:")
    print(restaurante_aleatorio[['name','state','city','promedio_sentimientos_positivos','promedio_sentimientos_negativos','stars']].head())
    print("Restaurantes Más Similares (Top 10):")
    print(restaurantes_similares[['name','state','city','promedio_sentimientos_positivos','promedio_sentimientos_negativos','stars']])
    
    # Prepare the output for the top 10 similar restaurants
    top_10_similar_restaurants_output = f"Restaurantes Más Similares (Top 10):\n{restaurantes_similares[['name','state','city','promedio_sentimientos_positivos','promedio_sentimientos_negativos','stars']].to_string(index=False)}"

    # Prepare the output for the randomly selected restaurant
    random_restaurant_output = f"\nRestaurante aleatorio seleccionado:\n{restaurante_aleatorio[['name','state','city','promedio_sentimientos_positivos','promedio_sentimientos_negativos','stars']].head().to_string(index=False)}"

    # Combine both outputs
    combined_output = top_10_similar_restaurants_output + random_restaurant_output
    return combined_output

### Metodo Ridge
def metodo_ridge(random_state_user):
    # Copy the data
    set = prom_final_y_one_hot.copy()

    # Drop unnecessary columns
    set = set.drop(['business_id', 'name', 'address', 'city', 'state', 'postal_code', 'BusinessParking'], axis=1)

    # Separar datos
    X = set.drop('stars_volume', axis=1)
    y = set['stars_volume']

    # Dividir datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=random_state_user)

    # Entrenar el modelo con regularización Ridge
    ridge_model = Ridge(alpha=0.1)  # Alpha controla la fuerza de la regularización
    ridge_model.fit(X_train, y_train)

    # Evaluar el modelo
    y_pred_ridge = ridge_model.predict(X_test)
    mse_ridge = mean_squared_error(y_test, y_pred_ridge)
    mae_ridge = mean_absolute_error(y_test, y_pred_ridge)
    r2_ridge = r2_score(y_test, y_pred_ridge)
    explained_var_ridge = explained_variance_score(y_test, y_pred_ridge)

    # Prepare the output for Ridge results
    ridge_results = {
        'Ridge Regression': {
            'Mean Squared Error': mse_ridge,
            'Mean Absolute Error': mae_ridge,
            'R-squared': r2_ridge,
            'Explained Variance Score': explained_var_ridge
        }
    }

    # Plot the top 25 features
    # Obtener los nombres de las características
    feature_names = X.columns

    # Obtener los coeficientes del modelo Ridge
    coefs = ridge_model.coef_

    # Obtener los coeficientes y nombres de las top 25 características
    top_25_coefs = coefs.argsort()[-25:]
    top_25_feature_names = feature_names[top_25_coefs]

    # Obtener los coeficientes correspondientes a las top 25 características
    top_25_coefs = coefs[top_25_coefs]

    # Plot the top 25 features
    # plt.figure(figsize=(12, 8))
    # plt.bar(range(len(top_25_coefs)), top_25_coefs)
    # plt.xlabel('Característica')
    # plt.ylabel('Coeficiente')
    # plt.title('Coeficientes mas importantes detectados por el Modelo Ridge:')
    # plt.xticks(range(len(top_25_coefs)), top_25_feature_names, rotation=90)
    # plt.tight_layout()
    # Visualizar los coeficientes de las top 25 características
    
    # Disable PyplotGlobalUseWarning
    st.set_option('deprecation.showPyplotGlobalUse',False)
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.bar(range(len(top_25_coefs)), top_25_coefs)
    ax.set_xlabel('Característica')
    ax.set_ylabel('Coeficiente')
    ax.set_title('Coeficientes mas importantes detectados por el Modelo Ridge:')
    ax.set_xticks(range(len(top_25_coefs)))
    ax.set_xticklabels(top_25_feature_names, rotation=90)
    plt.tight_layout()
   
    # Display the plot using Streamlit
    # st.pyplot(fig)

    return ridge_results

def app():
    st.title('Opciones para negocios')
    st.header('Proyecto Yelp & Google Maps')

    # Streamlit app
    st.subheader("Ridge Regression Analysis")

    # User input for random_state_user
    random_state_user = st.number_input("Enter a random seed (random_state_user):", value=23, step=1)

    # Run the Ridge method and get the results
    ridge_results = metodo_ridge(random_state_user)

    # Display the results
    st.write("Ridge Regression Results:")
    st.write(ridge_results)

    # Display the plot of top 25 features
    st.pyplot()

    # Streamlit app
    st.title("Cosine Similarity App")

    # User input for random_state_cs
    random_state_cs = st.number_input("Enter a random seed (random_state_cs):", value=42, step=1)

    # Get the combined output
    output = cosine_similaritys(random_state_cs)

    # Display the output
    st.text(output)