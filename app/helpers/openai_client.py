from openai import OpenAI


def validate_openai_api_key(api_key):
    try:
        client = get_openai_client(api_key=api_key)
        client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": "this is a test",
                }
            ],
            max_tokens=1,
            n=1,
        )
        return True
    except Exception:
        return False


def get_openai_client(api_key):
    if not api_key:
        raise ValueError(
            "OpenAI API key is not set. Please set it in your environment variables."
        )
    return OpenAI(api_key=api_key)
