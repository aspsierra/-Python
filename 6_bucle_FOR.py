
#? FOR
"""
for i in ['ea', 7, True]:   #! Funciona como un foreach de PHP
    print(i)
"""
"""
for i in ["Pildoras", "Informáticas", 3]:
    print(i, end=' ')   #! Con End especificamos el caracter con el que acabar la línea

"""
"""
email = False

for i in 'asp.sierra@gmail.es': #! También podemos recorrer Strings
    if(i == '@'):
        email = True

if email ==True:
    print('mail correcto')
else:
    print('mail no correcto')
"""

#? For con Range
"""
for i in range(5):  #! Con range creamos una lista de 5 elementos, se parece a un for mas clásico
    print(f"valor de la variable {i}")  #! con f accedemos al formateo de los textos, sin usar concatenaciones
print()
for i in range(5,10): #! el rango empieza en 5 y termina en 9 
        print(f"valor de la variable {i}") 
print()
for i in range(5,48, 7): #! el tercer parametro hace la funcion de step
    print(f"valor de la variable {i}") 
"""
