"""print("Bienvenido al portal de notas ")
nota_alumno= int(input("Ingrese su nota: "))

def evaluacion(nota): #lo hacemos en menos lineas
    valoracion="aprobado"
    if nota<6:
        valoracion="desaprobado" 
        return valoracion
    

print(evaluacion(nota_alumno))     
"""
"""
print("verificacion de acceso")
Edad_acceso= int(input("Por favor indique su edad: "))
def eva_edad(edad):
    if edad>=18:
        mayoria="Muchas gracias"
        print(mayoria)
    elif 0<edad<18: 
        mayoria2="No posee mayoria de edad"
        print(mayoria2)
    else:
        print("edad incorrecta")    
print(eva_edad(Edad_acceso))

#concatenamos operadores
sal_pres=int(input("Ingrese salario presiednte: "))  
print("El salario del presiendente es: "+ str(sal_pres))
sal_vice=int(input("Ingrese salario vice: "))  
print("El salario del vice es: "+ str(sal_vice))
sal_admin=int(input("Ingrese salario admin: "))  
print("El salario del admin es: "+ str(sal_admin))
if sal_admin<sal_vice<sal_pres:
    print("esta todo normal")
else:
    print("Algo anda raro")   
"""
"""
#asignaturas a elegir
print("asignaturas a elegir")
print("asigaturas optativas: Civil- Informatica- Quimica- Textil- Naval")  
asignatura= input("Elige la asignatura:")
asignatura=asignatura.lower()
if asignatura in ("civil" ,"informatica", "Quimica","textil", "naval") :
     
    print("asignatura elegida: " + asignatura)
else:
    print("la asignatura no esta")   

#bucle for in
for i in [4,6,3,2,4]: #Se repite cinco veces
    print("Numeros")

#bucle for in
for i in [4,6,3,2,4]: #Se repite cinco veces
    print(i)

#bucle for in end
for i in [4,6,3,2,4]: #Se repite cinco veces
    print(i, end=" ")

#bucle en 
email=False
mail= input("Ingrese su email: ")

for i in mail:
    if i=="@": #lee que exista un en el mail
        email=True 

if email : #asume que email =true
    print("El email es correcto")

else:
    print("el email es incorrecto")  
"""
"""
#contador   
contador=0 #lo iniciamos
count=0
mi_email=input("ingrese su email: ")

for i in mi_email:
    if  i==".":
        contador=contador+1
        
    elif i=="@": 
        count=count+1


if (contador>=1 and count==1):
    print("el email es correcto")
elif count>=2:
    print("No puede tener mas de un @")
elif contador<1:
    print("El correo debe contener al menos un punto")        
    
#range
for x in range(5,11,3):#del 5 al 10 de 3 en 3
    print(f"hola el valor de la variable: {x}")
    print(x)
#len
valido=False
mi_email=input("ingrese su email: ")
for i in range(len(mi_email)): 
#len lee largo del mail .
#range pasa por todas las posiciones una por una hasta el largo de len (en este caso el final)      
    if mi_email[i] == "@": #si la en laposicion de i(osea pasando uno por uno)
 #hay un elemento que es igual a @ en mi email entonces convierte
        valido=True
if valido:
    print("El email contiene @ [i]==@")
else:
    print("no contiene @ [i]!=@")    

"""            
i=1
while i<=10: #imprime el 10 tambien 
    print(i) #es infinito a menos que lo cortes
    i=i+1

    





