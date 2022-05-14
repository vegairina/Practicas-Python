import pickle

"""lista= ["Analia","Carlos","Jose", "Mariana"] #nos va a quedar en carpeta se crea
fichero_binario= open("lista","wb") #fichero en memoria
pickle.dump(lista, fichero_binario)
fichero_binario.close()"""

fichero= open("lista", "rb")
lista_t=pickle.load(fichero)
print(lista_t) #leemos lista, la rescatamos de binario