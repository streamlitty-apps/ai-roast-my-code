import streamlit as st
from helpers.openai_client import validate_openai_api_key


def run_streamlit_app():
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


if __name__ == "__main__":
    run_streamlit_app()
