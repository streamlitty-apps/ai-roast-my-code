import streamlit as st
import os
import asyncio
from helpers.openai_client import validate_anyscale_api_key
from aiconfig import AIConfigRuntime

async def run_streamlit_app():
    st.header("AI, Roast My Code!")
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

    savage_mode = st.toggle("Savage Mode", True)

    with st.form("code_input_form"):
        code_input = st.text_area("Paste your code here to let the roasting begin")
        submit = st.form_submit_button("Get Roasted")

    if submit:
        if not code_input: 
            st.error("Code input is empty")
        else:
            config = AIConfigRuntime.load('app/roast_my_code.aiconfig.json')
            review = await get_ai_generated_code_review(code_input, config)
            st.session_state["review"] = review
            st.session_state["savage_review"] = await get_savage_review(review, config)
    
    if "savage_review" in st.session_state and "review" in st.session_state:
        if savage_mode:
            st.markdown(st.session_state["savage_review"])
        else:
            st.markdown(st.session_state["review"])

    
async def get_ai_generated_code_review(code, config):
    params_for_codellama = {"code": code}

    # calling prompt that uses codellama, see roast_my_code.aiconfig.json for full details
    response = await config.run("review_code", params_for_codellama)
    
    return response[0].data

async def get_savage_review(review, config):
    params_for_chat_gpt = {"review": review}

    # calling prompt that uses chatgpt, see roast_my_code.aiconfig.json for full details
    response = await config.run("make_review_savage", params_for_chat_gpt)
    
    return response[0].data


if __name__ == "__main__":
    asyncio.run(run_streamlit_app())
