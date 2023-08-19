import os
from elevenlabs import generate , play
from LLM import *



def transcribe_audio():
    text = None

    segments, info = audio_transcribe_model.transcribe("recording.wav")


    for segment in segments:
        text = segment.text

    os.remove("recording.wav")

    return text

def play_audio(text):
    # elevenlabs
    audio = generate(
        text=text,
        voice="Bella",
        model='eleven_multilingual_v1'
    )
    play(audio)

print(transcribe_audio())
