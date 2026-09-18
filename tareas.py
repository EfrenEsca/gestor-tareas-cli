tareas = []
siguiente_id = 1


def agregar_tarea(titulo):
    global siguiente_id
    NuevaTarea = {
        "id": siguiente_id,
        "titulo": titulo,
        "completada": False   
    }
    tareas.append(NuevaTarea)
    siguiente_id += 1
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
    
def eliminar_tarea(id_tarea):
    global tareas 
    tareas = [tarea for tarea in tareas if tarea["id"] != id_tarea]
    print(f"tarea {id_tarea} eliminada (si existia)")
    
agregar_tarea("Comprar Leche")
agregar_tarea("Estudiar Python")
eliminar_tarea(1)
agregar_tarea("Hacer Ejercicio")
listar_tareas()