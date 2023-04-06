#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 19:57:11 2023

@author: hellano
"""

import streamlit as st

st.header('REAJUSTE SALARIAL')

salar = float(st.number_input('Qual o seu salário atual: ', min_value = 0.00))

taxa = 0.15
almento = 0.15*salar
nsalar = salar + almento

if salar !=0:
    st.write('Você ganha {:.2f}R\$, com um reajuste de 15\%, você passa a receber {:.2f}R\$. Um almento de {:.2f}R\$'.format(salar, nsalar, almento))