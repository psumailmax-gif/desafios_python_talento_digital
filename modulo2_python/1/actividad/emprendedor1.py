"""Un emprendedor quiere crear una app que provea un servicio de entrega de comida para
mascotas. Este proyecto tiene buenos pronósticos, pero su éxito dependerá de cuántos
usuarios pueda alcanzar. La manera en la que se medirá esto es calculando las utilidades
delproyecto.Estasutilidadessepuedencalcularmediantelasiguientefórmula:
𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇
Donde:
P: PreciodeSuscripción
U: NúmerodeUsuarios
GT:GastosTotales
Paraello,setepidedesarrollarestecálculoentresversiones."""

precioSuscripcion = int(input("Ingresa el precio de la suscripción: "))
numeroUsuario = int(input("Ingresa la cantidad de usuarios: "))
gastoTotal = int(input("Ingresa el gasto total: "))
utilidades = precioSuscripcion * numeroUsuario - gastoTotal
print(f"Las utilidades son {utilidades}")