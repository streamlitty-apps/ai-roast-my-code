from openai import OpenAI


def validate_anyscale_api_key(api_key):
    '''
    The OpenAI Python library supports setting an environment variable specifying the base for calls,
    which we will set this to point at Anyscale Endpoints.
    We will leverage the the library to validate that the provided key is a valid Anyscale api key.
    See https://docs.endpoints.anyscale.com/text-generation/migrate-from-openai/
    '''
    try:
        client = get_openai_client(api_key=api_key)
        client.models.list()
        return True
    except Exception:
        return False


def get_openai_client(api_key):
    if not api_key:
        raise ValueError(
            "Anyscale API key is not set. Please set it in your environment variables."
        )
    return OpenAI(api_key=api_key, base_url="https://api.endpoints.anyscale.com/v1")
