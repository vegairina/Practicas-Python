#nombre_usuario= input("Ingrese nombra usuario: ")
#print("Eel nomre de usuario es: "+ nombre_usuario.capitalize() )
edad= input("Introduce tu edad: ")
#print(edad.isdigit())

def edadPermitida(edad):

    while (edad.isdigit()==False):
     print("Eso no es un numero. Introduce un numero por favor")
     edad= input("Introduce tu edad: ")   
    if(int(edad)>18):
        print( "Puedes pasar")
    else: 
        print ("no puedes pasar")    
#si dice return poner print

edadPermitida(edad)