from logic.logic import leer_json_a_lista,leer_json_a_dicionario, agregar_datos_a_lista, guardar_lista_en_json
import json

#Ejercicios de Listas y Tuplas
#-----------------------------
#Ejercicio 1
#Escribir un programa que almacene las asignaturas de un
#curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
#en una lista y la muestre por pantalla.
def desingTypeOneExOne():
    
    print("    Este es un programa para añadir y guardar cursos \n")
    while True:
        try:
            while True:
                ruta = "databases/dataTypeOneExOne.json"
                lista_datos = leer_json_a_lista(ruta)
                print(f"""    El listado actual es el siguiente:
    {lista_datos}""")

                cursoNombre = str(input("    Ingrese el Cursos que desee añadir a la lista: "))
                
                lista_datos = agregar_datos_a_lista(lista_datos,cursoNombre)
                
                guardar_lista_en_json(ruta,lista_datos) 
                
                print(f"    la lista actual ahora es {lista_datos}")

                print("    Desea agregar otro elemento?: ")
                respuesta = input ("    1) si 2)no ")
                if respuesta == "1" or respuesta == "si":
                    pass
                else:
                    return print("Ok")
        except:
            pass

#Ejercicio 2

#scribir un programa que almacene las asignaturas de un curso
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
#en una lista y la muestre por pantalla el mensaje `Yo estudio <asignatura>`,
#donde `<asignatura>` es cada una de las asignaturas de la lista.
# 

def desingTypeOneExTwo():
    print("    Este es un programa para añadir , guardar cursos e imprimirlos en consola \n")
    while True:
        try:
            while True:
                ruta = "databases/dataTypeOneExTwo.json"
                lista_datos = leer_json_a_lista(ruta)
                print(f"""    El listado actual es el siguiente:
    {lista_datos}""")

                cursoNombre = str(input("    Ingresar los cursos que yo estudio: "))
                
                lista_datos = agregar_datos_a_lista(lista_datos,cursoNombre)
                
                guardar_lista_en_json(ruta,lista_datos) 
                
                print(f"    Yo estudio:", ",".join(map(str,lista_datos)))

                print("    Desea agregar otro elemento?: ")
                respuesta = input ("    1) si 2)no ")
                if respuesta == "1" or respuesta == "si":
                    pass
                else:
                    return print("Ok")
        except:
            pass


#-----------------------------
# Ejercicio 3

#Escribir un programa que almacene las asignaturas de un curso 
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
#en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y
#después las muestre por pantalla con el mensaje `En <asignatura> has sacado <nota>` donde
#`<asignatura>` es cada una des las asignaturas de la lista y `<nota>`
#cada una de las correspondientes notas introducidas por el usuario.


def desingTypeOneExThree():

    ruta = "databases/dataTypeOneExThree.json"
    
    mattersAndNotes = leer_json_a_dicionario(ruta)
    

    if mattersAndNotes :
        allMatters = []
        
    else :
        allMatters = []
        mattersAndNotes={}
    
    print("    This is a program to match the subjects with the note")
    while True: 
        try:
            matters = str(input("    Enter the subjects: "))
            allMatters.append(matters)
                     
            awnser = int(input(f"    Do you need to add more? 1)yes 2)no (1-2)" ))

            
            if awnser != 1:
                dictlen = len(allMatters)
                
                for i in range(0,dictlen):
                    noteMatter = input(f"    Enter the note for {allMatters[i]}: ")
                    mattersAndNotes.update({allMatters[i]:noteMatter})

                    
                    
                guardar_lista_en_json(ruta, mattersAndNotes)

                for key, value in mattersAndNotes.items():
                    print(f"    For the subjects {key} you have: {value}")
                print("")
                break
            
            else:
                pass
                
        except ValueError:
            pass
            

    


 #last line if code



## Ejercicio 4

#Escribir un programa que pregunte al usuario los números ganadores 
#de la lotería primitiva, los almacene en una lista y los muestre por 
#pantalla ordenados de menor a mayor.

def desingTypeOneExFour():
    
        ruta = "databases/dataTypeOneExFour.json"
        lista = leer_json_a_lista(ruta)
            
        try:
            while True:    
                nuevosDatos = int(input("    Enter the numbers for primivite lottery: "))
                
                lista.append(nuevosDatos)
                
                awnser = int(input(f"    Do you want to enter a new number? 1)yes 2)no: "))
                
                
                if awnser == 2:
                
                    lista.sort()
                    print(f"    This is the winning numbers for primitive lottery \n    {lista}")
                    
                    
                    guardar_lista_en_json(ruta, lista)
                    break
                
                else :
                    
                    pass
        except:
            pass


## Ejercicio 5

#Escribir un programa que almacene en una lista los números del 1 
#al 10 y los muestre por pantalla en orden inverso separados por comas.      


def desingTypeOneExFive():
    
    ruta = "databases/dataTypeOneExFive.json"
    lista = leer_json_a_lista(ruta)
            
    try:
        while True:    
            nuevosDatos = int(input("    Enter the numbers between 1 - 10: "))
            
            if nuevosDatos < 1 or nuevosDatos > 10:
                raise ValueError
                        
            lista.append(nuevosDatos)
            
            awnser = int(input(f"    Do you want to enter a new number? 1)yes 2)no: "))
            
            
            if awnser == 2:
            
                lista.sort(reverse=True)
                print(f"    This is the list for the numbers in descendend order ", ",".join(map(str,lista) ) )
                
                
                guardar_lista_en_json(ruta, lista)
                break
            
            else :
                pass
    except ValueError:
        print("    Enter the correct number")
        pass



# Ejercicio 6

#Escribir un programa que almacene 
#las asignaturas de un curso (por ejemplo 
#Matemáticas, Física, Química, Historia y Lengua) en una lista,
#pregunte al usuario la nota que ha sacado en cada asignatura y elimine de
#la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla 
#las asignaturas que el usuario tiene que repetir.

def desingTypeOneExSix():
    pass


#last line of code