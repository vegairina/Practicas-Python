
print("=====================================")
print("Bienvenido Gonzalito")
print("=====================================")
print("Consulte aqui cual es el mayor de tres numeros")
print("=====================================")

#numero mas grande de tres numeros
num1= int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segundo numero: "))
num3= int(input("Ingrese el tercer numero: "))

if num1==num2 or num1==num3 or num3==num2:
    print("Hay igualdad en algunos numeros, Ingresa todo de nuevo")
else:
    if num1>num2 and num1>num3:
        num1= str(num1)
        print("El numero mas grande es: " f"{num1}" )

    elif num2>num1 and num1>num3:
        num2= str(num2)
        print("El numero mas grande es: " f"{num2}" )

    elif num1>num2 and num1<num3:
        num3= str(num3)
        print("El numero mas grande es: " f"{num3}" )