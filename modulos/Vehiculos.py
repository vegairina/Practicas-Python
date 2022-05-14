
class Vehiculos():
    def __init__(self, marca, modelo): #va a recibir marca y modelo
        self.marca=marca
        self.modelo=modelo
        self.en_marcha=False
        self.acelera=False

    def arrancar(self):
        self.en_marcha= True   

    def acelerar(self):
        self.acelera= True

    def estado(self):
        print("Marca: ", self.marca,  "\n Modelo:", self.modelo,
         "\n En marcha:", self.en_marcha, "\n Acelera:", self.acelera,)    