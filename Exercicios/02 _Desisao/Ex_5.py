'''Média Escolar'''
import streamlit as st

N1 = float(st.number_input('Digite a sua Primeira Nota de [0-10]: ', step=int()))
N2 = float(st.number_input('Digite a sua Segunda Nota de [0-10]: ', step=int()))

Med = (N1 + N2) / 2 

if st.button ('Calcular'):
    if (N1 and N2 > 10):
        st.write ('---- ERRO ---- NOTA MAIOR QUE 10')
    elif (Med == 10):
        st.write ('Sua Média é igual a: '+ str(Med) + ' - APROVADO COM DISTINÇÃO')
    elif (Med >= 7):
        st.write ('Sua Média é igual a: '+ str(Med) + ' - APROVADO')
    else:
        st.write ('Sua Média é igual a:  '+ str(Med) + ' - REPROVADO')
        