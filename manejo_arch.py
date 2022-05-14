from io import open
archivo_texto=open("archivo.txt","r+")
lista_texto=archivo_texto.readlines()
lista_texto[1] = "Esta linea ha sido incluida desde el exterior \n"
archivo_texto.writelines(lista_texto)
archivo_texto.seek(0)
lista_texto1=archivo_texto.readlines()
lista_texto1[1] = "hola que tla mi nombre es irina \n"
archivo_texto.writelines(lista_texto1)
archivo_texto.seek(0)

archivo_texto.close()