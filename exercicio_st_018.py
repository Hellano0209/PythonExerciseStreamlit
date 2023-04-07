#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 19:58:38 2023

@author: hellano
"""

import streamlit as st
from math import radians, sin, cos, tan

st.header('Calulo do Seno, Cosseno e Tangente de um Angulo')

angulo = st.number_input('Digite o valor de um angulo: ')
radiano = radians(angulo)

seno = sin(radiano)
coss = cos(radiano)
tang = tan(radiano)

st.write('O Seno, Cosseno e a Tangente do algulo {} é {:.2f}, {:.2f} e {:.2f}, respectivamente.'.format(angulo, seno, coss, tang))