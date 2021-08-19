import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


# import plotly.express as px
# import plotly.figure_factory as ff


header = st.beta_container()
dataset = st.beta_container()
team = st.beta_container()
footer = st.beta_container()


@st.cache(persist=True)
def load_data(data):
    pass
    # data = pd.read_csv('./data/galaxies.csv')
    # return data


with header:
    st.title('Delta NLP')  # site title h1
    st.subheader('Naturally learning stuff')
    st.markdown("""---""")
    image = Image.open('data/nlp.png')
    st.image(image, caption="NLP")
    st.text(' ')



#############################

with dataset:

    st.markdown("")
    st.subheader("Youtube Link")
    st.text("Paste your link below")
    st.markdown("")

    st.text_input('Enter some text')
    st.selectbox('Select', ['Transcript','English Translation','Summary'])
    



#############################

    st.markdown("")
    st.markdown("""---""") 
    st.markdown("")

   
##############################
with team:
    st.subheader('Team Delta NLP')
    col1, col2, col3, col4, col5, col6= st.beta_columns(6)
    with col1:
        st.markdown('[Farrukh]()')
    with col2:
        st.markdown('[Umut]()')
    with col3:
        st.markdown('[Deniz]()')
    with col4:
        st.markdown('[Gabriel]()')
    with col5:
        st.markdown('[Fabio](https://github.com/fistadev)')
    with col6:
        st.markdown('[Nurlan]()')



# Footer
with footer:
    st.markdown("""---""")
    st.markdown("")
    st.markdown("")
    st.markdown(
        "If you have any questions, checkout our [documentation](https://github.com/deltaNLP/youtube-nlp) ")
    st.text(' ')
