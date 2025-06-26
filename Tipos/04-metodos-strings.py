# Metodos de cadenas de texto
# Los métodos de cadenas de texto son funciones que se pueden aplicar a los strings para realizar diversas
# operaciones, como convertir a mayúsculas o minúsculas, reemplazar caracteres, dividir cadenas, etc.
# Elaborado por: Javier Yepez Ramirez
# Inicio: 23/06/2025

animal = " peRRo feliz "
print(animal.upper())  # Convierte a mayúsculas
print(animal.lower())  # Convierte a minúsculas
print(animal.capitalize())  # Convierte la primera letra a mayúscula y el resto a minúsculas
print(animal.title())  # Convierte la primera letra de cada palabra a mayúscula
print(animal.strip())  # Elimina espacios en blanco al inicio y al final del string
print(animal.rstrip())  # Elimina espacios en blanco al final del string
print(animal.find("fe")) # Busca un substring y devuelve su índice, o -1 si no se encuentra
print(animal.replace("feliz", "triste"))  # Reemplaza un substring por otro
print("RRo" in animal)  # Verifica si un substring está presente en el string, devuelve True o False
print("RRo" not in animal)  # Verifica si un substring no está presente en el string, devuelve True o False

# Podemos combinar varios métodos
print(animal.strip().capitalize())  # Divide el string en una lista de palabras y capitaliza cada palabra