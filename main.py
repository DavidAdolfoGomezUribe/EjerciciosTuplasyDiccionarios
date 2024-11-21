from diseñodemenus.desing import desingTypeOneExOne,desingTypeOneExTwo,desingTypeOneExThree,desingTypeOneExFour,desingTypeOneExFive,desingTypeOneExSix,desingTypeOneExSeven,desingTypeOneExEight,desingTypeOneExNine,desingTypeOneExTen,desingTypeTwoExOne,desingTypeTwoExTwo

from logic.logic import timeSleep
import time


#usar el siguiente formato para commits
#   UPDATE: Solution for exercise x-x complete(state of the  proyect)

# recordar poner un intentado de 4 espacios para el diseño

while True:
    try:
        exercicesTypeSelector = int(input("""    1)Ejercicios de Listas y Tuplas
    2)Ejercicios de Diccionarios     
    Seleccione: """))
        if exercicesTypeSelector == 1:
            while True:
                try:
                    print(    "Listado de ejercicios (1-10), 11 para regresar al menu anterior")
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
                        
                    elif exerciceSelector == 10:
                        desingTypeOneExTen()
                        timeSleep()                 
                    elif exerciceSelector == 11:
                        print("    Regresando al menu anterior \n")
                        break
                    
                    else:
                        
                        raise ValueError
                except ValueError:
                    print("    Enter a valid option")
                    pass
                

        elif exercicesTypeSelector == 2:         
             while True:
                try:
                    print("    Listado de ejercicios (1-10), 11 para regresar al menu anterior")
                    exerciceSelector = int(input("    Seleccione el ejercicio que desee consultar: "))
                    
                    if exerciceSelector == 1:
                        desingTypeTwoExOne()
                        timeSleep()
                    
                    if exerciceSelector == 2:
                        desingTypeTwoExTwo()
                        timeSleep()
                    
                        
                        
                except ValueError:
                    pass
        else:
            print("    Leaving the program")
            break
    except ValueError:
        print("    Enter a valid option")
        pass
            
            
            
# last line of code            