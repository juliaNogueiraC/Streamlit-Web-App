import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Título da aplicação
st.title('Exemplo de Aplicação com Streamlit')

# Barra lateral com um controle deslizante
st.sidebar.header('Parâmetros')
n_points = st.sidebar.slider('Número de pontos no gráfico', 10, 100, 50)

# Gerando dados fictícios
data = np.random.normal(0, 1, n_points)
df = pd.DataFrame(data, columns=['Valores'])

# Exibindo o DataFrame
st.write('### Dados Gerados')
st.write(df)

# Criando um gráfico de histograma
fig, ax = plt.subplots()
ax.hist(data, bins=10)
st.pyplot(fig)

# Controles deslizantes para ajuste de parâmetros do gráfico
bin_min = st.slider('Mínimo do bin', int(data.min()), 0, int(data.min()))
bin_max = st.slider('Máximo do bin', 0, int(data.max()), int(data.max()))
bin_width = (bin_max - bin_min) / 10  # Assume 10 bins for simplicity

# Atualizando o gráfico com os novos parâmetros
fig, ax = plt.subplots()
ax.hist(data, bins=np.arange(bin_min, bin_max + bin_width, bin_width))
st.pyplot(fig)

# Rodapé com informação adicional
st.markdown('---')
st.markdown('**Esta é uma aplicação exemplo criada com Streamlit.**')
