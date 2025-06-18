import json
import html
import re
import os
import requests
from datetime import datetime
from PIL import Image
from io import BytesIO
import google.generativeai as genai


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


with open("re.json", "r", encoding="utf-8") as f:
    data = json.load(f)

markdown = ["# Discourse forum\n"]


for post in data["post_stream"]["posts"]:
    name = post.get("name", "Unknown")
    username = post.get("username", "Unknown")
    created_at = post.get("created_at", "")
    readable_time = datetime.fromisoformat(created_at.replace("Z", "+00:00")).strftime('%Y-%m-%d %H:%M:%S')
    post_url = f"https://discourse.onlinedegree.iitm.ac.in{post.get('post_url', '')}"
    cooked_html = html.unescape(post.get("cooked", ""))
    
    
    text_content = re.sub(r"<[^>]+>", "", cooked_html)

    
    images = re.findall(r'<img[^>]+src="([^"]+)"[^>]*>', cooked_html)
    
    markdown.append(f"## {name} (@{username})")
    markdown.append(f"- **Posted on**: {readable_time}")
    markdown.append(f"- **Link**: [{post_url}]({post_url})\n")
    markdown.append(text_content.strip())

    if images:
        markdown.append("\n### 🖼 Image Descriptions")
        for i, img_url in enumerate(images, 1):
            try:
                response = requests.get(img_url)
                response.raise_for_status()
                image = Image.open(BytesIO(response.content))
                gemini_response = model.generate_content([image, "Describe this image in detail."])
                description = gemini_response.text.strip()
                markdown.append(f"\n**Image {i}**: {description}")
            except Exception as e:
                markdown.append(f"\n**Image {i}**: (Error: {e})")

    markdown.append("\n---\n")


with open("thread121.md", "w", encoding="utf-8") as f:
    f.write("\n".join(markdown))
