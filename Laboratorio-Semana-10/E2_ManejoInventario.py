#ESTRUCTURA DE DATOS
    #Ejercicio 2. Manejo de Inventario con Listas y Diccionarios

#lista para almacenar los productos
inventario = []

#función para agregar un producto al inventario
def agregar_producto():
    nombre = input("Ingrese el nombre del producto:")
    categoria = input("Ingrese la categoría del producto:")
    precio = float(input("Ingrese el precio del producto:"))
    cantidad = int(input("Ingrese la cantidad del producto:"))
    
    #creamos un diccionario para los productos
    producto = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "cantidad": cantidad
    }
    
    inventario.append(producto)
    print(f"Producto {nombre} agregado al inventario.")

#función para eliminar un producto
def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar:")
    
    #buscamos el producto en la lista de inventario
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            inventario.remove(producto)
            print(f"Producto {nombre} eliminado del inventario.")
            return
    print(f"El producto {nombre} no se encuentra en el inventario.")

#función para buscar un producto
def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ")
    
    #buscamos el producto en la lista
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            print(f"Producto encontrado:{producto}")
            return
    print(f"El producto {nombre} no se encuentra en el inventario.")

#función para mostrar todos los productos ordenados
def mostrar_productos_ordenados():
    
    inventario_ordenado = sorted(inventario, key=lambda x: x["precio"])
    
    print("Productos ordenados por precio (de menor a mayor):")
    for producto in inventario_ordenado:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Categoría: {producto['categoria']}, Cantidad: {producto['cantidad']}")

#menu del programa 
def menu():
    while True:
        print("\n    Menú de Inventario    ")
        print("1.Agregar producto")
        print("2.Eliminar producto")
        print("3.Buscar producto")
        print("4.Mostrar productos ordenados por precio")
        print("5.Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            eliminar_producto()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            mostrar_productos_ordenados()
        elif opcion == "5":
            print("¡Gracias por usar el sistema de inventario! Hasta luego.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

menu()