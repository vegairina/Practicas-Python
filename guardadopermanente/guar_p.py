import pickle
class Persona():
    def __init__(self, nombre, genero, edad) :
        self.nombre=nombre
        self.genero=genero
        self.edad= edad
        print("Se creo persona nombre:", self.nombre, "edade", self.edad, "genero", self.genero,
        )
    def __str__(self) :
        return "{} {} {}".format(self.nombre,self.edad,self.genero,)
#creamos lista persona
class ListaPersona:
    def __init__(self): #creamos metodo para que se encarge de crear fichero
        ListaDePersonas=open("FicheroExterno","ab+") #agregar informacion binaria
        ListaDePersonas.seek(0)
        try:#usamos try porque al principio va aestar vacio, para que no salga error
            self.personas=pickle.load(ListaDePersonas)#personas se va a cargar en lista de personas que va estar en fichero
            print("se cargaron {} personas del fichero externo".format(len(self)))
        except:
            print("El fichero esta vacio aun")    
        finally:
            ListaDePersonas.close()
            del (ListaDePersonas)    


    personas=[] #iniciamos la lista
    def agregaPersonas(self,p):
        self.personas.append(p) #agregamos personas a la lista
        self.guardarPersonasenFichero()
    def mostrarPersonas(self): #metodo de mostrar personas
        for p in self.personas: #muestra persona por persona in lista
            print(p)   

    def guardarPersonasenFichero(self):#metodo de guardar personas
        ListaPersona=open("FicheroExterno","wb")
        pickle.dump(self.personas, ListaPersona)
        ListaPersona.close()
        del(ListaPersona)

    def mostrarficheroexterno(self):
        print("La informacion del fichero externo es la siguiente: ")
        for p in self.personas:
            print (p)


#cramos la lista  en donde se va a llamar al metodo
miLista=ListaPersona() #aplicamos clase a milista


p1=Persona("sandra", "femenino",29)        
p2=Persona("Joaquin", "masculino",45) 
p3=Persona("Lourdes", "femenino",39)        
p4=Persona("Francisco", "masculino",29) 
 

miLista.agregaPersonas(p1)
miLista.agregaPersonas(p2)
miLista.agregaPersonas(p3)
miLista.agregaPersonas(p4)
miLista.mostrarPersonas()
miLista.mostrarficheroexterno()
