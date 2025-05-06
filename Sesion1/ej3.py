oracion = str(input("Escribe una oración: "))

contador = 0

for letra in oracion:
    if letra == "a":
        contador += 1
    elif letra == "e":
        contador += 1
    elif letra == "i":
        contador += 1
    elif letra == "o":
        contador += 1
    elif letra == "u":
        contador += 1

print(f"El número de vocales es: {contador}")


