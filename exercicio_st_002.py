#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 14:10:11 2023

@author: hellano
"""

import streamlit as st

st.header('SEJA BEM VINDO!')

nome = st.text_input("Digite o seu nome: ").capitalize()

if nome != "":
    st.write('Oi {}, é um prazer te conhecer!'.format(nome))

