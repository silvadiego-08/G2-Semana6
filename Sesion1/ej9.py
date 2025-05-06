numero = int(input("Escribe un numero entero positivo: "))

contadores = [0] * 11
i = 0
while i < len(numero):
    digito = int(numero[i])
    contadores[digito] += 1
    i += 1
for j in range(10):
    print(f"El digito {j} aparece {contadores[j]} veces.")

