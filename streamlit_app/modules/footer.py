import streamlit as st

def load_css(file_name):
    with open(file_name, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def display_footer():
    load_css('assets/styles.css')

    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.session_state.get('logged_in', False):  # Only display the button if the user is logged in
                if 'recording_status' not in st.session_state:
                    st.session_state.recording_status = "stopped"
                
                if st.session_state.recording_status == "stopped":
                    if st.button("Record"):
                        # This is where you'll integrate the backend functionality to start recording audio
                        st.session_state.recording_status = "recording"
                else:
                    if st.button("Stop"):
                        # This is where you'll integrate the backend functionality to stop recording and transcribe audio
                        user_transcribed_message = "Placeholder for transcribed message"
                        st.session_state.chat_messages.append({"role": "user", "content": user_transcribed_message})
                        
                        # Placeholder for the assistant's response
                        assistant_response = "Placeholder for assistant's response"
                        st.session_state.chat_messages.append({"role": "assistant", "content": assistant_response})
                        
                        st.session_state.recording_status = "stopped"

        st.write("© 2023 NexTech Nexus Voice Assistant")