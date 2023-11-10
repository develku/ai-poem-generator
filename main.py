import streamlit as st
# from dotenv import load_dotenv  # Uncomment for local development
from langchain.llms import CTransformers
import time

# Uncomment the line below for local development to load environment variables from a .env file
# load_dotenv()

# Initialize Streamlit interface.
st.title('AI Poem Generator')

# Instantiate the language model.
llm = CTransformers(
    model="llama-2-7b-chat.ggmlv3.q3_K_L.bin",
    model_type="llama"
)

# Input field for the poem title.
content = st.text_input('Enter the title of the poem:')

# Button to trigger poem generation.
if st.button('Generate Poem'):
    with st.spinner('Generating poem...'):
        # Simulate a processing delay.
        time.sleep(5)
        # Generate a poem using the provided title.
        prompt = f"{content}, write a very short funny poem about the subject."
        result = llm.predict(prompt)
        st.write(result)
