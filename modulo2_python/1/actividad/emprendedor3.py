precioSuscripcion = float(input("Ingresa el precio de la suscripción: "))
gastoTotal = float(input("Ingresa el gasto total: "))
usuarioNormal = float(input("Ingresa la cantidad de usuarios normales: "))
usuarioPremium=float(input("Ingresa la cantidad de usuarios primium: "))

utilidades = (precioSuscripcion * usuarioNormal) + (precioSuscripcion * 1.5 * usuarioPremium) - gastoTotal
utilidadesAnoAnterior = float(input("Ingresa las utilidades del año anterior: "))
razon = round((utilidades/utilidadesAnoAnterior), 2)

print(f"La razón de las utilidades es {razon}")