#ALGORITMOS DE PROGRAMACION
    #Ejercicio 8. Implementacion de Mergesort

#ordenar dos listas en orden ascendente
def fusionar(lista1, lista2):
    resultado = []  
    
    #mientras haya elementos en ambas listas
    while len(lista1) > 0 and len(lista2) > 0:
        if lista1[0] < lista2[0]:
            resultado.append(lista1.pop(0))  
        else:
            resultado.append(lista2.pop(0))
    
    #si quedan elementos en alguna de las dos listas, los agregamos a resultado
    resultado.extend(lista1)
    resultado.extend(lista2)
    
    return resultado

#función para dividir la lista y ordenarla
def mergesort(lista):
   
    if len(lista) <= 1:
        return lista
    
    #dividimos la lista en dos mitades
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    
    #ordenamos
    izquierda = mergesort(izquierda)
    derecha = mergesort(derecha)
    
    return fusionar(izquierda, derecha)


def main():
    #pedimos al usuario que ingrese números
    entrada = input("Ingresa una lista de números separados por espacio: ")
    
    #convertimos la entrada del usuario a una lista de números (enteros)
    lista = [int(num) for num in entrada.split()]
    
    print("\nLista original:", lista)
    
    #ordenamos la lista utilizando Mergesort
    lista_ordenada = mergesort(lista)
    
    print("\nLista ordenada:", lista_ordenada)

main()