import openai
from langchain.llms import OpenAI
from faster_whisper import WhisperModel
from elevenlabs import set_api_key

llm = OpenAI(openai_api_key='')
audio_transcribe_model = WhisperModel("medium")
set_api_key("")
