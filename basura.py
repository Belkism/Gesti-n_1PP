from archivos import*
from csv import*

def retomar_proyecto(lista_proyectos: list):
    alta = False

    for proyecto in lista_proyectos:
        if proyecto.get("Estado") == "Cancelado":  # Usamos get para evitar errores si "Estado" no existe
            print(proyecto.get("Estado"))
            proyecto["Estado"] = "Activo"  # Cambiamos "Activado" por "Activo" para mantener consistencia
            alta = True
            print(f"El proyecto '{proyecto['Nombre del Proyecto']}' ha sido retomado y ahora está 'Activo'.")

    if not alta:
            print("No se encontraron proyectos en estado 'Cancelado' para retomar.")

    return alta

print(retomar_proyecto(lista_proyectos))