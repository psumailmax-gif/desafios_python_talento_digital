print("Bienvenido a la aplicacion de primeros auxilio")
respuesta1 = input("¿La persona afectda Responde a estimulos? (si/no)").strip().lower()

if respuesta1 in ["si", "sí", "s"]:
    print("Valorar la señal de llevarlo al hospital mas cercano")
else:
    print("Abrir la via aerea")
    
    respuesta2 = input("¿Respira?").strip().lower()
    if respuesta2 in ["si", "sí", "s"]:
      print( "permitir respirar" )
    else: 
      print ("administrar 5 ventilaciones y llamar a emergencia ")
      ambulancia = "no"
      while ambulancia== "no":

          respuesta3 = input ("Tiene signos de vida (si/no)").lower().strip()
          if respuesta3 in ["si", "sí", "s"]:
              print ("reevaluar a la espera de la ambulancia")
          else:
              print ("Administrar las compresiones toráxicas hasta que llegue la ambulancia")
          ambulancia= input ("llego la ambulancia (si/no)")