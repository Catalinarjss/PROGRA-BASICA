#Generar la secuencia de Fibonacci hasta un número dado de terminos.

#Se solicita el número de términos al usuario.
numero = int(input("Introduce el número de términos para la secuencia de Fibonacci: "))

#Se verifica que el número de términos sea positivo
if numero <= 0:
    print("Ingresa un número entero positivo mayor que 0.")
else:
    #Inicializa los primeros dos términos de la secuencia
    x, y = 0, 1
    print("Secuencia de Fibonacci:")

    #Se imprimen los términos de la secuencia
    for i in range(numero):
        print(x, end=" ")
        #Se actualizan los valores
        x, y = y, x + y