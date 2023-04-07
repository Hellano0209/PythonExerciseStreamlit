#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 19:49:47 2023

@author: hellano
"""

import streamlit as st
from math import floor

st.header('PARTE INTEIRA DE UM NÚMERO REAL')

n = st.number_input('Digite um número real: ')
n2 = floor(n)

if n != 0:
    st.write('A parte inteira do número {} é {}.'.format(n, n2))