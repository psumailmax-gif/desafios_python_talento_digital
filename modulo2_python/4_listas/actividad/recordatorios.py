recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

# --- PASO 1: Agregar "Empezar el Año" (2 de Febrero de 2021 a las 06:00) ---
# Cronológicamente va después de '2021-01-01' (índice 0) y antes de '2021-05-01' (índice 1).
# Lo insertamos en la posición (índice) 1.
recordatorios.insert(1, ['2021-02-02', '06:00', 'Empezar el año'])

# --- PASO 2: Corregir el feriado del 15 de Julio al 16 de Julio ---
# Buscamos el elemento que tiene la fecha '2021-07-15'. 
# Ahora que agregamos un elemento, su posición actual en la lista es el índice 3.
# Modificamos directamente el primer elemento de esa sublista (la fecha).
recordatorios[3][0] = '2021-07-16'

# --- PASO 3: Eliminar el evento del Día del Trabajo ("No trabajar" el 1 de Mayo) ---
# El evento '2021-05-01' está en la posición (índice) 2. 
# Lo eliminamos usando .pop(2). También se podría usar .remove() si se busca el elemento.
recordatorios.pop(2)

# --- PASO 4: Agregar Cena de Navidad y Cena de Año Nuevo ---
# - "Cena de Navidad" (24 de Diciembre a las 22:00):
#   Cronológicamente va antes de "Navidad" (25 de Diciembre). 
#   En la lista actual, "Navidad" está en el índice 3. Insertamos la cena en el índice 3.
recordatorios.insert(3, ['2021-12-24', '22:00', 'Cena de Navidad'])

# - "Cena de Año Nuevo" (31 de Diciembre a las 22:00):
#   Va al final de toda la lista, después de "Navidad" (25 de Diciembre). 
#   Podemos usar .append() para agregarlo al final.
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])


# --- OUTPUT ESPERADO ---
print(recordatorios)