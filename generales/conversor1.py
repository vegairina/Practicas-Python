"""conversor de numeros a letras"""
print("conversor")

opcion = int(input("""Pulse:
1. Si desea transformar de letras a numeros
2. Si deseas transformar de numeros a letras
:"""))

if opcion==1:
    letras= input("Como se llama el numero?")
    letras= letras.lower()
    if letras=="uno":
        print('El numero es "1"')
    elif letras=="dos" or letras== "dos":
        print('El numero es "2"')
    elif letras=="tres" or letras== "tres":
        print('El numero es "3"')
    elif letras=="cuatro" or letras=="cuatro":
        print('El numero es "4"')
    elif letras=="cinco":
        print('El numero es "5"')        
    else:
        print('El numero que elegiste no lo tenemos registrado, intenta de nuevo')


elif opcion==2:
    numero = int( input("Cual es el numero que deseas convertir del 1 al 5?"))
    if numero==1:
        print('El numero es "Uno"')
    elif numero==2:
        print('El numero es "Dos"')
    elif numero==3:
        print('El numero es "Tres"')
    elif numero==4:
        print('El numero es "Cuatro"')
    elif numero==5:
        print('El numero es "Cinco"')        
    else:
        print('El numero que elegiste no lo tenemos registrado, intenta de nuevo')      
else:
     print("esa opcion no existe intentalo de nuevo")  

     

 