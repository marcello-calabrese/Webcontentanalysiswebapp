
# get the text of the webpage and save it to a file

import datetime
import json
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
#options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36')
options.headless = True
driver = webdriver.Chrome(options=options)

URL = 'https://selenium-python.readthedocs.io/locating-elements.html'

driver.get(URL)

# get the text from the page

'''in the recent selenium version, to get the element of a page you need to use the following syntax:'''

elem = driver.find_element(By.TAG_NAME, "body")

# get the text from the page

text = elem.text

driver.quit()

# load the text into a dataframe

df = pd.DataFrame(text.splitlines())

# save the dataframe as a csv file

df.to_csv('selenium_text.csv', index=False)