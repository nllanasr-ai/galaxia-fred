def calcular_area_triangulo(base, altura):
    # Fórmula correcta: (base * altura) / 2
    area = (base * altura) / 2
    return area

if __name__ == "_main_":
    b = 5
    h = 3
    resultado = calcular_area_triangulo(b, h)
    print(f"El area del triangulo es: {resultado}") 