class Perro:
    def __init__(self, nombre, edad, peso, raza, color, estado="NO ATENDIDO"):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso
        self.__raza = raza
        self.__color = color
        self.__estado = estado
        self.__tipo = self.__determinar_tipo()

    def __determinar_tipo(self):
        if self.__peso < 10:
            return "Perro Pequeño"
        else:
            return "Perro Grande"

    def get_info(self):
        return {
            "Nombre": self.__nombre,
            "Edad": self.__edad,
            "Peso": self.__peso,
            "Raza": self.__raza,
            "Color": self.__color,
            "Estado": self.__estado,
            "Tipo": self.__tipo
        }

    def registrar(self):
        self.__estado = "ATENDIDO"

class Veterinaria:
    def __init__(self):
        self.__perros = []

    def agregar_perro(self, perro):
        self.__perros.append(perro)
        perro.registrar()

    def mostrar_perros(self):
        for perro in self.__perros:
            print(perro.get_info())

veterinaria = Veterinaria()

while True:
    print("1. Agregar perro")
    print("2. Mostrar perros")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del perro: ")
        edad = int(input("Ingrese la edad del perro: "))
        peso = float(input("Ingrese el peso del perro: "))
        raza = input("Ingrese la raza del perro: ")
        color = input("Ingrese el color del perro: ")
        perro = Perro(nombre, edad, peso, raza, color)
        veterinaria.agregar_perro(perro)
    elif opcion == "2":
        veterinaria.mostrar_perros()
    elif opcion == "3":
        break
    else:
        print("Opción inválida")

if __name__ == "perro":
  perro()