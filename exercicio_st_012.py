#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 19:41:33 2023

@author: hellano
"""

import streamlit as st

st.header('CALCOLO DE DESCONTO')
st.write('Esse programa calcula quanto é um desconto de 5% no valor de um produto.')

valor = float(st.number_input('Qual o valor do produto: '))
taxa = 0.05
desconto = taxa*valor
preco = valor - desconto

if valor != 0:
    st.write('O valor do produto é {:.2f}R\$. Com desconto de 5\% fica no valor de {:.2f}R\$. O desconto foi de {:.2f}R\$!'.format(valor, preco, desconto))