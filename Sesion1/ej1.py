N = int(input("Escribe un numero entero positivo: "))

#acumulador
suma = 0

for i in range(1, N+1):
    suma += i

print(f"La suma de los {N} primeros numeros enteros es: {suma}")