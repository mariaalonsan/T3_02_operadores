"""
Crear 5 variables con 5 notas numéricas y realizar la media aritmética. Mostrar el resultado final con un mensaje como este: "La nota media es 6.0"
"""
#Primero creamods las 5 variables notas:
nota_1 = 6
nota_2 = 7.25
nota_3 = 8
nota_4 = 3.5
nota_5 = 5.75

#Calculamos la media, usando una operacion muy basica que suma todas las notas y divide ese resultadp entre el numero de notas que hay, en este caso 5:
media = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5

#Printeamos la media:
print("La nota media es", media)

#Otra forma de printearlo:
print(f"La nota media es {media}")
