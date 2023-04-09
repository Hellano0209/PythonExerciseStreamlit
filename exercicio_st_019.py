#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 21:59:21 2023

@author: hellano
"""

import streamlit as st
import random

st.header('SORTEIO DE ALUNO')

col1, col2, col3,  col4 = st.columns(4)

with col1:
    aluno1 = st.text_input('Nome do primeiro aluno: ')
with col2:
    aluno2 = st.text_input('Nome do segundo aluno: ')
with col3:
    aluno3 = st.text_input('Nome do terceiro aluno: ')
with col4:
    aluno4 = st.text_input('Nome do quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

sortear = st.button('Sortear')
if sortear:
    escolhido = random.choice(lista)
    st.write('O aluno escolhido foi o(a) {}'.format(escolhido))