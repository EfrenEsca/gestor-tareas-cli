tareas = []

def agregar_tareas(titulo):
    NuevaTarea = {
        "id": len(tareas) + 1,
        "titulo": titulo,
        "completada": False   
    }
    tareas.append(NuevaTarea)
    print(f"Tarea Agregada: {titulo}")
    
def listar_tareas():
    if not tareas:
        print("No hay tareas registradas")
        return

    for tarea in tareas:
        estado = "👍" if tarea["completada"] else "✖️"
        print(f"{tarea["id"]}. [{estado}] {tarea["titulo"]}")
        
def completar_tarea(id_tarea):
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tarea["completada"] = True
            print(f"Tarea {id_tarea} marcada como completada")
            return
        
    print(f"No se encontro ninguna tarea con el id {id_tarea}")
    
    
agregar_tareas("Comprar Leche")
agregar_tareas("Estudiar Python")
completar_tarea(1)
listar_tareas()