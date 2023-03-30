#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 12:50:03 2023

@author: hellano
"""

import streamlit as st

st.header('Conversor de Modedas: Real para Dolar')

real = st.number_input("Entre com o valor em real que deseja converter:")
cot = 5.12
dolar = real/cot

st.write('A cotação do dolar: {:.2f} = R$1'.format(cot))
st.write('Com R${:.2f} você consegue comprar {:.2f}'.format(real, dolar))