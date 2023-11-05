class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena= False

    def arrancar (self):
        self.enMarcha = True
    def frena (self):
        self.frena = True
    def acelera (self):
        self.acelera = True

    def __str__(self) -> str: #! Este sería el equivalente al método __toString de PHP
        return (f"Marca: {self.marca}\nModelo: {self.modelo}\nEn Marcha: {self.enMarcha}"+
            f"\nAcelerando: {self.acelera}\nFrenando : {self.frena}")

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar

        if(self.cargado):
            return 'Furgoneta cargada'
        else:
            return 'Furgoneta vacía'

class Moto(Vehiculos): #! para heredar, se escribe el nombre de la clase padre en los paréntesis 
    caballito = ""
    def caballito (self):
        self.caballito = "Voy hacioendo el caballito"

    def __str__(self) -> str:
        return (super().__str__() + f"\n{self.caballito}")  #! super() hace la llamada al padre

class VElectricos():
    def __init__(self) -> None:
        self.autonimia = 100
    
    def cargarBatería(self):
        self.cargando = True

#! Puede heredar de varias clases. se le da preferencia a la primera clase de la que heredemos
class BiciElectrica(VElectricos, Vehiculos): 
    pass

moto = Moto('Honda', 'CBR')
moto.caballito()
print(moto)

furgo = Furgoneta('Citroën', 'C15')
furgo.arrancar()
print(furgo.carga(True))
print(furgo)

bici = BiciElectrica()