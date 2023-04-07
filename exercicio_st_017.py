#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 19:54:54 2023

@author: hellano
"""

import streamlit as st
from math import sqrt

st.header('CALCULO DA HIPOTENUSA')

co = st.number_input('Cateto Oposto: ')
ca = st.number_input('Cateto Adjacente: ')

hi = sqrt(co**2 + ca**2)

st.write('A hipotenusa do triângulo é {:.2f}'.format(hi))