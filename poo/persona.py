from msilib.schema import Class


class Persona ():
    def __init__(self, nombre, edad, lugar_residencia) :

        self.nombre= nombre
        self.edad= edad
        self.lugar_residencia= lugar_residencia

    def descripcion (self):
        print("Nombre: ",self.nombre,"\nEdad:",self.edad,"\nLugar de residencia: ", 
        self.lugar_residencia, )

class Empleado(Persona):

    def __init__(self, salario, antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
       # super().__init__("Juan", "38", "Buenos Aires") #son valores fijos 
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado) #super toma valores de init
        self.salario= salario
        self.antiguedad= antiguedad

    #agregamos def para que se visualice salario y antiguedad
    def descripcion(self):
        super().descripcion()
        print("Salario:",self.salario, "\nAntiguedad:",self.antiguedad,)

      
#comenzamos 
antonio= Persona("Antonio", "32", "Buenos Aires")
antonio.descripcion() #nombre, edad, residencia

#descripcion pertenece a persona, lo tomamos cuando tomamos empleado
 
manuel=Empleado(1500,"5 años","Manuel","32", "Rosario") #debemos ingresarlo nosotros
manuel.descripcion() #nombre, edad, residencian salario, antig

#is instance (variable, clase) TRue o false
print(isinstance(manuel, Empleado))
print(isinstance(manuel, Persona))

carlos=Persona("CArlos",38,"Bahia Blanca")
print(isinstance(carlos,Empleado))