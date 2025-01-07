import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo csv com os dados de veículos
car_data = pd.read_csv('./vehicles.csv')

# Exibindo um título na página
st.header('Dados de anúncios de vendas de carros')

# Exibindo texto orientativo de funcionamento do sistema
st.write('**Selecione ao menos uma das opções abaixo para visualizar o respectivo gráfico**')

# Checkbox para gerar um histograma
hist_checkbox = st.checkbox(
    'Criar um histograma de preço x ano do modelo dos carros')

# se o checkbox para criar histograma for clicado
if hist_checkbox:
    # Escrever uma mensagem
    st.write(
        '*Criando um histograma...*')

    # Criar um histograma
    fig = px.histogram(car_data, x='price', color='model')

    # Exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


# Checkbox para gerar gráfico de dispersão
scatter_checkbox = st.checkbox(
    'Criar um gráfico de dispersão de Preço x Ano do modelo')

# Se o checkbox para criar gráfico de dispersão for clicado
if scatter_checkbox:
    # Exibir uma mensagem
    st.write('*Criando um gráfico de dispersão...*')

    # Criar um gráfico de dispersão
    fig = px.scatter(car_data, x='price', color='model')

    # Exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
