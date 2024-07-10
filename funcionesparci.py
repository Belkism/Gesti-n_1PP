from funciones import*
from datetime import datetime


# #Mostrar los proyectos activos que duren menos de 3 años. En caso de que no haya indicar error
# #Calcular el/los proyectos activos con mayor presupuesto iniciados en invierno. En caso de que no
# haya indicar error



def calcular_diferencia_dias(fecha_inicio_str: str, fecha_fin_str: str) -> int: # Esta calcula la diferencia de dias entre fechas.
    # Convertir las cadenas de fecha a objetos datetime
    fecha_inicio = datetime.strptime(fecha_inicio_str, '%d-%m-%Y') # Utilizo el modulo datetime para transformar las fechas.
    #print(type(fecha_inicio))
    fecha_fin = datetime.strptime(fecha_fin_str, '%d-%m-%Y')
    
    # Calcular la diferencia en días
    diferencia = fecha_fin - fecha_inicio 
    
    # Retorna la diferencia en días como un entero
    return diferencia.days 


def proyectos_activos(lista_proyectos): # Esta función muestra los proyectos activos con una existencia menor a tres años.
    proyectos_activos = []
    for proyecto in lista_proyectos: #Este for recorre la lista de proyectos hasta la clave "Estado" y si es activo, obtiene la fechas.
        if proyecto["Estado"].strip() == "Activo":
            # Se obtienen las fechas de inicio y fin del proyecto como cadenas
            fecha_inicio_str = proyecto["Fecha de inicio"].strip()
            fecha_inicio = datetime.strptime(fecha_inicio_str, '%d-%m-%Y')
            
            fecha_fin_str = proyecto["Fecha de Fin"].strip()
            fecha_fin = datetime.strptime(fecha_fin_str, '%d-%m-%Y')
            
            # Formatear las fechas como cadenas en el formato 'día, mes, año'
            fecha_inicio_formateada = fecha_inicio.strftime('%d, %m, %Y')
            fecha_fin_formateada = fecha_fin.strftime('%d, %m, %Y')
            
            # Calcular la diferencia en días entre las fechas de inicio y fechas de fin
            diferencia_dias = calcular_diferencia_dias(fecha_inicio_str, fecha_fin_str)
            
            # Agrega el proyecto activo a la lista si la diferencia es menor a 3 años (aprox. 1095 días)
            if diferencia_dias < 1095:
                proyectos_activos.append(proyecto) # Se apendean en la lista de proyectos activos.
    if not proyectos_activos: # En caso de que no se encuentren proyectos menores a tres años, retornar error.
        return "Error: No hay proyectos activos, que duren menos de tres años"
    
    return proyectos_activos # Retorna los proyectos activos.

#print(proyectos_activos(lista_proyectos))


def calcular_presupuesto_activos(lista_proyectos): # Esta función calcula los proyectos activos con mayor presupuesto en los meses de invierno.
    proyectos_invierno = [] # Creo una lista vacia para apendear los proyectos que cumplan.

    # Filtrar proyectos activos que hayan comenzado en invierno
    for proyecto in lista_proyectos: # Hago un for que recorra la lista  con cada proyecto.
        estado = proyecto.get("Estado", "").strip().capitalize() # Utilizo el metodo get, para corroborar que sea un dict, tambien le  quito los espacio con el strip y que siempre empiece por mayuscula.
        fecha_inicio_str = proyecto.get("Fecha de inicio", "").strip() # Corrobo que la  fecha sea una clave de dict con get y le saco los espacios.
        
        if fecha_inicio_str: # aca corroboro la fecha de inicio
            fecha_inicio = datetime.strptime(fecha_inicio_str, '%d-%m-%Y') # La fecha de inico la formateo con datetime
            mes_inicio = fecha_inicio.month # creo la variable mes de inico porque la  necesitare para comparar los meses de frio.
            
            if estado == "Activo" and mes_inicio in [6, 7, 8]:  # Meses de invierno (junio, julio, agosto en Argentina )
                proyectos_invierno.append(proyecto) # Si el proyecto se inicio en invierno se apendea a la lista.
    
    # Si no hay proyectos en invierno, indicar error
    if not proyectos_invierno:
        return "Error: No hay proyectos activos que hayan comenzado en invierno."
    
    # Encontrar el proyecto con el presupuesto más alto
    proyecto_mayor_presupuesto = proyectos_invierno[0]
    for proyecto in proyectos_invierno:
        if proyecto.get("Presupuesto", 0) > proyecto_mayor_presupuesto.get("Presupuesto", 0): # Aqui comparo los proyectos dentro de la lista de proyectos de invierno por indice, el  proyecto de mayor presupuesto es el que se mostrara.
            proyecto_mayor_presupuesto = proyecto
    
    return proyecto_mayor_presupuesto # Retorna el proyecto con el presupuesto mas alto entre los proyectos iniciados  en invierno.


