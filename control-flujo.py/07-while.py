# While
# El while se cumplira miestras que la condicion se cumpla
# Elaborado por: Javier Yepez Ramirez
# Inicio: 23/06/2025

# Estructura de While
# While varialbe operador numero:
#      codigo

# numero = 1

# while numero < 100:
#     print (numero)
#     numero *= 2

comando = ""

# while comando.lower() != "salir":
#     comando = input("$ ")
#     print(comando)

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() ==  "salir":
        break