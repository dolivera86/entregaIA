from colorama import Fore
import random
import json
import re
from src.utils import generar_historia

def generar_quiz(tema, edad):
    print(Fore.CYAN + "\n📝 ¡Quiz de repaso generado por IA!\n")
    prompt = f"""
Crea 4 preguntas de opción múltiple sobre el tema "{tema}" para una niña de {edad} años.
Para cada pregunta, proporciona:
- El enunciado de la pregunta.
- Tres opciones de respuesta (una correcta y dos incorrectas).
- Indica cuál es la opción correcta (1, 2 o 3).

Devuelve SOLO el resultado en formato JSON válido con la estructura:
[
  {{
    "pregunta": "...",
    "opciones": ["...", "...", "..."],
    "respuesta": 1
  }},
  ...
]
No agregues explicaciones ni texto fuera del JSON.
"""
    quiz_json = generar_historia(prompt, edad)
    # Extraer JSON del texto de la IA
    match = re.search(r'\[.*\]', quiz_json, re.DOTALL)
    if not match:
        print(Fore.RED + "No se pudo generar el quiz automáticamente. Intenta de nuevo.")
        return
    quiz_json = match.group(0)
    try:
        preguntas = json.loads(quiz_json)
    except Exception:
        print(Fore.RED + "No se pudo generar el quiz automáticamente. Intenta de nuevo.")
        return

    random.shuffle(preguntas)
    puntaje = 0
    for i, q in enumerate(preguntas, 1):
        print(f"\nPregunta {i}: {q['pregunta']}")
        for idx, opcion in enumerate(q['opciones'], 1):
            print(f"  {idx}. {opcion}")
        resp = input("Tu respuesta (1-3): ").strip()
        if resp == str(q['respuesta']):
            print(Fore.GREEN + "¡Correcto! 😊")
            puntaje += 1
        else:
            print(Fore.RED + "Incorrecto.")
    print(Fore.YELLOW + f"\nTu puntaje: {puntaje}/{len(preguntas)}")
    print(Fore.CYAN + "¡Gracias por participar en el quiz!\n")