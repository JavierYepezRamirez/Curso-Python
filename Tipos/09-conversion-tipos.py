# Convertir tipos de datos en Python
# Este programa permite convertir tipos de datos en Python, específicamente de cadena a entero y viceversa.
# El usuario puede ingresar un número como cadena y el programa lo convertirá a entero.
# Elaborado por: Javier Yepez Ramirez
# Inicio: 23/06/2025

#x = input("")

# int() convierte a un entero
# str() convierte a una cadena
# float() convierte a un número de punto flotante
# bool() convierte a un booleano (True o False)

print(bool("")) # Falso porque una cadena vacía es considerada falsa en Python
print(bool("0")) # Verdadero, porque "0" es una cadena no vacía
print(bool(None)) # Falso, porque None es un valor nulo
print(bool(" ")) # Verdadero, porque un espacio es una cadena no vacía
print(bool(0)) # Falso, porque 0 es considerado falso en Python
print(bool(1)) # Verdadero, porque 1 es considerado verdadero en Python