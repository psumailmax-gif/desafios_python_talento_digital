"""La velocidad de escape de un planeta se define como la mínima velocidad necesaria para
salirdeunplanetavenciendolagravedad.
Lavelocidaddeescapesecalculamediantelasiguientefórmula:
𝑉𝑒=2𝑔𝑟
Ve :correspondealaVelocidaddeEscapeen[m/s].
g: correspondealaconstantegravitacionalen[m/s2].
r: Correspondealradiodelplanetaen[m]."""
import math
radio = float(input("Ingrese el radio en kilometros: "))
constante = float(input("Ingrese la constante gravitacional "))
velocidadEscape = math.sqrt(2 * radio * constante * 1000)
print(f"La velocidad de Escape es {velocidadEscape} [m/s]")