#Calcular el área y la circunferencia de un círculo.

#Realize este programa de dos maneras distintas 

#1 
#se solicita el radio del círculo al usuario
radio = float(input("Introduce el radio del círculo: "))

#se calcula el área y la circunferencia
area = 3.1416 * radio ** 2
circunferencia = 2 * 3.1416 * radio

#Resultados
print("El área del círculo es:", round(area, 2))
print("La circunferencia del círculo es:", round(circunferencia, 2))


#2
import math

#Se solicita el radio del círculo al usuario
radio_1 = float(input("Introduce el radio del círculo: "))

#Se calcula el área y la circunferencia
area_1 = math.pi * radio_1 ** 2
circunferencia_1 = 2 * math.pi * radio_1

#Resultados
print(f"El área del círculo es: {area_1:.2f}")
print(f"La circunferencia del círculo es: {circunferencia_1:.2f}")