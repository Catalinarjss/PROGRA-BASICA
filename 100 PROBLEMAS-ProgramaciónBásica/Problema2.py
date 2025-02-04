#Crear una calculadora simple que realice operaciones básicas.

#Se solicitan los números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

#Se solicita la operación a realizar
operacion = input("Elige la operación (suma, resta, multiplicacion, division): ")

# Realizar la operación
if operacion == "suma":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operacion == "resta":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operacion == "multiplicacion":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operacion == "division":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operación no válida.")