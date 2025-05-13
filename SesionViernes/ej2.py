frase = input("Escribe una frase: ")
contador = 0
for palabras in frase:
    if palabras == " ":
        contador += 1
print(f"El número de palabras en la frase es: {contador + 1}")