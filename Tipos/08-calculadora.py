# Calculadora de operaciones matemáticas básicas
# Este programa permite realizar operaciones matemáticas básicas como suma, resta, multiplicación y división.
# El usuario puede ingresar dos números y seleccionar la operación que desea realizar.
# Elaborado por: Javier Yepez Ramirez
# Inicio: 23/06/2025

# input es una función que permite al usuario ingresar datos desde la consola.
Numero1 = input("Ingrese el primer número: ")
Numero2 = input("Ingrese el segundo número: ")

Numero1 = int(Numero1)  # Convertimos el primer número a entero
Numero2 = int(Numero2)  # Convertimos el segundo número a entero  

Suma = Numero1 + Numero2
Resta = Numero1 - Numero2
Multiplicacion = Numero1 * Numero2
Division = Numero1 / Numero2

Mensaje = f"""
Para los numero {Numero1} y {Numero2}, los resultados son:
- Suma: {Suma}
- Resta: {Resta}
- Multiplicación: {Multiplicacion}
- División: {Division}
"""

print(Mensaje)