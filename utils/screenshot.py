# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import streamlit as st

# create a screenshot of the webpage
@st.cache
def screenshot(URL):
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    # Screenshot as a .png file with  selenium
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll' +X)
    driver.set_window_size(S('Width'), S('Height'))
    page_screen = driver.save_screenshot('page_screen.jpg')
    # visualize the screenshot with streamlit
    driver.quit()
    return page_screen