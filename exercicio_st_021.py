#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 15:54:55 2023

@author: hellano
"""
import streamlit as st
import pygame

st.header('MP3 PLAYER')

mp3 = st.file_uploader('Carreguar o audio')

play = st.button('Play')

if play:
    pygame.mixer.init()
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()
    input()
    pygame.event.wait()