# Respuesta del ejercicio de la calculadora
# Elaborar una calculador
# Si no hay numero el usuario tiene que ingreso un numero
# Si hay numero o el usuario ingreso un numero, el usuario tiene que ingresar una operacion
# Despues el usuario debe ingresar el sieguiente numero
# Debe de mostrar el resultado 
# EL resultado debe pasar a ser el numero inicial
# Se debe repertir hasta que ingrese "salir"
# Elaborado por: Javier Yepez Ramirez
# Inicio: 23/06/2025


print("Bienbenidos a la calculadora.")
print("Para salir escribe \"salir\".")
print("Las operaciones son \"suma\", \"resta\", \"div\" y \"multi\".")

resultado = ""

while True:
    if not resultado: 
        resultado = input("Ingrese numero: ")
        if resultado.lower() == "salir":
            break
        
    op = input("Ingresa operacio: ")
    if op.lower() == "salir":
        break
    
    n2 = input("Ingresa siguinte numero: ")
    if n2.lower() == "Salir":
      break
    n2 = int(n2)
  
    if op.lower() =="suma":
        resultado += n2
    elif op.lower() =="resta":
        resultado -= n2
    elif op.lower() =="div":
        resultado /= n2
    elif op.lower() =="mult":
        resultado *= n2
    else:
      print("Operacion no valida")
      break
    
    print(f"El resultado es {resultado}")
  