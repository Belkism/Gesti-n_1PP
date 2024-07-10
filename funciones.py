import os
from csv import*
from archivos import*
from datetime import datetime
from prueba import*
import json
Activo =1
Cancelado=2
Finalizado = 3

indice_inical=10
id_auto_incremental=indice_inical # Esta variable se creo para usarla en la función de incrementar id.


def incrementar_id(): # Es una función que va incrementando id dentro del programa.
    global id_auto_incremental # Se uso una variable global
    id_auto_incremental += 1 #  Es un contador que va  a ir agregando los id y por ende incrementando.
    return id_auto_incremental

def decrementar_id(): # Es una función que va decrementando id dentro del programa.
    global id_auto_incremental # Se uso una variable global
    id_auto_incremental += -1 #  Es este caso va decremmentando
    return id_auto_incremental




def eliminar_caracteres_especiales(cadena: str) -> str: #Esta función limmpia los caracteres especiales en la cadena.
    cadena_limpia = '' # Se le indica que la limpie
    for caracter in cadena: # Recorremos los caracteres de la cadena
        if caracter.isalpha() or caracter.isalnum(): # los caracteres pueden ser numeros o letras.
            cadena_limpia += caracter # Va limpiando conforme va encontrando
    return cadena_limpia # Retorna una cadena limpia
  

def ingresar_cadena(mensaje:str,mensaje_error:str): # la función retorna una cadena limppia, sin caratceres especiales.
    cadena = input(mensaje)
    cadena_limpia = eliminar_caracteres_especiales(cadena)
    while not cadena.isalpha() and len(cadena) > 30:
        cadena= input(mensaje_error)

    return cadena_limpia
# prueba = ingresar_cadena("ingrese cadena:","El mensaje es incorrecto")
# print (prueba)
    

def ingresar_txt_alfa(mensaje:str,mensaje_error:str): # La funcion retoma una cadena  con texto alfanumerico que no supera los 200 caracte
    texto= input(mensaje) # Se ingresa un texto
    cadena_limpia = eliminar_caracteres_especiales(texto) #Limpia la cadena
    while not texto.isalnum() and len(texto) > 200: # hace una validacion
        texto= input(mensaje_error)

    return cadena_limpia

# previa = ingresar_txt_alfa("Ingrese texto:","Error, ingrese nuevamente el texto")
# print(previa)

    
def ingresar_enteros(mensaje:str,mensaje_error:str,valor_min:int,valor_max:int): #Esta funcion nos retorna unicamente numeros
    numero = int(input(mensaje))
    while numero > valor_max or numero < valor_min: # Se valida de acuerdo al numero ingreso, retorna un numero
        numero = int(input(mensaje_error))
    return numero
    
# prueba = ingresar_enteros("Ingrese Numero:","Error!Ingrese nuevamente",1,100)
# print(prueba)

def ingresar_presupuesto(mensaje:str,mensaje_error:str,numero:int): # Retorna un presupuesto
    numero_presupuesto = int(input(mensaje)) #Ingresa presupuesto
    while numero_presupuesto < 500000: # Se valida con el monto exigido por el programa
        numero_presupuesto = int(input(mensaje_error))
    return numero_presupuesto # #Retorna presupuesto correspondiente a lo exigido


def ingresar_estado(mensaje:str,mensaje_error:str): # Esta función verifica que los estados ingresados correspondan al sistmema
    estado= input(mensaje) # se ingresa al sistmea
    estado = estado.capitalize() # Utilizamos el metodo capitalize para convetir la primera letra en mayuscula.

    while estado !="Activo" and estado !="Cancelado" and estado != "Finalizado": # Validamos los estados
        estado= input(mensaje_error).capitalize()
    return estado # Retornamos el estado correspondiente


#------------------------------------Funcion para ingresar fechas al sistema---------------------------------------

def ingresar_fecha_proyecto(): # En esta función se ingresa la fecha y utilizamos datetime para cambiar las fechas a dd/mm/aa, se maneja excepciones en caso de arrojar error.
    while True:
        try: # Usamos excepciones para manejar errores
            dia = int(input("Por favor, ingrese el día (1-31): ")) #Ingresamos los dias 
            if 1 <= dia <= 31:#Validamos el dato ingresado
                break
            else:
                print("Día inválido. Debe estar entre 1 y 31.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    while True:
        try:
            mes = int(input("Por favor, ingrese el mes (1-12): ")) #Ingresamos los meses 
            if 1 <= mes <= 12:#Validamos el dato ingresado
                break
            else:
                print("Mes inválido. Debe estar entre 1 y 12.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    while True:
        try:
            anio = int(input("Por favor, ingrese el año (Actual-2040): ")) #Ingresamos los años
            if datetime.today().year <= anio <= 2040: #Validamos el dato ingresado
                break
            else:
                print("Año inválido. Debe estar entre la fecha actual y el 2040.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    #   Se verifica que la fecha sea validada y se formatea con datatime.
    try:
        fecha = datetime(anio, mes, dia)
        fecha_formateada = fecha.strftime("%d/%m/%Y")
        return fecha_formateada
    except ValueError:
        print("La fecha ingresada no es válida. Intente nuevamente.")
        return ingresar_fecha_proyecto()
    
#print(ingresar_fecha_proyecto())



#---------- Funciones de Menu-------------------------
def imprimir_menu(): # Creamos un menu con los print que queremos ver en consola
    print("\n ¡Bienvenido a la empresa TechSolutions! Seleccione una opción:")
    print("1. Ingresar Proyecto:") # Ingresa el usuario un proyecto al programa
    print("2. Modificar Proyecto:")# Nos modifica los proyectos
    print("3. Cancelar Proyecto:") # Muestra los cancelados
    print("4. Comprobar Proyectos:") # Comprueba los proyectos
    print("5. Mostrar todos los Proyestos:") #Muesta en consola todos los proyectos
    print("6. Calcular presupuesto promedio") # Calcula el promedio total 
    print("7. Buscar proyecto por nombre") # Busca por nombre los proyectos
    print("8. Ordenar proyectos:") # Nos ordena los proyectos segun criterio
    print("9. Ingrese un presupuesto:") # Genera reporte txt de todos los presupuestos del proyecto
    print("10. Ingrese nombre de un proyecto:") #Generar reporte txt del nombre del proyecto especifico
    print("11. Retomar proyecto:")
    print("12. Proyectos Activos:")
    print("13. Proyectos Activo con mayor presupuesto:") 
    print("14. ProyectosFinalizados.json") 
    print("15. Salir") # Se deben actualizar los datos del proyecto
   

def validar_opcion(mensaje, mensaje_error): # Valida la opcion a ingresar al sistema y maneja una excepcion en caso de errores.
     while True:
        try:
            opcion = int(input(mensaje))
            if 1 <= opcion <= 15:
                return opcion
            else:
                print(mensaje_error)
        except ValueError:
            print(mensaje_error)


def ingresar_proyecto(id_auto_incremental:int,lista_proyectos:list): # Ingresar todos los datos de un nuevo proyecto, reutiliza funciones.
    retorno = False # Es una bandera 
    Nombre_del_Proyecto = ingresar_cadena("Ingrese nombre del proyecto:","Error / Reingrese el nombre nuevamente") # 
    descripcion = ingresar_txt_alfa("Describa su proyecto:","Error, describa nuevamente su proyecto")
    fecha_inicio = ingresar_fecha_proyecto()
    fecha_fin = ingresar_fecha_proyecto()
    Presupuesto =  ingresar_presupuesto("Ingrese presupuesto:","Error el presupuesto es incorrecto",500000)
    Estado = ingresar_estado("Ingrese estado del proyecto:"," Error, ingrese el estado nuevamente")
    
    proyecto = {"id":id_auto_incremental,"Nombre del Proyecto":Nombre_del_Proyecto,"Descripcion":descripcion,"Fecha de inicio":fecha_inicio,"Fecha de Fin":fecha_fin,"Presupuesto":Presupuesto,"Estado":Estado} # Se crea un diccionario donde se almacenaran los datos del nuevo proyecto

    
    print("Datos del proyecto ingresado")
    mostrar_proyecto(proyecto) # Se llama a la funcion mostrar proyecto, para que nos muestre el proyecto en consola
    if confirmar("\nConfirma dar de alta el siguiente Proyecto (S-N): ","\nERROR/Debe elegir entre (S/N) Confirma dar de alta el siguiente proyecto(S-N): "): # Confirmamos el ingreso del proyecto
        lista_proyectos.append(proyecto) #appendeamos los datos en la lista_proyectos
        retorno = True
        
    return retorno

#------------------------------Cantidad de Proyectos-------------------------------------------------


def cantidad_proyectos(lista_proyectos:list): # Retorna la cantidad de proyecto en nuestro programa de acuerdo
    cantidad_activos = 0 # Es un contador 
    for proyecto in lista_proyectos:
        if proyecto["Estado"].strip() == "Activo": #Hace una comparación si el "Estado" es igual a Activo, va contando
            cantidad_activos +=1 #Contador habilitado
        elif cantidad_activos >50: # Si la cantidad de proyectos supera los 50, muestra en consola que alcanzo el limite permitido.
            print("Alcanzo el maximo de proyectos permitidos")

    return cantidad_activos

nombre_archivo = "Proyectos.csv"
lista_proyectos = parse_csv(nombre_archivo)

print("Lista de proyectos leída del archivo CSV:")
for proyecto in lista_proyectos:
    print(proyecto)

# Normalizar los datos
resultado_normalizacion = normalizar_datos(lista_proyectos)
print(f"Resultado de la normalización de datos: {resultado_normalizacion}")

#
def confirmar(mensaje:str,mensaje_error:str): # Confirma al seleccionar un cambio en el programa por parte del usuario.
    confirmacion = input(mensaje) #ingresa la confirmación 
    confirmacion = confirmacion.upper()
    retorno = False
    
    while confirmacion != "S" and confirmacion != "N": #Hace una validación para "Si" o "No"
        confirmacion = input(mensaje_error) # Si coloca una letra distinta, da un mensaje de error, solicitando el ingreso nuevamente.
        confirmacion = confirmacion.upper() #Coloco el metodo Upper para que los datos ingresados por el usuario se procesen en mayuscula.
        
    if confirmacion == "S": # hace una comparación si coloca "S" es correcta la confirmación.
        retorno = True

    return retorno

def guardar_proyectos_finalizados_json(lista_proyectos): # Esta función guarda los proyectos finalizados en un archivo json.
    proyectos_finalizados = [] #Creo una lista vacia para agregar los proyectos que cumplan.

    for proyecto in lista_proyectos: # Creo un for que recorra los proyectos que cumplan con el estado finalizado.
        if proyecto.get('Estado', '').strip().capitalize() == 'Finalizado':  # Asegurar que el estado sea 'Finalizado'
            proyectos_finalizados.append(proyecto) # Si el proyecto cumple se apppendea en la lista de proyectos finalizados.

    # Convertir la lista de proyectos finalizados a formato JSON
    proyectos_finalizados_json = json.dumps(proyectos_finalizados, indent=4)

    # Guardar la cadena JSON en un archivo
    try:
        with open('proyectos_finalizados.json', 'w') as file: # Se crea un archivo Json donde se guardaran los archivos json que correspondan.
            file.write(proyectos_finalizados_json)
        print("Archivo 'proyectos_finalizados.json' creado exitosamente.")
    except IOError as e: # Se manejan excepciones en caso de manejar errores.
        print(f"Error al crear el archivo JSON: {e}")

