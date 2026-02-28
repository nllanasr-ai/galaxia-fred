# Inicializar contador
correctas = 0

# Pregunta 1
respuesta1 = input("¿Cuál es el océano más grande del mundo? ").lower()
if respuesta1 == "pacífico":
    correctas += 1

# Pregunta 2
respuesta2 = input("¿Quién escribió 'Don Quijote de la Mancha'? ").lower()
if respuesta2 == "miguel de cervantes" or respuesta2 == "cervantes":
    correctas += 1
# Pregunta 3
respuesta3 = input("¿Cuál es la capital de Francia? ").lower()
if respuesta3 == "parís":
    correctas += 1

# Mostrar resultado
print(f"Obtuviste {correctas} de 3 correctas")
if correctas == 3:
    print("¡Perfecto!")
elif correctas == 2:
    print("¡Muy bien!")
elif correctas == 1:
    print("Puedes mejorar")
else:
    print("Sigue estudiando")