import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configurações iniciais
st.set_page_config(page_title="Dashboard de Vendas", page_icon=":bar_chart:", layout="wide")

# Gerar dados fictícios
np.random.seed(42)
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Livros']

dados = {
    'Mês': np.random.choice(meses, 200),
    'Categoria': np.random.choice(categorias, 200),
    'Vendas': np.random.randint(1000, 10000, 200)
}

df = pd.DataFrame(dados)

# Título do Dashboard
st.title("Dashboard de Análise de Vendas")

# Visualização geral dos dados
st.header("Dados de Vendas")
st.dataframe(df)

# Filtros
st.sidebar.header("Filtros")
mes_selecionado = st.sidebar.multiselect("Selecione o(s) Mês(es)", meses, default=meses)
categoria_selecionada = st.sidebar.multiselect("Selecione a(s) Categoria(s)", categorias, default=categorias)

# Filtrar os dados
df_filtrado = df[(df['Mês'].isin(mes_selecionado)) & (df['Categoria'].isin(categoria_selecionada))]

# Gráfico de Barras - Vendas por Categoria
st.header("Vendas por Categoria")
fig, ax = plt.subplots()
sns.barplot(data=df_filtrado, x='Categoria', y='Vendas', estimator=sum, ci=None, ax=ax)
st.pyplot(fig)

# Gráfico de Linhas - Vendas ao longo dos meses
st.header("Vendas ao Longo dos Meses")
df_mes_categoria = df_filtrado.groupby(['Mês', 'Categoria'])['Vendas'].sum().unstack()
fig, ax = plt.subplots()
df_mes_categoria.plot(kind='line', ax=ax, marker='o')
plt.xticks(rotation=45)
st.pyplot(fig)

# Estatísticas principais
st.header("Estatísticas Principais")
st.write("Total de Vendas: ", df_filtrado['Vendas'].sum())
st.write("Média de Vendas: ", df_filtrado['Vendas'].mean())

# Gráfico de Dispersão - Análise por mês
st.header("Análise de Vendas por Mês")
fig, ax = plt.subplots()
sns.scatterplot(data=df_filtrado, x='Mês', y='Vendas', hue='Categoria', size='Vendas', sizes=(20, 200), ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)
