suma_pares = 0
suma_impares = 0

print("Escribe una serie de números enteros (0 para terminar):")
numero = int(input())

while numero != 0: 
    if numero % 2 == 0:
        suma_pares += numero
    else: suma_impares += numero
    numero = int(input())

print(f"La suma de los números pares es: {suma_pares}")
