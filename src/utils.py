from openai import OpenAI
from src.config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def generar_historia(prompt: str) -> str:

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content.strip()
