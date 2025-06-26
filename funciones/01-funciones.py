# Funciones
# Elaborado por: Javier Yepez Ramirez
# Inicio: 23/06/2025

# Estructura de funcion
# def NombreDeLaFuncion():
#     codigo
#
# Llamada a la funcion
#   NombreDeLaFuncion()

def hola(nombre): # def NombreDeLaFuncion(Parametro)
  print("Hola Mundo")
  print(f"Bienvenido {nombre}") # print(f"Bienvenido {Suo de paramtero}")
  
# Funcion con 2 Parametros
def NombreCompleto(nombre, apellido):
  print(f"Bienvenido {nombre} {apellido}")
  
# Funcion con argumento opcional
def NombreCompleto2(nombre, apellido=""):
  print(f"Bienvenido {nombre} {apellido}")
  
nombre = "Javier"
apellido = "Yepez"

hola(nombre)
hola("Javi") # NombreDeLaFuncion(Argumento)
NombreCompleto(nombre,  apellido) #Llamada a funcion 2 argumentos
NombreCompleto2(nombre) #Llamada a funcion argumento opcional

NombreCompleto(apellido = "Ramirez",  nombre = "Javier")