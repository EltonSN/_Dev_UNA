'''MENU-Streamlit'''
from tokenize import PseudoExtras
import streamlit as st

def main_page():
    st.markdown("# Inserir ")

    cod = st.text_input('Codigo: ')
    nome = st.text_input('Digite seu nome: ')
    email = st.text_input('Digite seu e-mail: ')
    btn_salvar = st.button('Salvar ')

def page2():
    st.markdown("# Consulta Cadastro ")
    st.sidebar.markdown("# Faça sua pesquisa")

    pesq = st.text_input('Pesquisar: ')

    btn_Buscar = st.button('Buscar ')


def page3():
    st.markdown("# Baixar ")
    st.sidebar.markdown("Clique no botão ao lado para baixar os usuários ")

    pesq2 = st.text_input('Buscar usuário: ')

    btn_baixar = st.button('Baixar ')

page_names_to_funcs = {
    "Cadastro": main_page,
    "Pesquisar": page2,
    "Baixar": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()