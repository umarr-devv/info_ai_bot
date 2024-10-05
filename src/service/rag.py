import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')


def extract_text(content: list[str], query: str, retrieve_count: int = 2) -> list[str] | None:
    embedding_content = model.encode(content)
    embedding_query = model.encode([query])

    index = faiss.IndexFlatL2(embedding_content.shape[1])
    index.add(embedding_content)

    distances, indices = index.search(embedding_query, retrieve_count)
    return [content[idx] for idx in indices[0]]
