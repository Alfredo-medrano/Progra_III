class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Seccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

class Supermercado:
    def __init__(self):
        self.secciones = {}
        self.compras = []

    def agregar_seccion(self, seccion):
        self.secciones[seccion.nombre] = seccion

    def agregar_producto_a_seccion(self, nombre_seccion, producto):
        if nombre_seccion in self.secciones:
            self.secciones[nombre_seccion].agregar_producto(producto)
        else:
            print(f"Sección '{nombre_seccion}' no encontrada.")

    def mostrar_secciones(self):
        for i, seccion in enumerate(self.secciones.values()):
            print(f"{i + 1}. {seccion.nombre}")

    def mostrar_productos(self, nombre_seccion):
        seccion = self.secciones.get(nombre_seccion)
        if seccion:
            for i, producto in enumerate(seccion.productos):
                print(f"{i + 1}. {producto.nombre} - ${producto.precio:.2f}")
        else:
            print(f"Sección '{nombre_seccion}' no encontrada.")

    def agregar_producto_a_compras(self, producto):
        self.compras.append(producto)

    def mostrar_lista_compras(self):
        if not self.compras:
            print("No hay productos en la lista de compras.")
        else:
            for producto in self.compras:
                print(f"{producto.nombre} - ${producto.precio:.2f}")

    def calcular_total_compras(self):
        total = sum(producto.precio for producto in self.compras)
        print(f"Total de la compra: ${total:.2f}")
        print("__________________________________________________________")

def main():
    supermercado = Supermercado()

    secciones = ["Frutas", "Verduras", "Carnes", "Lácteos", "Bebidas"]
    for nombre_seccion in secciones:
        supermercado.agregar_seccion(Seccion(nombre_seccion))

    productos = [
        Producto("Manzana", 1.50),
        Producto("Pera", 2.00),
        Producto("Tomate", 3.00),
        Producto("Lechuga", 2.50),
        Producto("Pollo", 5.00),
        Producto("Leche", 4.00),
        Producto("Agua", 1.00)
    ]

    productos_por_seccion = {
        "Frutas": ["Manzana", "Pera"],
        "Verduras": ["Tomate", "Lechuga"],
        "Carnes": ["Pollo"],
        "Lácteos": ["Leche"],
        "Bebidas": ["Agua"]
    }

    for producto in productos:
        for nombre_seccion, nombres_productos in productos_por_seccion.items():
            if producto.nombre in nombres_productos:
                supermercado.agregar_producto_a_seccion(nombre_seccion, producto)

    while True:
        print("\n1. Agregar producto a la lista de compras")
        print("2. Ver lista de compras")
        print("3. Calcular total de la compra")
        print("4. Salir")
        print("-------------------------------------------------")
        opcion = input("Selecciona una opción: ")
        print("-------------------------------------------------")
        if opcion == '1':
            print("Secciones disponibles:")
            supermercado.mostrar_secciones()
            indice_seccion = int(input("Ingrese el número de la sección: ")) - 1
            nombre_seccion = secciones[indice_seccion]
            print(f"Productos disponibles en la sección {nombre_seccion}:")
            supermercado.mostrar_productos(nombre_seccion)
            indice_producto = int(input("Ingrese el número del producto: ")) - 1
            producto = supermercado.secciones[nombre_seccion].productos[indice_producto]
            supermercado.agregar_producto_a_compras(producto)
            print(f"Producto '{producto.nombre}' agregado a la lista de compras.")

        elif opcion == '2':
            supermercado.mostrar_lista_compras()

        elif opcion == '3':
            supermercado.calcular_total_compras()

        elif opcion == '4':
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
