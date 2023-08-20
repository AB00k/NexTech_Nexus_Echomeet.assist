import openai
from langchain.llms import OpenAI
#from faster_whisper import WhisperModel
from elevenlabs import set_api_key

OPENAI_API_KEY="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"
ELVENLAB_API_KEY="2ef0d67d9c42500d65ecbb877bdc4660"
llm = OpenAI(openai_api_key=OPENAI_API_KEY)
#audio_transcribe_model = WhisperModel("medium")
set_api_key(ELVENLAB_API_KEY)
