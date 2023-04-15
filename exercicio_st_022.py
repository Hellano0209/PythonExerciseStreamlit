#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 11:35:21 2023

@author: hellano
"""

import streamlit as st

st.header('PRIMEIRO E ÚLTIMO NOME')

nome = st.text_input('Qual o seu nome completo: ')

if nome != '':
    # TRATAMENTO DA STRING
    nome = nome.strip()

    # SEPARANDO CADA PARTE DO NOME
    sep = nome.split()

    st.write('Seu primeiro nome é {} e seu último nome é {}'.format(sep[0].capitalize(), sep[len(sep)-1].capitalize()))