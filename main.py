from diseñodemenus.desing import desingTypeOneExOne,desingTypeOneExTwo
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
            time.sleep(1)
            print("    Regresando al menu |Ejercicios de Listas y Tuplas| \n")
            time.sleep(1)

        elif exerciceSelector == 2:
            desingTypeOneExTwo()
            time.sleep(1)
            print("    Regresando al menu |Ejercicios de Listas y Tuplas| \n")
            time.sleep(1)

        elif exerciceSelector == 3:
            break