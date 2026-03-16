import math

def area_circulo(radio):
    return math.pi * radio**2

if __name__ == "__main__":
    r = float(input("Radio: "))
    print("Área:", area_circulo(r)) 
