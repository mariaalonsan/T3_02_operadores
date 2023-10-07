"""
Practiquemos con los operadores de asignación (=, +=, *=, etc.):***

* Crea dos variables y asignales los números que quieras
* Incrementale a _num1_ su valor en 1
* Decrementale a _num2_ su valor en 2
* Multiplica _num1_ por 3 y actualiza su valor
* Dividide _num2_ por 2 y actualiza su valor
* Muestra los resultados
"""

#Primero creamos las 2 variables:
num_1 = 22
num_2 = 14

#1º Incrementamos a num_1 su valor en 1, para ello vamos a usar el operador de asignacion +=:
num_1 += 1
print("Incrementamos a num_1 su valor en 1:", num_1)

#2º Decrementamos a num_2 su valor en 2, para ello vamos a usar el operador de asignacion -=:
num_2 -= 2
print("Decrementamos a num_2 su valor en 2:", num_2)

#3º Multiplicamos num_1 por 3 y actualizamos su valor, para ello vamos a usar el operador de asignacion *=:
num_1 *= 3
print("Multiplicamos num_1 por 3 y actualizamos su valor:", num_1)

#4º Dividimos num_2 por 2 y actualizamos su valor, para ello vamos a usar el operador de asignacion /=:
num_2 /= 2
print("Dividimos num_2 por 2 y actualizamos su valor:", num_2)

#5º Printeamos los resultados FINALES:
print("Los resultados finales son:", num_1, "y", num_2)
