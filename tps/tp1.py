print("=====================================")
print("Bienvenido a Rappi")
print("=====================================")
print("Consulte aqui sus dias de vacaciones")
print("=====================================")
nombre= input("Ingrese el nombre del trabajador: ")
clave_dpto= int(input("Ingrese la clave numerica de su departamento: "))


if clave_dpto==15312:
    print("Bienvenido {} al departamento de Atencion al cliente".format(nombre))
    antig= int(input("Ingrese los años en los que va trabajando en la Municipalidad: "))
    if antig<1:
        print("Lamentamos informarle que no posee dias de vacaciones vigentes")
    elif antig==1:
        print("Le informamos {} que usted posee 6 dias de vacaciones".format(nombre))    
    elif antig>=2 and antig<=6:
        print("Le informamos {} que usted posee 14 dias de vacaciones".format(nombre))
    elif antig>=7:
        print("Le informamos {} que usted posee 20 dias de vacaciones".format(nombre))
       

elif clave_dpto==26314:
    print("bienvenido "+nombre+" al departamento de Logistica")
    antig= int(input("Ingrese los años en los que va trabajando en la Municipalidad"))
    if antig<1:
        print("Lamentamos informarle que no posee dias de vacaciones vigentes")
    elif antig==1:
        print("Le informamos "+nombre+" que usted posee 7 dias de vacaciones")    
    elif antig>=2 and antig<=6:
        print("Le informamos "+nombre+" que usted posee 15 dias de vacaciones")
    elif antig >=7:
        print("Le informamos "+nombre+" que usted posee 22 dias de vacaciones")

elif clave_dpto==35312:
    print("bienvenido "+nombre+" al departamento de Gerencia")
    antig= int(input("Ingrese los años en los que va trabajando en la Municipalidad"))
    if antig<1:
        print("Lamentamos informarle que no posee dias de vacaciones vigentes")
    elif antig==1:
        print("Le informamos "+nombre+" que usted posee 10 dias de vacaciones")    
    elif antig>=2 and antig<=6:
        print("Le informamos "+nombre+" que usted posee 20 dias de vacaciones")
    elif antig>=7:
        print("Le informamos "+nombre+" que usted posee 30 dias de vacaciones")
else:
    print("La clave ingresada es erronea o no pertenece a ninguna de las claves registradas")         