
# import libraries

import streamlit as st
import spacy
import en_core_web_lg
from spacytextblob.spacytextblob import SpacyTextBlob

# Preprocessing the text with spacy
@st.cache
def preprocess_text(text):
    nlp = en_core_web_lg.load()
    # remove stop words and lemmatize the text
    doc = nlp(text)
    filtered_tokens = []
    for token in doc:
        if token.is_stop or token.is_punct:
            continue
        filtered_tokens.append(token.lemma_)
    # remove the pronouns
    filtered_tokens = [token for token in filtered_tokens if token != '-PRON-']
    # remove the numbers
    filtered_tokens = [token for token in filtered_tokens if not token.isnumeric()]
    # remove the words with less than 3 characters
    filtered_tokens = [token for token in filtered_tokens if len(token) > 3]
    # remove verbs
    filtered_tokens = [token for token in filtered_tokens if token.pos_ != 'VERB']
    # make the text lowercase
    filtered_tokens = [token.lower() for token in filtered_tokens]
    
    
    return " ".join(filtered_tokens)
