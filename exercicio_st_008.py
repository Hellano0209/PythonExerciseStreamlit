#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:57:33 2023

@author: hellano
"""

import streamlit as st

st.header('Conversor: Sistema Internacional de Unidades')

n = st.number_input('Digite uma distância em metros:')

st.write('{} metros é equivalente a:\n{} micrômetros, {} milímetros, {} decímetros, {} decâmetros, {} hectômetros e {} quilômetros.'.format(n, n*1000000, n*1000, n*10, n/10, n/100, n/1000))