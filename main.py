from os import*
from funciones import*
from archivos import*
from prueba import*
from csv import*
from abm import*
from funcionesparci import*

system ("cls")


id_auto_incremental=1

def incrementar_id(): # Es una función que va incrementando id dentro del programa.
    global id_auto_incremental # Se uso una variable global
    id_auto_incremental += 1 #  Es un contador que va  a ir agregando los id y por ende incrementando.
    return id_auto_incremental

def decrementar_id(): # Es una función que va incrementando id dentro del programa.
    global id_auto_incremental # Se uso una variable global
    id_auto_incremental += -1 #  Es un contador que va  a ir agregando los id y por ende incrementando.
    return id_auto_incremental

def menu():
    global id_auto_incremental
    cargar_proyectos("proyectos.csv")
    
    if os.path.exists("proyecto.csv"): 
        print("Bienvenido a la empresa TechSolutions")
        archivo_existe = True
    else:
        print("Error,Archivo Inexistente")
        archivo_existe = False
    
    while True:
        system ("cls")
        imprimir_menu()
        opcion=validar_opcion("Ingrese una opción:","Error, ingrese la opcion correcta")
        if opcion==1:
            cantidad_proyectos_activos = len(lista_proyectos)
            if cantidad_proyectos_activos < 50:
                incrementar_id()
                nuevo_proyecto = ingresar_proyecto(id_auto_incremental, lista_proyectos)
                
                if nuevo_proyecto:
                    actualizar_csv("proyectos.csv",lista_proyectos)
                    print(f"Proyecto agregado: {nuevo_proyecto}")
                else:
                    decrementar_id()
                    print("El proyecto no fue agregado.")
            else:
                print("Error: Se ha alcanzado el límite de proyectos activos.")
                    
        
        elif opcion == 2:
            modificar_proyecto(lista_proyectos)   
            
        elif opcion == 3:
            if len(lista_proyectos)>0:
                cancelar_proyecto(lista_proyectos)
        elif opcion == 4:  
            comprobar_proyectos(lista_proyectos)
    
        elif opcion == 5:
            print(mostrar_proyectos(lista_proyectos)) 
            
        elif opcion == 6:
            print(calcular_presupuesto_promedio(lista_proyectos))

        elif opcion == 7:
            nombre_a_buscar = input("Ingrese el nombre del proyecto que desea buscar: ")
            buscar_proyecto_nombre(lista_proyectos,nombre_a_buscar)
        elif opcion == 8:   
            modo = input("Ingrese el modo de ordenación (nombre, presupuesto, fecha_inicio): ")
            direccion = input("Ingrese la dirección de ordenamiento (ascendente, descendente): ").lower()
            if direccion == "ascendente":
                ascendente = True
            elif direccion == "descendente":
                ascendente = False
            else:
                print("Dirección de ordenamiento no válida. Por default ascendente.")
                ascendente = True
            proyectos_ordenados = ordenar_proyectos(lista_proyectos, modo, ascendente)

            if proyectos_ordenados:
                for proyecto in proyectos_ordenados:
                    print(proyecto)
            else:
                print("No se pudieron ordenar los proyectos. Revise el criterio y la dirección de ordenamiento.")
        elif opcion == 9:  
            presupuesto_ingresado= int(input("Ingresar Presupuesto:"))
            presupuesto_txt(lista_proyectos,presupuesto_ingresado,"Reportes de Proyectos:")
        elif opcion ==10:
            nombre_proyecto = input ("Ingrese nombre de Proyecto a buscar:")
            buscar_proyecto_nombre_txt(nombre_proyecto)
        elif opcion ==11:
            retomar_proyecto(lista_proyectos)
        
        elif opcion == 12:
            proyectos = proyectos_activos(lista_proyectos)
            print(mostrar_proyectos(proyectos))
            
        elif opcion == 13:
            proyecto_invierno = calcular_presupuesto_activos(lista_proyectos)
            print(mostrar_proyecto(proyecto_invierno))
            
        elif opcion == 14:
            guardar_proyectos_finalizados_json(lista_proyectos)
            
        elif opcion ==15:
            actualizar_csv(nombre_archivo,lista_proyectos)
            
        
        continuar = input("¿Desea volver al menu inicial? (S/N): ").strip().upper()
        if continuar != 'S':
            print("¡Hasta luego!")
            break
            
        
        else:
            print("Opción no válida. Intente nuevamente.")
            
    


menu()
