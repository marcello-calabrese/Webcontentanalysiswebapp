#import libraries

import streamlit as st
import spacy
import en_core_web_lg
from spacytextblob.spacytextblob import SpacyTextBlob

# main function


# Name Entity Recognition with spacy
@st.cache
def name_ent_recognition(text):
    nlp = en_core_web_lg.load()
    doc = nlp(text)
    # get the name entities
    name_entities = [(entity.text, entity.label_) for entity in doc.ents]
    return name_entities