class Auto:
    def __init__(self, marca, modelo, año, color, tipo, precio_compra):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__color = color
        self.__tipo = tipo
        self.__precio_compra = precio_compra
        self.__precio_venta = self.__calcular_precio_venta()
        self.__ruedas = 4
        self.__capacidad_pasajeros = 5

    def __calcular_precio_venta(self):
        return self.__precio_compra * 1.4

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

class AutoNacional(Auto):
    def __init__(self, marca, modelo, año, color, precio_compra):
        super().__init__(marca, modelo, año, color, "Nacional", precio_compra)

class AutoImportado(Auto):
    def __init__(self, marca, modelo, año, color, precio_compra):
        super().__init__(marca, modelo, año, color, "Importado", precio_compra)

class Concesionario:
    def __init__(self):
        self.__autos = []

    def agregar_auto(self, auto):
        self.__autos.append(auto)

    def mostrar_autos(self):
        for auto in self.__autos:
            print(auto.get_info())

concesionario = Concesionario()

while True:
    print("1. Agregar auto nacional")
    print("2. Agregar auto importado")
    print("3. Mostrar autos")
    print("4. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        marca = input("Ingrese la marca del auto: ")
        modelo = input("Ingrese el modelo del auto: ")
        año = int(input("Ingrese el año del auto: "))
        color = input("Ingrese el color del auto: ")
        precio_compra = float(input("Ingrese el precio de compra del auto: "))
        auto = AutoNacional(marca, modelo, año, color, precio_compra)
        concesionario.agregar_auto(auto)
    elif opcion == "2":
        marca = input("Ingrese la marca del auto: ")
        modelo = input("Ingrese el modelo del auto: ")
        año = int(input("Ingrese el año del auto: "))
        color = input("Ingrese el color del auto: ")
        precio_compra = float(input("Ingrese el precio de compra del auto: "))
        auto = AutoImportado(marca, modelo, año, color, precio_compra)
        concesionario.agregar_auto(auto)
    elif opcion == "3":
        concesionario.mostrar_autos()
    elif opcion == "4":
        break
    else:
        print("Opción inválida")

if __name__ == "auto":
    Auto()