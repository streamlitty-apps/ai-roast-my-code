import unittest
from unittest.mock import patch, MagicMock, Mock
from openai_client import validate_openai_api_key, get_openai_client


class TestValidateOpenAIKey(unittest.TestCase):
    @patch("openai_client.OpenAI")
    def test_valid_api_key(self, mock_openai):
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_client.chat.completions.create.return_value = "response"

        result = validate_openai_api_key("valid_api_key")

        self.assertTrue(result)
        mock_openai.assert_called_once_with(api_key="valid_api_key")
        mock_client.chat.completions.create.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "this is a test"}],
            max_tokens=1,
            n=1,
        )

    @patch("openai_client.OpenAI")
    def test_invalid_api_key(self, mock_openai):
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_client.chat.completions.create.side_effect = Exception()

        result = validate_openai_api_key("invalid_api_key")

        self.assertFalse(result)
        mock_openai.assert_called_once_with(api_key="invalid_api_key")
        mock_client.chat.completions.create.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "this is a test"}],
            max_tokens=1,
            n=1,
        )

    def test_empty_api_key(self):
        result = validate_openai_api_key("")
        self.assertFalse(result)

    def test_invalid_format_api_key(self):
        result = validate_openai_api_key(12345)
        self.assertFalse(result)

    @patch("openai_client.OpenAI")
    def test_error_handling(self, mock_openai):
        mock_client = Mock()
        mock_openai.return_value = mock_client
        mock_client.chat.completions.create.side_effect = ValueError()

        result = validate_openai_api_key("invalid_api_key")

        self.assertFalse(result)


class TestGetOpenAIClient(unittest.TestCase):
    def test_get_openai_client(self):
        api_key = "test_api_key"

        client = get_openai_client(api_key)

        self.assertIsNotNone(client)
        self.assertEqual(client.api_key, api_key)

    def test_get_openai_client_no_api_key(self):
        api_key = None

        with self.assertRaises(ValueError):
            get_openai_client(api_key)


if __name__ == "__main__":
    unittest.main()
