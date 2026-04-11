# 1. Función para imprimir la tabla de multiplicar
def tabla(n, hasta=10):
    print(f"--- Tabla del {n} ---")
    for i in range(1, hasta + 1):
        print(f"{n} x {i} = {n * i}")
    print()  # Espacio vacío para separar


# 2. Función para verificar si un número es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# 3. Función para imprimir tablas de números primos
def tablas_primos(limite):
    print("=== TABLAS DE NÚMEROS PRIMOS ===")
    for numero in range(2, limite + 1):
        if es_primo(numero):
            tabla(numero)


# ✅ PROBAR EL PROGRAMA

# Prueba normal
tablas_primos(10)

# Prueba del Bonus: Tabla del 5 hasta el 15
print("\n--- BONUS: Tabla larga ---")
tabla(5, hasta=15)