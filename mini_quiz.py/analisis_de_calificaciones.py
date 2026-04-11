# 1. Función para calcular el promedio
def promedio(notas):
    suma = 0
    for nota in notas:
        suma = suma + nota
    return suma / len(notas)

# 2. Función para encontrar la nota mayor
def mayor(notas):
    max_nota = notas[0]  # Empezamos asumiendo que la primera es la mayor
    for nota in notas:
        if nota > max_nota:
            max_nota = nota
    return max_nota

# 3. Función para encontrar la nota menor
def menor(notas):
    min_nota = notas[0]  # Empezamos asumiendo que la primera es la menor
    for nota in notas:
        if nota < min_nota:
            min_nota = nota
    return min_nota

# 4. Función para contar aprobados
def contar_aprobados(notas, minimo=61):
    contador = 0
    for nota in notas:
        if nota >= minimo:
            contador = contador + 1
    return contador

# --- BONUS: Función Histograma ---
def histograma(notas):
    for nota in notas:
        # Multiplicamos el asterisco por la nota para hacer la barra
        print(f"{nota}: {'*' * nota}")

# 5. Función Reporte que usa todas las anteriores
def reporte(notas):
    print("===== REPORTE DE CALIFICACIONES =====")
    print(f"Lista de notas: {notas}")
    print(f"Promedio: {promedio(notas):.2f}")
    print(f"Nota mayor: {mayor(notas)}")
    print(f"Nota menor: {menor(notas)}")
    print(f"Cantidad de aprobados: {contar_aprobados(notas)}")
    print("\n--- HISTOGRAMA ---")
    histograma(notas)


# ✅ PROBAR EL PROGRAMA CON LOS DATOS DEL EJERCICIO
notas_prueba = [85, 42, 73, 61, 55, 90, 38, 77, 95, 60]
reporte(notas_prueba)