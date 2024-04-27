from aiconfig import AIConfigRuntime, Prompt

# Create an AIConfig runtime for the code analysis application
aiconfig = AIConfigRuntime.create(
    "code_analysis_config", "Python code analysis and feedback system"
)

# Set GPT-3.5 as default model for analyzing Python code
model_name = "gpt-3.5"
model_settings = {
    "top_k": 40,
    "top_p": 0.6,
    "model": "gpt-3.5",
    "temperature": 0.3,  # Slightly higher temperature for more varied suggestions
}
aiconfig.add_model(model_name, model_settings)

# Code Analysis Prompt
code_analysis_prompt = Prompt(
    name="code_analysis",
    input="{{code_submission}}",
    metadata={
        "model": {
            "name": "gpt-3.5",
            "settings": {
                "system_prompt": """
                    Given a piece of Python code, analyze it for common errors, style issues, and performance problems. 
                    Provide feedback and suggestions on how to improve the code. Assume the role of an experienced Python developer
                    who is assisting a less experienced colleague.

                    Output should be detailed explanations of any issues found with a touch of humor, along with concrete suggestions for improvements.
                """
            },
        },
    },
)
aiconfig.add_prompt("code_analysis", code_analysis_prompt)

# Save the AIConfig
aiconfig.save("code_analysis_aiconfig.json", include_outputs=False)