class Coche ():
    def desplazamiento (self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    def desplazamiento (self):
        print("Me desplazo con dos ruedas")

class Camion():
    def desplazamiento (self):
        print("Me desplazo con seis ruedas")       
""""        
#Moto
mi_vehiculo=Moto() #Marco la clase
mi_vehiculo.desplazamiento()  # Marco la funcion(o metodo) arealizar 
#auto
mi_vehiculo2=Coche()
mi_vehiculo2.desplazamiento()  
#camion
mi_vehiculo3=Camion()
mi_vehiculo3.desplazamiento()  
"""
 #POLIMORFISMO

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


mi_vehiculo= Camion() #creamos vehiculo, llamamos a la clase
desplazamientoVehiculo(mi_vehiculo) #usamos funcion de polimorfismo