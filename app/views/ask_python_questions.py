import streamlit as st
import os
from helpers.openai_client import validate_anyscale_api_key
from aiconfig import AIConfigRuntime
from chromadb_utils.chromadb_helpers import run_query

async def ask_python_questions():
    st.header("AI, Answer My Python Questions!")

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
            with st.spinner('Pondering your question...'):
                context = run_query(question_input, "pep8_guidelines", 2)
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