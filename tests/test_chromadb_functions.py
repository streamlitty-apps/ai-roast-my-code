import unittest
from unittest.mock import patch, MagicMock
from app.chromadb_utils.chromadb_helpers import (
    run_query,
    retrieve_data,
    serialize_retrieved_data,
)
from app.chromadb_utils.ingest import ingest_data


class TestChromaDBFunctions(unittest.TestCase):

    @patch("app.chromadb_utils.chromadb_helpers.chromadb.PersistentClient")
    def test_run_query(self, mock_client):
        mock_collection = MagicMock()
        mock_client.return_value.get_collection.return_value = mock_collection
        mock_collection.query.return_value = {"documents": [["doc1", "doc2"]]}

        result = run_query("test query", "test_collection", 2)

        self.assertEqual(result, "doc1\ndoc2")
        mock_collection.query.assert_called_with(
            query_texts=["test query"], n_results=2
        )

    def test_retrieve_data(self):
        mock_collection = MagicMock()
        mock_collection.query.return_value = {"documents": [["doc1", "doc2"]]}

        result = retrieve_data(mock_collection, "sample query", 1)

        self.assertEqual(result, {"documents": [["doc1", "doc2"]]})

    def test_serialize_retrieved_data(self):
        data = {"documents": [["doc1", "doc2"]]}
        result = serialize_retrieved_data(data)
        self.assertEqual(result, "doc1\ndoc2")

    @patch("glob.glob")
    @patch("builtins.open")
    @patch("app.chromadb_utils.chromadb_helpers.chromadb.PersistentClient")
    async def test_ingest_data(self, mock_client, mock_open, mock_glob):
        mock_glob.return_value = ["path/to/file1.txt", "path/to/file2.txt"]
        mock_open.return_value.__enter__.return_value.read.return_value = "file content"

        mock_collection = MagicMock()
        mock_client.return_value.create_collection.return_value = mock_collection

        directory = "test_dir"
        collection_name = "test_collection"
        chromadb_path = "test.db"

        await ingest_data(directory, collection_name, chromadb_path)

        self.assertEqual(mock_collection.add.call_count, 2)
        mock_open.assert_called()
        mock_client.return_value.create_collection.assert_called_with(
            name=collection_name
        )


if __name__ == "__main__":
    unittest.main()
