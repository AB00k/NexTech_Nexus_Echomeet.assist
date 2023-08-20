import openai
from langchain.llms import OpenAI
#from faster_whisper import WhisperModel
from elevenlabs import set_api_key
from Keys import *

# from dotenv import load_dotenv


# # Specify the path to the .env file and load environment variables from it
# dotenv_path = os.path.join(os.path.dirname(os.getcwd()),'.env')
# load_dotenv(dotenv_path=dotenv_path)

# # Fetch the API keys from environment variables
# openai_api_key = "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"
# elevenlabs_api_key = "e5de56c08b212f70e7d4e66fa7c32af8"


llm = OpenAI(openai_api_key=OPENAI_API_KEY)
#audio_transcribe_model = WhisperModel("medium")
set_api_key(ELVENLAB_API_KEY)
