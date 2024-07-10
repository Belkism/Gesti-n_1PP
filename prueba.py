from archivos import*





def mostrar_proyectos(lista_proyectos:list):
    informacion ="PROYECTOS TechSolutions:\nID |     NOMBRE DEL PROYECTO              |                            DESCRIPCION                                      |FECHA DE INICIO| FECHA DE FIN |PRESUPUESTO|ESTADO \n"
    for proyecto in lista_proyectos:
        estado = proyecto["Estado"].strip()
        if estado in ["Activo", "Cancelado", "Finalizado"]:
            informacion += f"{proyecto['id']:>2} | {proyecto['Nombre del Proyecto']:>40} | {proyecto['Descripcion']:>76}  |{proyecto['Fecha de inicio']:<7} |{proyecto['Fecha de Fin']:<7} |{proyecto['Presupuesto']:<10} |{proyecto['Estado']}\n"      
    
    return informacion

# print(mostrar_proyectos(lista_proyectos))



def mostrar_proyecto(proyecto:dict):
    informacion_s ="PROYECTOS TechSolutions:\nID |       NOMBRE DEL PROYECTO                |                            DESCRIPCION                                      |FECHA DE INICIO| FECHA DE FIN |PRESUPUESTO|ESTADO \n"
    for key in proyecto:
        if key == "Estado":
            informacion_s+= f"{proyecto['id']:>2} | {proyecto['Nombre del Proyecto']:>40} | {proyecto['Descripcion']:>76}  |{proyecto['Fecha de inicio']:<7} |{proyecto['Fecha de Fin']:<7} |{proyecto['Presupuesto']:<10} |{proyecto['Estado']}\n"
    
    return informacion_s
