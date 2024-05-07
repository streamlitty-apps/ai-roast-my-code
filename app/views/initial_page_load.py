import streamlit as st
import os
from helpers.openai_client import validate_anyscale_api_key


def initial_page_load():
    st.header("AI, Roast My Code: Enter an Anyscale API Key to continue")

    if "api_key" not in st.session_state:
        api_key = st.text_input("Please enter your Anyscale API key:", type="password")
    
        button_html = """
        <style>
        .styledButton {
            color: white;
            background-color: #007BFF;
            padding: 8px 20px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            font-size: 14px;
            margin-bottom: 10px;
            display: block; 
            transition: background-color 0.3s, box-shadow 0.3s;
        }
        .styledButton:hover {
            background-color: #0056b3;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }
        </style>
        <button class="styledButton" onclick="window.open('https://app.endpoints.anyscale.com/docs')">Get API Key</button>
        <button class="styledButton" onclick="window.open('https://app.endpoints.anyscale.com/credentials')">API Credentials</button>
        """
        st.markdown(button_html, unsafe_allow_html=True)

        if api_key:
            is_valid = validate_anyscale_api_key(api_key)
            if is_valid:
                st.session_state["api_key"] = api_key
                os.environ["ANYSCALE_ENDPOINT_API_KEY"] = st.session_state["api_key"]
                st.experimental_rerun()
            else:
                st.error("Incorrect or invalid Anyscale API key")
                st.stop()
        else:
            st.info("Your Anyscale API key is required to continue")
            st.stop()
    else:
        os.environ["ANYSCALE_ENDPOINT_API_KEY"] = st.session_state["api_key"]
