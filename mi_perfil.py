# miperfil.py

def crear_perfil():
    print("=== Creación de Mi Perfil ===")

    nombre = input("Nombre: ")
    edad = input("Edad: ")
    ciudad = input("Ciudad: ")
    hobby = input("Hobby favorito: ")

    perfil = {
        "Nombre": nombre,
        "Edad": edad,
        "Ciudad": ciudad,
        "Hobby": hobby
    }

    return perfil


def mostrar_perfil(perfil):
    print("\n=== Mi Perfil ===")
    for clave, valor in perfil.items():
        print(f"{clave}: {valor}")


# Programa principal
if __name__ == "__main__":
    mi_perfil = crear_perfil()
    mostrar_perfil(mi_perfil)


