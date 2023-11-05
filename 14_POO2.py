class Coche():

    def __init__(self): #! Constructor de la clase
        #! Con __ delante de la variable hacemos que sea privada
        self.__largo = 250
        self.__ancho = 120
        self.__ruedas = 4 
        self.__enMarcha = False

    def arrancar(self): #! para acceder a las propiedades del propio objeto hay que pasarlo por parámetro con self
        if(not self.__enMarcha):
            check = self.__check()
        if(not self.__enMarcha and check):
            self.__enMarcha = True #! self se usa igual que this
        elif(not check):
            return 'error en chequeo, no se puede arrancar'
        else:
            self.__enMarcha = False
        return self.estado()

    def estado(self):
        if self.__enMarcha == True:
            return "Coche en marcha"
        else:
            return "Coche parado"
        
    def out(self):
        return f'El coche tiene {self.__ruedas} ruedas, {self.__ancho} cm de ancho y {self.__largo} cm de largo '

    def __check(self): #! Igual que en las variables, con __ delante de las funciones serán privadas
        print('Realizando chequeo interno')
        self.gas = True
        self.oil = False
        self.puertas = True

        if(self.gas and self.oil and self.puertas):
            return True
        else: 
            return False




miCoche = Coche() #! no se declaran con new

print(miCoche.arrancar())
print(miCoche.out())

print("-----------A continuación creamos el segundo objeto--------------")

coche2 = Coche()
print(coche2.estado())
print(coche2.out())