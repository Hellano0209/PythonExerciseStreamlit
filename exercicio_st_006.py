#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:03:24 2023

@author: hellano
"""

import streamlit as st
import math

st.header("OPERADORES ARITMÉTICOS")

n = st.number_input("Digite um valor numérico: ")
st.write("O dobro de {:.2f} é {:.2f}.\nO triplo de {:.2f} é {:.2f}.\nA raíz quadrada de {} é {:.2f}.".format(n, 2*n, n, 3*n, n, math.sqrt(n)))