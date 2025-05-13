def es_par(numero):
    return numero % 2 == 0

def main():
    numero_usuario = int(input("Introduce un número entero positivo: "))
    
    lista_numeros = list(range(1, numero_usuario + 1))
    
    print(f"Números pares y sus cuadrados desde 1 hasta {numero_usuario}:")
    for num in lista_numeros:
        if es_par(num):
            print(f"Número {num} es par y su cuadrado es {num ** 2}")
if __name__ == "__main__":
    main()
           