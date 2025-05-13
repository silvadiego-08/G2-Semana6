import datetime
import random

fecha = datetime.date.today()

print(f"Bienvenido \n {fecha}")

def adivina (num_usuario, num_rdn):
    if num_usuario == num_rdn:
        print("¡Felicidades! Adivinaste el número.")
    else:
        print("Lo siento, no adivinaste el número.")

def main():
    num_alea = random.randint(1, 10)
    resp = "S"
    while resp.lower() != "N":
        num = input("Ingresa un numero del 1 al 10: ")
        adivina (int(num), num_alea)
        response = input("¿Quieres jugar de nuevo? (S/N): ")      
main()
    
