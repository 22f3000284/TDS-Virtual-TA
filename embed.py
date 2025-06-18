import numpy as np
import time
from pathlib import Path
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from semantic_text_splitter import MarkdownSplitter

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text: str) -> list[float]:
    embedding = model.encode(text)
    return embedding.tolist()


def get_chunks(file_path: str, chunk_size: int = 15000):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    splitter = MarkdownSplitter(chunk_size)
    chunks = splitter.chunks(content)
    return chunks
if __name__ == "__main__":
    files = [*Path("markdowns").glob("*.md"), *Path("markdowns").rglob("*.md")]
    all_chunks = []
    all_embeddings = []
    total_chunks = 0
    file_chunks = {}
    for file_path in files:
        chunks = get_chunks(file_path)
        file_chunks[file_path] = chunks
        total_chunks += len(chunks)

    with tqdm(total=total_chunks, desc="Processing embeddings") as pbar:
        for file_path, chunks in file_chunks.items():
            for chunk in chunks:
                try:
                    embedding = get_embedding(chunk)
                    all_chunks.append(chunk)
                    all_embeddings.append(embedding)
                    pbar.set_postfix({"file": file_path.name, "chunks": len(all_chunks)})
                    pbar.update(1)
                except Exception as e:
                    print(f"Skipping chunk from {file_path.name} due to error: {e}")
                    pbar.update(1)
                    continue
    np.savez("embeddings.npz", chunks=all_chunks, embeddings=all_embeddings)
    test_path = Path("markdowns/discourse/thread1.md")
    chunks = get_chunks(test_path, chunk_size=1000)
    embedding = get_embedding(chunks[0])
    print("Embedding vector length:", len(embedding))
