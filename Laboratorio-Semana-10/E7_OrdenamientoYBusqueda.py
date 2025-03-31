#ALGORITMOS DE PROGRAMACION
    #Ejercicio 7. Ordenamiento y Busqueda

import random

#función principal
def main():
    #lista de 10 números aleatorios entre 1 y 100
    lista = [random.randint(1, 100) for _ in range(10)]
    
    print("Lista original:", lista)
    
    #ordenamos la lista con el método sort de Python
    lista.sort()
    print("\nLista ordenada:", lista)
    
    #pedimos al usuario que ingrese un número para buscar
    objetivo = int(input("\nIngresa un número para buscar en la lista: "))
    
    #busqueda secuencial
    if objetivo in lista:
        print(f"El número {objetivo} se encuentra en la lista.")
    else:
        print(f"El número {objetivo} no se encuentra en la lista.")

main()