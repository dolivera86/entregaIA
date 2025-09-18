from openai import OpenAI
from src.config import OPENAI_API_KEY, MODEL
from dotenv import load_dotenv

load_dotenv()

# GPT-4
client = OpenAI(api_key=OPENAI_API_KEY)

def generar_historia(prompt: str, edad: str) -> str:
    # Ajustar prompt por edad
    prompt_con_edad = f"""
{prompt}

IMPORTANTE: adapta la historia para una niña de {edad} años.
"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt_con_edad}],
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content.strip()