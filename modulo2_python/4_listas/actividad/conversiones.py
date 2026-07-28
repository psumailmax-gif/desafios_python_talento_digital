import sys

# Validación básica para asegurar que el usuario pase los argumentos necesarios
if len(sys.argv) < 4:
    print("Error: Faltan parámetros.")
    print("Uso correcto: python imc.py <sol_peruano> <peso_argentino> <dolar_americano> <peso_chileno>")
    sys.exit(1)

# 1. Ingreso y captura de datos desde la línea de comandos (CLI)
# sys.argv[0] es el nombre del archivo. Los datos reales empiezan en el índice 1 y 2.
sol_peruano = float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar_americano = float(sys.argv[3])
peso_chileno = int(sys.argv[4])

diccionario = {}
diccionario["soles"] = sol_peruano
diccionario["argentino"]= peso_argentino
diccionario["dolar"]= dolar_americano
print(f"Los pesos {peso_chileno} chilenos equivalen: ")
for clave, valor in diccionario.items():
  print(f"el nombre de la moneda {clave} y el monto es {peso_chileno * valor}")

