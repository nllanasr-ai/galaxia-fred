import math 
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True 
if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    if es_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.") 