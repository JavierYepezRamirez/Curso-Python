# For
# Un for sirve para iterar algo N numero de veces principla mente un lista.
# Elaborado por: Javier Yepez Ramirez
# Inicio: 23/06/2025

# Estructura de un For
# for variable in range(numero):
#     codigo
# Donde numero es el rango empezando de 0, 1, 2, ... , Numero-1

# for numero in range(5):
#   print(numero)
#   #print(numero, numero * '1')

buscar = 10 
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("No encontre el numero buscado :( ") 
  
# Break sirve para terminar la iterasion y que no se siga.

for char in "Ultimate Python":
    print(char)