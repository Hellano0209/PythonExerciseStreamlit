#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 11:47:41 2023

@author: hellano
"""

import streamlit as st

st.header('DECOMPOSIÇÃO DE UM NÚMERO INTEIRO')

n = st.number_input('Digite um número entre 1 e 9999: ', min_value = 1, max_value = 9999)

uni = n % 10
dec = n // 10 % 10
cen = n // 100 % 10
mil = n // 1000

st.write('O número {} com posto por {} unidades, {} dezenas, {} centenas e {} milhares'.format(n, uni, dec, cen, mil))