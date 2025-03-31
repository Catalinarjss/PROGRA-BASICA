#FUNCIONES
    #Ejercicio 4. Calculadora de Estadisticas

import math

#función que calcula las estadísticas
def calcular_estadisticas(*args):
    #convertimos los argumentos en una lista
    numeros = list(args)

    #calcular promedio usando lambda
    promedio = (lambda nums: sum(nums) / len(nums))(numeros)

    #calcular mediana
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    if n % 2 == 1:
        mediana = numeros_ordenados[n // 2]
    else:
        mediana = (numeros_ordenados[n // 2 - 1] + numeros_ordenados[n // 2]) / 2

    #calcular desviación estándar
    varianza = (lambda nums, prom: sum((x - prom) ** 2 for x in nums) / len(nums))(numeros, promedio)
    desviacion_estandar = math.sqrt(varianza)

    #devolver los resultados
    return promedio, mediana, desviacion_estandar

#función principal para solicitar los datos
def main():
    #solicitamos una lista de números
    numeros_str = input("Ingrese una lista de números separados por espacio: ")
    numeros = [float(x) for x in numeros_str.split()]

    promedio, mediana, desviacion_estandar = calcular_estadisticas(*numeros)

    print(f"Promedio: {promedio}")
    print(f"Mediana: {mediana}")
    print(f"Desviación Estándar: {desviacion_estandar}")

main()
