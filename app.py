
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


car_data = pd.read_csv('C:/Users/Aguacate/vehicle-data-analysis/vehicles_us.csv')
st.title("Análisis de Datos de Vehículos")
st.write("Datos cargados exitosamente!")
st.write(f"El dataset tiene {len(car_data)} filas y {len(car_data.columns)} columnas")

st.header('Dashboard de Análisis de Vehículos')

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un grafcio de dispersion el conjunto de datos de anuncios de venta de coches')

    # Crear un grafico dispersion
    # Se crea una figura vacía y luego se añade
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

   
