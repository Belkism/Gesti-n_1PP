import os
from funciones import*
from archivos import*
from prueba import*
from datetime import datetime
from csv import*
import operator
import ast
ACTIVO =1
CANCELADO=2
FINALIZADO = 3
MODIFICACION_CORRECTA = 1
MODIFICACION_ERRONEA = 2
MODIFICACION_CANCELADA = 3

id_auto_incremental=0

def id_incremental(): # Esta función se creo para incrementar el id correspondiente a cada proyecto que se vaya creando.
    global id_auto_incremental # variable global
    id_auto_incremental += 1 #Contador
#print(id_auto_incremental)


def eliminar_caracteres_especiales(cadena: str) -> str: # Elimina los caracteres especiales dentro de una cadena.
    cadena_limpia = ''
    for caracter in cadena:
        if caracter.isalpha() or caracter.isalnum():
            cadena_limpia += caracter
    return cadena_limpia


def ingresar_cadena(mensaje:str,mensaje_error:str): # Esta función ingresa una cadena, la valida si los caracteres son alfabeticos y la cadena no excede los 30 caracteres.
    cadena = input(mensaje)
    cadena_limpia = eliminar_caracteres_especiales(cadena)
    while not cadena.isalpha() and len(cadena) > 30:
        cadena= input(mensaje_error)

    return cadena_limpia


def ingresar_txt_alfa(mensaje:str,mensaje_error:str): # Esta función, permite el ingreso un texto alfanumérico de no más de 200 caracteres.
    texto= input(mensaje)
    cadena_limpia = eliminar_caracteres_especiales(texto)# Reutlizamos una función dentro de esta, para eliminar caracteres especiales.
    while not texto.isalnum() and len(texto) > 200: #validamos que sea alfanumerico y no mayor a 200 caracteres.
        texto= input(mensaje_error)

    return cadena_limpia #Retorna una cadena limpia.

def ingresar_fecha_proyecto():
    while True:
        try:
            dia = int(input("Por favor, ingrese el día (1-31): "))
            if 1 <= dia <= 31:
                break
            else:
                print("Día inválido. Debe estar entre 1 y 31.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    while True:
        try:
            mes = int(input("Por favor, ingrese el mes (1-12): "))
            if 1 <= mes <= 12:
                break
            else:
                print("Mes inválido. Debe estar entre 1 y 12.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    while True:
        try:
            anio = int(input("Por favor, ingrese el año (2010-2050): ")) #Colocar DATATIME.NOW()
            if 2010 <= anio <= 2050:
                break
            else:
                print("Año inválido. Debe estar entre 2010 y 2050.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    # Verificar si la fecha es válida
    try:
        fecha = datetime(anio, mes, dia)
        fecha_formateada = fecha.strftime("%d-%m-%Y")
        return fecha_formateada
    except ValueError:
        print("La fecha ingresada no es válida. Intente nuevamente.")
        return ingresar_fecha_proyecto()

def ingresar_presupuesto(mensaje:str,mensaje_error:str,numero:int): # Esta función permite ingresar presupuestos.
    numero_presupuesto = int(input(mensaje)) #Ingrese presupuesto
    while numero_presupuesto < 500000: #Hace una validación al presupuesto, el cual no puede ser menor a 500000.
        numero_presupuesto = int(input(mensaje_error)) # Si ingresa menos, da un error 
        numero_presupuesto = int(input(mensaje)) #Solicita ingresar el presupuesto nuevamente.
    return numero_presupuesto

def ingresar_estado(mensaje:str,mensaje_error:str): #Esta  función permite ingresar un estado al proyecto.
    estado= input(mensaje) # Solicita el estado
    estado = estado.capitalize() #Utiliza el metodo capitalize para asegurarme que la primera letra este en Mayuscula.

    while estado !="Activo" and estado !="Cancelado" and estado != "Finalizado": # valida que el estado corresponda a las opciones.
        estado= input(mensaje_error).capitalize
    return estado # retorna el estado

def confirmar(mensaje:str,mensaje_error:str):
    confirmacion = input(mensaje)
    confirmacion = confirmacion.upper()
    retorno = False

    while confirmacion != "S" and confirmacion != "N":
        confirmacion = input(mensaje_error)
        confirmacion = confirmacion.upper()

    if confirmacion == "S":
        retorno = True

    return retorno



def ingresar_proyecto(lista_proyectos:list):
    global id_auto_incremental

    
    Nombre_del_Proyecto = ingresar_cadena("Ingrese nombre del proyecto:","Error / Reingrese el nombre nuevamente")
    descripcion = ingresar_txt_alfa("Describa su proyecto:","Error, describa nuevamente su proyecto")
    fecha_inicio = ingresar_fecha_proyecto()
    fecha_fin = ingresar_fecha_proyecto()
    Presupuesto =  ingresar_presupuesto("Ingrese presupuesto:","Error el presupuesto es incorrecto",500000)
    Estado = ingresar_estado("Ingrese estado del proyecto:"," Error, ingrese el estado nuevamente")

    proyecto = {"id":id_auto_incremental,"Nombre del Proyecto":Nombre_del_Proyecto,"Descripcion":descripcion,"Fecha de inicio":fecha_inicio,"Fecha de Fin":fecha_fin,"Presupuesto":Presupuesto,"Estado":Estado}

    print("Datos del proyecto ingresado")
    mostrar_proyecto(proyecto)
    if confirmar("\nConfirma dar de alta al siguiente proyecto (S-N): ","\nERROR/Debe elegir entre (S/N) Confirma dar de alta el siguiente proyecto(S-N): "):
        lista_proyectos.append(proyecto)
        id_auto_incremental += 1 
        return  proyecto

    else:
        return None


# agregar_proyecto=ingresar_proyecto(lista_proyectos)
# # conteo= id_auto_incremental
# print(agregar_proyecto)
# # print(conteo)

def buscar_proyecto(lista_proyectos:list,id_a_buscar:int): # Esta función permite ubicar un proyecto con su ID.
    retorno = None

    for i in range(len(lista_proyectos)): # Recorre la lista por su indice
        if lista_proyectos[i]["id"] == id_a_buscar:# Si el indice id corresponde al id a buscar, se encontro el proyecto.
            print("Se encontro el Proyecto")
            mostrar_proyecto(lista_proyectos[i]) # se llama la funcion mostrar proyecto, para que  nos muestre el proyecto por su indice.
            retorno = i
            break

    return retorno # la funcion retorna el indice.

# 
#----------- Modificación----------------------------------


def modificar_proyecto(lista_proyectos:list): # Esta función nos modifica un proyecto ya creado, solicita el id a modificar.
    retorno = MODIFICACION_ERRONEA
    mostrar_proyectos(lista_proyectos)

    id_a_modificar = int(input("Ingrese el id del Proyecto a modificar: "))
    indice = buscar_proyecto(lista_proyectos,id_a_modificar)

    if indice != None:
        proyecto_original =lista_proyectos[indice].copy()
        proyecto_aux =    proyecto_original.copy()
        
        # Se obtiene el proyecto a modificar

        while True: # Se crea un sub- menu para permitir al usuario que  eliga el dato a modificar.
            print("\n¿Qué dato desea modificar?")
            print("1. Nombre del Proyecto:")
            print("2. Descripción:")
            print("3. Fecha de Inicio:")
            print("4. Fecha de Fin:")
            print("5. Presupuesto:")
            print("6. Estado:")
            print("7. Salir:")

            opcion = input("Ingrese el número de la opción: ") # Se solicita el ingreso de la opcion.

            if opcion == "1":
                proyecto_aux["Nombre del Proyecto"] = ingresar_cadena("Ingrese Nuevo nombre del proyecto:", "Error / Reingrese el nombre nuevamente")
            elif opcion == "2":
                proyecto_aux["Descripcion"] = ingresar_txt_alfa("Ingrese nueva descripción de proyecto:", "Error, describa nuevamente su proyecto")
            elif opcion == "3":
                proyecto_aux["Fecha de inicio"] = ingresar_fecha_proyecto()
            elif opcion == "4":
                proyecto_aux["Fecha de Fin"] = ingresar_fecha_proyecto()
            elif opcion == "5":
                proyecto_aux["Presupuesto"] = ingresar_presupuesto("Ingrese nuevo presupuesto :", "Error el presupuesto es incorrecto", 500000)
            elif opcion == "6":
                proyecto_aux["Estado"] = ingresar_estado("Ingrese nuevo estado del proyecto:", "Error, ingrese el estado nuevamente")
                print(f"Nuevo estado ingresado {proyecto_aux['Estado']}")
            elif opcion == "7":
                print("Saliste del Sub-menu")
                break
            else:
                print("Opcion no valida. Por favor, elija una opcion valida.")
            '''
            Cuando el usuario ingrese las opciones que desee modificar debe confirmarlas para que se apliquen al proyecto
            '''

            if confirmar("\nConfirma modificar el siguiente Proyecto (S-N): ","\nERROR/Debe elegir entre (S/N) Confirma modificar el siguiente Proyecto (S-N): "):
                lista_proyectos[indice] = proyecto_aux
                retorno = MODIFICACION_CORRECTA
                print("Proyecto modificado correctamente")
            else:
                retorno = MODIFICACION_CANCELADA
                print("Modificacion cancelada")
    else:
        print(f"No se encontró ningún proyecto con el ID {id_a_modificar}.")

    return retorno

# print(modificar_proyecto(lista_proyectos))

def cancelar_proyecto(lista_proyectos:list): # Esta función nos permite cancelar un proyecto, primero nos pide el id para buscarlo.
    mostrar_proyectos(lista_proyectos)
    id_cancelar = int(input("Ingrese id a Cancelar:")) # Ingrese id a cancelar
    print(id_cancelar)
    indice = buscar_proyecto(lista_proyectos, id_cancelar) # Busca el proyecto por su indice. 
    print(indice)
    if indice != None:
        print(lista_proyectos [indice])
        lista_proyectos[indice] ["Estado"] = "Cancelado"
        print(lista_proyectos[indice])

    # if not proyecto_encontrado:
    #     print("No se encontró ningún proyecto con el ID especificado.")
    return id_cancelar

#print(cancelar_proyecto(lista_proyectos))

def comprobar_proyectos(lista_proyectos:list) -> bool: #Cambiará el estado de todos los proyectos que ya hayan finalizados.
    cambio= False
    for proyecto in lista_proyectos:
        Fecha_fin = datetime.strptime(proyecto["Fecha de Fin"], '%d-%m-%Y')
        if Fecha_fin < datetime.now():
            proyecto["Estado"] = "Activo"
            cambio= True
            print(" El Estado del proyecto a sido cambiado")
            break
    if not cambio:
        print("No se encontraron proyectos para finalizar")
    return cambio

# print(comprobar_proyectos(lista_proyectos))


def calcular_presupuesto_promedio(lista_proyectos:list): #Esta función nos calcula el presupuesto de todos los proyectos
    contador_proyecto = 0 #Implemente un contador para contar los presupuestos de cada proyecto
    suma_presupuesto = 0 # Contenedor donde ire guardando los presuspuestos de cada proyecto
    for proyecto in lista_proyectos:
            presupuesto = int(proyecto["Presupuesto"])
            suma_presupuesto += presupuesto
            contador_proyecto += 1

    if contador_proyecto == 0:
        print("No se admite la divisíón por 0")
        return 0
    return suma_presupuesto/contador_proyecto #Retorna el promedio solicitado.
lista_proyectos = parse_csv("proyectos.csv")
print(calcular_presupuesto_promedio(lista_proyectos))

def buscar_proyecto_nombre(lista_proyectos:list, nombre_buscar:str): # Esta función busca los proyectos por nombre
    retorno = None
    for proyecto in lista_proyectos:
        if proyecto ["Nombre del Proyecto"] == nombre_buscar: # Si el nombre a buscar corresponde a uno dentro del proyecto, lo muestra.
            print("El nombre del proyecto es :")
            print(mostrar_proyecto(proyecto))
            retorno = proyecto["Nombre del Proyecto"] # Nos retorna el nombre del proyecto  a buscar.
            break

        else:
            print("No existe el proyecto en nuestra base de datos") # Si no existe el proyecto en nuestra base nos muestra esto.
    return retorno


#buscar_proyecto_nombre(lista_proyectos,"Laboratorio de Microbiologia")

import operator

def ordenar_proyectos(lista_proyectos:list, modo:str, ascendente:bool=True): # Nos ordena el proyecto de acuerdo al modo que se desee.

    if modo == "nombre":
        clave = "Nombre del Proyecto"
    elif modo == "presupuesto":
        clave = "Presupuesto"
    elif modo == "fecha_inicio":
        clave = "Fecha de inicio"
    else:
        print("Criterio de ordenación no válido.")


    # Ordenar la lista de proyectos
    getter = operator.itemgetter(clave)

    lista_ordenada = sorted(lista_proyectos, key=getter, reverse=not ascendente)
    for proyecto in lista_ordenada:
        print(proyecto)

    return lista_ordenada # Nos retorna una lista ordenada.


def presupuesto_txt(lista_proyectos:list,presupuesto_ingresado:float,mensaje:str): # Esta función nos retorna un reporte txt, con todos los proyectos que sean mayor al presupuesto ingresado.
    proyecto_condicion = [] # Cree esta lista vacia para guardar todos los proyectos que cumplan con la condicón.
    id_contador = 1 # coloque un contador iniciado en 1
    for proyecto in lista_proyectos: # Este for recorre los proyectos en la lista
        if float(proyecto["Presupuesto"]) > presupuesto_ingresado: # El presupuesto lo harcodeo con un float en caso de que coloque decimales.
            proyecto["id"] = id_contador #Asigna contador
            proyecto_condicion.append(proyecto) # Los proyectos que cumplen con la condición se appendean a la lista.
            print(f"El proyecto '{proyecto['Nombre del Proyecto']}' tiene un presupuesto mayor al presupuesto ingresado.")
            id_contador += 1  # Incrementar el contador de ID

    if not proyecto_condicion: # En caso de que no haya proyectos que cumplan muestra en consola.
        print("No hay proyectos que cumplan con el presupuesto especificado.")
    else:
        cantidad_proyectos = len(proyecto_condicion)
        with open("archivo.txt", "w") as archivo: #  Cree un archivo txt en modo escritura, con la fecha actual en que se genera el reporte.
            fecha_solicitud = datetime.now() 
            fecha_formateada = fecha_solicitud.strftime("%d-%m-%Y")
            archivo.write(f"Cantidad de proyectos que cumplen: {cantidad_proyectos}\n\n")
            archivo.write(f"{mensaje}\n")
            archivo.write(f"Fecha de solicitud: {fecha_formateada}\n")
            for proyecto in proyecto_condicion:
                archivo.write(f"Id: {proyecto['id']}\n")
                archivo.write(f"Nombre del Proyecto: {proyecto['Nombre del Proyecto']}\n")
                archivo.write(f"Descripcion del Proyecto: {proyecto['Descripcion']}\n")
                archivo.write(f"Fecha de Inicio: {proyecto['Fecha de inicio']}\n")
                archivo.write(f"Fecha de Fin: {proyecto['Fecha de Fin']}\n")
                archivo.write(f"Presupuesto: {proyecto['Presupuesto']}\n")
                archivo.write(f"Estado: {proyecto['Estado']}\n")
                archivo.write("\n")
    return proyecto_condicion



def leer_numero_reporte():
    try:
        with open("numero_reporte.txt", "r") as archivo:
            numero_reporte = int(archivo.read().strip())
    except FileNotFoundError:
        numero_reporte = 1
    return numero_reporte

def guardar_numero_reporte(numero_reporte):
    with open("numero_reporte.txt", "w") as archivo:
        archivo.write(str(numero_reporte))



def buscar_proyecto_nombre_txt(nombre_buscar: str):
    encontrado = False
    proyecto = [] 
    id_contador_p = 1
    with open("proyectos.txt", "r") as archivo_lectura:
        for linea in archivo_lectura:
            datos= linea.strip().split(",")  #Se supone que cada linea la separan comas.
            if datos[1] == nombre_buscar:  # El nombre del proyecto se encuentra en la segunda posición
                encontrado = True
                proyecto=datos
                id_contador_p += 1#Se guardan los datos del proyecto encontrado.
                break # Se rompe porque se supone que  el proyecto se encontro

    if encontrado:
        numero_reporte = leer_numero_reporte()
        # Si se encuentra el proyecto, se crea un archivo para escribir la información.
        with open(f"reporte_{nombre_buscar}.txt", "w") as archivo_escritura:
            fecha_solicitud = datetime.now()
            fecha_formateada = fecha_solicitud.strftime("%d-%m-%Y")
            archivo_escritura.write(f"Fecha de solicitud: {fecha_formateada}\n")
            archivo_escritura.write(f"Id: {proyecto[0]}\n")
            archivo_escritura.write(f"Nombre del Proyecto: {proyecto[1]}\n")
            archivo_escritura.write(f"Descripcion del Proyecto: {proyecto[2]}\n")
            archivo_escritura.write(f"Fecha de Inicio: {proyecto[3]}\n")
            archivo_escritura.write(f"Fecha de Fin: {proyecto[4]}\n")
            archivo_escritura.write(f"Presupuesto: {proyecto[5]}\n")
            archivo_escritura.write(f"Estado: {proyecto[6]}\n")
        print(f"Se ha generado el reporte 'reporte_{nombre_buscar}.txt' con la información del proyecto '{nombre_buscar}'.")
        
        numero_reporte += 1
        guardar_numero_reporte(numero_reporte)
    else:
        print(f"No se encontró ningún proyecto con el nombre '{nombre_buscar}' en nuestra base de datos.")

    return encontrado



def retomar_proyecto(lista_proyectos: list):
    proyecto_retomado = False

    for proyecto in lista_proyectos:
        if proyecto.get("Estado") == "Cancelado":  # Usamos get para evitar errores si "Estado" no existe
            print(proyecto.get("Estado"))
            proyecto["Estado"] = "Activo" 
            proyecto_retomado= True
            print(f"El proyecto '{proyecto['Nombre del Proyecto']}' ha sido retomado y ahora está 'Activo'.")

    if not proyecto_retomado:
            print("No se encontraron proyectos en estado 'Cancelado' para retomar.")
            
        

    return proyecto_retomado

print(retomar_proyecto(lista_proyectos))



def calcular_diferencia_dias(fecha_inicio_str, fecha_fin_str):
    # Convertir las fechas de cadena a objetos de fecha
    fecha_inicio = datetime.strptime(fecha_inicio_str, "%d-%m-%Y")
    fecha_fin = datetime.strptime(fecha_fin_str, "%d-%m-%Y")

    # Calcular la diferencia en días
    diferencia = fecha_fin - fecha_inicio

    # Obtener la diferencia en días como un número entero
    return diferencia.days

