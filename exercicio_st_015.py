#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 20:50:38 2023

@author: hellano
"""

import streamlit as st

st.header('ALUGUEL DE CARRO')

st.write('Esse programa calcula o valor a pagar de um aluguel de carro dado a quantidade de dias que o cliente ficou com o carro e a quilometragem percorrida.')
st.write('Diária do carro custa R\$60,00')
st.write('R\$0,15 por quilometro rodado')

dias = st.number_input('Quanto dias você ficou com o veículo: ', min_value = 0)
km = st.number_input('Quilometragem percorrida: ', min_value = 0.00)

valor = 60*dias + 0.15*km

if dias != 0 and km !=0:
    st.write('Valor do aluguel do veículo é de: R${}.'.format(valor))