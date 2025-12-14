"""
Module de styles minimalistes pour application Streamlit
Styles épurés et modernes pour une interface claire et performante
"""

import streamlit as st


def inject_global_styles():
    """
    Applique les styles globaux de base pour toute l'application. 
    Arrière-plan neutre et conteneur principal épuré.
    Compatible light mode et dark mode.
    """
    st.markdown("""
        <style>
        /* Import de police moderne */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Variables CSS pour light/dark mode */
        :root {
            --bg-primary: #ffffff;
            --bg-secondary: #f8fafc;
            --text-primary:  #0f172a;
            --text-secondary: #475569;
            --border-color: #e2e8f0;
            --accent-color: #2563eb;
            --accent-hover: #1d4ed8;
        }
        
        /* Dark mode */
        @media (prefers-color-scheme: dark) {
            :root {
                --bg-primary: #0f172a;
                --bg-secondary: #1e293b;
                --text-primary:  #f1f5f9;
                --text-secondary: #cbd5e1;
                --border-color: #334155;
                --accent-color: #3b82f6;
                --accent-hover: #2563eb;
            }
        }
        
        /* Styles globaux */
        * {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }
        
        /* Body */
        body {
            background-color: var(--bg-secondary);
            color: var(--text-primary);
        }
        
        /* Conteneur principal */
        .main {
            background-color: var(--bg-primary);
            border-radius: 12px;
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        /* Espacement des blocs */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 900px;
        }
        
        /* Supprimer le padding du top */
        .main . block-container {
            padding-top: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)


def inject_header_logo_style():
    """
    Style pour le header avec logo centré et titre.  
    Logo + Titre "Coach Sportif IA" sur la même ligne
    Sous-titre "Pose-moi une question…" en dessous
    """
    st.markdown("""
        <style>
        /* Conteneur du header */
        .header-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 2rem 0 1.5rem 0;
            text-align: center;
        }
        
        /* Logo + Titre sur la même ligne */
        .logo-title-wrapper {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 0.5rem;
        }
        
        /* Logo image */
        .app-logo-img {
            width: 80px;
            height: 80px;
            border-radius:  12px;
            object-fit: cover;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        /* Logo emoji (fallback) */
        .app-logo {
            font-size:  3rem;
            line-height: 1;
        }
        
        /* Titre principal */
        .app-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--text-primary);
            margin: 0;
            line-height: 1;
            letter-spacing: -0.02em;
        }
        
        /* Sous-titre */
        .app-subtitle {
            font-size: 1.1rem;
            font-weight: 400;
            color: var(--text-secondary);
            margin:  0.5rem 0 0 0;
            letter-spacing: 0.01em;
        }
        
        /* Description */
        .app-description {
            font-size: 0.95rem;
            font-weight: 400;
            color: var(--text-secondary);
            margin:  1rem 0 0.5rem 0;
        }
        
        /* Badge/Tag */
        .app-badge {
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 0.5rem 1.2rem;
            border-radius:  50px;
            font-size:  0.9rem;
            font-weight:  600;
            margin-top: 1rem;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }
        </style>
    """, unsafe_allow_html=True)


def inject_button_style():
    """
    Boutons minimalistes avec un style épuré et moderne.
    """
    st.markdown("""
        <style>
        /* Boutons principaux */
        . stButton > button {
            width: 100%;
            background-color: var(--accent-color);
            color: white;
            border:  none;
            border-radius:  8px;
            padding: 0.75rem 1.5rem;
            font-weight: 500;
            font-size: 0.95rem;
            transition: all 0.2s ease;
            cursor: pointer;
            box-shadow: 0 2px 8px rgba(37, 99, 235, 0.15);
        }
        
        /* Effet de survol */
        .stButton > button:hover {
            background-color: var(--accent-hover);
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
        }
        
        /* État actif */
        . stButton > button: active {
            transform: translateY(0);
            box-shadow: 0 2px 6px rgba(37, 99, 235, 0.2);
        }
        
        /* Focus */
        .stButton > button:focus {
            outline: 2px solid var(--accent-color);
            outline-offset: 2px;
        }
        
        /* Boutons dans les colonnes (questions rapides) */
        [data-testid="column"] . stButton > button {
            font-size: 0.9rem;
            padding: 0.65rem 1rem;
            text-align: left;
        }
        </style>
    """, unsafe_allow_html=True)


def inject_chat_style():
    """
    Messages de chat avec bulles épurées et modernes.
    Compatible light/dark mode.
    """
    st.markdown("""
        <style>
        /* Conteneur des messages */
        .stChatMessage {
            padding: 1.25rem;
            margin: 1rem 0;
            border-radius: 12px;
            background-color:  var(--bg-secondary);
            border:  1px solid var(--border-color);
            transition: all 0.2s ease;
        }
        
        /* Messages utilisateur */
        .stChatMessage[data-testid="user-message"] {
            background:  linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
            border-left: 4px solid var(--accent-color);
            border:  1px solid var(--accent-color);
        }
        
        /* Messages assistant */
        .stChatMessage[data-testid="assistant-message"] {
            background-color: var(--bg-secondary);
            border-left: 4px solid var(--text-secondary);
        }
        
        /* Texte dans les messages */
        .stChatMessage p {
            line-height: 1.7;
            margin: 0;
            color: var(--text-primary);
            font-size: 0.95rem;
        }
        
        /* Avatar dans les messages */
        .stChatMessage [data-testid="chatAvatarIcon"] {
            background-color: var(--accent-color);
            border-radius: 8px;
        }
        </style>
    """, unsafe_allow_html=True)


def inject_input_style():
    """
    Champ de saisie minimaliste et fonctionnel.
    """
    st.markdown("""
        <style>
        /* Conteneur du chat input */
        .stChatInput {
            border-radius: 12px;
            padding: 0.5rem 0;
        }
        
        /* Champ de saisie */
        .stChatInput > div > div > input {
            border: 2px solid var(--border-color);
            border-radius: 12px;
            padding: 0.85rem 1.2rem;
            font-size:  0.95rem;
            transition: all 0.2s ease;
            background-color: var(--bg-primary);
            color: var(--text-primary);
        }
        
        /* Focus sur l'input */
        .stChatInput > div > div > input:focus {
            border-color: var(--accent-color);
            outline: none;
            box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.1);
        }
        
        /* Placeholder */
        .stChatInput > div > div > input::placeholder {
            color: var(--text-secondary);
            font-weight: 400;
        }
        
        /* Bouton d'envoi */
        .stChatInput button {
            border-radius: 8px;
            background-color: var(--accent-color);
            transition: all 0.2s ease;
        }
        
        . stChatInput button:hover {
            background-color: var(--accent-hover);
        }
        </style>
    """, unsafe_allow_html=True)


def inject_header_style():
    """
    Titres simples et lisibles avec hiérarchie claire.
    """
    st. markdown("""
        <style>
        /* Titres */
        h1, h2, h3, h4 {
            color:  var(--text-primary);
            font-weight: 600;
            letter-spacing: -0.02em;
        }
        
        /* Titre H1 */
        h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            line-height: 1.2;
            font-weight: 700;
        }
        
        /* Titre H2 */
        h2 {
            font-size:  1.875rem;
            margin-bottom: 0.875rem;
            line-height:  1.3;
        }
        
        /* Titre H3 */
        h3 {
            font-size:  1.5rem;
            margin-bottom: 0.75rem;
            line-height: 1.4;
            color: var(--text-primary);
        }
        
        /* Titre H4 (sous-titres) */
        h4 {
            font-size: 1.125rem;
            margin-bottom: 0.5rem;
            color: var(--text-secondary);
            font-weight: 500;
        }
        </style>
    """, unsafe_allow_html=True)


def inject_card_style():
    """
    Cartes modernes pour organiser le contenu.
    """
    st.markdown("""
        <style>
        /* Cartes */
        .card {
            background:  var(--bg-primary);
            border:  1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1rem 0;
            transition: all 0.2s ease;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        }
        
        .card:hover {
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            transform: translateY(-2px);
        }
        
        /* Conteneurs de colonnes */
        [data-testid="column"] {
            padding: 0.5rem;
        }
        
        /* Containers Streamlit */
        [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
            background-color: var(--bg-primary);
            border-radius: 12px;
            padding: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)


def inject_spinner_style():
    """
    Indicateur de chargement minimaliste et moderne.
    """
    st. markdown("""
        <style>
        /* Spinner */
        .stSpinner > div {
            border-top-color: var(--accent-color) !important;
            border-width: 3px !important;
        }
        
        /* Texte du spinner */
        .stSpinner > div > div {
            color: var(--text-secondary);
            font-weight: 500;
            font-size: 0.95rem;
        }
        
        /* Animation de pulsation pour le spinner */
        @keyframes pulse {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity:  0.5;
            }
        }
        
        . stSpinner {
            animation: pulse 1.5s ease-in-out infinite;
        }
        </style>
    """, unsafe_allow_html=True)


def inject_image_style():
    """
    Images avec style épuré et moderne.
    """
    st.markdown("""
        <style>
        /* Images */
        img {
            border-radius: 12px;
            max-width:  100%;
            height: auto;
            transition: all 0.3s ease;
        }
        
        /* Images dans colonnes */
        [data-testid="column"] img {
            width: 100%;
            object-fit: cover;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        }
        
        /* Effet hover sur les images */
        [data-testid="column"] img:hover {
            transform: scale(1.02);
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
        }
        
        /* Images de vidéos (thumbnails) */
        .stImage {
            border-radius: 12px;
            overflow: hidden;
        }
        </style>
    """, unsafe_allow_html=True)


def inject_link_style():
    """
    Liens simples et lisibles avec effet moderne.
    """
    st. markdown("""
        <style>
        /* Liens */
        a {
            color: var(--accent-color);
            text-decoration: none;
            font-weight: 500;
            transition: all 0.2s ease;
            position: relative;
        }
        
        /* Survol */
        a:hover {
            color: var(--accent-hover);
        }
        
        /* Effet underline animé */
        a::after {
            content: '';
            position: absolute;
            width: 0;
            height:  2px;
            bottom:  -2px;
            left: 0;
            background-color: var(--accent-color);
            transition: width 0.3s ease;
        }
        
        a: hover::after {
            width:  100%;
        }
        
        /* Liens dans les messages de chat */
        .stChatMessage a {
            color: var(--accent-color);
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)


def inject_container_style():
    """
    Conteneurs et sections épurés.
    """
    st.markdown("""
        <style>
        /* Conteneurs */
        .element-container {
            margin: 0. 5rem 0;
        }
        
        /* Espacement vertical */
        [data-testid="stVerticalBlock"] {
            gap: 1rem;
        }
        
        /* Séparateurs */
        hr {
            border: none;
            height: 1px;
            background-color: var(--border-color);
            margin:  2. 5rem 0;
        }
        
        /* Containers avec bordure */
        . stContainer {
            border-radius: 12px;
            padding: 1.5rem;
        }
        </style>
    """, unsafe_allow_html=True)


def inject_animation_style():
    """
    Animations légères et fluides.
    """
    st.markdown("""
        <style>
        /* Animation fade-in légère */
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Application aux messages */
        .stChatMessage {
            animation: fadeIn 0.4s ease;
        }
        
        /* Animation slide-up pour les éléments */
        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Application aux conteneurs */
        .element-container {
            animation: slideUp 0.3s ease;
        }
        
        /* Transition douce pour tous les éléments interactifs */
        button, input, a, .card {
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }
        </style>
    """, unsafe_allow_html=True)


def inject_video_recommendations_style():
    """
    Style pour les vidéos recommandées dans le chat.
    """
    st.markdown("""
        <style>
        /* Conteneur des vidéos recommandées */
        .stChatMessage [data-testid="column"] {
            background-color: transparent;
            padding: 0.5rem;
        }
        
        /* Cartes de vidéos */
        .stChatMessage [data-testid="column"] > div {
            background-color: var(--bg-primary);
            border:  1px solid var(--border-color);
            border-radius: 12px;
            padding: 1rem;
            transition: all 0.3s ease;
            height: 100%;
        }
        
        . stChatMessage [data-testid="column"] > div:hover {
            transform: translateY(-4px);
            box-shadow:  0 8px 20px rgba(0, 0, 0, 0.12);
            border-color: var(--accent-color);
        }
        
        /* Titre des vidéos */
        .stChatMessage [data-testid="column"] p strong {
            color: var(--text-primary);
            font-size: 0.9rem;
            line-height: 1.4;
        }
        
        /* Liens vers les vidéos */
        . stChatMessage [data-testid="column"] a {
            display: inline-block;
            margin-top: 0.5rem;
            padding: 0.4rem 0.8rem;
            background-color: var(--accent-color);
            color:  white ! important;
            border-radius:  6px;
            font-size: 0.85rem;
            font-weight: 500;
            text-align: center;
            transition: all 0.2s ease;
        }
        
        .stChatMessage [data-testid="column"] a:hover {
            background-color: var(--accent-hover);
            transform:  scale(1.05);
        }
        
        . stChatMessage [data-testid="column"] a:: after {
            display: none;
        }
        </style>
    """, unsafe_allow_html=True)


def inject_sidebar_style():
    """
    Style pour la sidebar si utilisée.
    """
    st.markdown("""
        <style>
        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: var(--bg-secondary);
            border-right: 1px solid var(--border-color);
        }
        
        [data-testid="stSidebar"] . block-container {
            padding: 2rem 1rem;
        }
        </style>
    """, unsafe_allow_html=True)


def inject_all_styles():
    """
    Applique tous les styles minimalistes en une seule fois.
    Cette fonction doit être appelée au début de votre application Streamlit.
    """
    inject_global_styles()
    inject_header_logo_style()
    inject_button_style()
    inject_chat_style()
    inject_input_style()
    inject_header_style()
    inject_card_style()
    inject_spinner_style()
    inject_image_style()
    inject_link_style()
    inject_container_style()
    inject_animation_style()
    inject_video_recommendations_style()
    inject_sidebar_style()

