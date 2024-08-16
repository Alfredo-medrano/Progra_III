# Definición de la clase base Auto
class Auto:
    # Método constructor para inicializar un auto
    def __init__(self, marca, modelo, año, color, tipo, precio_compra):
        self.__marca = marca                
        self.__modelo = modelo              
        self.__año = año                    
        self.__color = color                
        self.__tipo = tipo                  
        self.__precio_compra = precio_compra  
        self.__precio_venta = self.__calcular_precio_venta()  # Calcula el precio de venta con un margen del 40%
        self.__ruedas = 4                   
        self.__capacidad_pasajeros = 5      

    # Método privado para calcular el precio de venta (40% sobre el precio de compra)
    def __calcular_precio_venta(self):
        return self.__precio_compra * 1.4

    # Método público para obtener la información del auto en forma de diccionario
    def get_info(self):
        return {
            "Marca": self.__marca,
            "Modelo": self.__modelo,
            "Año": self.__año,
            "Color": self.__color,
            "Tipo": self.__tipo,
            "Precio de compra": self.__precio_compra,
            "Precio de venta": self.__precio_venta,
            "Ruedas": self.__ruedas,
            "Capacidad de pasajeros": self.__capacidad_pasajeros
        }

# Clase AutoNacional que hereda de Auto
class AutoNacional(Auto):
    # Método constructor para inicializar un auto nacional
    def __init__(self, marca, modelo, año, color, precio_compra):
        super().__init__(marca, modelo, año, color, "Nacional", precio_compra)  # Se inicializa como un Auto nacional

# Clase AutoImportado que hereda de Auto
class AutoImportado(Auto):
    # Método constructor para inicializar un auto importado
    def __init__(self, marca, modelo, año, color, precio_compra):
        super().__init__(marca, modelo, año, color, "Importado", precio_compra)  # Se inicializa como un Auto importado

# Clase Concesionario que gestiona una colección de autos
class Concesionario:
    # Método constructor para inicializar la lista de autos
    def __init__(self):
        self.__autos = []  # Lista privada para almacenar los autos

    # Método para agregar un auto a la lista del concesionario
    def agregar_auto(self, auto):
        self.__autos.append(auto)  # Añade el auto a la lista

    # Método para mostrar la información de todos los autos en el concesionario
    def mostrar_autos(self):
        for auto in self.__autos:  # Itera sobre la lista de autos
            print(auto.get_info())  # Imprime la información de cada auto

# Instancia de la clase Concesionario
concesionario = Concesionario()

# Ciclo principal del programa para la interacción con el usuario
while True:
    # Mostrar las opciones disponibles
    print("1. Agregar auto nacional")
    print("2. Agregar auto importado")
    print("3. Mostrar autos")
    print("4. Salir")
    print("********************************")
    
    # Leer la opción seleccionada por el usuario
    opcion = input("Ingrese una opción: ")

    # Lógica para manejar las opciones seleccionadas por el usuario
    if opcion == "1":
        # Si el usuario elige agregar un auto nacional, se le solicita la información
        marca = input("Ingrese la marca del auto: ")
        modelo = input("Ingrese el modelo del auto: ")
        año = int(input("Ingrese el año del auto: "))
        color = input("Ingrese el color del auto: ")
        precio_compra = float(input("Ingrese el precio de compra del auto: "))
        auto = AutoNacional(marca, modelo, año, color, precio_compra)  # Se crea una instancia de AutoNacional
        concesionario.agregar_auto(auto)  # Se agrega el auto al concesionario
    elif opcion == "2":
        # Si el usuario elige agregar un auto importado, se le solicita la información
        marca = input("Ingrese la marca del auto: ")
        modelo = input("Ingrese el modelo del auto: ")
        año = int(input("Ingrese el año del auto: "))
        color = input("Ingrese el color del auto: ")
        precio_compra = float(input("Ingrese el precio de compra del auto: "))
        auto = AutoImportado(marca, modelo, año, color, precio_compra)  # Se crea una instancia de AutoImportado
        concesionario.agregar_auto(auto)  # Se agrega el auto al concesionario
    elif opcion == "3":
        # Si el usuario elige mostrar los autos, se llama al método correspondiente
        concesionario.mostrar_autos()
    elif opcion == "4":
        # Si el usuario elige salir, se rompe el ciclo y el programa termina
        break
    else:
        # Si el usuario ingresa una opción inválida, se muestra un mensaje de error
        print("Opción inválida")

