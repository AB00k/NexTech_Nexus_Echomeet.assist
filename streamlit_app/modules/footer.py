import streamlit as st
from codes.Audio import AudioRecorder
from codes.Transcribe import *
from codes.Agent_implementation import *


#Initializing Audio Object
audio_recorder=AudioRecorder()

def load_css(file_name):
    with open(file_name, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def display_footer():
    load_css('assets/styles.css')
    session_state = st.session_state

    with st.container():
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.session_state.get('logged_in', False):  # Only display the button if the user is logged in
                
                if not session_state.get("recording"):
                    if st.button("Record"):
                        #Implementing Recording backend
                        audio_recorder.start_recording()
                        session_state.recording = True
                else:
                    if st.button("Stop"):
                        audio_recorder.stop_recording("recording.wav")

                        user_transcribed_message = transcribe_audio()
                        session_state.chat_messages.append({"role": "user", "content": user_transcribed_message})
                        

                        assistant_response = agent.run(user_transcribed_message)
                        session_state.chat_messages.append({"role": "assistant", "content": assistant_response})
                        play_audio(assistant_response)
                        os.remove("recording.wav")
                        os.remove("recording1.wav")
                        
                        session_state.recording = False

        #st.markdown("© 2023 NexTech Nexus Voice Assistant")
