from unittest import result
"""

def division(n1,n2):
    
        try :
            return n1/n2
            
        except ZeroDivisionError:
            print("No se puede dividir por cero intente de nuevo")
        return "chau"
        
while True:
    try:    
        n1=int(input("Ingrese primer numero: "))
        n2= int(input("Ingrese segundo numero: "))
        break
    except ValueError:
        print(" Los valores introducidods no son correctods. Iintente de nuevo")
print (division(n1,n2))
"""


def value_edad(edad):
    if edad<20:
        raise TypeError(" solo numero")
        return"Eres joven"
    elif edad<40:
        return"Estas grande"
    elif edad<65:
        return"Tas maduro"
    elif edad<100:
        return "Cuidate"

print(value_edad(16))                  
