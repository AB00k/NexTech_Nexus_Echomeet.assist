import streamlit as st

def display_login_sidebar():
    session_state = st.session_state

    if not session_state.get('logged_in'):
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
        st.sidebar.subheader("Dashboard")
        st.sidebar.text("Upcoming Meetings: 3")
        st.sidebar.text("Unread Emails: 5")
        if st.sidebar.button("Logout"):
            session_state.logged_in = False
            session_state.username = None  # Clear the username from session_state