from langgraph.graph import MessagesState, StateGraph
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.prebuilt import ToolNode
from langgraph.graph import END
from langgraph.prebuilt import tools_condition
from config import llm
from rag import retrieve



#graphe langgraph

def query_or_respond(state:  MessagesState):
    # Vérifie si la dernière question utilisateur nécessite une recherche
    last_human_message = None
    for msg in reversed(state["messages"]):
        if msg.type == "human":
            last_human_message = msg
            break
    
    if not last_human_message:
        return {"messages": []}

    # Appel manuel de l'outil retrieve
    context, video_recommendations = retrieve(last_human_message.content)

    # Préparer le prompt pour le LLM
    prompt = f"""
    Tu es un coach sportif professionnel francophone spécialisé dans l'accompagnement des débutants. 
    Réponds à la question de l'utilisateur en te basant sur le contexte suivant : 

   {context}

    Question :  {last_human_message.content}
    """

    #llm response generation
    response = llm.invoke([HumanMessage(content=prompt)])

    #add recommandations comme video si possible
    response.artifact = video_recommendations

    return {"messages": [response]}


tools = ToolNode([retrieve])


def generate(state: MessagesState):
    """Génère la réponse finale en utilisant le contexte récupéré"""
    recent_tool_messages = []
    for message in reversed(state["messages"]):
        if message.type == "tool": 
            recent_tool_messages. append(message)
        else:
            break
    tool_messages = recent_tool_messages[: :-1]

    all_transcripts = {}
    docs_content = ""
    
    for doc in tool_messages:
        docs_content += doc.content
        if doc.artifact:
            all_transcripts. update(doc.artifact)

    system_message_content = f"""
Tu es un coach sportif professionnel francophone spécialisé dans l'accompagnement des débutants. Tu fournis des conseils basés sur des preuves scientifiques concernant :  
- Les exercices adaptés aux différents objectifs (prise de muscle, perte de poids, souplesse)
- La nutrition, incluant la planification des repas et la supplémentation
- La prévention des blessures et la sécurité pendant l'entraînement

PRINCIPES DE RÉPONSE :  
- Réponds TOUJOURS en français, de manière claire et accessible
- Utilise un ton encourageant et bienveillant
- Base tes réponses sur le contexte fourni
- Évite le jargon technique complexe
- Décompose les concepts en étapes simples
- Insiste sur la bonne forme et la technique
- Inclus des avertissements de sécurité pertinents
- Fournis des recommandations actionnables

STRUCTURE DE RÉPONSE :
1. Réponds directement à la question
2. Appuie-toi sur des références spécifiques du contexte
3. Fournis des étapes pratiques d'implémentation
4. Inclus les considérations de sécurité
5. Termine avec des recommandations claires

LIMITES :  
- Ne fournis que des conseils basés sur le contexte disponible
- Distingue clairement les principes généraux des recommandations spécifiques
- Si un conseil médical est nécessaire, redirige vers un professionnel de santé
- Reconnaîs quand une question dépasse le contexte fourni

CONTEXTE DE LA BASE DE CONNAISSANCES :
{docs_content}
    """
    
    conversation_messages = [
        message
        for message in state["messages"]
        if message.type in ("human", "system")
        or (message.type == "ai" and not message.tool_calls)
    ]
    
    prompt = [SystemMessage(system_message_content)] + conversation_messages
    response = llm.invoke(prompt)

    return {"messages": [response]}


# Construction du graphe
graph_builder = StateGraph(MessagesState)
graph_builder.add_node(query_or_respond)
graph_builder.add_node(tools)
graph_builder.add_node(generate)

graph_builder.set_entry_point("query_or_respond")
graph_builder.add_conditional_edges(
    "query_or_respond",
    tools_condition,
    {END: END, "tools": "tools"},
)
graph_builder.add_edge("tools", "generate")
graph_builder.add_edge("generate", END)

graph = graph_builder.compile()