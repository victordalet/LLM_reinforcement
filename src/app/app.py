import streamlit as st
from transformers import pipeline

st.title("Simple chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

output_dir = "./mini-gpt-finetuned"

image_output_dir = "./image-model-finetuned"


@st.cache_resource
def get_generator():
    return pipeline("text-generation", model=output_dir, tokenizer=output_dir)


generator = None
try:
    generator = get_generator()
except Exception as e:
    st.sidebar.error(f"Failed to load model: {e}")

if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    if generator is not None:
        outputs = generator(
            prompt,
            max_length=100,
            num_return_sequences=3,
            do_sample=True,
            top_k=50,
            top_p=0.95,
        )
        assistant_content = "".join(outputs[0]['generated_text'])

        with st.chat_message("assistant"):
            st.markdown(assistant_content)
        st.session_state.messages.append({"role": "assistant", "content": assistant_content})
