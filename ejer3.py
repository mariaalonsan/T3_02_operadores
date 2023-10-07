"""
Crea dos variables que almacenen 2 strings (username y password). Realizar las siguientes comprobaciones utilizando operadores lógicos:**
* Que la longitud de username sea mayor o igual que tres y menor que diez
* Que la password sea igual a "Tokio" o que sea igual a "Python".
    La salida por pantalla tiene que ser:
        * **Username: True o False** (según se haya evaluado)
        * **Password: True o False** (según se haya evaluado)
"""
#Primero creamos las 2 variables:
username = "Sonia.02"
password = "Tokio"

#Ahora vamos a comprobar que la longitud de username sea mayor o igual que 3 y menor que 10, vamos a usar len() que nos dice la cantidad de caracteres en la cadena de entrada:
username_comprobacion = len(username) >= 3 and len(username) < 10

#Y para a comprobar que la password sea igual a "Tokio" o que sea igual a "Python", vamos a usar el operador logico or, y vamos a comparar la password con las 2 opciones que nos dan (==):
password_comprobacion = password == "Tokio" or password == "Python"

#Printeamos los resultados de las comprobaciones:
print("Username:", username_comprobacion)
print("Password:", password_comprobacion)
