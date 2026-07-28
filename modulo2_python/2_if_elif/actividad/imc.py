peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso /(altura**2)
print (f"Su indice de masa corporal es {imc:.2f}")
if imc < 18.5:
    print("Baja de peso")
elif 18.5 <= imc < 25:
    print("Adecuado")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 35:
    print("Obedidad grado 1")
elif 35 <= imc < 40:
    print("Obesidad grado 2")
elif imc >= 40:
    print("Obesidad grado 3")
