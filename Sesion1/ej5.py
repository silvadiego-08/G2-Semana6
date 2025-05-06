N = int(input("Introduce un número entero positivo: "))

if N < 0:
    print("Por favor, introduce un número entero positivo.")
else:
    factorial = 1

    while N > 1:
        factorial *= N  
        N -= 1  

    print("El factorial es:", factorial)
