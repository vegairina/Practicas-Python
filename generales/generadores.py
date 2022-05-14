#sirven para ahorrar espacio en memoria
#solo da el primer numero de lo que pidas a menos que lo llames mas veces

#como funcion
def funPares(limite):
    num=1
    lista=[]
    while num< limite:
        lista.append(num* 2)
        num=num+1
    return lista

print(funPares(10))   

#como generador 
def genera_pares (limite):
    num=1
    while num<limite:
        yield num*2
        num=num+1

devuelvePares= genera_pares(10)
print(next(devuelvePares))  
       
print(next(devuelvePares)) 
print(next(devuelvePares))         
print(next(devuelvePares))


