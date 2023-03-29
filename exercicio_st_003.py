#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 14:24:47 2023

@author: hellano
"""

import streamlit as st

st.header("A SOMA DE DOIS NÚMEROS")

n1 = st.number_input("Digite um número:")
n2 = st.number_input("Digite um segundo número:")

st.write("A soma entre {} e {} é igual a {}".format(n1, n2, n1+n2))