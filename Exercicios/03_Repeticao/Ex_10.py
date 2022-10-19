import streamlit as st
num1 = st.number_input('Digite o primeiro número inteiro: ', step=int())
num2 = st.number_input('Digite o segundo número inteiro: ', step=int())

btn = st.button('Calcular')
number = st.slider("Pick a number", 0, 100)
date = st.date_input("Pick a date")

for contador in range(num1, num2,2):
    st.write(contador)
