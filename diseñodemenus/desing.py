from logic.logic import leer_json_a_lista,leer_json_a_dicionario, agregar_datos_a_lista, guardar_lista_en_json
import json

#Ejercicios de Listas y Tuplas
#-----------------------------
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
                     
            awnser = int(input("    Do you need to add more? 1)yes 2)no (1-2)" ))

            
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
