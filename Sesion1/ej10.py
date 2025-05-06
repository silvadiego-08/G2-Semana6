print("Bienvenido a tu cajero automatico")
saldo_inicial = int(input("Introduce el saldo inicial: "))
print("Su saldo inicial es: ", saldo_inicial)

# Contadores
contador_depositos = 0
contador_retiros = 0

while True: #Seleccionar opcion
    print("1. Depositar")
    print("2. Retirar")
    print("3. Salir")

    opcion = int(input("Selecciona una opcion: "))
    
    if opcion == 1: # Opcion deposito
        Cantidad_depositar = float(input("Ingrese la cantidad a depositar: "))
        if Cantidad_depositar > 0:
            saldo_inicial += Cantidad_depositar
            contador_depositos += 1
            print(f"Deposito exitoso. Su nuevo saldo es: {saldo_inicial:.2f}")
        else:
            print("Cantidad no valida. Intente de nuevo.")

    elif opcion == 2: # Opcion retiro
        Cantidad_retirar = float(input("Ingrese la cantidad a retirar: "))
        if Cantidad_retirar > 0 and Cantidad_retirar <= saldo_inicial:
            saldo_inicial -= Cantidad_retirar
            contador_retiros += 1
            print(f"Retiro exitoso. Su nuevo saldo es: {saldo_inicial:.2f}")
        else:
            print("Cantidad no valida o saldo insuficiente. Intente de nuevo.")
    elif opcion == 3: # Opcion salir
        print("Gracias por usar el cajero automatico.")
        print(f"Total de depositos realizados: {contador_depositos}")
        print(f"Total de retiros realizados: {contador_retiros}")
        break
    else:
        print("Opcion no valida. Selecciona 1,2 o 3.")

