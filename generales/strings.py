"""
mensaje = "Hola"
mensaje += ", "
mensaje += "como tas"
print (mensaje)
print("debe imprimir mensaje")

numero_uno = 1
numero_dos = 15
resultado= numero_dos+  numero_uno
resultado = str(resultado)
print("el resultado es:" + resultado) 

#ebuscar cadena
cadena = "Hola Irina como estas chiquita"
buscar_cadena = cadena.find("Irina")
print(buscar_cadena)

#estraer partes
cadena = "Hola Irina como estas chiquita"
extraer_cadena = cadena[1:8] #desde el uno hasta el 7 inclusive
print(extraer_cadena)
"""

#comparacion
msj1 = "irina"
msj2 = "vega"
msj3 = "irina"
print(msj1 == msj2) #true o false
print(msj1 == msj3)

#format
nombre= "carlos"
edad= 25
dia="miercoles"
print("Hola {}, tu tienes {} años".format(nombre,edad))
print("Hola {nombre}, como estas, hoy es {dia}".format( nombre="Irina" ,dia = "jueves"))
print("Hola {dia}, como estas, hoy es {dia}".format( nombre="Irina" ,dia = "jueves"))

nombre= "computadora"
edad= 3
dia="miercoles"
print("Esta es mi {0}, tiene {1} años de uso, hoy es {2}".format(nombre, edad , dia))

#f-strings
print(f"{4+1}")

print(f"Hola {nombre}")

num1= 9
num2=5
print(f"el resultado de resta {num1}-{num2} es {num1-num2}")
