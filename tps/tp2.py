print("=====================================")
print("Bienvenido")
print("=====================================")
print("Consulte aqui lo que requiera saber")
print("=====================================")
num = int(input("Ingrese numero a determinar su paridad: "))

if num%2 == 0:
    num=str(num)
    print("El numero " + num+ " es PAR") 
elif num%2 != 0:
    num=str(num)
    print("El numero " + num +" es IMPAR")
else:
    print("El numero ingresado no es correcto")    