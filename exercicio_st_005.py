#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 10:51:27 2023

@author: hellano
"""

import streamlit as st

st.header("Sucessor e Antecessor")

n = st.number_input("Ditite um valor inteiro", step = 1)
st.write("Analizando o número {}, o seu antecessor é {} e o seu sucessor é {}".format(n, n-1, n+1))