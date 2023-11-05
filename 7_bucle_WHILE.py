
#? WHILE

edad = int(input('Introduce tu edad: '))

while edad < 5 or edad > 100:
    print("La edad introducida no es correcta")
    edad = int(input('Introduce tu edad: '))

print('adelante')