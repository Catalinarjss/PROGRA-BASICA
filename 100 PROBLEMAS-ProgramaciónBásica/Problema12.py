# Encontrar el mayor entre tres números dados.


num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

if num1 >= num2 and num1 >= num3:
    num_mayor = num1
elif num2 >= num1 and num2 >= num3:
    num_mayor = num2
else:
    num_mayor = num3

print("El número mayor es:", num_mayor)