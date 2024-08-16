# Definición de la clase base Articulo
class Articulo:
    # Método constructor para inicializar un artículo
    def __init__(self, nombre, marca, precio_compra):
        self.__nombre = nombre            # Nombre del artículo
        self.__marca = marca              # Marca del artículo
        self.__precio_compra = precio_compra  # Precio de compra del artículo
        self.__precio_venta = self.__calcular_precio_venta()  # Calcula el precio de venta con un margen del 30%

    # Método privado para calcular el precio de venta (30% sobre el precio de compra)
    def __calcular_precio_venta(self):
        return self.__precio_compra * 1.30

    # Método público para obtener la información del artículo
    def get_info(self):
        return {
            "Nombre": self.__nombre,
            "Marca": self.__marca,
            "Precio de compra": self.__precio_compra,
            "Precio de venta": self.__precio_venta
        }

# Clase Cuaderno que hereda de Articulo
class Cuaderno(Articulo):
    # Método constructor para inicializar un cuaderno
    def __init__(self, hojas, precio_compra):
        super().__init__("Cuaderno", "HOJITAS", precio_compra)  # Se inicializa como un Articulo
        self.__hojas = hojas  # Número de hojas del cuaderno

    # Método para obtener la información del cuaderno, incluyendo el número de hojas
    def get_info(self):
        info = super().get_info()  # Llama al método get_info de la clase padre
        info["Hojas"] = self.__hojas  # Añade el número de hojas al diccionario de información
        return info

# Clase Lapiz que hereda de Articulo
class Lapiz(Articulo):
    # Método constructor para inicializar un lápiz
    def __init__(self, tipo, precio_compra):
        super().__init__("Lápiz", "RAYAS", precio_compra)  # Se inicializa como un Articulo
        self.__tipo = tipo  # Tipo de lápiz (grafito o colores)

    # Método para obtener la información del lápiz, incluyendo el tipo
    def get_info(self):
        info = super().get_info()  # Llama al método get_info de la clase padre
        info["Tipo"] = self.__tipo  # Añade el tipo de lápiz al diccionario de información
        return info

# Clase Papeleria que gestiona una colección de artículos
class Papeleria:
    # Método constructor para inicializar la lista de artículos
    def __init__(self):
        self.__articulos = []  # Lista privada para almacenar los artículos

    # Método para agregar un artículo a la papelería
    def agregar_articulo(self, articulo):
        self.__articulos.append(articulo)  # Añade el artículo a la lista

    # Método para mostrar la información de todos los artículos en la papelería
    def mostrar_articulos(self):
        for articulo in self.__articulos:  # Itera sobre la lista de artículos
            print(articulo.get_info())  # Imprime la información de cada artículo

# Instancia de la clase Papeleria
papeleria = Papeleria()

# Ciclo principal del programa para la interacción con el usuario
while True:
    # Mostrar las opciones disponibles
    print("1. Agregar cuaderno")
    print("2. Agregar lápiz")
    print("3. Mostrar artículos")
    print("4. Salir")
    print("__________________________________")
    
    # Leer la opción seleccionada por el usuario
    opcion = input("Ingrese una opción: ")

    # Lógica para manejar las opciones seleccionadas por el usuario
    if opcion == "1":
        # Si el usuario elige agregar un cuaderno, se le solicita la información
        hojas = int(input("Ingrese el número de hojas del cuaderno: "))
        precio_compra = float(input("Ingrese el precio de compra del cuaderno: "))
        cuaderno = Cuaderno(hojas, precio_compra)  # Se crea una instancia de Cuaderno
        papeleria.agregar_articulo(cuaderno)  # Se agrega el cuaderno a la papelería
    elif opcion == "2":
        # Si el usuario elige agregar un lápiz, se le solicita la información
        tipo = input("Ingrese el tipo de lápiz (grafito o colores): ")
        precio_compra = float(input("Ingrese el precio de compra del lápiz: "))
        lapiz = Lapiz(tipo, precio_compra)  # Se crea una instancia de Lapiz
        papeleria.agregar_articulo(lapiz)  # Se agrega el lápiz a la papelería
    elif opcion == "3":
        # Si el usuario elige mostrar los artículos, se llama al método correspondiente
        papeleria.mostrar_articulos()
    elif opcion == "4":
        # Si el usuario elige salir, se rompe el ciclo y el programa termina
        break
    else:
        # Si el usuario ingresa una opción inválida, se muestra un mensaje de error
        print("Opción inválida")
