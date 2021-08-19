import base64
import os
import json
import pickle
import uuid
import re
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from googletrans import Translator
import nltk
from nltk.tokenize import word_tokenize
import readtime
import textstat
import matplotlib.pyplot as plt
# from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from IPython.display import YouTubeVideo
from urllib.parse import urlparse
# from summary import get_summarized_text
from transcript import generate_transcript
# from gensim.summarization import summarize
from wordcloud import WordCloud, STOPWORDS
import spacy
from sklearn.feature_extraction.text import CountVectorizer 


header = st.container()
dataset = st.container()
team = st.container()



@st.cache(persist=True)
def load_data(data):
    pass


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






st.markdown("")
st.markdown("<h2 style='text-align: left; color:#58A6FF;'><b>Youtube Link<b></h2>", unsafe_allow_html=True)
st.markdown("")


##################################
# YOUTUBE LINK #
# https://www.youtube.com/watch?v=Tuw8hxrFBH8


# if YouTubeTranscriptApi._errors.VideoUnavailable == True:
#     pass    

#Getting the youtube link and retrieving the youtube id:
def yt_link_id():
    url = st.text_input('Paste your Youtube link here')
    url_data = urlparse(url)
    yt_id = url_data.query[2::]
    return yt_id

yt_link = yt_link_id()

#getting the transcript:
def transc():
    transcript, no_of_words = generate_transcript(yt_link)
    return transcript


transcript = transc()

# summary = get_summarized_text(transcript_link)


#################################
# WORDCLOUD #

def get_transcript_from_link(link):
    transcript = YouTubeTranscriptApi.get_transcript(link)
    return transcript

transcript =get_transcript_from_link(yt_link)


def get_df_transcript(transcript):
    transcript = pd.DataFrame(transcript)
    return transcript

df = get_df_transcript(transcript)


def get_text_column_from_df(df_transcript):
    df_text = df_transcript.loc[:, ['text']]
    return df_text

df_text = get_text_column_from_df(df)


def lemmatize_text(df_text):
    nlp = spacy.load('en_core_web_sm')
    sent = []
    doc = nlp(df_text)
    for word in doc:
        sent.append(word.lemma_)
    return " ".join(sent)

df_text_lemmatized = df_text.applymap(lemmatize_text)


def get_text_from_df_above_3_letters(df_text):
    text = " ".join(i for i in df_text.text)
    text_split = text.split()
    text_3_letters = []
    for i in text_split:
        if len(i) > 3:
            text_3_letters.append(i)
    text_3_letters = " ".join(i for i in text_3_letters)
    return text_3_letters

text_3_letters = get_text_from_df_above_3_letters(df_text_lemmatized)


def get_wordcloud(text):
    wordcloud = WordCloud(background_color='white',
                          stopwords=STOPWORDS,
                          max_words=200,
                          max_font_size=40,
                          scale=3,
                          random_state=1 # chosen at random by flipping a coin; it was heads
                         ).generate(text)
    return wordcloud

wordcloud = get_wordcloud(text_3_letters)


def plot_wordcloud(wordcloud):
    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.show()
    st.pyplot(fig)
    return fig

plot_wordcloud = plot_wordcloud(wordcloud)

################################


# if transcript == False:
#     st.write('https://www.youtube.com/watch?v=Tuw8hxrFBH8')
# else:
#     st.write(transcript)


#######
#PAGES
######


st.subheader('Convert text :speech_balloon:')
nav = st.radio('',['Transcript','Translation','Summarize', 'Wordcloud', 'Measure'])
    


#-----------------------------------------
   
#Transcript
########
       
if nav == 'Transcript':
    st.markdown("<h3 style='text-align: left; color:#58A6FF;'><b>Transcript Text<b></h3>", unsafe_allow_html=True)
    st.text('')
    if st.button('Transcript'):
        with st.spinner('Learning...'):
            st.write(transcript)

if nav == 'Translation':
    st.markdown("<h3 style='text-align: left; color:#58A6FF;'><b>Translation<b></h3>", unsafe_allow_html=True)
    st.text('')
    if st.button('Translation'):
        with st.spinner('Learning...'):
            st.write(transcript)

# if nav == 'Summarize':
#     st.markdown("<h3 style='text-align: left; color:#58A6FF;'><b>Summarization<b></h3>", unsafe_allow_html=True)
#     st.text('')
#     if st.button('Summarize'):
#         with st.spinner('Learning...'):
#             st.write(summary)

if nav == 'Wordcloud':
    st.markdown("<h3 style='text-align: left; color:#58A6FF;'><b>Wordcloud<b></h3>", unsafe_allow_html=True)
    st.text('')
    if st.button('Wordcloud'):
        with st.spinner('Learning...'):
            st.write(plot_wordcloud)

    # input_me = st.text_area("Input some text in English, and scroll down to analyze it", max_chars=5000)
    # input_me = st.write(transcript)







#-----------------------------------------
   
#MEASURE
########
       
if nav == 'Measure':
    st.markdown("<h3 style='text-align: left; color:#58A6FF;'><b>Measure Text<b></h3>", unsafe_allow_html=True)
    st.text('')

    # input_me = st.text_area("Input some text in English, and scroll down to analyze it", max_chars=5000)
    # input_me = st.write(transcript)

    if st.button('Measure'):
        with st.spinner('Learning...'):
            nltk.download('punkt')
            rt = readtime.of_text(transcript)
            tc = textstat.flesch_reading_ease(transcript)
            tokenized_words = word_tokenize(transcript)
            lr = len(set(tokenized_words)) / len(tokenized_words)
            lr = round(lr,2)
            st.text('Reading Time')
            st.write(rt)
            st.text('Text Complexity (score from 0 (hard to read), to 100 (easy to read))')
            st.write(tc)
            st.text('Use of different words (bigger number means more variety of words)')
            st.write(lr)

    # st.markdown('___') 
    
    # components.html(
    #                     """
    #                     <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-text="This is SYNTHIA, the AI that turns words into knowledge via @lopezyse" data-url="https://share.streamlit.io/dlopezyse/synthia/main" data-hashtags="AI,Education,MachineLearning,Synthia" data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    #                     """,
    #                     )

####################################

# Footer

st.markdown("")
st.markdown("""---""")
st.markdown("")
st.markdown("")
st.markdown(
    "If you have any questions, checkout our [documentation](https://github.com/deltaNLP/youtube-nlp) ")
st.text(' ')







#saving the output to txt file:
def saving_to_txt():
  with open('data/transcript.txt','w')as f:
	  f.writelines(transc())


def download_button(object_to_download, download_filename, button_text, pickle_it=False):
    """
    Generates a link to download the given object_to_download.

    Params:
    ------
    object_to_download:  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv,
    some_txt_output.txt download_link_text (str): Text to display for download
    link.
    button_text (str): Text to display on download button (e.g. 'click here to download file')
    pickle_it (bool): If True, pickle file.

    Returns:
    -------
    (str): the anchor tag to download object_to_download

    Examples:
    --------
    download_link(your_df, 'YOUR_DF.csv', 'Click to download data!')
    download_link(your_str, 'YOUR_STRING.txt', 'Click to download text!')

    """
    if pickle_it:
        try:
            object_to_download = pickle.dumps(object_to_download)
        except pickle.PicklingError as e:
            st.write(e)
            return None

    else:
        if isinstance(object_to_download, bytes):
            pass

        elif isinstance(object_to_download, pd.DataFrame):
            object_to_download = object_to_download.to_csv(index=False)

        # Try JSON encode for everything else
        else:
            object_to_download = json.dumps(object_to_download)

    try:
        # some strings <-> bytes conversions necessary here
        b64 = base64.b64encode(object_to_download.encode()).decode()

    except AttributeError as e:
        b64 = base64.b64encode(object_to_download).decode()

    button_uuid = str(uuid.uuid4()).replace('-', '')
    button_id = re.sub('\d+', '', button_uuid)

    custom_css = f""" 
        <style>
            #{button_id} {{
                background-color: rgb(255, 255, 255);
                color: rgb(38, 39, 48);
                padding: 0.25em 0.38em;
                position: relative;
                text-decoration: none;
                border-radius: 4px;
                border-width: 1px;
                border-style: solid;
                border-color: rgb(230, 234, 241);
                border-image: initial;

            }} 
            #{button_id}:hover {{
                border-color: rgb(246, 51, 102);
                color: rgb(246, 51, 102);
            }}
            #{button_id}:active {{
                box-shadow: none;
                background-color: rgb(246, 51, 102);
                color: white;
                }}
        </style> """

    dl_link = custom_css + f'<a download="{download_filename}" id="{button_id}" href="data:file/txt;base64,{b64}">{button_text}</a><br></br>'

    return dl_link