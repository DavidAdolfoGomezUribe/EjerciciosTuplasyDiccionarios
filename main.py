from diseñodemenus.desing import desingTypeOneExOne,desingTypeOneExTwo,desingTypeOneExThree,desingTypeOneExFour,desingTypeOneExFive,desingTypeOneExSix,desingTypeOneExSeven,desingTypeOneExEight,desingTypeOneExNine

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
            
        elif exerciceSelector == 5:
            desingTypeOneExFive()
            timeSleep()
            
        elif exerciceSelector == 6:
            desingTypeOneExSix() 
            timeSleep()

        elif exerciceSelector == 7:
            desingTypeOneExSeven()
            timeSleep() 
            
        elif exerciceSelector == 8:
            desingTypeOneExEight()
            timeSleep()     
            
        elif exerciceSelector == 9:
            desingTypeOneExNine()
            timeSleep()                 
            