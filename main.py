from diseñodemenus.desing import desingTypeOneExOne,desingTypeOneExTwo,desingTypeOneExThree,desingTypeOneExFour
from logic.logic import timeSleep
import time


#usar el siguiente formato para commits
#   UPDATE: Solution for exercise x-x complete(state of the  proyect)

# recordar poner un intentado de 4 espacios para el diseño


exercicesTypeSelector = int(input("""    1)Ejercicios de Listas y Tuplas
    2)Ejercicios de Diccionarios     
    Seleccione: """))

if exercicesTypeSelector == 1:
    pass
    while True:
        exerciceSelector = int(input("    Seleccione el ejercicio que desee consultar: "))
        if exerciceSelector == 1:
            desingTypeOneExOne()
            timeSleep()

        elif exerciceSelector == 2:
            desingTypeOneExTwo()
            timeSleep()

        elif exerciceSelector == 3:
            desingTypeOneExThree()
            timeSleep()
        
        elif exerciceSelector == 4:
            desingTypeOneExFour()
            timeSleep()