class Estudiante:
    def __init__(self, nombre, canet, carrera):
        self.nombre = nombre
        self.canet = canet
        self.carrera = carrera
        self.notas = []  # Lista vacía para almacenar notas
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Canet: {self.canet}")
        print(f"Carrera: {self.carrera}") 
    
    def agregar_nota(self, nota):
        self.notas.append(nota)
        print(f"Nota agregada: {nota}") 
    
    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0
        promedio = sum(self.notas) / len(self.notas)
        print(f"Promedio de notas: {promedio}")
        return promedio 
    
    def aprobado(self, promedio):
        if promedio >= 7.0:
            print("El estudiante ha aprobado.")
        else:
            print("El estudiante no ha aprobado.")

# Crear un estudiante de ejemplo
estudiante1 = Estudiante("Monica perez", "12345", "Ingeniería en Sistemas")
estudiante1.mostrar_informacion()
estudiante1.agregar_nota(8.5)
estudiante1.agregar_nota(9.0)
estudiante1.agregar_nota(7.5)
promedio = estudiante1.calcular_promedio()
estudiante1.aprobado(promedio)


