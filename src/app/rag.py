import os
import json
import chromadb
from chromadb.config import Settings
from config import embed_model



# Init CHROMA (base de donnees vectorielle)

chroma_client = chromadb.PersistentClient(path="./chroma_db")

# Créer ou récupérer la collection
try:
    collection = chroma_client.get_collection(name="fitness_coach")
except:  
    collection = chroma_client.create_collection(
        name="fitness_coach",
        metadata={"hnsw: space": "cosine"}
    )
    
    # upload dataset fitness JSON file
    fitness_data_path = "fitness_dataset.json"  
    
    if os.path.exists(fitness_data_path):
        with open(fitness_data_path, 'r', encoding='utf-8') as f:
            fitness_data = json.load(f)
        
        # Indexer le dataset
        documents = []
        metadatas = []
        ids = []
        
        for idx, item in enumerate(fitness_data):
            documents.append(item.get("content", ""))
            metadatas.append({
                "title":  item.get("title", ""),
                "video":   item.get("video", ""),
                "category": item.get("category", "general")
            })
            ids.append(f"fitness_{idx}")
        
        # genere les embeddings
        embeddings = embed_model.encode(documents).tolist()
        
        # add to Chroma
        collection.add(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )
        print("✅ Base de données fitness chargée avec succès!")


# RAG - recuperation de contexte


def retrieve(query: str):
    """Récupère des informations détaillées sur les exercices, la nutrition et la prévention des blessures en fonction de la question de l'utilisateur."""
    
    # Génération de l'embedding de la requête
    query_embedding = embed_model.encode(query).tolist()
    
    # search in chroma
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5,
        include=["documents", "metadatas", "distances"]
    )
    
    # results extract
    documents = results['documents'][0]
    metadatas = results['metadatas'][0]
    
    # text building 
    context_parts = []
    video_recommendations = {}
    
    for idx, (doc, meta) in enumerate(zip(documents, metadatas)):
        context_parts.append(f"**{meta['title']}**\n{doc}")
        
        # Préparer les recommandations vidéo
        if meta.get('video') and idx < 3:
            video_recommendations[f"vid_{idx}"] = {
                "title": meta['title'],
                "video_url":  meta['video'],
                "thumbnail_url": f"https://img.youtube.com/vi/{meta['video'].split('v=')[-1]}/maxresdefault.jpg" if 'youtube.com' in meta['video'] else ""
            }
    
    final_context = "\n\n---\n\n".join(context_parts)
    
    return final_context, video_recommendations