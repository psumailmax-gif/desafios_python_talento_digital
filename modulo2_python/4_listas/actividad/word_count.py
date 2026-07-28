import sys

# 1. Recuperar el nombre del archivo desde los argumentos de la terminal
# sys.argv[0] es el nombre del script (word_count.py)
# sys.argv[1] será el nombre del archivo de texto (lorem_ipsum.txt)
nombre_archivo = sys.argv[1]

# 2. Importar y leer el archivo de texto
with open(nombre_archivo, "r", encoding="utf-8") as file:
    texto = file.read()

# 3. Contar caracteres distintos
# Convertimos el texto completo en un set para obtener caracteres únicos
caracteres_distintos = set(texto)
total_caracteres_distintos = len(caracteres_distintos)

# 4. Contar palabras distintas
# Usamos .split() para separar el texto por espacios y saltos de línea, obteniendo una lista de palabras
palabras = texto.split()
# Convertimos la lista de palabras en un set para obtener solo las palabras únicas
palabras_distintas = set(palabras)
total_palabras_distintas = len(palabras_distintas)

# 5. Mostrar los resultados esperados en pantalla
print(f"El número de caracteres distintos es: {total_caracteres_distintos}")
print(f"El número de palabras distintas es: {total_palabras_distintas}")