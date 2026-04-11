# 1. Función para cifrar un solo carácter
def cifrar_caracter(c, desplazamiento):
    # Verificar si es letra minúscula
    if 'a' <= c <= 'z':
        # Convertir a posición 0-25
        posicion = ord(c) - ord('a')
        # Aplicar fórmula y volver a letra
        nueva_pos = (posicion + desplazamiento) % 26
        return chr(nueva_pos + ord('a'))
    else:
        # Si no es letra, lo dejamos igual
        return c


# 2. Función para cifrar un mensaje completo
def cifrar_mensaje(mensaje, desplazamiento):
    resultado = ""
    for letra in mensaje:
        resultado = resultado + cifrar_caracter(letra, desplazamiento)
    return resultado


# 3. Función para descifrar
def descifrar_mensaje(mensaje, desplazamiento):
    # Es lo mismo que cifrar pero con el desplazamiento negativo
    return cifrar_mensaje(mensaje, -desplazamiento)


# --- BONUS: Fuerza Bruta ---
def fuerza_bruta(mensaje_cifrado):
    print("=== INTENTANDO DESCRIFRAR (Fuerza Bruta) ===")
    for desplazamiento in range(26):
        texto = descifrar_mensaje(mensaje_cifrado, desplazamiento)
        print(f"Desplazamiento {desplazamiento}: {texto}")


# ✅ PROBAR EL PROGRAMA

# Ejemplo del ejercicio
print("Cifrar 'hola' con desplazamiento 3:")
print(cifrar_mensaje("hola", 3))  # Debe salir 'krod'

print("\nDescifrar 'krod' con desplazamiento 3:")
print(descifrar_mensaje("krod", 3)) # Debe salir 'hola'

# Probar el Bonus
print("\n--- PRUEBA DE FUERZA BRUTA ---")
fuerza_bruta("krod")