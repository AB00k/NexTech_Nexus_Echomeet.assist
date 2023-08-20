import streamlit as st
from codes.Audio import AudioRecorder
from codes.Transcribe import *
from codes.Agent_implementation import *
import os

audio_recorder = AudioRecorder()

def load_css(file_name):
    with open(file_name, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def display_footer():
    # Load the CSS file
    load_css("assets/styles.css")

    # Check recording status
    session_state = st.session_state
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if not session_state.get('recording'):
            if st.button("Record", key="record_button"):
                # Start recording
                audio_recorder.start_recording()
                session_state.recording = True

        else:
            if st.button("Stop", key="stop_button"):
                # Stop recording
                audio_recorder.stop_recording(os.path.join(os.path.dirname(__file__), "recording.wav"))
                session_state.recording = False

                #Transcribing the recorded audio
                text = transcribe_audio()

                #Getting Response from agent
                response = agent.run(text)

                #Playing audio response
                play_audio(response)
                