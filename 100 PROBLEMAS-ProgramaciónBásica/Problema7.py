#Determinar si un número es par, impar o múlitplo de otro.

#Se solicitan los números al usuario
numero = int(input("Introduce un número: "))
multiplo = int(input("Introduce otro número para comprobar si es múltiplo: "))

#Aqui se verifica si el número es par o impar
if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")

#Aqui se verificarsi el número es múltiplo del otro número
if numero % multiplo == 0:
    print(f"{numero} es múltiplo de {multiplo}.")
else:
    print(f"{numero} no es múltiplo de {multiplo}.")