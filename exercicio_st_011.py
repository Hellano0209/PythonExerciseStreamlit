#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:59:56 2023

@author: hellano
"""

import streamlit as st

st.header('PINTURA DE UMA PAREDE')

largura = st.number_input('Largura da parede: ', min_value = 0.00)
altura = st.number_input('Altura da parede: ', min_value = 0.00)

area = altura*largura
tinta = area/2 # 1 litro de tinta para 2 m² de parede

if largura != 0 and altura != 0:
    st.write('Essa parede tem uma área de {:.2f}m².'.format(area))
    st.write('Você irá precisar de {:.2f}l de tinta'.format(tinta))