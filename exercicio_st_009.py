#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:13:54 2023

@author: hellano
"""

import streamlit as st
import pandas as pd
import numpy as np

st.header('Tabuada')

n = st.number_input('Digite um valor entre 1 e 9:', min_value=1, max_value = 9)

st.write('A tabuada do número {} é:'.format(n))
for i in range(0, 9):
    st.write('{}x{} = {}'.format(i+1, n, n*(i+1)))
