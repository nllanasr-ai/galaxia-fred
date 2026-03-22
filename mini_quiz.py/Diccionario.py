#Diccionario personal 
from turtle import update


diccionario ={ "Nombre": "Nanci", "Edad": 58, "Ciudad": "Ciudad de Guatemala", "Lenguaje_favorito": "Python" } 
diccionario.update({"universidad": "San Pablo"})
diccionario["Edad"] = 18 
print(diccionario) 
print(diccionario["Nombre"]) 
print(diccionario["Edad"]) 
print(diccionario["Ciudad"])
print(diccionario["Lenguaje_favorito"]) 
clave = input("Ingresa la clave que deseas consultar: ") 
if clave in diccionario: 
    print(f"El valor de '{clave}' es: {diccionario[clave]}")
else:
    print(f"La clave '{clave}' no existe en el diccionario.")

# Iterar con .items() e imprimir cada par clave-valor
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")

# Verificar si "email" existe con "in"
if "email" in diccionario:
    print("La clave 'email' existe.")
else:
    print("La clave 'email' no existe.")

# Usar .get() para acceder a "telefono" sin error
telefono = diccionario.get("telefono", "3176 4802")
print(f"Teléfono: {telefono}") 
print("Valores del diccionario:")
for valor in diccionario.values():
    print(f" - {valor}") 
    diccionario.update({"Profesión": "Estudiante"})
print("Diccionario actualizado:", diccionario) 

