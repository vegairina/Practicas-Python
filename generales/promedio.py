
nombre= input("Hola alumno cual es su nombre?: ")
mate = int(input("Cual es tu calificacion en matematicas?: "))
bio= int(input("Cual es tu calificacion en Biologia?: "))
quimica= int(input("Cual es tu calificacion en Quimica?: "))
promediosuma= mate+bio+quimica
promedio= promediosuma/3
promedio=float(promedio)

if promedio>=6:
    print('Felicidades ' + nombre +  '"aprobaste" con un promedio de', promedio)
    print('Felicidades ' + nombre +  '"aprobaste" con un promedio de'+ round(promedio,2)) #2decima dsp coma
elif promedio >10:
    print('Alumno' + nombre +  'Alguna de sus notas es incorrecta' )
else: 
    print('Lo siento ' + nombre + '"Desaprobaste" con un promedio de ', promedio)   

