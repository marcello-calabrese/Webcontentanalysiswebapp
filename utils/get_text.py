# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import streamlit as st


# get text from the webpage and dump it into a json variable
@st.cache
def get_text(URL):
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    elem = driver.find_element(By.TAG_NAME, "body")
    text = elem.text
    driver.quit()
    return text