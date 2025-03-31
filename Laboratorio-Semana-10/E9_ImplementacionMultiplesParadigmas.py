#PARADIGMAS DE PROGRAMACION
    #Ejercicio 9. Implementacion de Multiples Paradigmas

#función para mostrar el menú 
def mostrar_menu():
    print("\n     Sistema de Gestión de Tareas     ")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir")

#agregar una tarea
def agregar_tarea(tareas):
    tarea = input("Ingresa la descripción de la tarea: ")
    tareas.append({"descripcion": tarea, "completada": False})
    print("Tarea agregada exitosamente.")

#función para listar todas las tareas
def listar_tareas(tareas):
    if len(tareas) == 0:
        print("No hay tareas en la lista.")
    else:
        for i, tarea in enumerate(tareas):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i + 1}. {tarea['descripcion']} - {estado}")

#tarea como completada
def marcar_completada(tareas):
    listar_tareas(tareas)
    if len(tareas) == 0:
        return
    try:
        numero_tarea = int(input("Ingresa el número de la tarea que quieres marcar como completada: "))
        if 1 <= numero_tarea <= len(tareas):
            tareas[numero_tarea - 1]["completada"] = True
            print("Tarea marcada como completada.")
        else:
            print("Número de tarea no válido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def ejecutar():
    tareas = []  #lista para almacenar las tareas

    while True:
        mostrar_menu()  #mostrar el menú
        try:
            opcion = int(input("Elige una opción: "))
            if opcion == 1:
                agregar_tarea(tareas)
            elif opcion == 2:
                listar_tareas(tareas)
            elif opcion == 3:
                marcar_completada(tareas)
            elif opcion == 4:
                print("Saliste del sistema")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")


if __name__ == "__main__":
    ejecutar()