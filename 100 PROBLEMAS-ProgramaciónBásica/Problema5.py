#Verificar  si un numero es primo.

#Se solicita el número que se quiere verificar al usuario
numero = int(input("Introduce un número para verificar si es primo: "))

#Se verifica si el número es mayor que 1 y comprobar si tiene divisores
if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print(f"{numero} no es un número primo.")
            break
    else:
        print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
