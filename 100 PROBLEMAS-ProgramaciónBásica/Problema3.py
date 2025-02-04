#Calcular el factorial de un número dado.

#Se solicita el número al usuario
numero = int(input("Introduce un número entero positivo para calcular su factorial: "))

#El número debe ser positivo
if numero < 0:
    print("El número debe ser positivo.")
else:
    #Inicializar el resultado del factorial
    factorial = 1
    
    #Utilizamos un bucle para calcular el factorial
    for i in range(1, numero + 1):
        factorial *= i

    print(f"El factorial de {numero} es {factorial}")
