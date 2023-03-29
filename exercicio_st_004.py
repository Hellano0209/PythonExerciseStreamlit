#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 14:45:02 2023

@author: hellano
"""

import streamlit as st

st.header("O que você dititou?")

algo = st.text_input("Digite algo: ")

if algo.isnumeric():
    st.write("{} é um número.".format(algo))
if algo.isalnum():
    st.write("{} é alfanumérico.".format(algo))
if algo.isalpha():
    st.write("{} é alfabético.".format(algo))
    if algo.istitle():
        st.write("{} está capitalizado.".format(algo))
    if algo.isupper():
        st.write("{} tem todas as letras maiúsculas.".format(algo))
    if algo.islower():
        st.write("{} tem todas as letras minúsculas.".format(algo))