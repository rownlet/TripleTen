import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos desde un archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis Visual de Datos de Vehículos')

# Mostrar imagen de marcas de autos
car_logo_url = "https://www.nicepng.com/png/full/290-2903528_marcas-de-autos-png-ks-car-logo.png"
st.image(car_logo_url)

# Permitir al usuario elegir la columna para el histograma
st.write("Opciones Avanzadas")
column_hist = st.selectbox('Elige una columna', [
                           'odometer', 'price', 'days_listed'])
build_histogram = st.checkbox('Mostrar Histograma')
if build_histogram:
    st.write(f'Histograma para la columna "{column_hist}"')
    fig_hist = px.histogram(car_data, x=column_hist)
    st.plotly_chart(fig_hist, use_container_width=True)

# Permitir al usuario elegir las columnas para el gráfico de dispersión
st.write("Gráficos de Dispersión")
options_scatter = {
    'odometer vs price': ('odometer', 'price'),
    'odometer vs days_listed': ('odometer', 'days_listed'),
    'price vs days_listed': ('price', 'days_listed')
}
choice_scatter = st.selectbox(
    'Elige una columna', list(options_scatter.keys()))
build_scatter = st.checkbox('Mostrar Gráfico de Dispersión')
if build_scatter:
    x, y = options_scatter[choice_scatter]
    st.write(f'Gráfico de dispersión para "{x}" vs "{y}"')
    fig_scatter = px.scatter(car_data, x=x, y=y)
    st.plotly_chart(fig_scatter, use_container_width=True)

# Permitir al usuario elegir la columna para el gráfico de barras
st.write("Gráficos de Barras")
column_bar = st.selectbox('Elige una columna', [
                          'condition', 'fuel', 'transmission', 'type', 'paint_color'])
build_bar = st.checkbox('Mostrar Gráfico de Barras')
if build_bar:
    st.write(f'Gráfico de barras para la columna "{column_bar}"')
    count_data = car_data[column_bar].value_counts().reset_index()
    count_data.columns = [column_bar, 'count']
    # Ordenar los datos en orden descendente por 'count'
    count_data = count_data.sort_values('count', ascending=True)
    fig_bar = px.bar(count_data, y=column_bar, x='count', text_auto=True,
                     title=f"Distribución de {column_bar}", orientation='h')
    st.plotly_chart(fig_bar, use_container_width=True)

# Permitir al usuario elegir la columna para el gráfico de torta
st.write("Gráfico de Torta")
column_pie = st.selectbox('Elige una columna', [
                          'condition', 'fuel', 'transmission', 'type'])
build_pie = st.checkbox('Mostrar Gráfico de Torta')
if build_pie:
    st.write(f'Gráfico de torta para la columna "{column_pie}"')
    pie_data = car_data[column_pie].value_counts().reset_index()
    pie_data.columns = [column_pie, 'count']
    fig_pie = px.pie(pie_data, names=column_pie, values='count',
                     title=f"Distribución de {column_pie}")
    st.plotly_chart(fig_pie, use_container_width=True)
