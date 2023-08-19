import openai
from langchain.llms import OpenAI
from faster_whisper import WhisperModel
from elevenlabs import set_api_key

llm = OpenAI(openai_api_key=OPENAI_API_KEY)
audio_transcribe_model = WhisperModel("medium")
set_api_key(ELVENLAB_API_KEY)
