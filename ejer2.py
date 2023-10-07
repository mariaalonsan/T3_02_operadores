"""
Busca en la documentación la forma correcta de redondear el siguiente resultado a tan solo 2 decimales: operacion = (365 / 12) * 14.7*
"""

#Primero hacemos la operacion:
operacion = (365 / 12) * 14.7

#Vamos a printear el resultado de la operacion, para ver todos los decimales que salen:
print("El resultado de la operacion es", operacion)

#Ahora vamos a redondear el resultado de la operacion a 2 decimales (vamos a usar round() para redondearlo):
print("El resultado de la operacion redondeado a 2 decimales es", round(operacion, 2))