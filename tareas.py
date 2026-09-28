tareas = []
siguiente_id = 1


def agregar_tarea(titulo):
    global siguiente_id
    nueva_tarea = {
        "id": siguiente_id,
        "titulo": titulo,
        "completada": False   
    }
    tareas.append(nueva_tarea)
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
    
def menu():
    while True:
        print("====== Gestor de tareas ======")
        print("1.- Agregar Tarea ")
        print("2.- Listar Tarea ")
        print("3.- Completar Tarea ")
        print("4.- Eliminar Tarea")
        print("5.- Salir")
        opcion = input("")
        
        if opcion == "1":
            titulo = input("Titulo de la tarea: ")
            agregar_tarea(titulo)
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            id_tarea = int(input("Id de la tarea a completar: "))
            completar_tarea(id_tarea)
        elif opcion == "4":
            id_tarea = int(input("Id de la tarea a Eliminar: "))
            eliminar_tarea(id_tarea)
        elif opcion == "5":
            print("Hasta luego!")
            break
        else:
            print("Opcion No valida, intente de nuevo")
        
menu()
        