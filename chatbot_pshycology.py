import openai
import streamlit as st

# Set your OpenAI API key
openai.api_key = "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"

# Initialize a global list to store conversation history
messages = [{"role": "system", "content": "You are a School Psychologist specialized in kids with autism"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

# Streamlit app layout
st.title("School Psychologist specialized in kids with autism")

# Text input for user query
user_input = st.text_input("Your question:", "")

# Button to send query
if st.button("Send"):
    reply = CustomChatGPT(user_input)
    st.text_area("Response:", value=reply, height=500)
