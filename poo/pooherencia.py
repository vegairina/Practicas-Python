


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


class Moto(Vehiculos):
    hcaballito= ""
    def caballito(self):
        self.hcaballito="Voy haciendo caballito"

    def estado(self): #sobreeescribimos estado()
        print("\nMarca: ", self.marca, "\n Modelo:",self.modelo,
         "\n En marcha:",self.en_marcha,"\n Acelera:",self.acelera,"\n",self.hcaballito, )  
    
    pass
class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado=cargar
        if (self.cargado):
            return("esta cargado")
        else:
            return("Esta descargado")

class vElectricos(Vehiculos): #independiente, no hereda de nadie , a menos que lo pongamos
    def __init__(self, marca, modelo):  #init solo recibe un parametro
        #con super podemos adjuntar marca y modelo a velectricos
        super().__init__(marca,modelo)
        self.autonomia=100
    def cargarenergia(self):
        self.cargando=True

class Bicielectrica(vElectricos, Vehiculos): #multiherencia (preferencia al primero)
    pass

mi_bici= Bicielectrica("oracle bici", "x-250") #marca y modelo ahora pertenece a vElectricos
mi_bici.estado()

#moto
mi_moto=Moto("Honda", "xl500") #nuevo elemento que hereda de la clase 
mi_moto.acelerar()
mi_moto.estado()

#furgoneta
mi_furgoneta=Furgoneta("Renault", "kangoo")
mi_furgoneta.acelerar()
mi_furgoneta.estado()
print(mi_furgoneta.carga(True))
#RETURN USAMOS PRINT
