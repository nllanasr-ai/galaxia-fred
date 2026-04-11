# --- FUNCIONES BÁSICAS ---

def celsius_a_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def celsius_a_kelvin(c):
    return c + 273.15

# --- BONUS: Rankine ---
def fahrenheit_a_rankine(f):
    return f + 459.67


# --- FUNCIÓN PRINCIPAL ---

def convertir(valor, origen, destino):
    
    # Primero convertimos todo a Celsius como punto medio
    if origen == "C":
        c = valor
    elif origen == "F":
        c = fahrenheit_a_celsius(valor)
    elif origen == "K":
        c = valor - 273.15
    elif origen == "R": # Bonus
        c = fahrenheit_a_celsius(valor - 459.67)
    else:
        # Origen no válido
        return None
    
    # Ahora convertimos de Celsius al destino
    if destino == "C":
        return c
    elif destino == "F":
        return celsius_a_fahrenheit(c)
    elif destino == "K":
        return celsius_a_kelvin(c)
    elif destino == "R": # Bonus
        return celsius_a_fahrenheit(c) + 459.67
    else:
        # Destino no válido
        return None


# --- PROBAR EL PROGRAMA ---

# Ejemplo: Convertir 100 C a F
print(convertir(100, "C", "F"))

# Ejemplo: Convertir 32 F a C
print(convertir(32, "F", "C"))

# Ejemplo Bonus: Convertir 212 F a Rankine
print(convertir(212, "F", "R"))