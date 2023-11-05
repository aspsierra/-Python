
#? IF
"""
print("Evaluación de notas")

notaAlumno = input("nota del alumno: ") #! Introducir valor por teclado


def evaluacion(nota):

    if nota < 5:
        return "suspenso"
    
    return "aprobado"

print(evaluacion(int(notaAlumno))) #! int() convierte el dato a integer
"""

#? If Else else if
"""
edad = int(input("introduce tu edad "))

if edad < 18:
    print("Prohibido")
elif edad>100:
    print("edad incorrecta")
else:
    print('adelante')
"""  

#? otras consideraciones

edad = -7

if 0 < edad < 100:  #! Se pueden acotar acotar condiciones de forma facil
    print('edad incorrecta')
else:
    print('edad incorrecta')