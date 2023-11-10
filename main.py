# Import the chat model and dotenv loader.
# This function will load environment variables from a `.env` file located in the same directory as the script.
# The `.env` file is typically used to store sensitive information such as API keys securely.
import streamlit as st
from langchain.chat_models import ChatOpenAI
# from dotenv import load_dotenv # for local development
import time

# Load environment variables containing API keys and other sensitive information.
# for local development, you can use a `.env` file to store environment variables.
# load_dotenv()

# Initialize Streamlit interface and the chat model.
st.title('AI Poem Generator')
chat_model = ChatOpenAI()

# Create a text input for poem title.
content = st.text_input('Enter the title of the poem:')

# Button to trigger poem generation.
if st.button('Generate Poem'):
    # Starting the spinner to indicate that the poem is being generated.
    with st.spinner('Wait for it...'):
        time.sleep(5)

    # Generate a poem using the provided title and display it.
    prompt = f"{content}, write a very short funny poem about the subject."
    result = chat_model.predict(prompt)

    st.write(result)
