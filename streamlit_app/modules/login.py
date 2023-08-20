import streamlit as st

def display_login_sidebar():
    session_state = st.session_state

    if not session_state.get('logged_in'):
        st.sidebar.image("logo.png")
        st.sidebar.text("Please log in to continue.")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        
        if st.sidebar.button("Login"):
            session_state.username = username
            session_state.logged_in = True
            # Force Streamlit to rerun the app
            st.experimental_rerun()
    else:
        # Placeholder for the dashboard
        st.sidebar.image("logo.png")
        st.sidebar.title("Dashboard")
        st.sidebar.subheader("Welcome User!")
        if st.sidebar.button("Logout"):
            session_state.logged_in = False
            session_state.username = None  # Clear the username from session_state