import openai
from langchain.llms import OpenAI
from faster_whisper import WhisperModel
from elevenlabs import set_api_key

llm = OpenAI(openai_api_key='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')
audio_transcribe_model = WhisperModel("medium")
set_api_key("2ef0d67d9c42500d65ecbb877bdc4660")
