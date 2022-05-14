#fibonacci
import math

"""
a=0
c=1
while c<=1597:
    print(a,c, end=" ")
    a=a+c
    c=a+c
    
#break
print("While con sentencia break \n")
x=0
while x<10:
    
    x+=1
    if x==5:
        break    
    print("valor de la variable: ", x)   #se paaliza 

#continue
print("\n While con sentencia contunie \n")
x=0
while x<10: #bloquea el cinco pero sigue
    
    x+=1
    if x==5:
        continue    
    print("valor de la variable: ", x)     
#ej 3
edad= int(input("introduce tu edad por favor: "))
intentos=0
while edad<0:
    print("edad incorrecta. vuelve a intentarlo")
    edad=int(input("Introduce tu edad nuevamente: "))
    intentos= intentos+1

    if intentos ==3 :
        print("No se le permiten mas intentos")
        break

else: 
    print("gracias por colaborar")
    print("la edad del amigo es: " +str(edad))
"""
#ej 4
print("Calculo de raiz cuadrada")
numero= int(input("Introduce el valor: "))
intentos=0

while numero<0:
    print("no se puede hallar la raiz de un numero negativo")
    numero=int(input("Ingrese de nuevo su valor: "))
    intentos=intentos+1
    if intentos==1: #con dos intentos
        print("===================================")
        print("Solo se le permite un intento mas.")
        print("===================================")
    if intentos==2: #won tres intentos
        print("===================================")
        print("No se le permite mas intentos") 
        print("===================================")  
        break
if numero>1:
    num= math.sqrt(numero)
    print(f"El valor de la raiz cuadrada de {numero} es:" +str(num))




    
