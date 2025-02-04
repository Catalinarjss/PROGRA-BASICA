#Calcular el interés compuesto dado un capital, tasa y tiempo.

#Se solicita los datos al usuario
capital_inicial = float(input("Introduce el capital inicial: "))
tasa_interes = float(input("Introduce la tasa de interés anual (en %): "))
tiempo = float(input("Introduce el tiempo en años: "))

#Se calcula el interés compuesto
interes_compuesto = capital_inicial * (1 + tasa_interes / 100) ** tiempo

# Mostrar el resultado
print(f"El total después de {tiempo} años será: {interes_compuesto:.2f}")