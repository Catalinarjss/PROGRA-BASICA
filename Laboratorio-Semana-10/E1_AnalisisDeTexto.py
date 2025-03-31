#ESTRUCTURA DE DATOS
    #Ejercicio 1. Analisis de textoo con diccionarios y conjuntos


def analizar_tx(texto):
    #Convertimos el texto a minúsculas
    texto = texto.lower()
    
    #Separamos el texto en palabras
    palabras = texto.split()
    
    palabras_unicas = set(palabras)
    
    #Diccionario para contar la frecuencia de cada palabra
    frecuencia = {}
    
    for palabra in palabras:
        #La palabra está en el diccionario, aumentamos su contador
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        #La palabra no está en el diccionario, la agregamos con un contador de 1
        else:
            frecuencia[palabra] = 1
    
    #Buscamos la palabra más frecuente 
    palabra_frecuente = max(frecuencia, key=frecuencia.get)
    frecuencia_palabra_frecuente = frecuencia[palabra_frecuente]
    
    #Imprimimos los resultados
    print(f"Numero total de palabras: {len(palabras)}")
    print(f"Cantidad de palabras unicas: {len(palabras_unicas)}")
    print("Frecuencia de cada palabra:")
    for palabra, count in frecuencia.items():
        print(f"{palabra}: {count}")
    print(f"La palabra más frecuente es '{palabra_frecuente}' y aparece {frecuencia_palabra_frecuente} veces.")

#Solicita al usuario el texto para analizar
texto_usuario = input("Ingresa un texto para analizar: ")
analizar_tx(texto_usuario)