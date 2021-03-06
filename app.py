import base64
import os
import json
import pickle
import uuid
import re
import pathlib
# import pandas as pd
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
from youtube_transcript_api import YouTubeTranscriptApi
from IPython.display import YouTubeVideo
from urllib.parse import urlparse
# from transformers import pipeline
# from summary import get_summarized_text
from transcript import get_transcript_from_link, clean_text_farukh
from wordcloud_functions import get_df_transcript, get_text_column_from_df, lemmatize_text, get_text_from_df_above_3_letters, get_wordcloud
# from gensim.summarization import summarize
# from wordcloud import WordCloud, STOPWORDS
# from sklearn.feature_extraction.text import CountVectorizer 


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
expander.write('NLP')


#Team
######
expander = st.sidebar.expander('Delta NLP Team')
expander.write('[Farrukh](https://github.com/fbulbulov)')
expander.write('[Umut](https://github.com/aktumut)')
expander.write('[Deniz](https://github.com/Deniz-shelby)')
expander.write('[Gabriel](https://github.com/Calypso25)')
expander.write('[Fabio](https://github.com/fistadev)')
expander.write('[Nurlan](https://github.com/nsarkhanov)')






st.markdown("")
st.markdown("<h2 style='text-align: left; color:#58A6FF;'><b>Youtube Link<b></h2>", unsafe_allow_html=True)
st.markdown("")


##################################
# YOUTUBE LINK #
# https://www.youtube.com/watch?v=Tuw8hxrFBH8
# https://www.youtube.com/watch?v=eBSeCp__xhI


# if YouTubeTranscriptApi._errors.VideoUnavailable == True:
#     pass    

#Getting the youtube link and retrieving the youtube id:
url = st.text_input('Paste your Youtube link here')
@st.cache
def yt_link_id():
    if url == True:   
        url_data = urlparse(url)
    else:
        url_data = urlparse('https://www.youtube.com/watch?v=eBSeCp__xhI')
    
    yt_id = url_data.query[2::]
    return yt_id

yt_link = yt_link_id()


#getting the transcript:
transcript = get_transcript_from_link(yt_link)
transcript_farr = clean_text_farukh(transcript)

# summary = get_summarized_text(transcript_link)


# if transcript == False:
#     st.write('https://www.youtube.com/watch?v=eBSeCp__xhI')
# else:
#     st.write(transcript)



##########
#PAGES
##########


st.subheader('Convert text :speech_balloon:')
nav = st.radio('',['Transcript', 'Wordcloud', 'Measure'])
# nav = st.radio('',['Transcript','Summarize', 'Wordcloud', 'Measure'])
    


#-----------------------------------------
   
#TRANSCRIPT
###########
       
if nav == 'Transcript':
    st.markdown("<h3 style='text-align: left; color:#58A6FF;'><b>Transcript Text<b></h3>", unsafe_allow_html=True)
    st.text('')
    # if st.button('Transcript'):
    with st.spinner('Learning...'):
        st.write(transcript_farr)



#-----------------------------------------

#SUMMARY
########


# if nav == 'Summarize':
#     st.markdown("<h3 style='text-align: left; color:#58A6FF;'><b>Summarization<b></h3>", unsafe_allow_html=True)
#     st.text('')
#     if st.button('Summarize'):
#         with st.spinner('Learning...'):
#             st.write(summary)



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

# if st.button('Measure'):
    with st.spinner('Learning...'):
        nltk.download('punkt')
        rt = readtime.of_text(transcript_farr)
        # tc = textstat.flesch_reading_ease(transcript)
        # tokenized_words = word_tokenize(transcript_farr)
        # lr = len(set(tokenized_words)) / len(tokenized_words)
        # lr = round(lr,2)
        st.text('Reading Time')
        st.write(rt)
        # st.text('Text Complexity (score from 0 (hard to read), to 100 (easy to read))')
        # st.write(tc)
        # st.text('Use of different words (bigger number means more variety of words)')
        # st.write(lr)

    # st.markdown('___') 
    
    # components.html(
    #                     """
    #                     <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-text="This is SYNTHIA, the AI that turns words into knowledge via @lopezyse" data-url="https://share.streamlit.io/dlopezyse/synthia/main" data-hashtags="AI,Education,MachineLearning,Synthia" data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    #                     """,
    #                     )




#-----------------------------------------
   
#WORDCLOUD
##########


@st.cache
def wordcloud_function(transcript):
    df = get_df_transcript(transcript)
    df_text = get_text_column_from_df(df)
    df_text_lemmatized = df_text.applymap(lemmatize_text)
    text_3_letters = get_text_from_df_above_3_letters(df_text_lemmatized)
    wordcloud = get_wordcloud(text_3_letters)
    return wordcloud



def plot_wordcloud(wordcloud):
    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.show()
    st.pyplot(fig)
    return fig



if nav == 'Wordcloud':
    st.markdown("<h3 style='text-align: left; color:#58A6FF;'><b>Wordcloud<b></h3>", unsafe_allow_html=True)
    st.text('')
    # if st.button('Wordcloud'):
    with st.spinner('Learning...'):
    #         st.pyplot(plot_wordcloud)
        plot_wordcloud = plot_wordcloud(wordcloud_function(transcript))

################################







# Footer

st.markdown("")
st.markdown("""---""")
st.markdown("")
st.markdown("")
st.markdown(
    "If you have any questions, checkout our [documentation](https://github.com/deltaNLP/youtube-nlp) ")
st.text(' ')







#saving the output to txt file:
# @st.cache
# def saving_to_txt():
#   with open('data/transcript.txt','w')as f:
# 	  f.writelines(transc())


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