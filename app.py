# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "argparse",
#     "fastapi",
#     "httpx",
#     "markdownify",
#     "numpy",
#     "semantic_text_splitter",
#     "tqdm",
#     "uvicorn",
#     "google.generativeai",
#     "pillow",
#     "openai",
#     "pydantic",
# ]
# ///
import numpy as np
import os
from pathlib import Path
from fastapi import FastAPI, Request
from pydantic import BaseModel
from openai import OpenAI
import time
import google.generativeai as genai
import base64

app = FastAPI()

class RateLimiter:
    def __init__(self, requests_per_minute=60, requests_per_second=2):
        self.requests_per_minute = requests_per_minute
        self.requests_per_second = requests_per_second
        self.request_times = []
        self.last_request_time = 0
    def wait_if_needed(self):
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        if time_since_last < (1.0 / self.requests_per_second):
            sleep_time = (1.0 / self.requests_per_second) - time_since_last
            time.sleep(sleep_time)
        current_time = time.time()
        self.request_times = [t for t in self.request_times if current_time - t < 60]
        
        if len(self.request_times) >= self.requests_per_minute:
            sleep_time = 60 - (current_time - self.request_times[0])
            if sleep_time > 0:
                time.sleep(sleep_time)
                current_time = time.time()
                self.request_times = [t for t in self.request_times if current_time - t < 60]
        
        self.request_times.append(current_time)
        self.last_request_time = current_time

rate_limiter = RateLimiter(requests_per_minute=5, requests_per_second=2)

def get_image_description(image_data):
    """Get a description of the image using OpenAI."""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    image_bytes = base64.b64decode(image_data)
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Describe the content of this image in detail, focusing on any text, objects, or relevant features that could help answer questions about it."
                    },
                    {
                        "type": "image",
                        "image": image_bytes
                    }
                ]
            }
        ],
        max_tokens=300
    )
    
    return response.choices[0].message.content

def get_embedding(text: str, max_retries: int = 3) -> list[float]:
    for attempt in range(max_retries):
        try:
            rate_limiter.wait_if_needed()
            response = genai.embed_content(
                model="models/embedding-001",
                content=text,
                task_type="retrieval_document"
            )
            return response["embedding"]
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}, retrying...")
            time.sleep(2 ** attempt)
    raise Exception("Failed to get embedding after retries.")


def load_embeddings():
    """Load chunks and embeddings from npz file"""
    data = np.load("embeddings.npz", allow_pickle=True)
    return data["chunks"], data["embeddings"]

def generate_llm_response(question: str, context: str):
    """Generate a response from the LLM using the question and context."""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    system_prompt = """You are a concise teaching assistant. Answer briefly using only the information from the context.
Use Markdown formatting.
Keep responses under 100 words.
if the context does not contain enough information to answer the question, respond with "I don't know"
Do not attempt to guess, fabricate, or add external information.
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Context: {context}\nQuestion: {question}"}
        ],
        max_tokens=512,
        temperature=0.5,
        top_p=0.95
    )
    return response.choices[0].message.content

def answer(question: str, image: str = None):
    loaded_chunks, loaded_embeddings = load_embeddings()
    if image:
        image_data = image.split(",")[1] if "," in image else image
        image_description = get_image_description(image_data)
        question += f" {image_description}"
    question_embedding = get_embedding(question)
    similarities = np.dot(loaded_embeddings, question_embedding) / (
        np.linalg.norm(loaded_embeddings, axis=1) * np.linalg.norm(question_embedding)
    )
    top_indices = np.argsort(similarities)[-5:][::-1]
    top_chunks = [loaded_chunks[i] for i in top_indices]

    response = generate_llm_response(question, "\n".join(top_chunks))
    return {
        "question": question,
        "response": response,
        "top_chunks": top_chunks
    }

@app.post("/api/")
async def api_answer(request: Request):
    try:
        data = await request.json()
        print(data)
        return answer(data.get("question"), data.get("image"))
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="0.0.0.0", port=10000)