n = int(input("Ingresa el numero de calificaciones:"))

#contador
suma_calificaciones = 0

for i in range(n):
    calificacion = float(input(f"Ingresa la calificacion {i+1}: "))
    suma_calificaciones += calificacion

promedio = suma_calificaciones / n
print(f"El promedio de las calificaciones es: {promedio:.2f}")
