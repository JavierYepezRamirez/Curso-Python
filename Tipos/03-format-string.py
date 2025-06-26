# Formato de cadenas en Python
# Dar formato a cadenas en Python es una forma de insertar valores dentro de un string de manera dinámica.
# Elaborado por: Javier Yepez Ramirez
# Inicio: 23/06/2025

nombre = "Javier"
apellido = "Yepez"
nombre_completo = nombre + " " + apellido
print(nombre_completo)

# Formato de cadenas con f-strings
# variable = f"texto {variable}"
nombre_completo1 = f"{nombre} {apellido}"
print(nombre_completo1)

nombre_completo2 = f"{nombre[0]} {2 + 5}"
print(nombre_completo2)