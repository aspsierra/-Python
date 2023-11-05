"""def evaluaEdad(edad):
    if edad<0:
        raise TypeError("No se permite edad negativa")  #! Lanzar excepciones propias con RAISE, equivalente a throw
    if edad<20:
        return 'muy joven'
    if edad<40:
        return 'adulto'
    if edad<65:
        return 'retírate'
    if edad<100:
        return 'huele a tierra'
    

print(evaluaEdad(80))

"""

import math

def calculaRaiz(num1):

    if num1<0:
        raise ValueError("El número no puede ser menor que 0")
    else:
        return math.sqrt(num1)

op1 = (int(input("Número: ")))

try:
    print(calculaRaiz(op1))
except ValueError as NumNegativo: #! al lanzar excepciones podemos usar un alias para facilitar el trabajo
    print(NumNegativo)
