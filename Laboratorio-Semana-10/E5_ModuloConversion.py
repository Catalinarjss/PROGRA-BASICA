#FUNCIONES
    #Ejercicio 5. Modulo para conversion de unidades.

#función para convertir kilómetros a millas
def km_a_millas(km):
    millas = km * 0.621371 
    return millas

#función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#función para convertir litros a galones
def litros_a_galones(litros):
    galones = litros * 0.264172 
    return galones

#menú 
def mostrar_menu():
    print("Seleccione una opción de conversión:")
    print("1.Kilómetros a Millas")
    print("2.Celsius a Fahrenheit")
    print("3.Litros a Galones")
    print("4.Salir")

#función principal que maneja las conversiones
def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desea: ")

        if opcion == "1":
            km = float(input("Ingrese la cantidad en kilómetros: "))
            millas = km_a_millas(km)
            print(f"{km} kilómetros son {millas} millas.")
        
        elif opcion == "2":
            celsius = float(input("Ingrese la temperatura en grados Celsius: "))
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius}°C son {fahrenheit}°F.")
        
        elif opcion == "3":
            litros = float(input("Ingrese la cantidad en litros: "))
            galones = litros_a_galones(litros)
            print(f"{litros} litros son {galones} galones.")
        
        elif opcion == "4":
            print("¡Gracias por usar el conversor! Hasta luego.")
            break
        
        else:
            print("Opción no válida, por favor intente de nuevo.")

main()