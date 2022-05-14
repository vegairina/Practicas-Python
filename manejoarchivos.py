"""from io import open
archivo_texto=open("archivo.txt", "w")
frase= "Hola como estas, \n hoy es un dia para aprender python"
archivo_texto.write(frase)
archivo_texto.close()
"""

from io import open

archivo_texto=open("archivo.txt", "r")
texto=archivo_texto.read()
archivo_texto.seek(8) 
#como la leyo la podemos imprimir aqui
print(archivo_texto.read()) #o estas, 
#si imprimimps de nuevo    NO VA A LEER DE NUEVO
archivo_texto.seek(0)
#archivo_texto.seek(len(archivo_texto.read())) lee longitud del texto
#ahora si lee de nuevo, solo hayq que llamarlo

archivo_texto.close()

#readline lee y transforma en lista
from io import open
archivo_texto=open("archivo.txt", "r")
lineas_texto=archivo_texto.readlines()
archivo_texto.close()
print(lineas_texto)
print(lineas_texto[0]) #prmemr elemento

#append
"""from io import open
archivo_texto=open("archivo.txt", "a")
text=archivo_texto.write("\n Siempre es una buena ocacion para aprender python")
archivo_texto.close()"""

#posicion cero del cursor al escribir
from io import open
archivo_texto=open("archivo.txt", "r+")
texto1=archivo_texto.write("Hello world")
archivo_texto.close()
