'''fornecer 2 valores e exibir o maior'''
import streamlit as st 

a = st.text_input('Digite o primeiro numero: ')
b = st.text_input('Digite o segundo numero: ')

if (a > b):
    print ('O maior número é o: ' + str (a))
elif (a < b):
    print ('O maior número é o: ' + str (b))
else:
    print ('Os números são iguais')
