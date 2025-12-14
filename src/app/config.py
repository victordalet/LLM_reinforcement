import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from langchain_community.chat_models import ChatOllama



#config
load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "false"

# init du LLM avec Ollama => Mistral 7B
llm = ChatOllama(
    model="mistral: 7b-instruct",
    temperature=0.7,
    num_predict=512,  # une limite de tokens pour la réponse
    top_p=0.9,
    repeat_penalty=1.1,
)

# Modèle d'embeddings multilingue (fr inclus)
embed_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2')