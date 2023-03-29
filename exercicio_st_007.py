#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:17:28 2023

@author: hellano
"""

import streamlit as st

st.header("NOTA MÉDIA")

col1, col2 = st.columns(2)

with col1:
    n1 = st.number_input("Nota da primeira prova: ")
with col2:
    n2 = st.number_input("Nota da segunda prova: ")
    
st.write("Sua nota média é {:.2f}!".format((n1 + n2)/2))
