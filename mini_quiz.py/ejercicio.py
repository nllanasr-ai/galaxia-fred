import random
numero_secreto = random.randint(1, 100)
intentos = 0
MAX_INTENTOS = 7

while True:
    if intentos >= MAX_INTENTOS:
        print(f"Has alcanzado el máximo de {MAX_INTENTOS} intentos. El número era {numero_secreto}.")
        break

    intento = int(input("Adivina el número entre 1 y 100: "))
    intentos += 1
    
    if intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
        break

