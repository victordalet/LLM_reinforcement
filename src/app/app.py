import streamlit as st
from ui_components import (
    init_session_state,
    render_header,
    render_quick_questions,
    handle_user_input,
    display_chat_history
)


#config de la page
st.set_page_config(page_title="Coach Sportif IA", page_icon="💪", layout="wide")


# initialisation
init_session_state()


#interface utilisateur
render_header()
render_quick_questions()


# gestion utilisateur
handle_user_input()


# hsitoire du chat
display_chat_history()