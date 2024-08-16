# Definición de la clase Perro
class Perro:
    # Método constructor de la clase Perro
    def __init__(self, nombre, edad, peso, raza, color, estado="NO ATENDIDO"):
        # Atributos privados de la clase
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso
        self.__raza = raza
        self.__color = color
        self.__estado = estado
        self.__tipo = self.__determinar_tipo()  # Determina si el perro es pequeño o grande según su peso

    # Método privado para determinar el tipo de perro según su peso
    def __determinar_tipo(self):
        if self.__peso < 10:  # Si el peso es menor a 10 kg
            return "Perro Pequeño"
        else:  # Si el peso es igual o mayor a 10 kg
            return "Perro Grande"

    # Método público para obtener la información del perro en forma de diccionario
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

    # Método para registrar al perro, cambiando su estado a "ATENDIDO"
    def registrar(self):
        self.__estado = "ATENDIDO"

# Definición de la clase Veterinaria
class Veterinaria:
    # Método constructor de la clase Veterinaria
    def __init__(self):
        self.__perros = []  # Lista privada que almacenará los perros agregados

    # Método para agregar un perro a la lista de la veterinaria
    def agregar_perro(self, perro):
        self.__perros.append(perro)  # Se añade el perro a la lista
        perro.registrar()  # Se marca el perro como "ATENDIDO"

    # Método para mostrar la información de todos los perros en la lista
    def mostrar_perros(self):
        for perro in self.__perros:  # Itera sobre cada perro en la lista
            print(perro.get_info())  # Imprime la información del perro

# Creación de una instancia de la clase Veterinaria
veterinaria = Veterinaria()

# Ciclo principal del programa para la interacción con el usuario
while True:
    # Mostrar las opciones disponibles
    print("1. Agregar perro")
    print("2. Mostrar perros")
    print("3. Salir")
    print("------------------------------")
    
    # Leer la opción seleccionada por el usuario
    opcion = input("Ingrese una opción: ")

    # Lógica para manejar las opciones seleccionadas por el usuario
    if opcion == "1":
        # Si el usuario elige agregar un perro, se le solicita la información del perro
        nombre = input("Ingrese el nombre del perro: ")
        edad = int(input("Ingrese la edad del perro: "))
        peso = float(input("Ingrese el peso del perro: "))
        raza = input("Ingrese la raza del perro: ")
        color = input("Ingrese el color del perro: ")
        
        # Se crea una instancia de la clase Perro con los datos ingresados
        perro = Perro(nombre, edad, peso, raza, color)
        
        # Se agrega el perro a la veterinaria
        veterinaria.agregar_perro(perro)
    elif opcion == "2":
        # Si el usuario elige mostrar los perros, se llama al método correspondiente
        veterinaria.mostrar_perros()
    elif opcion == "3":
        # Si el usuario elige salir, se rompe el ciclo y el programa termina
        break
    else:
        # Si el usuario ingresa una opción inválida, se muestra un mensaje de error
        print("Opción inválida")
