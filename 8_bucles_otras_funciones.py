
#? COONTINUE
"""
nombre = "Álvaro Sierra Pérez"
contador = 0

for letra in nombre:
    if letra == " ":
        continue    #! Con continue saltamos la iteración actual y pasamos a la siguiente
    contador += 1

print(f"tu nombre tiene {contador} letras")
"""

#? PASS
"""
class clase:
    pass    #! anula la instrucción pero no interrumpe la ejecución
"""

#? ELSE

email = input("mail: ")

for i in email:
    if i =='@':
        arroba = True
        break;

else: #! al usarla en un bucle se ejecuta al acabar, al usar el break justo antes el bucle no llega a terminar por lo ge el else no se ejecutará
    arroba = False

print(arroba)