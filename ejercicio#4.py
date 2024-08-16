class DispositivoElectronico:
    def __init__(self, tipo, pantalla, memoria, procesador, camara, precio_compra):
        self.__tipo = tipo
        self.__pantalla = pantalla
        self.__memoria = memoria
        self.__procesador = procesador
        self.__camara = camara
        self.__precio_compra = precio_compra
        self.__precio_venta = self.__calcular_precio_venta()
        self.__marca = "PHR"
        self.__importado = True

    def __calcular_precio_venta(self):
        return self.__precio_compra * 1.7

    def get_info(self):
        return {
            "Tipo": self.__tipo,
            "Pantalla": self.__pantalla,
            "Memoria": self.__memoria,
            "Procesador": self.__procesador,
            "Cámara": self.__camara,
            "Precio de compra": self.__precio_compra,
            "Precio de venta": self.__precio_venta,
            "Marca": self.__marca,
            "Importado": self.__importado
        }

class Celular(DispositivoElectronico):
    def __init__(self, pantalla, memoria, procesador, camara, precio_compra):
        super().__init__("Celular", pantalla, memoria, procesador, camara, precio_compra)

class Tablet(DispositivoElectronico):
    def __init__(self, pantalla, memoria, procesador, camara, precio_compra):
        super().__init__("Tablet", pantalla, memoria, procesador, camara, precio_compra)

class Portatil(DispositivoElectronico):
    def __init__(self, pantalla, memoria, procesador, camara, precio_compra):
        super().__init__("Portátil", pantalla, memoria, procesador, camara, precio_compra)

class Almacen:
    def __init__(self):
        self.__dispositivos = []

    def agregar_dispositivo(self, dispositivo):
        self.__dispositivos.append(dispositivo)

    def mostrar_dispositivos(self):
        for dispositivo in self.__dispositivos:
            print(dispositivo.get_info())

almacen = Almacen()

while True:
    print("1. Agregar celular")
    print("2. Agregar tablet")
    print("3. Agregar portátil")
    print("4. Mostrar dispositivos")
    print("5. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        pantalla = input("Ingrese la pantalla del celular: ")
        memoria = input("Ingrese la memoria del celular: ")
        procesador = input("Ingrese el procesador del celular: ")
        camara = input("Ingrese la cámara del celular: ")
        precio_compra = float(input("Ingrese el precio de compra del celular: "))
        celular = Celular(pantalla, memoria, procesador, camara, precio_compra)
        almacen.agregar_dispositivo(celular)
    elif opcion == "2":
        pantalla = input("Ingrese la pantalla del tablet: ")
        memoria = input("Ingrese la memoria del tablet: ")
        procesador = input("Ingrese el procesador del tablet: ")
        camara = input("Ingrese la cámara del tablet: ")
        precio_compra = float(input("Ingrese el precio de compra del tablet: "))
        tablet = Tablet(pantalla, memoria, procesador, camara, precio_compra)
        almacen.agregar_dispositivo(tablet)
    elif opcion == "3":
        pantalla = input("Ingrese la pantalla del portátil: ")
        memoria = input("Ingrese la memoria del portátil: ")
        procesador = input("Ingrese el procesador del portátil: ")
        camara = input("Ingrese la cámara del portátil: ")
        precio_compra = float(input("Ingrese el precio de compra del portátil: "))
        portatil = Portatil(pantalla, memoria, procesador, camara, precio_compra)
        almacen.agregar_dispositivo(portatil)
    elif opcion == "4":
        almacen.mostrar_dispositivos()
    elif opcion == "5":
        break
    else:
        print("Opción inválida")

if __name__ == "dispositivoelectronico":
    DispositivoElectronico()