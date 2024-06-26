import chromadb


def run_query(query, collection_name, k):
    chroma_client = chromadb.PersistentClient(path="app/chromadb_utils/chroma.db")
    collection = chroma_client.get_collection(name=collection_name)
    data = retrieve_data(collection, query, k)
    serialized_data = serialize_retrieved_data(data)
    return serialized_data


def retrieve_data(collection, query, k):
    data = collection.query(query_texts=[query], n_results=k)
    return data


def serialize_retrieved_data(data):
    out = "\n".join(data["documents"][0])
    return out
