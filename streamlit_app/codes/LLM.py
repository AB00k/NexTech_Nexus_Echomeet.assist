import os
from dotenv import load_dotenv
import openai
from langchain.llms import OpenAI
from faster_whisper import WhisperModel
from elevenlabs import set_api_key

# Specify the path to the .env file and load environment variables from it
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

# Fetch the API keys from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")

llm = OpenAI(openai_api_key=openai_api_key)
audio_transcribe_model = WhisperModel("medium")
set_api_key(elevenlabs_api_key)
