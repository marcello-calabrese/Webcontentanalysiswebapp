'''this streamlit app will be used to scrape webpage, extract the text and the create a wordcloud from it, the wordcloud can be also saved as an image file. 
The app also will be used to create a sentiment analysis of the text and Name Entity Recognition. 
The app will also be used to create a screenshot and download it. 

the app is useful for content writers, bloggers, and anyone who wants to create a wordcloud from a webpage, to monitor the topics that are being discussed in the webpage.



Library used:

-  streamlit
- requests
- selenium
- spacy
- wordcloud
- matplotlib
- PIL
- json
- pandas

'''
### Importing the libraries ###

import streamlit as st

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
import io
from wordcloud import STOPWORDS, ImageColorGenerator, WordCloud
import warnings

#### Main functions import from utils: ###

from utils.get_text import get_text
from utils.preprocess_text import preprocess_text
from utils.sentiment_analysis import sentiment_analysis
from utils.name_ent_recognition import name_ent_recognition
from utils.screenshot import screenshot


## Warnings ignore ###

warnings.filterwarnings(action='ignore')
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)



### App layout ###

def main():
    # create a wide layout
    st.set_page_config(
        page_title="Scrapify ¦ Web Page Analysis For Content Writers",
        page_icon="📰",
        initial_sidebar_state="expanded",
        layout="wide")
    
    
    # create a sidebar menu
    option = st.sidebar.selectbox("Select an option", ["Home", "Webpage Text Scraper", "Word Cloud", "Sentiment Analysis", "Name Entity Recognition", "Screenshot"])
    
    
    if option == "Home":
        
        
        # add an image
        display = image = Image.open("img/Sport+Performance+Analysis+-+Web+Scraping+21.png")
        display = np.array(display)
        st.image(display, width=500)
        st.title("Scrapyfy\n")
        st.success('**Web Page Text Analysys App** for Content Writers, Bloggers, to monitor the topics that are being discussed on the webpage.')
               
        st.markdown('''This streamlit app will be used to scrape webpage, extract the text and create a wordcloud from it, the wordcloud can be also saved as an image file. 
    The app also will be used to create a sentiment analysis of the text and Name Entity Recognition. The multiple features are accessible from the sidebar menu on the left.\n
The app will also be used to create a screenshot and download it. The app is useful for content writers, bloggers, and anyone who wants to create a wordcloud from a webpage, 
to monitor the topics that are being discussed in the webpage.\n''') 

        st.subheader('''**🧾 The features of the app you will find on the sidebar menu on the left are:**\n''')
   
        st.success('''- **Webpage Text Scraper:** Scrape the text from the webpage and show the first ten lines of the text in a table.\n
- **Word Cloud:** Create a Wordcloud from the text scraped from the webpage.\n
- **Sentiment Analysis:** Create a sentiment analysis of the text scraped from the webpage.\n
- **Name Entity Recognition:** Create a name entity recognition of the text scraped from the webpage.\n
- **Screenshot:** Create a screenshot of the webpage and download it.\n''')
        st.info('''👈👈Start playing selecting the option from the sidebar menu on the left.👈👈\n''')
        
        # create a footer
        st.caption('''App created by [**@marcellodichiera**](https://marcello-personal-website.netlify.app/)''') 
    ## Webpage Text Scraper
    elif option == "Webpage Text Scraper":
        st.title("Webpage Scraper test")
        st.markdown('##### This option lets you scrape a webpage, extract the text from it and show the first 10 lines in a table and download the text as a csv file.')
        
        # create a text box to enter the URL
        URL = st.text_input("Enter the URL of the webpage you want to scrape")
        # create a button to scrape the text from the webpage
        if URL is not None:
            if st.button("Scrape"):
                text = get_text(URL)
                df = pd.DataFrame(text.splitlines(), columns=["Webpage_text"], index=None)
                # show the text in the dataframe
                st.markdown('## Showing the first ten lines of the text')
                st.dataframe(df.head(10))
                # download the text as a csv file
                st.info('''Download the text as a csv file if you like.''')
                st.download_button(label="Download the text as a csv file", 
                                   data=df.to_csv(index=False, encoding='utf-8'),
                                   file_name='webpage_text.csv', 
                                   mime='text/csv')
              
        else:
            st.warning("Please enter a valid URL")
    
    # Word Cloud
    elif option == "Word Cloud":
        st.title("Word Cloud")
        st.markdown('##### This option lets you create a wordcloud text from a webpage')
        
        # create a text box to enter the URL
        URL = st.text_input("Enter the URL of the webpage you want to scrape")
        # create a button to scrape the text from the webpage
        if URL is not None:
           
            if st.button("Scrape"):
                text = get_text(URL)
                # create a wordcloud
                wordcloud = WordCloud(width=800, height=400, background_color="white", stopwords=STOPWORDS).generate(text)
                # wordcloud title
                st.info('#### Wordcloud of {}'.format(URL))
                plt.figure(figsize=(10, 5))
                plt.imshow(wordcloud, interpolation="bilinear")
                plt.axis("off")
                # show the wordcloud
                st.pyplot()
            
                
        else:
            st.warning("Please enter a valid URL")
            
    # Sentiment Analysis
    
    elif option == "Sentiment Analysis":
        st.title("Sentiment Analysis")
        st.markdown('##### This option lets you create a sentiment analysis of the text from a webpage')
        
        # create a text box to enter the URL
        URL = st.text_input("Enter the URL of the webpage you want to scrape")
        # create a button to scrape the text from the webpage
        if URL is not None:
            if st.button("Scrape"):
                text = get_text(URL)
                # preprocess the text
                #text = preprocess_text(text)
                #get the sentiment score and label
                sentiment_score, sentiment_label = sentiment_analysis(text)
                # show the sentiment score rounded to 2 decimals and label
                st.markdown('#### Sentiment score: {}'.format(round(sentiment_score, 2)))
                
                st.markdown('#### Sentiment of web page content is: {}'.format(sentiment_label))
        else:
            st.warning("Please enter a valid URL")      
    
    # Name Entity Recognition
    
    elif option == "Name Entity Recognition":
        st.title("Name Entity Recognition")
        st.markdown('##### This option lets you create a Name Entity Recognition of the text from a webpage')
        st.markdown('Name Entity Recognition is a process of extracting the entities from the text, such as person, location, organization, etc.')
        
        # create a text box to enter the URL
        URL = st.text_input("Enter the URL of the webpage you want to scrape")
        # create a button to scrape the text from the webpage
        if URL is not None:
            if st.button("Scrape"):
                text = get_text(URL)
                # preprocess the text
                text = preprocess_text(text)
                #get the name entities
                name_entities = name_ent_recognition(text)
                # show the name entities
                st.markdown('#### Name entities of web page content are: {}'.format(name_entities))
        else:
            st.warning("Please enter a valid URL")
        
        
    
    # Screenshot
    
    elif option == 'Screenshot':
        st.title("Screenshot")
        st.markdown('##### This option lets you create a screenshot of a webpage and download it')
        
        # create a text box to enter the URL
        URL = st.text_input("Enter the URL of the webpage you want to scrape")
        # create a button to scrape the text from the webpage
        if URL is not None:
            if st.button("Scrape"):
                # get the screenshot
                take_screen = screenshot(URL)
                # show the screenshot
                img_screen = Image.open('page_screen.jpg')
                
                st.image(img_screen, caption='Screenshot of the webpage', use_column_width=True)

                

        else:
            st.warning("Please enter a valid URL")
        
# run the app   
   
if __name__ == "__main__":
    main()