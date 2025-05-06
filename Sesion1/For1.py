#Leer una palabra diferente a fin y convertirla a mayuscula
palabra = input("Escribe una palabra: ")
palabra = "fin"

for fin in palabra:
    if palabra == fin:
        print("Adios...")
        break
    else:
        palabra = input("Escribe una palabra: ")
        while palabra != "fin":
            print(f"{palabra.upper()} tiene {len(palabra)} letras")
            palabra = input("Escribe una palabra: ")
else:
    print("Adios...")

