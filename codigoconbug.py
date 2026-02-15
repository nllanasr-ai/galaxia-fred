def calcular_area_triangulo(base, altura):
    # Bug: Fórmula incorrecta (falta dividir entre 2)
    area = base * altura
    return area

if _name_ == "_main_":
    b = 5
    h = 3
    resultado = calcular_area_triangulo(b, h)
    print(f"El área del triángulo es: {resultado}")
    # Print de debug temporal
    print(f"Base: {b}, Altura: {h}, Cálculo realizado: {b} * {h}")