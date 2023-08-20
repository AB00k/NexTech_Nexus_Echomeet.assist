import streamlit as st
from modules import Main, login, dashboard
from codes.Audio import AudioRecorder
import os

def main():
    session_state = st.session_state

    # Left Sidebar
    login.display_login_sidebar()
    audio_recorder = AudioRecorder()

    # Main Content Area
    if st.session_state.get('logged_in'):
        st.title("Welcome to EchoMeet.assist")
        st.subheader("--------------A voice powered assistant--------------")
        #dashboard.display_dashboard_content()
        Main.display_footer()
        st.markdown('<div class="footer">NexTech Nexus Voice Assistant © 2023</div>', unsafe_allow_html=True)

    else:
        st.title("Welcome to EchoMeet.assist")
        st.subheader("--------------A voice powered assistant--------------")
        st.write("Please log in from the sidebar to access your dashboard and features.")
        st.markdown('<div class="footer">NexTech Nexus Voice Assistant © 2023</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()