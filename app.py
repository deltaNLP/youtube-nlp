import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit.components.v1 as components
# from gensim.summarization import summarize
from googletrans import Translator
import nltk
from nltk.tokenize import word_tokenize
import readtime
import textstat
import matplotlib.pyplot as plt
# from wordcloud import WordCloud, STOPWORDS
# import spacy
# from youtube_transcript_api import YouTubeTranscriptApi
# from sklearn.feature_extraction.text import CountVectorizer 


header = st.container()
dataset = st.container()
team = st.container()



@st.cache(persist=True)
def load_data(data):
    pass
    # data = pd.read_csv('./data/galaxies.csv')
    # return data



#############################

with header:
    image = Image.open('data/nlp.png')
    st.image(image, caption="")

#############################



#########
#SIDEBAR
########


st.sidebar.title('Delta NLP')  # site title h1
st.sidebar.subheader('Naturally learning stuff')
st.sidebar.markdown("""---""")
st.sidebar.text(' ')

# st.sidebar.header('Convert text :speech_balloon:')
# nav = st.sidebar.radio('',['Transcript','English Translation','Summary', 'Measure text'])
# nav = st.sidebar.radio('',['Measure text'])
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')

#About
######
expander = st.sidebar.expander('About')
expander.write('Text')


#Team
######
expander = st.sidebar.expander('Delta NLP Team')
expander.write('[Farrukh]()')
expander.write('[Umut]()')
expander.write('[Deniz]()')
expander.write('[Gabriel]()')
expander.write('[Fabio](https://github.com/fistadev)')
expander.write('[Nurlan]()')




#######
#PAGES
######

with dataset:

    st.markdown("")
    st.markdown("<h2 style='text-align: left; color:#58A6FF;'><b>Youtube Link<b></h2>", unsafe_allow_html=True)
    st.markdown("")

    st.text_input('Paste your Youtube link here')
    st.subheader('Convert text :speech_balloon:')
    nav = st.radio('',['Transcript','English Translation','Summary', 'Measure text'])
    



#############################

    st.markdown("")
    st.markdown("""---""") 
    st.markdown("")

#-----------------------------------------
   
#MEASURE
########
       
if nav == 'Measure text':
    st.markdown("<h3 style='text-align: left; color:#58A6FF;'><b>Measure Text<b></h3>", unsafe_allow_html=True)
    st.text('')

    input_me = st.text_area("Input some text in English, and scroll down to analyze it", max_chars=5000)

    if st.button('Measure'):
        if input_me =='':
            st.error('Please enter some text')
        elif len(input_me) < 500:
            st.error('Please enter a larger text')
        else:
            with st.spinner('Learning...'):
                nltk.download('punkt')
                rt = readtime.of_text(input_me)
                tc = textstat.flesch_reading_ease(input_me)
                tokenized_words = word_tokenize(input_me)
                lr = len(set(tokenized_words)) / len(tokenized_words)
                lr = round(lr,2)
                st.text('Reading Time')
                st.write(rt)
                st.text('Text Complexity (score from 0 (hard to read), to 100 (easy to read))')
                st.write(tc)
                st.text('Use of different words (bigger number means more variety of words)')
                st.write(lr)

    st.markdown('___') 
    
    # components.html(
    #                     """
    #                     <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-text="This is SYNTHIA, the AI that turns words into knowledge via @lopezyse" data-url="https://share.streamlit.io/dlopezyse/synthia/main" data-hashtags="AI,Education,MachineLearning,Synthia" data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    #                     """,
    #                     )

####################################

# Footer

# st.markdown("""---""")
st.markdown("")
st.markdown("")
st.markdown(
    "If you have any questions, checkout our [documentation](https://github.com/deltaNLP/youtube-nlp) ")
st.text(' ')