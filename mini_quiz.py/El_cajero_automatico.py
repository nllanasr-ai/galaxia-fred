def calcular_billetes(monto):
    
    # Verificar si es múltiplo de 5
    if monto % 5 != 0:
        print("Error: El monto no es múltiplo de 5")
        return None
    
    # Calcular cantidad de billetes
    b200 = monto // 200
    monto = monto % 200
    
    b100 = monto // 100
    monto = monto % 100
    
    b50 = monto // 50
    monto = monto % 50
    
    b20 = monto // 20
    monto = monto % 20
    
    b10 = monto // 10
    monto = monto % 10
    
    b5 = monto // 5
    monto = monto % 5
    
    # Mostrar resultado
    print(f"{b200}x Q200, {b100}x Q100, {b50}x Q50, {b20}x Q20, {b10}x Q10, {b5}x Q5")


# PROBAR CON 470
calcular_billetes(470)