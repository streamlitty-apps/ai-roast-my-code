import streamlit as st
from openai import OpenAI


def get_openai_client(api_key):
    if not api_key:
        raise ValueError(
            "OpenAI API key is not set. Please set it in your environment variables."
        )
    return OpenAI(api_key=api_key)


def validate_openai_api_key(api_key):
    try:
        client = get_openai_client(api_key=api_key)
        client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": "this is a test",
                }
            ],
            max_tokens=1,
            n=1,
        )
        return True
    except Exception:
        return False


st.header("AI, Roast My Code!")
if "api_key" not in st.session_state:
    api_key = st.text_input("Enter your OpenAI API key", type="password")
    is_valid = validate_openai_api_key(api_key)
    if is_valid:
        st.session_state["api_key"] = api_key
        st.experimental_rerun()
    elif not is_valid and api_key:
        st.error("Incorrect or invalid OpenAI API key")
        st.stop()
    else:
        st.info("OpenAI API key required to continue")
        st.stop()
