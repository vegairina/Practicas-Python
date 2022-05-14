n=0
suma=0
nota=1
while nota!=0:
    nota=float(input("Ingrese ingrese nota"))
    if nota!=0:
        suma+=nota
        n+=1

resultado=suma/n   
print("El promedio final es :", resultado)

