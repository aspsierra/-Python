
#? Listas, funciones básicas (Arrays)

lista = ['Mari', False, 'Pepe']
lista2 = ['Toño', 'Chema'] * 3  #! Repite la lista 3 veces

lista3 = lista + lista2     #! Suma de listas

lista.append('Concha')          #! agregar al final
lista.insert(2, 'Moncho')       #! agregar en punto intermedio

lista.extend([5.2, "Pepe", 'Tucho'])     #! concatenar otra lista

lista.remove(False) #! eliminar elemento
lista.pop()         #! eliminar último elemento

print(lista[:])     #! lista completa, se imprime con corchetes []
print(lista[2])     #! elemento en concreto
print(lista[-2])    #! elemento contando desde el final (empieza desde -1)
print(lista[0:2])   #! porción, primer número incluido segundo excluido
print(lista[:2])    #! porción, entiende que se empieza desde el primer índice
print(lista[2:])    #! porción, a partir del índice 2
print('Concha' in lista)    #! comprobar si está en la lista
print(lista.index('Pepe'))  #! índice del elemento, primer resultado
