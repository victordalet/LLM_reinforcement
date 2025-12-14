import streamlit as st
from css import inject_all_styles
from ui_components import (
    init_session_state,
    render_header,
    render_quick_questions,
    handle_user_input,
    display_chat_history
)


#config de la page
st.set_page_config(page_title="Coach Sportif IA", page_icon="💪", layout="wide")

inject_all_styles()


# initialisation
init_session_state()


#interface utilisateur
render_header()
render_quick_questions()

# historique du chat
display_chat_history()

# gestion utilisateur
handle_user_input()


