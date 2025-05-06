M = int(input("Escribe un numero entero positivo: "))

producto = 1
contador = 0

while contador < M:
    contador += 1
    numero_par = 2 * contador
    producto *= numero_par

print(f"El producto de los {M} primeros numeros pares es: {producto}")