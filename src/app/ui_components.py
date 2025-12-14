import streamlit as st
import time
import asyncio
from langchain_core.messages import HumanMessage
from agent import graph
import os
import base64

BASE_DIR = os.path.dirname(__file__)
logo_path = os.path.join(BASE_DIR, "logo.png")


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
        "role":  role,
        "content": content,
        "recommendations": recommendations,
        "response_time": response_time
    })


def display_chat_history():
    """Affiche l'historique des messages dans l'ordre chronologique"""
    
    for message in st.session_state.chat_history: 
        with st.chat_message(message["role"]):
            st.markdown(message["content"], unsafe_allow_html=True)

            if message.get("recommendations"):
                st.subheader("📹 Vidéos recommandées :")
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
        # Placeholder pour le spinner
        spinner_placeholder = st.empty()
        
        # Afficher le spinner pendant le chargement
        with spinner_placeholder: 
            with st.spinner("✨ Je réfléchis à ta question...✨"):
                message_placeholder = st.empty()
                full_response = ""
                all_transcripts = {}

                async for message, metadata in graph.astream(
                    {"messages":  [HumanMessage(content=prompt)]},
                    stream_mode="messages",
                ):
                    if not isinstance(message, HumanMessage) and message.type != "tool":
                        full_response += message.content
                        message_placeholder.markdown(full_response + "▌", unsafe_allow_html=True)

                    if message.type == "tool" and message.artifact:
                        all_transcripts.update(message.artifact)

                # Afficher la réponse finale sans le curseur
                message_placeholder.markdown(full_response.strip(), unsafe_allow_html=True)
        
        
        spinner_placeholder.empty()
        
        # Afficher la réponse finale (en dehors du spinner)
        st.markdown(full_response.strip(), unsafe_allow_html=True)
        
        # Afficher les vidéos recommandées si disponibles
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
def get_image_base64(image_path):
    """Convertit une image en base64 pour l'afficher dans HTML"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

def render_header():
    """Affiche l'en-tête de l'application avec logo centré."""
    

    logo_base64 = get_image_base64(logo_path)
    
    if logo_base64:
        st.markdown(f"""
            <div class="header-container">
                <div class="logo-title-wrapper">
                    <img src="data:image/png;base64,{logo_base64}" class="app-logo-img" alt="Logo" style="width: 80px; height: 80px; border-radius: 12px;" />
                    <h1 class="app-title" style="margin: 0;">Coach Sportif IA</h1>
                </div>
                <p class="app-subtitle">Pose-moi une question…</p>
                <p class="app-description">Pose-moi des questions sur les entraînements, la nutrition ou la prévention des blessures !</p>
                <span class="app-badge">🚀 Conseils d'expert 100% gratuits et locaux !</span>
            </div>
            <hr style="margin: 2rem 0;">
        """, unsafe_allow_html=True)
    else:

        st.markdown("""
            <div class="header-container">
                <div class="logo-title-wrapper">
                    <span class="app-logo">💪</span>
                    <h1 class="app-title" style="margin: 0;">Coach Sportif IA</h1>
                </div>
                <p class="app-subtitle">Pose-moi une question…</p>
                <p class="app-description">Pose-moi des questions sur les entraînements, la nutrition ou la prévention des blessures ! </p>
                <span class="app-badge">🚀 Conseils d'expert 100% gratuits et locaux ! </span>
            </div>
            <hr style="margin: 2rem 0;">
        """, unsafe_allow_html=True)


def render_quick_questions():
    """Affiche les boutons de questions rapides."""
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Comment faire un squat correctement ? "):
                st.session_state.current_question = "Comment faire un squat correctement ?"
            if st.button("Quels exercices pour perdre du poids ?"):
                st.session_state.current_question = "Quels exercices pour perdre du poids ?"
        with col2:
            if st.button("Comment éviter les douleurs au dos ?"):
                st.session_state.current_question = "Comment éviter les douleurs au dos ?"
            if st.button("Programme full-body pour débutants ?"):
                st.session_state.current_question = "Programme full-body pour débutants ?"



def handle_user_input():
    """Gère l'input utilisateur (questions prédéfinies et chat input)"""
    # Gestion des questions prédéfinies
    if st.session_state.current_question:
      
        add_message("user", st.session_state.current_question)
        
        # Générer la réponse (qui s'affichera automatiquement avec stream_response)
        response, recommendations, response_time = asyncio.run(
            stream_response(st.session_state.current_question)
        )
        
        # Ajouter la réponse à l'historique
        add_message("assistant", response, recommendations, response_time)
        
        # Réinitialiser la question et recharger
        st.session_state.current_question = None
        st.rerun()

    # User input
    if prompt := st.chat_input("Quelle est ta question sur le fitness ou la nutrition ?"):
       
        add_message("user", prompt)
        
        # Générer la réponse (qui s'affichera automatiquement avec stream_response)
        response, recommendations, response_time = asyncio.run(
            stream_response(prompt)
        )
        
        # Ajouter la réponse à l'historique
        add_message("assistant", response, recommendations, response_time)
        
        # Recharger l'application
        st.rerun()