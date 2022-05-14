"""
class coche():
    def __init__(self):
        
        self.largo_chasis= 250
        self.ancho_chasis=120
        self.__ruedas__=4 #encapsulamos ruedas
        self.en_marcha= False #esta detenido

    def arrancar(self):  #metodo:funcion que pertenece a la clase #funcion:no
        self.en_marcha=True
    def estado(self):
        if(self.en_marcha):
            return "el coche esta en marcha"
        else:
            return"El coche esta detenenido"    
mi_coche=coche
"""
