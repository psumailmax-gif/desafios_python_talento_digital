import random
opcion_usuario= input ("elige piedra, papel, tijeras.").strip().lower()
# .strip() elimina los espacios y .lower() comvierte todo a minuscula
if opcion_usuario == "piedra" or opcion_usuario == "papel" or opcion_usuario =="tijeras":
    opcion_computadora = random.choice (["piedra","papel","tijeras"])
    print (f"la opcion del computador es {opcion_computadora}"  )
    if opcion_usuario== opcion_computadora:
        print ("empate")
    else : 
        if opcion_usuario=="papel" and opcion_computadora =="piedra":
            print ("gana usuario, sacaste papel y computadora piedra")
        elif opcion_usuario== "tijeras" and opcion_computadora=="piedra":
            print ("gana computadora, sacaste tijera y computador piedra")
        elif opcion_usuario== "piedra" and opcion_computadora=="papel":
            print ("gana computadora, sacaste piedra y computadora papel")
        elif opcion_usuario=="papel" and opcion_computadora=="tijeras":
            print ("gana computadora, sacaste papel y computadora tijeras")
        elif opcion_usuario=="tijeras" and opcion_computadora== "papel":
            print ("gana usuario, sacaste tijeras computadora papel")
        elif opcion_usuario== "piedra" and opcion_computadora=="tijeras":
            print ("gana usuario, sacaste piedra y computadora tijeras")
else: 
    print("opcion no valida")