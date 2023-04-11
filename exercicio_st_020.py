#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 21:46:27 2023

@author: hellano
"""

import streamlit as st
import random as rd

st.header('ORDEM DE APRESENTAÇÃO')

col1, col2, col3, col4 = st.columns(4)

with col1:
    a1 = st.text_input('Aluno 1: ')
with col2:
    a2 = st.text_input('Aluno 2: ')
with col3:
    a3 = st.text_input('Aluno 3: ')
with col4:
    a4 = st.text_input('Aluno 4: ')

lista = [a1, a2, a3, a4]
rd.shuffle(lista)

click = st.button('APRESENTAÇÃO')

if click:
    for i in range(4):
        st.write('{}º a se apresentar é o(a) {}.'.format(i+1, lista[i]))