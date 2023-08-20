import os
from elevenlabs import generate , play
#from codes.LLM import *
import speech_recognition as sr
from pydub import AudioSegment

def convert_to_wav(input_path, output_path):
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format="wav")

def transcribe_audio():
    recognizer = sr.Recognizer()
    convert_to_wav("recording.wav","recording1.wav")

    with sr.AudioFile("recording1.wav") as source:
        audio_data = recognizer.record(source)  # Record the audio from the file


        try:
            text = recognizer.recognize_google(audio_data)
            os.remove("recording.wav")            
            os.remove("recording1.wav")
            return text
        except sr.UnknownValueError:
            return "Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Web Speech API; {e}"
    




# def transcribe_audio():
#     text = None

#     segments, info = audio_transcribe_model.transcribe("recording.wav")


#     for segment in segments:
#         text = segment.text

#     os.remove("recording.wav")

#     return text

def play_audio(text):
    # elevenlabs
    audio = generate(
        text=text,
        voice="Bella",
        model='eleven_multilingual_v1'
    )
    play(audio)
