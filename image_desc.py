import google.generativeai as genai
from PIL import Image
import os
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
image_path = "project-tds-virtual-ta-q1.webp"
image = Image.open(image_path)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
prompt = "Describe this image in detail in Markdown format."
response = model.generate_content([image, prompt])
with open("image_description2.md", "w", encoding="utf-8") as f:
    f.write(response.text)

