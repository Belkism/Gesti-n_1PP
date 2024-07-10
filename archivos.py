import os
import csv
#from archivos import*
from datetime import datetime
from funciones import*


'''
La empresa "TechSolutions" nos ha solicitado desarrollar un software de gestión de proyectos para
llevar a cabo un control exhaustivo de los mismos.

'''

#Primer paso abrimos y corroboramos la existencia del archivo
indice_inical=10
id_auto_incremental= indice_inical

def incrementar_id(): # Es una función que va incrementando id dentro del programa.
    global id_auto_incremental # Se uso una variable global
    id_auto_incremental += 1 #  Es un contador que va  a ir agregando los id y por ende incrementando.
    return id_auto_incremental





def parse_csv(nombre_archivo:str): 
    lista_proyectos = []#Lista de proyectos
    lista_claves =[] #acá guardo mis keys de la lista CSV
    if os.path.exists(nombre_archivo): #corroboramos que exista nuestro archivo
        with open(nombre_archivo,"r") as archivo: #Abrimos nuestro archivo en modo lectura
            primer_linea = archivo.readline() #Leemos la primera linea
            primer_linea = primer_linea.replace("\n","") #la primera linea reemplazamos el salto de linea por el espacio
            lista_claves = primer_linea.split(",") #Dividimos la cadena en sub- cadena y la pasamos en forma de lista
            
            for linea in archivo: #  Se crea un for para leer las lineas del archivo
                linea_aux= linea.replace("\n"," ") #Se utiliza una linea aux para no romper el archivo
                lista_valores = linea_aux.split(",") #Dividimos la cadena en sub- cadena y la pasamos en forma de lista corresponde  a los valores
                diccionario_aux = {} #Proyectos # almacenara nuestros datos
                
                if len(lista_claves) != len(lista_valores):
                    print(f"Advertencia: Desajuste entre claves y valores en la línea: {linea}")
                    continue
                
                for i in range (len(lista_claves)): #Recorremos la lista de claves, desde el I =O Asi con los valores 
                    diccionario_aux[lista_claves[i]] = lista_valores[i]
                lista_proyectos.append(diccionario_aux) # a nuestra lista de proyecto que estaba vacia la apendeamos el diccionario
                
        
        return lista_proyectos #Returnamos nuestra lista diccionario
    else:
        # return False #MANEJAR EL MENSAJE DESDE EL MENU #PILAS CON ESTO  DESDE EL MENU
        print("ARCHIVO NO ENCONTRADO")
        
lista_proyectos = parse_csv("proyectos.csv")
# print(lista_proyectos)


#Normalizamos nuestros base de datos


def normalizar_datos (lista_proyectos:list): # Creo una funcion para normalizar los datos de mi lista diccionario, los datos que me solicitan estan en Str.
    if lista_proyectos != []: # Corroboro que mi lista no esta vacia
        print (True)
    else:
        print( False) #Imprime false si la lita esta vacia
        
    dato_key_value= {"id":int,"Nombre del Proyecto":str,"Descripcion":str,"Fecha de inicio":str,"Fecha de Fin":str,"Presupuesto":int,"Estado":str} # Creo un dicionario con la clave y el tipo de dato  que yo necesito modificar 
    
    datos_normalizados =True
    
    for proyecto in lista_proyectos: # Recorro mi lista_proyectos"Proyecto" por "Proyecto"
        for key,tipo in dato_key_value.items(): #Hago un segundo For anidado para que me recorra las key dentro del proyecto y ver si el tipo corresponde a las pre-definidas 
            if key in proyecto:
                proyecto[key] = tipo(proyecto[key]) 
                datos_normalizados = True    
            else:
                print("Normalizar Datos")
                datos_normalizados =False  
    

    return datos_normalizados

            
# resultado= normalizar_datos(lista_proyectos)
# print(resultado)




def actualizar_csv(nombre_archivo: str, lista_proyectos: list): #Creo una función para actualizar el archivo csv.
    if lista_proyectos: 
        lista_claves = lista_proyectos[0].keys() #Las claves
        with open(nombre_archivo, "w", newline='') as archivo: #Abro el archivo en modo escritura
            escritor_csv = csv.DictWriter(archivo, fieldnames=lista_claves) 
            print(escritor_csv)
            escritor_csv.writeheader()
            for proyecto in lista_proyectos:
                escritor_csv.writerow(proyecto)
        print(f"Archivo guardado en: {os.path.abspath(nombre_archivo)}")
    else:
        print("No hay datos para escribir en el archivo") #revisar si esta tomando el 0 o 1 en un Bool
# print(actualizar_csv("proyectos.csv",lista_proyectos))
    
def cargar_proyectos(nombre_archivo): # Esta funcion se creo para cargar proyectos
    global id_auto_incremental # Se declara que la funcion usa una variable global.
    if os.path.exists(nombre_archivo): #Verifica que el archivo exista
        with open(nombre_archivo, "r", newline='') as archivo: #Abre el archivo en modo lectura 
            lector_csv = csv.DictReader(archivo) # La fila la interpreta como dict.
            for fila in lector_csv: #Itera sobre cada fila del csv
                fila["id"] = int(fila["id"]) #convierte el valor de la clave en un entero.
                lista_proyectos.append(fila) #appenda la fila a la lista de proyectos
                id_auto_incremental = max(id_auto_incremental, fila["id"] + 1) #Actualiza
    else:
        id_auto_incremental = id_auto_incremental #Inicializa id_auto_incremental en 0 si el archivo no existe. 

# print(cargar_proyectos("proyectos.csv"))

