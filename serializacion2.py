import pickle
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

coche1= Vehiculos("BMX","X6")
coche2= Vehiculos("Honda","Civic")
coche3= Vehiculos("Renault","12")
coche4= Vehiculos("Ford","Fiesta")

coches=[coche1,coche2,coche3,coche4] #lo metemos en una coleccion para no serializarlos uno en uno
#creamos fichero con bytes
fichero= open("Los coches", "wb") #escritura de bytes
pickle.dump(coches, fichero)
fichero.close()
del fichero #borramos l fichero del disco duro

#trnasformamos fichero a lectura normal
fichero_lectura=open("Los coches", "rb")
misCoches=pickle.load(fichero_lectura)
fichero_lectura.close()
#para imprimir uno a uno
for i in misCoches:
    print(i.estado())