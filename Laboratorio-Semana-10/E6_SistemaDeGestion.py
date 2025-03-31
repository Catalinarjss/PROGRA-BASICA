#CLASES
    #Ejercicio 6. Sistema de Gestion de Vehiculos

#clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
       
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def mostrar_informacion(self):
        #información del vehículo
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Precio: {self.precio} USD")

#subclase Automovil
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, precio, numero_puertas):
       
        super().__init__(marca, modelo, año, precio)
        
        self.numero_puertas = numero_puertas

    def mostrar_informacion(self):
        #la información básica y el número de puertas
        super().mostrar_informacion()
        print(f"Número de puertas: {self.numero_puertas}")

#subclase Motocicleta 
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, precio, cilindrada):
        
        super().__init__(marca, modelo, año, precio)
        
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        #información básica y la cilindrada
        super().mostrar_informacion()
        print(f"Cilindrada: {self.cilindrada} cc")

#crear un automóvil
auto = Automovil("Honda", "Civic Type R", 2023, 45000, 4)

#crear una motocicleta
moto = Motocicleta("Kawasaki", "Ninja ZX-10R", 2022, 16000, 998)

#mostrar la información de ambos vehículos
print("Información del Automóvil:")
auto.mostrar_informacion()

print("\nInformación de la Motocicleta:")
moto.mostrar_informacion()