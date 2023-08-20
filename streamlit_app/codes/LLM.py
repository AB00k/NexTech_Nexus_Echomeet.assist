import os
import openai
from langchain.llms import OpenAI
from elevenlabs import set_api_key
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
#audio_transcribe_model = WhisperModel("medium")
set_api_key(elevenlabs_api_key)