# Lista para guardar el historial (Bonus)
historial = []

# 1. Calcular propina
def calcular_propina(subtotal, porcentaje):
    return subtotal * (porcentaje / 100)

# 2. Calcular total
def calcular_total(subtotal, propina):
    return subtotal + propina

# 3. Dividir cuenta
def dividir_cuenta(total, personas):
    if personas <= 0:
        return "Error: Número de personas inválido"
    return total / personas

# 4. Aplicar descuento
def aplicar_descuento(subtotal, descuento_pct):
    descuento = subtotal * (descuento_pct / 100)
    return subtotal - descuento

# 5. Mostrar menú
def mostrar_menu():
    print("\n===== CALCULADORA DE PROPINAS =====")
    print("1. Calcular propina")
    print("2. Dividir cuenta entre personas")
    print("3. Aplicar descuento + propina")
    print("4. Resumen de operaciones")
    print("5. Salir")
    print("------------------------------------")

# --- FUNCIÓN PRINCIPAL ---
def main():
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("❌ Error: Debes escribir un número.")
            input("Presiona Enter para continuar...")
            continue

        # OPCIÓN 1: CALCULAR PROPINA
        if opcion == 1:
            try:
                subtotal = float(input("Ingresa el subtotal: Q"))
                print("Sugerencias: 10%, 15%, 20%")
                porcentaje = float(input("Ingresa el porcentaje de propina: "))
                
                propina = calcular_propina(subtotal, porcentaje)
                total = calcular_total(subtotal, propina)
                
                print(f"\n💸 Propina: Q{propina:.2f}")
                print(f"🧾 Total a pagar: Q{total:.2f}")
                
                # Guardar en historial
                historial.append(f"Propina {porcentaje}%: Subtotal Q{subtotal:.2f} -> Total Q{total:.2f}")
                
            except ValueError:
                print("❌ Error: Ingresa valores numéricos válidos.")
            input("\nPresiona Enter para continuar...")

        # OPCIÓN 2: DIVIDIR CUENTA
        elif opcion == 2:
            try:
                total = float(input("Ingresa el total a pagar: Q"))
                personas = int(input("¿Entre cuántas personas se divide? "))
                
                resultado = dividir_cuenta(total, personas)
                print(f"\n👥 Cada persona paga: {resultado}")
                
                historial.append(f"División: Total Q{total:.2f} entre {personas} personas -> Q{resultado:.2f}")
                
            except ValueError:
                print("❌ Error: Ingresa valores válidos.")
            input("\nPresiona Enter para continuar...")

        # OPCIÓN 3: DESCUENTO + PROPINA
        elif opcion == 3:
            try:
                subtotal = float(input("Ingresa el subtotal: Q"))
                descuento = float(input("Ingresa porcentaje de descuento: "))
                porcentaje_propina = float(input("Ingresa porcentaje de propina: "))
                
                subtotal_con_dto = aplicar_descuento(subtotal, descuento)
                propina = calcular_propina(subtotal_con_dto, porcentaje_propina)
                total_final = calcular_total(subtotal_con_dto, propina)
                
                print(f"\n📉 Subtotal con descuento: Q{subtotal_con_dto:.2f}")
                print(f"💸 Propina: Q{propina:.2f}")
                print(f"🧾 Total final: Q{total_final:.2f}")
                
                historial.append(f"Descuento {descuento}% + Propina {porcentaje_propina}%: Total Q{total_final:.2f}")
                
            except ValueError:
                print("❌ Error: Ingresa valores válidos.")
            input("\nPresiona Enter para continuar...")

        # OPCIÓN 4: RESUMEN (BONUS)
        elif opcion == 4:
            print("\n📜 === HISTORIAL DE OPERACIONES ===")
            if not historial:
                print("Aún no se han realizado operaciones.")
            else:
                for i, operacion in enumerate(historial, 1):
                    print(f"{i}. {operacion}")
            input("\nPresiona Enter para continuar...")

        # OPCIÓN 5: SALIR
        elif opcion == 5:
            print("👋 Saliendo del programa... ¡Hasta luego!")
            break

        # OPCIÓN INVÁLIDA
        else:
            print("❌ Opción no válida, intenta de nuevo.")
            input("Presiona Enter para continuar...")


# ✅ EJECUTAR PROGRAMA
main()