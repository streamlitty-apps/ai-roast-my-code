import os
import streamlit as st


def aiconfig_page():
    st.header("About AIConfig")
    st.markdown(
        """
            AIConfig represents a standard JSON structure designed to save prompts and model configurations within 
            source control systems. This AI artifact can be seamlessly integrated into various applications. 
            Utilize the provided Python or Node SDKs to link an AIConfig with your application code. 
            \nCheck out the [LastMile AI GitHub account](https://github.com/lastmile-ai/aiconfig) for more!
        """
    )

    file = "app/roast_my_code.aiconfig.json"
    absolute_path = os.path.abspath(file)

    code = open(absolute_path, "r").read()

    st.code(code, language="json")
