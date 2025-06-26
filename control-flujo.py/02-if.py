# If elif y else
# If, elif y else son estructuras de control de flujo que 
# permiten ejecutar diferentes bloques de código según ciertas condiciones.
# Elaborado por: Javier Yepez Ramirez
# Inicio: 23/06/2025

# Estructura if
# La estructura if se utiliza para ejecutar un bloque de código si una condición es verdadera.
# Si la condición es falsa, el bloque de código no se ejecuta.
#    if condicion:
#        bloque_de_codigo


# Estructura if-else
# La estructura if-else se utiliza para ejecutar un bloque de código si una condición es verdadera
# y otro bloque de código si la condición es falsa.
#    if condicion:
#        bloque_de_codigo_verdadero
#    else:
#        bloque_de_codigo_falso

# Estructura if-elif-else
# La estructura if-elif-else se utiliza para ejecutar un bloque de código si una condición
# es verdadera, otro bloque de código si una segunda condición es verdadera
# y un bloque de código final si ninguna de las condiciones anteriores es verdadera.
#    if condicion1:
#        bloque_de_codigo_condicion1
#    elif condicion2:
#        bloque_de_codigo_condicion2
#    else:
#        bloque_de_codigo_final

edad = 10

if edad > 50:
    print("Puede ver la película, pero con descuento")
elif edad > 17:
    print("Puede ver la película")
else:
    print("No puede ver la película")

print("Listo")
