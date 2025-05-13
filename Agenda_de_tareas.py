#/***************************************************************/
#NOMBRE: Leonel Figueroa Jauregui
#FECHA: 13 de Mayo de 2025
#PROGRAMA: Agenda_de_tareas.py 
#CENTRO UNIVERSITARIO DE LOS ALTOS / UNIVERSIDAD DE GUADALAJARA
#PROFESOR: Francisco Javier Ulloa Cortez
#DESCRIPCION: Agenda de tareas, permite agregar tareas y verlas en una lista.
#/***************************************************************/

print("""
      
 █████╗  ██████╗ ███████╗███╗   ██╗██████╗  █████╗     ██████╗ ███████╗    ████████╗ █████╗ ██████╗ ███████╗ █████╗ ███████╗
██╔══██╗██╔════╝ ██╔════╝████╗  ██║██╔══██╗██╔══██╗    ██╔══██╗██╔════╝    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝
███████║██║  ███╗█████╗  ██╔██╗ ██║██║  ██║███████║    ██║  ██║█████╗         ██║   ███████║██████╔╝█████╗  ███████║███████╗
██╔══██║██║   ██║██╔══╝  ██║╚██╗██║██║  ██║██╔══██║    ██║  ██║██╔══╝         ██║   ██╔══██║██╔══██╗██╔══╝  ██╔══██║╚════██║
██║  ██║╚██████╔╝███████╗██║ ╚████║██████╔╝██║  ██║    ██████╔╝███████╗       ██║   ██║  ██║██║  ██║███████╗██║  ██║███████║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚══════╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
                                                                                          /Proyecto Final/
      
============================================================================================================================================
============================================================================================================================================
                                        
""")

print(""" 

      
                           ______                _                             _            _        
                          |  ____|              (_)                           (_)          | |       
                          | |__ _   _ _ __   ___ _  ___  _ __   __ _ _ __ ___  _  ___ _ __ | |_ ___  
                          |  __| | | | '_ \ / __| |/ _ \| '_ \ / _` | '_ ` _ \| |/ _ \ '_ \| __/ _ \ 
                          | |  | |_| | | | | (__| | (_) | | | | (_| | | | | | | |  __/ | | | || (_) |
                          |_|   \__,_|_| |_|\___|_|\___/|_| |_|\__,_|_| |_| |_|_|\___|_| |_|\__\___/ 
                                                                            
                                                                            

    
                          ///Bienvenido a la Agenda de Tareas, su funcionamiento es simple, en esta 
                            tiene un menu de opciones que te permite agregar, eliminar, modificar y
                            otras opciones, antes y despues de cada cambio se imprime la lista para 
                            que el usuario pueda ver los cambios realizados.///
                          

      
                       
                                                                   ██╗ 
                                                                ██╗╚██╗
                                                                ╚═╝ ██║
                                                                ██╗ ██║
                                                                ╚═╝██╔╝
                                                                   ╚═╝ 
      
=============================================================================================================================================
=============================================================================================================================================
      """)


# Definimos una lista vacía para almacenar las tareas
tareas_lunes = []
tareas_martes = []
tareas_miercoles = []
tareas_jueves = []
tareas_viernes = []
tareas_sabado = []
tareas_domingo = []


#    ______                 _                      
#   / ____/_  ______  _____(_)___  ____  ___  _____
#  / /_  / / / / __ \/ ___/ / __ \/ __ \/ _ \/ ___/
# / __/ / /_/ / / / / /__/ / /_/ / / / /  __(__  ) 
#/_/    \__,_/_/ /_/\___/_/\____/_/ /_/\___/____/  
                                                  
#Funcion 0: Mostrar el menú de opciones
def mostrar_menu():
    print("""
┳┳┓         ┓    ┏┓   •                      
┃┃┃┏┓┏┓┓┏  ┏┫┏┓  ┃┃┏┓┏┓┏┓┏┓┏┓┏               
┛ ┗┗ ┛┗┗┻  ┗┻┗   ┗┛┣┛┗┗┗┛┛┗┗ ┛               
┓   ┏┓             ┛                         
┃   ┣┫┏┓┏┓┏┓┏┓┏┓┏┓  ╋┏┓┏┓┏┓┏┓                
┻•  ┛┗┗┫┛ ┗ ┗┫┗┻┛   ┗┗┻┛ ┗ ┗┻                
       ┛     ┛                               
┏┓   ┏┓┓•   •                                
┏┛   ┣ ┃┓┏┳┓┓┏┓┏┓┏┓  ╋┏┓┏┓┏┓┏┓                
┗━•  ┗┛┗┗┛┗┗┗┛┗┗┻┛   ┗┗┻┛ ┗ ┗┻                
┏┓   ┳┳┓   ┓•┏•                              
 ┫   ┃┃┃┏┓┏┫┓╋┓┏┏┓┏┓  ╋┏┓┏┓┏┓┏┓              
┗┛•  ┛ ┗┗┛┗┻┗┛┗┗┗┻┛   ┗┗┻┛ ┗ ┗┻              
┏┓   ┓┏      ┓•       ┓                      
┃┃   ┃┃┏┓┏┓  ┃┓┏╋┏┓  ┏┫┏┓  ╋┏┓┏┓┏┓┏┓┏        
┗╋•  ┗┛┗ ┛   ┗┗┛┗┗┻  ┗┻┗   ┗┗┻┛ ┗ ┗┻┛        
┏━   ┳┓                ┓     ┓               
┗┓   ┣┫┏┓┏┓┏┓┏┓┏┓  ╋┏┓┏┫┏┓┏  ┃┏┓┏  ╋┏┓┏┓┏┓┏┓┏
┗┛•  ┻┛┗┛┛ ┛ ┗┻┛   ┗┗┛┗┻┗┻┛  ┗┗┻┛  ┗┗┻┛ ┗ ┗┻┛
┏┓   ┏┓  ┓•                                  
┣┓   ┗┓┏┓┃┓┏┓                                
┗┛•  ┗┛┗┻┗┗┛                                 
                                             
""")
    
#==========================================================================================================================
#========================================================================================================================== 

#Funcion 1: Agregar tarea
def agregar_tarea():
    dia = input("Introduce el día de la semana: ").lower()
    print(f"Lista actual para {dia}:")
    if dia == "lunes":
        print(tareas_lunes)
        tarea = input("Introduce la tarea a agregar: ")
        tareas_lunes.append(tarea)
        print(f"Lista actualizada para {dia}: {tareas_lunes}")
    elif dia == "martes":
        print(tareas_martes)
        tarea = input("Introduce la tarea a agregar: ")
        tareas_martes.append(tarea)
        print(f"Lista actualizada para {dia}: {tareas_martes}")
    elif dia == "miercoles":
        print(tareas_miercoles)
        tarea = input("Introduce la tarea a agregar: ")
        tareas_miercoles.append(tarea)
        print(f"Lista actualizada para {dia}: {tareas_miercoles}")
    elif dia == "jueves":
        print(tareas_jueves)
        tarea = input("Introduce la tarea a agregar: ")
        tareas_jueves.append(tarea)
        print(f"Lista actualizada para {dia}: {tareas_jueves}")
    elif dia == "viernes":
        print(tareas_viernes)
        tarea = input("Introduce la tarea a agregar: ")
        tareas_viernes.append(tarea)
        print(f"Lista actualizada para {dia}: {tareas_viernes}")
    elif dia == "sabado":
        print(tareas_sabado)
        tarea = input("Introduce la tarea a agregar: ")
        tareas_sabado.append(tarea)
        print(f"Lista actualizada para {dia}: {tareas_sabado}")
    elif dia == "domingo":
        print(tareas_domingo)
        tarea = input("Introduce la tarea a agregar: ")
        tareas_domingo.append(tarea)
        print(f"Lista actualizada para {dia}: {tareas_domingo}")
    else:
        print("Dia no valido. Por favor, elige un dia de la semana.")

#==========================================================================================================================
#========================================================================================================================== 

#Funcion 2: Eliminar tarea
def eliminar_tarea():
    dia = input("Introduce el día de la semana: ").lower()
    print(f"Lista actual para {dia}:")
    if dia == "lunes":
        print(tareas_lunes)
        tarea = input("Introduce la tarea a eliminar: ")
        if tarea in tareas_lunes:
            tareas_lunes.remove(tarea)
            print(f"Lista actualizada para {dia}: {tareas_lunes}")
        else:
            print("La tarea no se encuentra en la lista de lunes.")
    elif dia == "martes":
        print(tareas_martes)
        tarea = input("Introduce la tarea a eliminar: ")
        if tarea in tareas_martes:
            tareas_martes.remove(tarea)
            print(f"Lista actualizada para {dia}: {tareas_martes}")
        else:
            print("La tarea no se encuentra en la lista de martes.")
    elif dia == "miercoles":
        print(tareas_miercoles)
        tarea = input("Introduce la tarea a eliminar: ")
        if tarea in tareas_miercoles:
            tareas_miercoles.remove(tarea)
            print(f"Lista actualizada para {dia}: {tareas_miercoles}")
        else:
            print("La tarea no se encuentra en la lista de miercoles.")
    elif dia == "jueves":
        print(tareas_jueves)
        tarea = input("Introduce la tarea a eliminar: ")
        if tarea in tareas_jueves:
            tareas_jueves.remove(tarea)
            print(f"Lista actualizada para {dia}: {tareas_jueves}")
        else:
            print("La tarea no se encuentra en la lista de jueves.")
    elif dia == "viernes":
        print(tareas_viernes)
        tarea = input("Introduce la tarea a eliminar: ")
        if tarea in tareas_viernes:
            tareas_viernes.remove(tarea)
            print(f"Lista actualizada para {dia}: {tareas_viernes}")
        else:
            print("La tarea no se encuentra en la lista de viernes.")
    elif dia == "sabado":
        print(tareas_sabado)
        tarea = input("Introduce la tarea a eliminar: ")
        if tarea in tareas_sabado:
            tareas_sabado.remove(tarea)
            print(f"Lista actualizada para {dia}: {tareas_sabado}")
        else:
            print("La tarea no se encuentra en la lista de sabado.")
    elif dia == "domingo":
        print(tareas_domingo)
        tarea = input("Introduce la tarea a eliminar: ")
        if tarea in tareas_domingo:
            tareas_domingo.remove(tarea)
            print(f"Lista actualizada para {dia}: {tareas_domingo}")
        else:
            print("La tarea no se encuentra en la lista de domingo.")
    else:
        print("Dia no valido. Por favor, elige un dia de la semana.")

#==========================================================================================================================
#========================================================================================================================== 

#Funcion 3: Modificar tarea
def modificar_tarea():
    dia = input("Introduce el día de la semana: ").lower()
    print(f"Lista actual para {dia}:")
    if dia == "lunes":
        print(tareas_lunes)
        tarea_vieja = input("Introduce la tarea a modificar: ")
        if tarea_vieja in tareas_lunes:
            tarea_nueva = input("Introduce la nueva tarea: ")
            index = tareas_lunes.index(tarea_vieja)
            tareas_lunes[index] = tarea_nueva
            print(f"Lista actualizada para {dia}: {tareas_lunes}")
        else:
            print("La tarea no se encuentra en la lista de lunes.")
    elif dia == "martes":
        print(tareas_martes)
        tarea_vieja = input("Introduce la tarea a modificar: ")
        if tarea_vieja in tareas_martes:
            tarea_nueva = input("Introduce la nueva tarea: ")
            index = tareas_martes.index(tarea_vieja)
            tareas_martes[index] = tarea_nueva
            print(f"Lista actualizada para {dia}: {tareas_martes}")
        else:
            print("La tarea no se encuentra en la lista de martes.")
    elif dia == "miercoles":
        print(tareas_miercoles)
        tarea_vieja = input("Introduce la tarea a modificar: ")
        if tarea_vieja in tareas_miercoles:
            tarea_nueva = input("Introduce la nueva tarea: ")
            index = tareas_miercoles.index(tarea_vieja)
            tareas_miercoles[index] = tarea_nueva
            print(f"Lista actualizada para {dia}: {tareas_miercoles}")
        else:
            print("La tarea no se encuentra en la lista de miercoles.")
    elif dia == "jueves":
        print(tareas_jueves)
        tarea_vieja = input("Introduce la tarea a modificar: ")
        if tarea_vieja in tareas_jueves:
            tarea_nueva = input("Introduce la nueva tarea: ")
            index = tareas_jueves.index(tarea_vieja)
            tareas_jueves[index] = tarea_nueva
            print(f"Lista actualizada para {dia}: {tareas_jueves}")
        else:
            print("La tarea no se encuentra en la lista de jueves.")
    elif dia == "viernes":
        print(tareas_viernes)
        tarea_vieja = input("Introduce la tarea a modificar: ")
        if tarea_vieja in tareas_viernes:
            tarea_nueva = input("Introduce la nueva tarea: ")
            index = tareas_viernes.index(tarea_vieja)
            tareas_viernes[index] = tarea_nueva
            print(f"Lista actualizada para {dia}: {tareas_viernes}")
        else:
            print("La tarea no se encuentra en la lista de viernes.")
    elif dia == "sabado":
        print(tareas_sabado)
        tarea_vieja = input("Introduce la tarea a modificar: ")
        if tarea_vieja in tareas_sabado:
            tarea_nueva = input("Introduce la nueva tarea: ")
            index = tareas_sabado.index(tarea_vieja)
            tareas_sabado[index] = tarea_nueva
            print(f"Lista actualizada para {dia}: {tareas_sabado}")
        else:
            print("La tarea no se encuentra en la lista de sabado.")
    elif dia == "domingo":
        print(tareas_domingo)
        tarea_vieja = input("Introduce la tarea a modificar: ")
        if tarea_vieja in tareas_domingo:
            tarea_nueva = input("Introduce la nueva tarea: ")
            index = tareas_domingo.index(tarea_vieja)
            tareas_domingo[index] = tarea_nueva
            print(f"Lista actualizada para {dia}: {tareas_domingo}")
        else:
            print("La tarea no se encuentra en la lista de domingo.")
    else:
        print("Dia no valido. Por favor, elige un dia de la semana.")

#==========================================================================================================================
#========================================================================================================================== 

#Funcion 4: Ver lista de tareas
def ver_lista_tareas():
    print("Todas las listas de tareas:")
    print(f"Lunes: {tareas_lunes}")
    print(f"Martes: {tareas_martes}")
    print(f"Miércoles: {tareas_miercoles}")
    print(f"Jueves: {tareas_jueves}")
    print(f"Viernes: {tareas_viernes}")
    print(f"Sábado: {tareas_sabado}")
    print(f"Domingo: {tareas_domingo}")

#==========================================================================================================================
#========================================================================================================================== 

#Funcion 5: Borrar todas las tareas
def borrar_todas_las_tareas():
    tareas_lunes.clear()
    tareas_martes.clear()
    tareas_miercoles.clear()
    tareas_jueves.clear()
    tareas_viernes.clear()
    tareas_sabado.clear()
    tareas_domingo.clear()
    print("Todas las tareas han sido borradas.")
    print(f"Lista de tareas para lunes: {tareas_lunes}")
    print(f"Lista de tareas para martes: {tareas_martes}")
    print(f"Lista de tareas para miercoles: {tareas_miercoles}")
    print(f"Lista de tareas para jueves: {tareas_jueves}")
    print(f"Lista de tareas para viernes: {tareas_viernes}")
    print(f"Lista de tareas para sabado: {tareas_sabado}")
    print(f"Lista de tareas para domingo: {tareas_domingo}")

#==========================================================================================================================
#==========================================================================================================================

#Funcion 6: Salir
def salir():
    print("Gracias por usar la agenda de tareas. ¡Hasta luego!")
    exit()

#==========================================================================================================================
#========================================================================================================================== 

# _____             _                      _     
#|   __|_ _ ___ ___|_|___ ___    _____ ___|_|___ 
#|   __| | |   |  _| | . |   |  |     | .'| |   |
#|__|  |___|_|_|___|_|___|_|_|  |_|_|_|__,|_|_|_|
                                                
#Funcion Ejecutiva: Ejecutar el programa
def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ")
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            eliminar_tarea()
        elif opcion == "3":
            modificar_tarea()
        elif opcion == "4":
            ver_lista_tareas()
        elif opcion == "5":
            borrar_todas_las_tareas()
        elif opcion == "6":
            salir()
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

# Llamada para iniciar el programa
ejecutar_programa()




# Fin del programa
