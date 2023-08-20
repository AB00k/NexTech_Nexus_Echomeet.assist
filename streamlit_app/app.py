import streamlit as st
from modules import login, footer, main

def main_app():
    session_state = st.session_state
    # Left Sidebar
    login.display_login_sidebar()

    # Main Content Area
    if st.session_state.get('logged_in'):
        st.title("Welcome to EchoMeet.assist")
        st.subheader("--------------A voice powered assistant--------------")
        main.display_main_content()
    else:
        st.title("Welcome to EchoMeet.assist")
        st.subheader("--------------A voice powered assistant--------------")
        st.write("Please log in from the sidebar to access the voice assistant.")

    # Footer
    footer.display_footer()

if __name__ == "__main__":
    main_app()