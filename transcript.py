from urllib.parse import urlparse
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
# import Punctuator
# import language_tool_python



#Generating and the translation of the transcripts:
def generate_transcript(id):
  transcript_list = YouTubeTranscriptApi.list_transcripts(id)
  transcript = transcript_list.find_generated_transcript(['en', 'ru', 'de', 'tg','tr','es','pt','fr','it'])
  #text translation to English
  Final_transcript=transcript.translate('en').fetch()
  script = ""
  #cleaning the text
  for text in Final_transcript:
    t = text["text"]
    if t != '[music]':
      script += t + " "
  return script,len(script.split())







#fixing punctuation mistakes
# def punct():
#   punct_model=Punctuator('data/INTERSPEECH-T-BRNN.pcl')
#   p_transcript=punct_model.punctuate(transc())
#   return p_transcript 



#fixing grammar mistakes

# tool = language_tool_python.LanguageTool('en-US')
# def grammar():
#   tool = language_tool_python.LanguageTool('en-US')
#   is_bad_rule = lambda rule: rule.message == 'Possible spelling mistake found.' and len(rule.replacements) and rule.replacements[0][0].isupper()
#   matches = tool.check(transc())
#   matches = [rule for rule in matches if not is_bad_rule(rule)]
#   final_trans= language_tool_python.utils.correct(transc(), matches)
#   return final_trans