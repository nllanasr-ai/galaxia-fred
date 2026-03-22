# 1. Crear tupla con coordenadas de Guatemala City
coordenadas = (14.634915, -90.506843)
print("=== TUPLAS EN PYTHON ===\n")
print(f"1. Coordenadas de Guatemala City: {coordenadas}")

# 2. Desempaquetar en variables lat, lon
lat, lon = coordenadas
print(f"   Latitud: {lat}")
print(f"   Longitud: {lon}\n")

# 3. Función que retorna (min, max, promedio) de una lista de números
def estadisticas_numeros(lista):
    min_val = min(lista)
    max_val = max(lista)
    promedio = sum(lista) / len(lista)
    return (min_val, max_val, promedio)

# Ejemplo de uso de la función
lista_ejemplo = [10, 20, 30, 40, 50]
resultado = estadisticas_numeros(lista_ejemplo)
print(f"2. Función que retorna tupla con estadísticas")
print(f"   Lista: {lista_ejemplo}")
print(f"   Resultado (min, max, promedio): {resultado}")
print(f"   Mínimo: {resultado[0]}, Máximo: {resultado[1]}, Promedio: {resultado[2]}\n")

# 4. Diccionario con tuplas como claves
distancias = {
    ("Guate", "Escuintla"): 58,
    ("Guate", "Antigua"): 45,
}
print(f"3. Tuplas como claves en diccionarios")
for ruta, km in distancias.items():
    print(f"   {ruta[0]} → {ruta[1]}: {km} km")
print()

# 5. Intentar modificar un elemento de la tupla (genera error)
mi_tupla = (1, 2, 3)
print(f"4. Las tuplas son INMUTABLES (no se pueden modificar)")
print(f"   Tupla original: {mi_tupla}")
print(f"   Intentar mi_tupla[0] = 10 causaría un ERROR")
print(f"   Error: 'tuple' object does not support item assignment")
# mi_tupla[0] = 10  # Error: 'tuple' object does not support item assignment

print("\n=== EJEMPLOS DE 'MODIFICACIÓN' DE TUPLAS ===")
print("Las tuplas son inmutables, pero podemos crear nuevas tuplas modificadas\n")

# 1. Crear nueva tupla con elementos modificados
tupla_original = (1, 2, 3, 4)
print(f"1. Tupla original: {tupla_original}")

# Crear nueva tupla cambiando el primer elemento
tupla_modificada = (10,) + tupla_original[1:]
print(f"   Cambiando primer elemento: {tupla_modificada}")

# Crear nueva tupla cambiando el último elemento
tupla_modificada2 = tupla_original[:-1] + (40,)
print(f"   Cambiando último elemento: {tupla_modificada2}")

# 2. Convertir a lista, modificar, y convertir de vuelta
print(f"\n2. Convertir a lista para modificar:")
tupla_a_lista = list(tupla_original)
print(f"   Tupla convertida a lista: {tupla_a_lista}")
tupla_a_lista[1] = 20  # Modificar elemento
tupla_de_lista = tuple(tupla_a_lista)
print(f"   Lista modificada convertida a tupla: {tupla_de_lista}")

# 3. Concatenar tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(f"\n3. Concatenar tuplas:")
print(f"   Tupla1: {tupla1}")
print(f"   Tupla2: {tupla2}")
print(f"   Concatenada: {tupla_concatenada}")

# 4. Repetir tuplas
tupla_repetida = tupla1 * 3
print(f"\n4. Repetir tuplas:")
print(f"   Tupla original: {tupla1}")
print(f"   Repetida 3 veces: {tupla_repetida}")

# 5. Agregar elementos creando nueva tupla
tupla_agregada = tupla_original + (5, 6)
print(f"\n5. Agregar elementos:")
print(f"   Tupla original: {tupla_original}")
print(f"   Con elementos agregados: {tupla_agregada}")

print("\n💡 RECUERDA: Las tuplas son inmutables por diseño.")
print("   Si necesitas modificar datos frecuentemente, usa listas en su lugar.") 
