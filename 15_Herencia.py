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
    
class Moto(Vehiculos): #! para heredar, se escribe el nombre de la clase padre en los paréntesis 
    pass

moto = Moto('Honda', 'CBR')
print(moto)