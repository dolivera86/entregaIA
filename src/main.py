from src.prompts import PROMPTS
from src.utils import generar_historia

def main():

    # Temas
    mapa_temas = {
        "1": "cambio_climatico",
        "2": "emociones",
        "3": "seguridad"
    }

    while True:

        # Pregunta tema
        print("Entendiendo el mundo actual: IA como puente de aprendizaje para niñas")
        print("Temas disponibles:")
        print("1. cambio_climatico")
        print("2. emociones")
        print("3. seguridad")

        opcion = input("Elige un tema (1-3): ").strip()
        tema = mapa_temas.get(opcion)

        if not tema:
            print("Tema no válido. Intenta nuevamente.\n")
            continue

        # Genera historia
        print("\nGenerando historia...\n")
        historia = generar_historia(PROMPTS[tema])
        print(historia)

        # Preguntar qué hacer después
        siguiente = input("\nPon 4 para finalizar o 6 para otra opción: ").strip()
        if siguiente == "4":
            print("¡Hasta luego!")
            break
        elif siguiente == "6":
            continue
        else:
            print("Opción no válida, finalizando.")
            break

if __name__ == "__main__": 
    main()