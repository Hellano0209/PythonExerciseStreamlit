#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 20:14:23 2023

@author: hellano
"""

import streamlit as st

st.header('CONVETENDO TEMPERATURA')

tipo = st.radio('Tipo de conversão', ['ºC para ºF', 'ºF para ºC'])

if tipo == 'ºC para ºF':
    grauc = float(st.number_input('Temperatura em ºC: '))
    grauf = (grauc*9/5) + 32
    st.write('{:.2f}ºC é equivalente a {:.2f}ºF.'.format(grauc, grauf))
else:
    grauf = float(st.number_input('Temperatura em ºF: '))
    grauc = (grauf - 32)*5/9
    st.write('{:.2f}ºF é equivalente a {:.2f}ºC.'.format(grauf, grauc))