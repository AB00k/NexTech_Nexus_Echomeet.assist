import os
from elevenlabs import generate , play
from LLM import *
from Audio import *



def transcribe_audio():
    text = None

    segments, info = audio_transcribe_model.transcribe(rec_path)


    for segment in segments:
        text = segment.text

    os.remove(rec_path)

    return text

def play_audio(text):
    # elevenlabs
    audio = generate(
        text=text,
        voice="Bella",
        model='eleven_multilingual_v1'
    )
    play(audio)
