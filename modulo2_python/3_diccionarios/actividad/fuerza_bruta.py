from string import ascii_lowercase
passwd=input("Ingrese su contraseña: ").lower()
intentos=0
for letra in passwd:
  for letra2 in ascii_lowercase:
    intentos+=1
    if letra2==letra:
      break
    
print(f"La contraseña fue forzada en {intentos}")
