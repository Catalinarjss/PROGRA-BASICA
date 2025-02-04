#Generar una lista de números pares e impares hasta un límite dado.

#Se solicita el límite de números al usuario
limite = int(input("Introduce el límite hasta donde desee generar la lista de números: "))

#Inicializamoos la listas para pares e impares
pares = []
impares = []

#Se generan los números hasta el límite
for i in range(1, limite + 1):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

#Listas de números pares e impares
print("Números pares:", pares)
print("Números impares:", impares)