# Strings en Python
# Un string es una secuencia de caracteres encerrados entre comillas simples o dobles.
# Elaborado por: Javier Yepez Ramirez
# Inicio: 23/06/2025

nombre_curso = "Python para principiantes"
descripcion_curso = """
Ultimate Paython,
este curso contempla todo lo
lo que necesitas para aprender
python desde cero.
"""
print(nombre_curso, descripcion_curso) 

# Funcion len()
# La función len() devuelve la longitud de un string, es decir, el número de caracteres

len(nombre_curso)

# Para poder ver lo que devuelve la función len() debemos imprimirlo
print(len(nombre_curso))

# Para acceder a un caracter específico de un string, se utiliza el índice del caracter entre corchetes.
# Los índices comienzan en 0, por lo que el primer caracter tiene índice 0, el segundo tiene índice 1, y así sucesivamente.
# Por ejemplo, para acceder al primer caracter de un string, se utiliza el índice 0.
# -prnt(string[índice])

print(nombre_curso[15])  # Imprime el primer caracter

print(nombre_curso[0:6])  # Imprime los caracteres del índice 0 al 5 (sin incluir el 6)

print(nombre_curso[7:])  # Imprime los caracteres desde el índice 7 hasta el final

print(nombre_curso[:6])  # Imprime los caracteres desde el inicio hasta el índice 5 (sin incluir el 6)

print(nombre_curso[:])  # Imprime todo el string