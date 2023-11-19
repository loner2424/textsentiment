from textblob import TextBlob
import pandas as pd
import streamlit as st


def analyze(x):
    if x >= 0.3:
        return 'Positive'
    elif x <= -0.3:
        return 'Negative'
    else:
        return 'Neutral'


st.header('Sentiment Analysis')
with st.expander('Analyze Text'):
    text = st.text_input('Text here: ')
    if text:
        blob = TextBlob(text)
        polarity=analyze(round(blob.sentiment.polarity,2))
        sentiment=analyze(round(blob.sentiment.subjectivity,2))
        
        st.write('Sentiment: ',polarity)
        st.write('Score:', round(blob.sentiment.polarity,2))

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
        
st.write("By Sahil Sobhani, 209303352")



