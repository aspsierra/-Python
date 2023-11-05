
#? TRY...EXCEPT

def suma(n1, n2):
    return n1 + n2

def resta(n1,n2):
    return n1-n2

def multi( n1,n2):
    return n1*n2

def div(n1,n2):
    #! Aquí se usa try...except que es un equivalente a try...catch
    try:    
        return n1/n2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return("Error")

while True:
    try:
        num1 = int(input("número 1: "))
        num2 = int(input('número 2: '))
        break
    except ValueError:
        print('valores no correctos, inténtalo otra vez')
    

operacion = int(input("elige operación:\n1-suma\n2-resta\n3-multiplicación\n4-división\n"))

if operacion == 1:
    print(suma(num1, num2))
elif operacion == 2:
    print(resta(num1, num2))
elif operacion == 3:
    print(multi(num1, num2))
elif operacion == 4:
    print(div(num1, num2))
else:
    print("error")


