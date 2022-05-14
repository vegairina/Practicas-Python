
def devuelveciudades(*ciudades):
    for elemento in ciudades: #devuelve ciudades
        for sub_elemt in elemento: 
            yield sub_elemt

devueltas=devuelveciudades("Buenos Aires", "Mendoza", "Bariloche","Rosario")

print(next(devueltas)) #devuelve primer letra

#ambas son lo mismo
def devuelveciudades(*ciudades):
    for elemento in ciudades: #devuelve ciudades 
            yield from elemento

devueltas=devuelveciudades("Buenos Aires", "Mendoza", "Bariloche","Rosario")

print(next(devueltas)) #devuelve primer letra


