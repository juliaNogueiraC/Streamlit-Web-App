import streamlit as st
from PIL import Image

# Configurações iniciais
st.set_page_config(page_title="Meu Portfólio", page_icon=":star:", layout="wide")

# Cabeçalho
st.title("Bem-vindo ao Meu Portfólio")

# Seção Sobre Mim
st.header("Sobre Mim")
st.write("""
Olá! Eu sou [Seu Nome], um desenvolvedor especializado em [Sua Especialidade]. 
Tenho experiência em [Tecnologias/áreas de atuação]. 
Este portfólio destaca alguns dos meus projetos e contribuições recentes.
""")

# Imagem de Perfil
image = Image.open("images/perfil.jpg")
st.image(image, caption='Seu Nome', width=250)

# Seção de Projetos
st.header("Projetos")
st.write("""
Aqui estão alguns dos meus projetos recentes:
""")

# Lista de Projetos
projetos = {
    "Projeto 1 - Nome do Projeto": "Descrição breve do projeto e as tecnologias usadas.",
    "Projeto 2 - Nome do Projeto": "Descrição breve do projeto e as tecnologias usadas.",
    "Projeto 3 - Nome do Projeto": "Descrição breve do projeto e as tecnologias usadas."
}

for nome, descricao in projetos.items():
    st.subheader(nome)
    st.write(descricao)

# Seção de Contato
st.header("Contato")
st.write("""
Se você deseja entrar em contato, fique à vontade para me enviar uma mensagem através das redes sociais ou por email.
""")

# Redes Sociais
st.write("[LinkedIn](https://www.linkedin.com/in/seu-perfil)")
st.write("[GitHub](https://github.com/seu-usuario)")
st.write("[Email](mailto:seu-email@example.com)")
