def calculadora():
    # Mostrar opciones de operación
    print("Selecciona la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    # Obtener entrada del usuario
    opcion = input("Ingresa el número de la operación deseada (1/2/3/4): ")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    # Realizar la operación seleccionada
    if opcion == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif opcion == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif opcion == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif opcion == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: No se puede dividir entre cerso")
    else:
        print("Opción no válida") 
        print("hola")

# Ejecutar la calculadora
calculadora()