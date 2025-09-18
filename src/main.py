from src.prompts import PROMPTS
from src.utils import generar_historia
from src.quiz import generar_quiz
from colorama import Fore, Style, init

init(autoreset=True)

def main():

    # Preguntar edad
    edad = input(Fore.CYAN + "👧 ¿Cuántos años tienes?: " + Style.RESET_ALL).strip()

    # Temas
    mapa_temas = {
        "1": "cambio_climatico",
        "2": "emociones",
        "3": "seguridad"
    }

    while True:

        # Pregunta tema
        print(Fore.CYAN + "\n🌍 Entendiendo el mundo actual: IA como puente de aprendizaje para niñas\n")
        print(Fore.YELLOW + "1. 🌍 Cambio Climático")
        print(Fore.MAGENTA + "2. 💖 Emociones")
        print(Fore.GREEN + "3. 🛡️ Seguridad")

        opcion = input(Fore.CYAN + "\n👉 Elige un tema (1-3): " + Style.RESET_ALL).strip()
        tema = mapa_temas.get(opcion)

        if not tema:
            print("Tema no válido. Intenta nuevamente.\n")
            continue

        # Genera historia
        print(Fore.BLUE + "\n✨ Generando historia...\n")
        historia = generar_historia(PROMPTS[tema], edad)
        print(Fore.WHITE + Style.BRIGHT + historia + Style.RESET_ALL)


        # Preguntar qué hacer después
        siguiente = input(Fore.CYAN + "\n🔄 Pon 4 para finalizar o 6 para otra opción: " + Style.RESET_ALL).strip()
        if siguiente == "4":
            generar_quiz(tema, edad)
            print(Fore.GREEN + "👋 ¡Hasta luego! Sigue aprendiendo y divirtiéndote 🌟")
            break
        elif siguiente == "6":
            continue
        else:
            print(Fore.RED + "❌ Opción no válida, finalizando.")
            break

if __name__ == "__main__": 
    main()