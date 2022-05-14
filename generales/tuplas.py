#las tuplas no se pueden modificar, no remove, no append, no pop
#no index
tupla=("irina", 1, 5 ,7889 )
print(tupla[2])
#transforma en lisa la tupla
lista=list(tupla)
print(lista)
#al reves
mi_lista= ["jopse","don","omar"]
mi_tupla=tuple(mi_lista)
print(mi_tupla)
#couynt
print(tupla.count(5))#cuantas veces se encuenta este elemento
#len
print(len(tupla))
#empaquetado de tupla
tupla2= "lopez", "perez", "ruiz", 2022
#desempaquetado de tupla
nombre1, nombre2, nombre3, agno= tupla2
print(nombre1)
print(nombre2)
print(nombre3)
print(agno)
