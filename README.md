# Proyecto de Prompt Engineering: Entendiendo el mundo actual: IA como puente de aprendizaje para niñas

Este proyecto fue desarrollado como parte de un proyecto personal para entrega académica.  
Su objetivo es ayudar a niñas en edad de aprendizaje (12 y 5 años) a comprender mejor temas actuales como:

- Cambio climático  
- Emociones  
- Seguridad en el crecimiento  

A través de historias cortas generadas con inteligencia artificial, se busca un enfoque educativo, divertido y fácil de entender.

---

## Estructura del Proyecto

- `README.md` → documentación del proyecto.
- `src/config.py` → achivo que conecta el modelo de IA. 
- `src/main.py` → archivo principal que ejecuta el programa.  
- `src/prompts.py` → contiene los temas y plantillas de prompts.  
- `src/utils.py` → funciones auxiliares para generar historias.
- `src/test.py` →  test fácil para conocer si se conecta con el modelo de IA.
- `ejemplos/cambio_climatico.md` → ejemplo que devuelve el modelo de IA al ejecutarse.
- `ejemplos/emociones.md` → ejemplo que devuelve el modelo de IA al ejecutarse.
- `ejemplos/seguridad.md` → ejemplo que devuelve el modelo de IA al ejecutarse.

---

## Ejecución del Proyecto

Para iniciar el programa, desde la raíz del proyecto:

```
python -m src.main
```

---

## Uso del Programa

Al ejecutar el proyecto, verás en la terminal algo como:

Entendiendo el mundo actual: IA como puente de aprendizaje para niñas
Temas disponibles:
1. cambio_climatico
2. emociones
3. seguridad
Elige un tema (1-3):

1. Escribe uno de los temas:  
   - `cambio_climatico`  
   - `emociones`  
   - `seguridad`

2. El sistema generará una **historia corta** adaptada al tema elegido.