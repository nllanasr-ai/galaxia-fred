import math 
def fibonacci(n):
    if n < 0:
        return "No se puede calcular la serie de Fibonacci para un número negativo"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
if __name__ == "__main__":
    numero = int(input("Ingrese un número para calcular su Fibonacci: "))
    print(f"El número de Fibonacci en la posición {numero} es: {fibonacci(numero)}")