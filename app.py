from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from googletrans import Translator
from streamlit_lottie import st_lottie
import json

st.title('Análisis de Sentimiento')
st.markdown("""
    <style>
    /* Fondo general */
    .stApp {
        background: radial-gradient(ellipse at center, #1a3a6b 0%, #0d1b3e 60%, #060d1f 100%);
    }

    /* Quitar franjas negras de la animación Lottie */
    iframe {
        background: transparent !important;
        border-radius: 16px;
    }

    /* Título principal */
    h1 {
        color: #ffffff !important;
        text-shadow: 0px 0px 12px rgba(100, 160, 255, 0.6);
    }

    /* Subtítulos */
    h2, h3 {
        color: #a8c8ff !important;
    }

    /* Texto general */
    p, label, .stText {
        color: #d0e4ff !important;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background-color: rgba(255, 255, 255, 0.08) !important;
        border-radius: 10px !important;
        color: #ffffff !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
    }

    /* Input de texto */
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.08) !important;
        color: #ffffff !important;
        border: 1px solid rgba(100, 160, 255, 0.4) !important;
        border-radius: 10px !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: rgba(6, 20, 50, 0.85) !important;
        border-right: 1px solid rgba(100,160,255,0.2);
    }

    /* Texto del sidebar */
    section[data-testid="stSidebar"] * {
        color: #a8c8ff !important;
    }
    </style>
""", unsafe_allow_html=True)
#image = Image.open('emoticones.jpg')
#st.image(image)

# Cargar y mostrar la animación
def load_lottie_file(path: str):
    with open(path, "r") as f:
        return json.load(f)

lottie_mood = load_lottie_file("Interactive Mood Selector UI.json")
st_lottie(lottie_mood, height=200, loop=True, key="mood_selector")

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

translator = Translator()

with st.sidebar:
               st.subheader("Polaridad y Subjetividad")
               ("""
                Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
                Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
                
               Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
               (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.

                 """
               ) 

with st.expander('Analizar texto'):
    text = st.text_input('Escribe por favor: ')
    if text:

        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x > 0.0 and x <=1.0:
            st.write( 'Es un sentimiento Positivo 😊')
        elif x >=-1 and x <= 0:
            st.write( 'Es un sentimiento Negativo 😔')
        else:
            st.write( 'Es un sentimiento Neutral 😐')
