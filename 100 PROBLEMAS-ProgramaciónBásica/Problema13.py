# Convertir una temperatura entre distintas escalas.

def celsius_a_fahrenheit(celsius):
    
    return (celsius * 9/5) + 32

def celsius_a_kelvin(celsius):
    return celsius + 273.15

print("Selecciona la escala de la temperatura: ")
print("1. Celsius a Fahrenheit")
print("2. Celsius a Kelvin")

opcion = int(input("Ingresa 1 o 2: "))

temperatura = float(input("Ingresa la temperatura en Celsius: "))

if opcion == 1:
    fahrenheit = celsius_a_fahrenheit(temperatura)
    print(f"{temperatura}°C es igual a {fahrenheit}°F")
elif opcion == 2:
    kelvin = celsius_a_kelvin(temperatura)
    print(f"{temperatura}°C es igual a {kelvin}K")

else:
    print("Opción no válida.")
