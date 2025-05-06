n = int(input("Ingresa el numero de digitos: "))

#acumulador
suma_digitos = 0

for i in range(n):
    digito = int(input(f"Ingresa el digito {i+1}: "))
    suma_digitos += digito

print(f"La suma de los {n} digitos es: {suma_digitos}")
