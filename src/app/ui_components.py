import streamlit as st
import time
import asyncio
from langchain_core.messages import HumanMessage
from agent import graph


# historique
def init_session_state():
    """Initialise l'état de session Streamlit"""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "current_question" not in st.session_state:
        st.session_state.current_question = None


def add_message(role, content, recommendations=None, response_time=None):
    """Ajoute un message à l'historique"""
    st.session_state.chat_history.append({
        "role": role,
        "content": content,
        "recommendations": recommendations,
        "response_time": response_time
    })


def display_chat_history():
    """Affiche l'historique des messages"""
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"], unsafe_allow_html=True)

            if message.get("recommendations"):
                st.subheader("Vidéos recommandées :")
                cols = st.columns(min(3, len(message["recommendations"])))

                for idx, (video_id, data) in enumerate(list(message["recommendations"].items())[:3]):
                    with cols[idx]:
                        if data.get('thumbnail_url'):
                            st.image(data['thumbnail_url'], use_container_width=True)
                        st.write(f"**{data['title']}**")
                        st.markdown(f"[▶️ Voir la vidéo]({data['video_url']})")


async def stream_response(prompt):
    """Génère une réponse en streaming"""
    start_time = time.time()
    with st.chat_message("assistant"):  
        with st.spinner("✨ Je réfléchis à ta question...✨"):
            message_placeholder = st.empty()
            full_response = ""
            all_transcripts = {}

            async for message, metadata in graph.astream(
                {"messages": [HumanMessage(content=prompt)]},
                stream_mode="messages",
            ):
                if not isinstance(message, HumanMessage) and message.type != "tool":
                    full_response += message.content
                    message_placeholder.markdown(full_response + "▌", unsafe_allow_html=True)

                if message.type == "tool" and message.artifact:
                    all_transcripts.update(message.artifact)

            message_placeholder.markdown(full_response.strip(), unsafe_allow_html=True)

            if all_transcripts:
                st.subheader("📹 Vidéos recommandées :")
                cols = st.columns(min(3, len(all_transcripts)))
                for idx, (video_id, data) in enumerate(list(all_transcripts.items())[:3]):
                    if idx >= 3:
                        break
                    with cols[idx]: 
                        if data.get('thumbnail_url'):
                            st.image(data['thumbnail_url'], use_container_width=True)
                        st.write(f"**{data['title']}**")
                        st.markdown(f"[▶️ Voir la vidéo]({data['video_url']})")
    
    end_time = time.time()
    response_time = end_time - start_time
    return full_response, all_transcripts, response_time


#UI UX

def render_header():
    """Affiche l'en-tête de l'application."""
    with st.container():
        col1, col2, col3 = st.columns([1, 6, 1])
        with col2:
            st.markdown("<h2 style='text-align: center;'>💪 Coach Sportif IA</h2>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; font-weight: bold;'>Pose-moi des questions sur les entraînements, la nutrition ou la prévention des blessures !</p>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Voici quelques questions fréquentes : </p>", unsafe_allow_html=True)



def render_quick_questions():
    """Affiche les boutons de questions rapides."""
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Comment faire un squat correctement ?"):
                st.session_state.current_question = "Comment faire un squat correctement ?"
            if st.button("Quels exercices pour perdre du poids ?"):
                st.session_state.current_question = "Quels exercices pour perdre du poids ?"
        with col2:
            if st.button("Comment éviter les douleurs au dos ?"):
                st.session_state.current_question = "Comment éviter les douleurs au dos ?"
            if st.button("Programme full-body pour débutants ?"):
                st.session_state.current_question = "Programme full-body pour débutants ?"

        st.markdown("<p style='text-align:  center; font-weight: bold; color: #27AE60;'>🚀 Conseils d'expert 100% gratuits et locaux !</p>", unsafe_allow_html=True)


def handle_user_input():
    """Gère l'input utilisateur (questions prédéfinies et chat input)"""
    # Gestion des questions pré définies
    if st.session_state.current_question:
        add_message("user", st.session_state.current_question)
        with st.chat_message("user"):
            st.markdown(st.session_state.current_question)
        response, recommendations, response_time = asyncio.run(
            stream_response(st.session_state.current_question)
        )
        add_message("assistant", response, recommendations, response_time)
        st.session_state.current_question = None
        st.rerun()

    #user input
    if prompt := st.chat_input("Quelle est ta question sur le fitness ou la nutrition ?"):
        add_message("user", prompt)
        with st.chat_message("user"):
            st.markdown(prompt)
        response, recommendations, response_time = asyncio.run(
            stream_response(prompt)
        )
        add_message("assistant", response, recommendations, response_time)
        st.rerun()