import streamlit as st
from transformers import pipeline
from diffusers import StableDiffusionPipeline
import torch
import os

from src.commons.data_manager import DataManager

st.title("Simple Chat")

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


@st.cache_resource
def get_image_generator():
    if not DataManager.exists_directory(image_output_dir):
        return None

    base_model = "runwayml/stable-diffusion-v1-5"

    pipe = StableDiffusionPipeline.from_pretrained(
        base_model, torch_dtype=torch.float32
    )

    pipe.unet = pipe.unet.from_pretrained(
        os.path.join(image_output_dir, "unet"), torch_dtype=torch.float32
    )

    device = "cpu"
    pipe.to(device)
    return pipe


text_gen = None
image_gen = None
try:
    text_gen = get_generator()
except Exception as e:
    st.sidebar.error(f"Failed to load text model: {e}")

try:
    image_gen = get_image_generator()
except Exception as e:
    st.sidebar.error(f"Failed to load image model: {e}")

if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    if text_gen is not None:
        outputs = text_gen(
            prompt,
            max_length=100,
            num_return_sequences=1,
            do_sample=True,
            top_k=50,
            top_p=0.95,
        )
        assistant_content = outputs[0]["generated_text"]

        with st.chat_message("assistant"):
            st.markdown(assistant_content)

        st.session_state.messages.append(
            {"role": "assistant", "content": assistant_content}
        )

        if image_gen is not None:
            with st.spinner("Generating image"):
                image = image_gen(prompt).images[0]

            st.image(image, caption="Generated Image")
