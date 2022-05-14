
lista =["juan", "pepe","maria", "ernesto"]
print(lista[2]) #posicion 2 = maria
print(lista[:]) #toda la lista
print(lista[-2])#empezando de atra: maria
print(lista[-3])#pepe
print(lista[0:3]) #imprime 0 1 2 
print(lista[:3])#imprime los dos primeros
print(lista[3:])#desde el 3 hasta el final ('ernesto')
lista.insert(2,"lucia")
print(lista)
lista2 =["jorge", "carlos","luz", "jorge","tomi"]
lista2.extend(["luis","doce"]) #toma solo un elemento
print(lista2)
#en que indice esta tal cosa
print(lista2.index("jorge")) #0 #si estan rep nos devuelve el primero
#comprobar si se encuentra en una lista un elemento
print("jorge" in lista2) #true o false
lista2.remove("jorge")
print(lista2)
lista2.pop()
print(lista2)


#concatenacion de listas
lista3=lista+lista2 #lista sin jorge
print(lista3)

