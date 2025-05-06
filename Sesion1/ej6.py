oracion = (input("Escribe una oracion: "))
palabra = oracion.split()
numero_palabras = 0

for palabra in palabra:
    numero_palabras += 1

print(f"El número de palabras es: {numero_palabras}")