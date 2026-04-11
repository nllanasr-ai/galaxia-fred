def validar_password(password):
    
    # Regla 1: Mínimo 8 caracteres
    if len(password) < 8:
        return False
    
    # Regla 2: Al menos una mayúscula
    tiene_mayuscula = False
    for letra in password:
        if letra.isupper():
            tiene_mayuscula = True
            break
    if not tiene_mayuscula:
        return False
    
    # Regla 3: Al menos un dígito
    tiene_numero = False
    for letra in password:
        if letra.isdigit():
            tiene_numero = True
            break
    if not tiene_numero:
        return False
    
    # Regla 4: Al menos un carácter especial (!, @, #, $, %)
    especiales = "!@#$%"
    tiene_especial = False
    for letra in password:
        if letra in especiales:
            tiene_especial = True
            break
    if not tiene_especial:
        return False
    
    # BONUS: No puede tener 3 iguales seguidos
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return False
    
    # Si llegó hasta aquí, TODAS se cumplieron
    return True


# -------------------------------------------------------------------

def diagnosticar_password(password):
    print("Analizando contraseña...")
    
    # Revisar cada regla y decir si falla
    if len(password) < 8:
        print("❌ Falla: Debe tener mínimo 8 caracteres")
        
    tiene_mayuscula = any(c.isupper() for c in password)
    if not tiene_mayuscula:
        print("❌ Falla: Falta una letra mayúscula")
        
    tiene_numero = any(c.isdigit() for c in password)
    if not tiene_numero:
        print("❌ Falla: Falta un número")
        
    especiales = "!@#$%"
    tiene_especial = any(c in especiales for c in password)
    if not tiene_especial:
        print("❌ Falla: Falta un carácter especial (! @ # $ %)")
        
    # Bonus
    tiene_tres_seguidos = False
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            tiene_tres_seguidos = True
            break
    if tiene_tres_seguidos:
        print("❌ Falla: No puede tener 3 caracteres iguales seguidos")
        
    # Si todo salió bien
    if validar_password(password):
        print("✅ La contraseña es VÁLIDA")


# -------------------------------------------------------------------
# ✅ PARA PROBARLO (cambia el texto por la que quieras probar)

# Prueba la validación
print("Resultado validar:", validar_password("MiClave123!"))

# Prueba el diagnóstico
diagnosticar_password("miclave")