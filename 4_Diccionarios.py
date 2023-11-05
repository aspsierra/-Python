
#? Diccionarios
#? Array asociativo

diccionario = {"Alemania" : "Berlín", "Francia": "París", "Portugal" : "Madrid"}    #! Se definen con {clave : valor, ...} 

diccionario["España"] = "Madrid"    #! Agregar nuevo elemento
diccionario["Portugal"] = "Lisboa"  #! Sobreescribir elemento
del diccionario["Alemania"]         #! Eliminar elemento

#! Pueden tener diferentes tipos de dato tanto en clave como en valor
diccionario["Alvaro"] = 26 
diccionario[1.8] = "Xiaomi"

#! Puede usarse una tupla para asigar las claves de un diccionario
tupla = ["Alemania", "Francia", "Portugal", "España"]
diccionario2 = {tupla[0]: "Berlín", tupla[1]: "París", tupla[2]: "Lisboa", tupla[3]: "Madrid"}

#! Se puede guardar una tupla dentro de un diccionario
tuplaAnillos = [1991,1992,1993,1996,1997,1998]
diccionario3 = {23: "Jordan", "Nombre": "Michael", "Equipo": "Chicago", "Anillos": tuplaAnillos}

#! Tambien podemos guardar un diccionario dentro de otro
diccAnillos = {"Temporada": [1991,1992,1993,1996,1997,1998]}
diccionario4 = {23: "Jordan", "Nombre": "Michael", "Equipo": "Chicago", "Anillos": diccAnillos}

print(diccionario)
print(diccionario["Francia"])
print(diccionario.keys())   #! Imprimir todas las claves
print(diccionario.values()) #! Imprimir todos los valores
print(len(diccionario))     #! Longitud

print(diccionario2)
print(diccionario[tupla[2]])

print(diccionario3)
print(diccionario3["Equipo"])
print(diccionario3["Anillos"])

print(diccionario4)
print(diccionario4["Anillos"])
