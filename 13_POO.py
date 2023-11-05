class Coche():
    largo = 250
    ancho = 120
    ruedas = 4
    enMarcha = False

    def arrancar(self): #! para acceder a las propiedades del propio objeto hay que pasarlo por parámetro con self
        self.enMarcha = True #! self se usa igual que this

    def estado(self):
        if self.enMarcha == True:
            return "Coche en marcha"
        else:
            return "Coche parado"

miCoche = Coche() #! no se declaran con new

print(miCoche.estado())
print(miCoche.largo)

miCoche.arrancar()
print(miCoche.estado())