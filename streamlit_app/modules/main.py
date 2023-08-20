import streamlit as st

def display_main_content():
    # Initialize the session state for chat messages
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = [{"role": "assistant", "content": "How can I help you?"}]
    
    # Display chat messages using Streamlit's built-in chat_message features
    for msg in st.session_state.chat_messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])