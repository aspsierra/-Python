
#? Funciones especificas para la construcción de listas
#? construyen las listas por eleentos individuales, al contrario de funciones clasicas
#? que pueden devolver toda la lista de golpe
#? Sería algo así como una función estática ya que recuerda el valor anterior


#? generar lista de números pares usando una función clásica
"""def generaPares(limite):
    num = 1

    listaPares = []

    while num < limite:
        listaPares.append(num * 2)
        num += 1
    
    return listaPares

print(generaPares(10))
"""
#? generar lista de números pares usando un GENERADOR
"""
def generaPares(limite):
    num = 1

    while num < limite:
        yield num * 2   #! Los diferentes valores se devuelven con YIELD
        num += 1

pares = generaPares(10) #! Guardamos la función dentro de una variable para poder llamar al generador

print(type(pares))
print(next(pares))
print(next(pares))
print(next(pares))
"""