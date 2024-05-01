import streamlit as st
import os
import asyncio
from helpers.openai_client import validate_anyscale_api_key
from aiconfig import AIConfigRuntime
from chromadb_utils.helpers.chromadb_helpers import run_query

async def run_streamlit_app():
    st.header("AI, Answer My Python Questions!")
    if "api_key" not in st.session_state:
        api_key = st.text_input("Enter your Anyscale API key", type="password")
        st.caption("You can get your key from https://app.endpoints.anyscale.com/docs (https://app.endpoints.anyscale.com/credentials)")
        is_valid = validate_anyscale_api_key(api_key)
        if is_valid:
            st.session_state["api_key"] = api_key
            st.experimental_rerun()
        elif not is_valid and api_key:
            st.error("Incorrect or invalid OpenAI API key")
            st.stop()
        else:
            st.info("OpenAI API key required to continue")
            st.stop()
    else:
        os.environ["ANYSCALE_ENDPOINT_API_KEY"] = st.session_state["api_key"]

    st.info("🔍 **Leveraging PEP 8 Standards**\n\n"
                    "To ensure that responses to Python-related questions adhere to industry best practices, "
                    "we follow the guidelines outlined in PEP 8, the official style guide for Python code. "
                    "PEP 8 promotes code readability and maintainability by establishing conventions for "
                    "naming, layout, and indentation.\n\n"
                    "For more information, refer to the [official Python PEP 8 documentation](https://www.python.org/dev/peps/pep-0008/).")

    with st.form("question_input_form"):
        question_input = st.text_area("Ask any Python-related question:")
        submit_question = st.form_submit_button("Submit Question")

    if submit_question:
        if not question_input:
            st.error("Question input is empty")
        else:
            context = run_query(question_input, "pep8_guidelines", 5)
            result = await generate_answer(context, question_input)
            st.write(result)

async def generate_answer(context, user_question):
    config = AIConfigRuntime.load("app/roast_my_code.aiconfig.json")
    params = {
        "context": context,
        "user_question": user_question
    }
    response = await config.run("python_help", params=params)
    return response[0].data


if __name__ == "__main__":
    asyncio.run(run_streamlit_app())
