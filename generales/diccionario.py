#diccionarios
#clave:valor
#no hay elementos repetidos
diccionario={"Alemania":"Berlin", "Austria": "Viena", "Belgica":"Bruselas",10:"Diegote"}
print(diccionario["Austria"])
print(diccionario)
diccionario["Italia"]="Lisboa"
print(diccionario)
#sobreescribimos
diccionario["Italia"]="Roma"
print(diccionario)
diccionario["italia"]="Roma"#es diferente
print(diccionario)
#eliminamos
del diccionario["Alemania"]#solo la clave
print(diccionario)


#relacionamos tuplas con diccionarios
tupla1=("Lunes", "Martes","Miercoles")
diccionario1={tupla1[0]:"11 de marzo",tupla1[1]:"12 de marzo",tupla1[2]:"13 de marzo"}
print(diccionario1)
print(diccionario1["Martes"])


#varios valores a una clave
diccionario2={"nombre":"Irina","apellido":"vega", "edad":23, "gustos":{"helados":["tramontana","chocolate","dulce","crema"]}}
print(diccionario2)
print(diccionario2["gustos"])
print(diccionario2.keys())
print(diccionario2.values())
print(len(diccionario2))