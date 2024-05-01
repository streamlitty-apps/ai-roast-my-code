import asyncio
import streamlit as st
from aiconfig import AIConfigRuntime, InferenceOptions


async def get_ai_generated_code_review(code, config, inference_options):
    params_for_codellama = {"code": code}
    response = await config.run(
        "review_code", params_for_codellama, options=inference_options
    )
    return response[0].data


async def get_savage_review(review, config, inference_options):
    params_for_chat_gpt = {"review": review}
    response = await config.run(
        "make_review_savage", params_for_chat_gpt, options=inference_options
    )
    return response[0].data


def roast_my_code_page():
    savage_mode = st.toggle("Savage Mode", True)
    with st.form("code_input_form"):
        code_input = st.text_area("Paste your code here to let the roasting begin")
        submit = st.form_submit_button("Get Roasted")

    if submit:
        if not code_input:
            st.error("Code input is empty")
        else:
            config = AIConfigRuntime.load("app/roast_my_code.aiconfig.json")
            inference_options = InferenceOptions(stream=True)
            review = asyncio.run(
                get_ai_generated_code_review(code_input, config, inference_options)
            )
            st.session_state["review"] = review
            st.session_state["savage_review"] = asyncio.run(
                get_savage_review(review, config, inference_options)
            )

    if "savage_review" in st.session_state and "review" in st.session_state:
        if savage_mode:
            st.markdown(st.session_state["savage_review"])
        else:
            st.markdown(st.session_state["review"])
