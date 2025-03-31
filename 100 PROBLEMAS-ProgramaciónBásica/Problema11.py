# Verificar si una cadena es un palíndromo.

def palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    
    if cadena == cadena[::-1]:
        return True
    else:
        return False

cadena_usuario = input("Ingresa una palabra o frase para verificar si es un palíndromo: ")

if palindromo(cadena_usuario):
    print(f'"{cadena_usuario}" es un palíndromo.')
else:
    print(f'"{cadena_usuario}" no es un palíndromo.')