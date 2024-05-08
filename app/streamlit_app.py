import sys

__import__("pysqlite3")
sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

import asyncio  # noqa: E402
import streamlit as st  # noqa: E402
from streamlit_option_menu import option_menu  # noqa: E402
from views.aiconfig_page import aiconfig_page  # noqa: E402
from views.initial_page_load import initial_page_load  # noqa: E402
from views.roast_my_code_page import roast_my_code_page  # noqa: E402
from views.about_us_page import about_us_page  # noqa: E402
from views.ask_python_questions import ask_python_questions  # noqa: E402


async def run_streamlit_app():
    st.set_page_config(page_title="AI, Roast My Code", page_icon=":clipboard:")

    with st.sidebar:
        selected = option_menu(
            menu_title="Navigation Menu",
            options=[
                "Roast My Code",
                "Ask Python Questions",
                "About AIConfig",
                "About Us",
            ],
            icons=["upload", "book", "people"],
            menu_icon="clipboard",
            default_index=0,
        )

    if selected == "Roast My Code":
        if not st.session_state.get("api_key"):
            initial_page_load()
        else:
            await roast_my_code_page()
    elif selected == "Ask Python Questions":
        if not st.session_state.get("api_key"):
            initial_page_load()
        else:
            await ask_python_questions()
    elif selected == "About AIConfig":
        aiconfig_page()
    elif selected == "About Us":
        about_us_page()


if __name__ == "__main__":
    asyncio.run(run_streamlit_app())
