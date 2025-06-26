# Operadores logicos 
# And, or, not
# Elaborado por: Javier Yepez Ramirez
# Inicio: 23/06/2025

# And
# True and True = True
# True and False =  False
# False and True = False
# False and False = False

# Or
# True and True = True
# True and False =  True
# False and True = True
# False and False = False

# not
# Cambia el valor de True a False
# Si gas = True, con  not gas = False

gas = False
encendido = True
edad = 18 

# if gas or encendido:
#   print("Puedes avanzar")
  
if gas and (encendido or edad > 17):
  print("Puedes avanzar")

