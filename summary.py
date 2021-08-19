from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from transcript import yt_link_id


yt_link = yt_link_id()

##############
## SUMMARIZE FUNCIOTNS ##


def get_transcript_from_link(link):
    transcript = YouTubeTranscriptApi.get_transcript(link)
    return transcript

transcript_link =get_transcript_from_link(yt_link_id)

summarizer = pipeline('summarization')

def get_summarized_text(transcript):
    length = '' 
    text_holder = transcript
    for i in text_holder:
            length += ' ' + i['text']  
    while len(length) > 500:  

        num_iters = int(len(length)/1000)
        summarized_text = []
        for i in range(0, num_iters + 1):
            start = 0
            start = i * 1000
            end = (i + 1) * 1000
            out = summarizer(length[start:end])
            out = out[0]
            out = out['summary_text']
            summarized_text.append(out)
            text_holder = summarized_text
        
        length = ''
        for i in text_holder:
            length += ' ' + i
    return text_holder 

# summary = get_summarized_text(transcript_link)