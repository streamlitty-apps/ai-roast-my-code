import streamlit as st
from helpers.openai_client import validate_anyscale_api_key


def initial_page_load():
    st.title("Welcome to Resume Fit!")
    if "api_key" not in st.session_state:
        st.session_state.api_key = None

    api_key = st.text_input("Please enter your Anyscale API key:", type="password")
    st.caption(
        "You can get your key from https://app.endpoints.anyscale.com/docs (https://app.endpoints.anyscale.com/credentials)"
    )
    if api_key:
        is_valid = validate_anyscale_api_key(api_key)
        if is_valid:
            st.session_state["api_key"] = api_key
            st.rerun()
        else:
            st.error("Incorrect or invalid Anyscale API key")
            st.stop()
    else:
        st.info("Your Anyscale API key is required to continue")
        st.stop()
