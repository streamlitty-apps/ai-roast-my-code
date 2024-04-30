import unittest
from unittest.mock import patch, MagicMock, Mock
from app.helpers.openai_client import get_openai_client, validate_anyscale_api_key


class TestValidateAnyscaleKey(unittest.TestCase):
    @patch("app.helpers.openai_client.OpenAI")
    def test_valid_api_key(self, mock_openai):
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_client.models.list.return_value = "response"

        result = validate_anyscale_api_key("valid_api_key")

        self.assertTrue(result)
        mock_openai.assert_called_once_with(api_key="valid_api_key", base_url="https://api.endpoints.anyscale.com/v1")
        mock_client.models.list.assert_called_once()

    @patch("app.helpers.openai_client.OpenAI")
    def test_invalid_api_key(self, mock_openai):
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_client.models.list.side_effect = Exception()

        result = validate_anyscale_api_key("invalid_api_key")

        self.assertFalse(result)
        mock_openai.assert_called_once_with(api_key="valid_api_key", base_url="https://api.endpoints.anyscale.com/v1")
        mock_client.models.list.assert_called_once()

    def test_empty_api_key(self):
        result = validate_anyscale_api_key("")
        self.assertFalse(result)

    def test_invalid_format_api_key(self):
        result = validate_anyscale_api_key(12345)
        self.assertFalse(result)

    @patch("app.helpers.openai_client.OpenAI")
    def test_error_handling(self, mock_openai):
        mock_client = Mock()
        mock_openai.return_value = mock_client
        mock_client.models.list.side_effect = ValueError()

        result = validate_anyscale_api_key("invalid_api_key")

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
