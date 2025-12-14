
"""
Module de styles personnalisés pour application Streamlit
Contient des fonctions réutilisables pour injecter du CSS personnalisé
"""

import streamlit as st


def inject_global_styles():
    """
    Applique les styles globaux de base pour toute l'application. 
    Inclut :  polices, couleurs de fond, marges générales. 
    """
    st.markdown("""
        <style>
        /* Import de polices modernes */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
        
        /* Styles globaux */
        * {
            font-family: 'Poppins', sans-serif;
        }
        
        /* Arrière-plan principal */
        . stApp {
            background:  linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        /* Conteneur principal */
        .main {
            background-color: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 2rem;
            margin: 1rem;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
        }
        
        /* Supprime les marges par défaut */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)


def inject_button_style():
    """
    Personnalise tous les boutons de l'application.
    Applique :  couleurs vives, effets de survol, animations, bordures arrondies.
    """
    st.markdown("""
        <style>
        /* Boutons principaux */
        .stButton > button {
            width: 100%;
            background: linear-gradient(135deg, #27AE60 0%, #229954 100%);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.8rem 1.5rem;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(39, 174, 96, 0.3);
            cursor: pointer;
        }
        
        /* Effet de survol */
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(39, 174, 96, 0.4);
            background: linear-gradient(135deg, #229954 0%, #27AE60 100%);
        }
        
        /* Effet de clic */
        .stButton > button:active {
            transform:  translateY(0);
            box-shadow: 0 2px 10px rgba(39, 174, 96, 0.3);
        }
        
        /* Animation de pulsation */
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        .stButton > button:focus {
            animation: pulse 0.5s ease;
            outline: none;
            box-shadow: 0 0 0 3px rgba(39, 174, 96, 0.2);
        }
        </style>
    """, unsafe_allow_html=True)


def inject_chat_style():
    """
    Stylise les messages du chat (utilisateur et assistant).
    Applique : bulles de chat colorées, avatars, espacement, alignement.
    """
    st.markdown("""
        <style>
        /* Conteneur des messages */
        .stChatMessage {
            background-color: transparent;
            border-radius: 15px;
            padding: 1rem;
            margin: 0.5rem 0;
        }
        
        /* Messages utilisateur */
        .stChatMessage[data-testid="user-message"] {
            background:  linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            margin-left: 20%;
        }
        
        /* Messages assistant */
        .stChatMessage[data-testid="assistant-message"] {
            background-color: #f8f9fa;
            border:  2px solid #e9ecef;
            margin-right: 20%;
        }
        
        /* Icônes de chat */
        .stChatMessage img {
            border-radius: 50%;
            border: 3px solid #27AE60;
        }
        
        /* Texte dans les messages */
        .stChatMessage p {
            line-height: 1.6;
            margin: 0;
        }
        </style>
    """, unsafe_allow_html=True)


def inject_input_style():
    """
    Personnalise le champ de saisie du chat.
    Applique : bordure élégante, focus animé, placeholder stylisé.
    """
    st.markdown("""
        <style>
        /* Champ de saisie principal */
        .stChatInput {
            border-radius: 25px;
            border: 2px solid #e9ecef;
            transition: all 0.3s ease;
        }
        
        /* Input texte */
        .stChatInput > div > div > input {
            border-radius: 25px;
            border: 2px solid #27AE60;
            padding:  1rem 1.5rem;
            font-size: 1rem;
            transition: all 0.3s ease;
        }
        
        /* Focus sur l'input */
        .stChatInput > div > div > input:focus {
            border-color: #229954;
            box-shadow:  0 0 0 3px rgba(39, 174, 96, 0.1);
            outline: none;
        }
        
        /* Placeholder */
        .stChatInput > div > div > input::placeholder {
            color: #95a5a6;
            font-style: italic;
        }
        </style>
    """, unsafe_allow_html=True)


def inject_header_style():
    """
    Stylise les titres et en-têtes (h1, h2, h3).
    Applique : dégradés de couleur, ombres, animations d'apparition.
    """
    st.markdown("""
        <style>
        /* Titres principaux */
        h1, h2, h3 {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip:  text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 700;
            letter-spacing: -0.5px;
        }
        
        /* Titre H1 */
        h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            animation: fadeInDown 0.8s ease;
        }
        
        /* Titre H2 */
        h2 {
            font-size: 2rem;
            margin-bottom: 0.8rem;
            animation: fadeInDown 0.8s ease 0.2s backwards;
        }
        
        /* Titre H3 */
        h3 {
            font-size: 1.5rem;
            margin-bottom: 0.6rem;
            color: #2c3e50;
        }
        
        /* Animation d'apparition */
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        </style>
    """, unsafe_allow_html=True)


def inject_card_style():
    """
    Crée des cartes élégantes pour contenus (vidéos, infos).
    Applique : ombres, bordures arrondies, effets de survol.
    """
    st.markdown("""
        <style>
        /* Cartes génériques */
        .card {
            background: white;
            border-radius: 15px;
            padding: 1.5rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            margin:  1rem 0;
        }
        
        /* Effet de survol sur les cartes */
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        }
        
        /* Conteneurs de colonnes */
        [data-testid="column"] {
            background: transparent;
            padding: 0.5rem;
        }
        
        /* Images dans les cartes */
        . card img {
            border-radius: 10px;
            width: 100%;
            height:  auto;
            transition: transform 0.3s ease;
        }
        
        .card img:hover {
            transform: scale(1.05);
        }
        </style>
    """, unsafe_allow_html=True)


def inject_spinner_style():
    """
    Personnalise les spinners et indicateurs de chargement.
    Applique : couleurs personnalisées, animations fluides.
    """
    st.markdown("""
        <style>
        /* Conteneur du spinner */
        .stSpinner > div {
            border-top-color: #27AE60 !important;
            border-right-color: #27AE60 !important;
        }
        
        /* Texte du spinner */
        .stSpinner > div > div {
            color: #27AE60;
            font-weight: 600;
            font-size: 1.1rem;
        }
        
        /* Animation personnalisée */
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        </style>
    """, unsafe_allow_html=True)


def inject_image_style():
    """
    Améliore le rendu des images (thumbnails vidéos, etc.).
    Applique : bordures arrondies, ombres, effets de zoom au survol.
    """
    st.markdown("""
        <style>
        /* Toutes les images */
        img {
            border-radius: 12px;
            box-shadow:  0 4px 15px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        
        /* Effet de survol sur images */
        img:hover {
            transform: scale(1.03);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
            cursor: pointer;
        }
        
        /* Images dans les colonnes */
        [data-testid="column"] img {
            width: 100%;
            height:  auto;
            object-fit: cover;
        }
        </style>
    """, unsafe_allow_html=True)


def inject_link_style():
    """
    Stylise les liens (vidéos YouTube, etc.).
    Applique : couleurs vives, soulignement animé, effets de survol. 
    """
    st.markdown("""
        <style>
        /* Liens généraux */
        a {
            color: #27AE60;
            text-decoration: none;
            font-weight: 600;
            position: relative;
            transition: all 0.3s ease;
        }
        
        /* Soulignement animé */
        a::after {
            content:  '';
            position: absolute;
            width: 0;
            height:  2px;
            bottom:  -2px;
            left: 0;
            background-color: #27AE60;
            transition: width 0.3s ease;
        }
        
        /* Effet de survol */
        a:hover {
            color:  #229954;
        }
        
        a:hover::after {
            width: 100%;
        }
        
        /* Liens dans les boutons vidéo */
        .stMarkdown a {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 1rem;
            background: linear-gradient(135deg, #27AE60 0%, #229954 100%);
            color: white ! important;
            border-radius:  8px;
            transition: all 0.3s ease;
        }
        
        .stMarkdown a:hover {
            transform: translateX(5px);
            box-shadow: 0 4px 15px rgba(39, 174, 96, 0.3);
        }
        </style>
    """, unsafe_allow_html=True)


def inject_container_style():
    """
    Améliore les conteneurs et sections de l'application.
    Applique : espacements, arrière-plans subtils, séparateurs.
    """
    st.markdown("""
        <style>
        /* Conteneurs principaux */
        .element-container {
            margin: 0. 5rem 0;
        }
        
        /* Sections avec bordures */
        [data-testid="stVerticalBlock"] {
            gap: 1rem;
        }
        
        /* Conteneurs personnalisés */
        .custom-container {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border-radius: 15px;
            padding: 2rem;
            margin: 1rem 0;
            border-left: 5px solid #27AE60;
        }
        
        /* Séparateurs */
        hr {
            border: none;
            height: 2px;
            background: linear-gradient(90deg, transparent, #27AE60, transparent);
            margin: 2rem 0;
        }
        </style>
    """, unsafe_allow_html=True)


def inject_animation_style():
    """
    Ajoute des animations d'apparition et de transition.
    Applique : fade-in, slide-in, bounce pour éléments dynamiques.
    """
    st.markdown("""
        <style>
        /* Animation fade-in globale */
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Animation slide-in depuis la gauche */
        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        /* Animation slide-in depuis la droite */
        @keyframes slideInRight {
            from {
                opacity: 0;
                transform: translateX(50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        /* Animation bounce */
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        
        /* Appliquer fade-in aux messages */
        .stChatMessage {
            animation: fadeIn 0.5s ease;
        }
        
        /* Appliquer slide-in aux colonnes */
        [data-testid="column"]:nth-child(odd) {
            animation: slideInLeft 0.6s ease;
        }
        
        [data-testid="column"]:nth-child(even) {
            animation: slideInRight 0.6s ease;
        }
        </style>
    """, unsafe_allow_html=True)


def inject_all_styles():
    """
    Fonction pratique qui applique TOUS les styles en une seule fois.
    Idéal pour initialiser le design complet de l'application.
    """
    inject_global_styles()
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


# Exemple d'utilisation dans app.py : 
# from streamlit_styles import inject_all_styles
# inject_all_styles()