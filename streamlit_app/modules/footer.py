import streamlit as st

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
                session_state.recording = True
        else:
            if st.button("Stop", key="stop_button"):
                # Stop recording
                session_state.recording = False

    # Display the footer text after the button
    st.markdown('<div class="footer">NexTech Nexus Voice Assistant © 2023</div>', unsafe_allow_html=True)