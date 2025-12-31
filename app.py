import streamlit as st
from openai import OpenAI
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_API_KEY = os.getenv("HF_API_KEY")

st.title("Text Helper with GPT")

# Dropdown
task = st.selectbox(
    "Select Task",
    ["Text to Text", "Text to Image"]
    
)

user_input = st.text_area("Type your message:")

if st.button("Ask"):

    # ---------- TEXT TO TEXT ----------
    if task == "Text to Text":
        if user_input:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": user_input}
    ]
)

        st.subheader(" Response:")
        st.write(response.choices[0].message.content)

    # ---------- TEXT TO IMAGE ----------
    elif task == "Text to Image":
        if user_input:
            image = client.text_to_image(
                model="black-forest-labs/FLUX.1-dev",
                prompt=user_input,
                
            )

            print(image)
            st.image(image.url)

            
