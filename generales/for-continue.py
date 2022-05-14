for letra in "Irina":
    print("Viendo la letra una por una:" + letra)
name= "Pildoras Informaticas"
contador=0
print(len(name))   
for l in name: #l pasa por cada letra y espacio
    if (l==" "):#si l =" " lo saltea
        continue#continua
    contador+=1#cuenta todas las l c/"" salteado
print(contador) 
#contador+=1


n=4 #cantidad de veces totales que quiero que el ciclo suceda
for i in range(n): #imprime cuatro veces "el numero es:"
    print("El num de ciclos es:" )
    print(i)

    #que es i? es la cantidad de vecces que se va imprimiendo "el numer es:"
    # comienza con 0 hasta 3 osea 0 1 2 3  

for i in range(n-1): #osea la cantidad es 3
    print("holi")
    print(i)    
    #el i es 0 1 2 cantidad de veces acumulandose (ITERACION) o RECORRIDO
    #[0,3)
for i in range(1,7): #imprime cuatro veces "el numero es:"
    print("chau" )
    print(i)
    #imprime (1,4)i=1 i=2 i=3 NO 4 NO 0 SI 1 osea incluye el de la izquierda
    #imprime (1,7) i=1 i=2 i=3 NO 0 NO 7 O [1,6]
for i in range(1,6,2):  
    print("JEHOVA" )
    print(i)    
#tiene un salto en dos, imprime 1 3 5 

#ejercicio Tablas

 
#tabla de multiplicar
for n in range (1,11):    
    print("____Tabla", n)
    for i in range (11):
        resultado=n*i
        print(n,"x", i, "=", resultado)

