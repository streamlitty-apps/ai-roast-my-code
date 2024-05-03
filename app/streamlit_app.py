import streamlit as st
from streamlit_option_menu import option_menu
from views.aiconfig_page import aiconfig_page
from views.initial_page_load import initial_page_load
from views.roast_my_code_page import roast_my_code_page


def run_streamlit_app():
    st.set_page_config(page_title="AI, Roast My Code", page_icon=":clipboard:")

    with st.sidebar:
        selected = option_menu(
            menu_title="Navigation Menu",
            options=["Roast My Code", "About AIConfig"],
            icons=["upload", "book"],
            menu_icon="clipboard",
            default_index=0,
        )

    if selected == "Roast My Code":
        if not st.session_state.get("api_key"):
            initial_page_load()
        else:
            roast_my_code_page()
    elif selected == "About AIConfig":
        aiconfig_page()


if __name__ == "__main__":
    run_streamlit_app()
