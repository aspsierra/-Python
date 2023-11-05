
#? Tuplas, listas inmutables
#? +rápidas, ocupan menos espacio, formatean strings, claves en diccionario

tupla = ("Juan", 12.5, True, -9)    #! Se definen con () aunque son opcionales
unaTupla = ('Paco', )               #! Tupla unitaria, importante la coma

tupla.append('a')   #! Son inmutables, no se pueden agregar ni eliminar valores

val1, val2, val3, val4 = tupla  #! asignación automática de valores (DESEMPAQUETADO)

lista = list(tupla)     #! Convertir tupla en lista
tuplaAux = tuple(lista) #! Covertir lista en tupla

print(tupla[:])             #! Se imprime con paréntesis
print('Juan' in tupla)      #! Buscar elemento en tupla (true si existe, false si no)
print('Juana' in tupla)
print(tupla.count(True))    #! Contar ocurrencias
print(len(tupla))           #! numero de elementos
print(val1, val2, val3, val4)
