# Elaborar una calculador
# Si no hay numero el usuario tiene que ingreso un numero
# Si hay numero o el usuario ingreso un numero, el usuario tiene que ingresar una operacion
# Despues el usuario debe ingresar el sieguiente numero
# Debe de mostrar el resultado 
# EL resultado debe pasar a ser el numero inicial
# Se debe repertir hasta que ingrese "salir"
# Elaborado por: Javier Yepez Ramirez
# Inicio: 23/06/2025

comando = ""

print("Bienbenidos a la calculadora")
print("Para salir escribe \"salir\"")
print("Las operaciones son \"suma\", \"resta\", \"div\" y \"multi\"")
Numero1 = ""
Numero2 = ""

while True:
  if Numero1 == "":
    Numero1 = input("Ingresa Numero: ")
    
    if Numero1.lower() == "salir":
      break
    
    Numero1 = int(Numero1)
  
  Numero2 = input("Ingresa siguiente Numero: ")
  if Numero2.lower() == "salir":
    break
  
  Numero2 = int(Numero2)
  
  operacion = input("Ingresa opereacion: ")
  if operacion.lower() == "salir":
    break
  
  if operacion.lower() == "suma":
    Numero1 += Numero2
  elif operacion.lower() == "resta":
    Numero1 -= Numero2
  elif operacion.lower() == "div":
    Numero1 /= Numero2
  elif operacion.lower() == "multi":
    Numero1 *= Numero2
  else:
    print("Operacion no valida")
    
  print(f"El resultado es: {Numero1}")
