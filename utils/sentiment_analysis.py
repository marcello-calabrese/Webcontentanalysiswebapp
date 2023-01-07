# import libraries

import streamlit as st
import spacy
import en_core_web_lg
from spacytextblob.spacytextblob import SpacyTextBlob


# Sentiment Analysis with spacy
@st.cache
def sentiment_analysis(text):
    nlp = en_core_web_lg.load()
    nlp.add_pipe("spacytextblob")    
    doc = nlp(text)
    # get the sentiment score
    sentiment_score = doc._.blob.polarity
    # get the sentiment label
    if sentiment_score > 0.5:
        sentiment_label = "Positive"
    elif sentiment_score < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    return sentiment_score, sentiment_label
