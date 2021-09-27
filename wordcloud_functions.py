import pathlib
import streamlit as st
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import spacy




@st.cache
def get_df_transcript(transcript):
    transcript = pd.DataFrame(transcript)
    return transcript


@st.cache
def get_text_column_from_df(df_transcript):
    df_text = df_transcript.loc[:, ['text']]
    return df_text


@st.cache
def lemmatize_text(df_text):
    path = pathlib.Path(__file__).parent / 'data/en_core_web_sm/en_core_web_sm-3.1.0'
    nlp = spacy.load(path)
    # nlp = spacy.load('en_core_web_sm')
    sent = []
    doc = nlp(df_text)
    for word in doc:
        sent.append(word.lemma_)
    return " ".join(sent)



@st.cache
def get_text_from_df_above_3_letters(df_text):
    text = " ".join(i for i in df_text.text)
    text_split = text.split()
    text_3_letters = []
    for i in text_split:
        if len(i) > 3:
            text_3_letters.append(i)
    text_3_letters = " ".join(i for i in text_3_letters)
    return text_3_letters



@st.cache
def get_wordcloud(text):
    wordcloud = WordCloud(background_color='white',
                          stopwords=STOPWORDS,
                          max_words=200,
                          max_font_size=40,
                          scale=3,
                          random_state=1 # chosen at random by flipping a coin; it was heads
                         ).generate(text)
    return wordcloud




