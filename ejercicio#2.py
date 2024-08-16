class Articulo:
    def __init__(self, nombre, marca, precio_compra):
        self.__nombre = nombre
        self.__marca = marca
        self.__precio_compra = precio_compra
        self.__precio_venta = self.__calcular_precio_venta()

    def __calcular_precio_venta(self):
        return self.__precio_compra * 1.30

    def get_info(self):
        return {
            "Nombre": self.__nombre,
            "Marca": self.__marca,
            "Precio de compra": self.__precio_compra,
            "Precio de venta": self.__precio_venta
        }

class Cuaderno(Articulo):
    def __init__(self, hojas, precio_compra):
        super().__init__("Cuaderno", "HOJITAS", precio_compra)
        self.__hojas = hojas

    def get_info(self):
        info = super().get_info()
        info["Hojas"] = self.__hojas
        return info

class Lapiz(Articulo):
    def __init__(self, tipo, precio_compra):
        super().__init__("Lápiz", "RAYAS", precio_compra)
        self.__tipo = tipo

    def get_info(self):
        info = super().get_info()
        info["Tipo"] = self.__tipo
        return info

class Papeleria:
    def __init__(self):
        self.__articulos = []

    def agregar_articulo(self, articulo):
        self.__articulos.append(articulo)

    def mostrar_articulos(self):
        for articulo in self.__articulos:
            print(articulo.get_info())

papeleria = Papeleria()

while True:
    print("1. Agregar cuaderno")
    print("2. Agregar lápiz")
    print("3. Mostrar artículos")
    print("4. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        hojas = int(input("Ingrese el número de hojas del cuaderno: "))
        precio_compra = float(input("Ingrese el precio de compra del cuaderno: "))
        cuaderno = Cuaderno(hojas, precio_compra)
        papeleria.agregar_articulo(cuaderno)
    elif opcion == "2":
        tipo = input("Ingrese el tipo de lápiz (grafito o colores): ")
        precio_compra = float(input("Ingrese el precio de compra del lápiz: "))
        lapiz = Lapiz(tipo, precio_compra)
        papeleria.agregar_articulo(lapiz)
    elif opcion == "3":
        papeleria.mostrar_articulos()
    elif opcion == "4":
        break
    else:
        print("Opción inválida")

if __name__ == "articulo":
    Articulo()