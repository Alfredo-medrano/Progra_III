"""Este es un progama donde el usuario puede pedir un supermercado mediante una serie de opciones 
donde pueda agregar y entar en diferentes secciones 
"""

# Define la clase Producto para representar los productos con nombre y precio.
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Define la clase Seccion para manejar las secciones del supermercado, que contienen productos.
class Seccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []  # Inicializa una lista vacía de productos.

    def agregar_producto(self, producto):
        self.productos.append(producto)  # Agrega un producto a la lista de productos.

# Define la clase Supermercado para gestionar secciones y compras.
class Supermercado:
    def __init__(self):
        self.secciones = {}  # Inicializa un diccionario vacío para las secciones.
        self.compras = []  # Inicializa una lista vacía para las compras.

    def agregar_seccion(self, seccion):
        self.secciones[seccion.nombre] = seccion  # Agrega una sección al diccionario.

    def agregar_producto_a_seccion(self, nombre_seccion, producto):
        # Añade un producto a una sección específica.
        if nombre_seccion in self.secciones:
            self.secciones[nombre_seccion].agregar_producto(producto)
        else:
            print(f"Sección '{nombre_seccion}' no encontrada.")  # Mensaje de error si la sección no existe.

    def mostrar_secciones(self):
        # Muestra todas las secciones disponibles.
        print("Secciones disponibles:")
        print("-" * 50)
        for i, seccion in enumerate(self.secciones.values()):
            print(f"{i + 1}. {seccion.nombre}")
        print("-" * 50)

    def mostrar_productos(self, nombre_seccion):
        # Muestra todos los productos de una sección específica.
        seccion = self.secciones.get(nombre_seccion)
        if seccion:
            print(f"\nProductos en la sección '{nombre_seccion}':")
            print("-" * 50)
            for i, producto in enumerate(seccion.productos):
                print(f"{i + 1}. {producto.nombre} - ${producto.precio:.2f}")
            print("-" * 50)
        else:
            print(f"Sección '{nombre_seccion}' no encontrada.")  # Mensaje de error si la sección no existe.

    def agregar_producto_a_compras(self, producto):
        self.compras.append(producto)  # Añade un producto a la lista de compras.

    def mostrar_lista_compras(self):
        # Muestra todos los productos en la lista de compras.
        print("\nLista de Compras:")
        print("-" * 50)
        if not self.compras:
            print("No hay productos en la lista de compras.")
        else:
            for producto in self.compras:
                print(f"{producto.nombre} - ${producto.precio:.2f}")
        print("-" * 50)

    def calcular_total_compras(self):
        # Calcula y muestra el total de la compra.
        total = sum(producto.precio for producto in self.compras)
        print("\nTotal de la compra:")
        print("-" * 50)
        print(f"Total: ${total:.2f}")
        print("-" * 50)

# Función principal que maneja la lógica del programa.
def main():
    supermercado = Supermercado()

    # Define las secciones del supermercado.
    secciones = ["Frutas", "Verduras", "Carnes", "Lácteos", "Bebidas"]
    for nombre_seccion in secciones:
        supermercado.agregar_seccion(Seccion(nombre_seccion))

    # Define los productos disponibles.
    productos = [
        Producto("Manzana", 1.50),
        Producto("Pera", 2.00),
        Producto("Tomate", 3.00),
        Producto("Lechuga", 2.50),
        Producto("Pollo", 5.00),
        Producto("Leche", 4.00),
        Producto("Agua", 1.00)
    ]

    # Asocia productos con sus respectivas secciones.
    productos_por_seccion = {
        "Frutas": ["Manzana", "Pera"],
        "Verduras": ["Tomate", "Lechuga"],
        "Carnes": ["Pollo"],
        "Lácteos": ["Leche"],
        "Bebidas": ["Agua"]
    }

    # Añade los productos a las secciones correspondientes.
    for producto in productos:
        for nombre_seccion, nombres_productos in productos_por_seccion.items():
            if producto.nombre in nombres_productos:
                supermercado.agregar_producto_a_seccion(nombre_seccion, producto)

    # Diccionario de funciones para manejar las opciones del menú.
    opciones_menu = {
        '1': lambda: agregar_producto(supermercado, secciones),
        '2': supermercado.mostrar_lista_compras,
        '3': supermercado.calcular_total_compras,
        '4': salir_programa
    }

    # Menú interactivo para el usuario.
    while True:
        print("\n" + "=" * 50)
        print("Menú del Supermercado")
        print("=" * 50)
        print("1. Agregar producto a la lista de compras")
        print("2. Ver lista de compras")
        print("3. Calcular total de la compra")
        print("4. Salir")
        print("=" * 50)
        opcion = input("Selecciona una opción: ")
        print("=" * 50)

        #diccionario de funciones
        accion = opciones_menu.get(opcion, lambda: print("Opción no válida. Inténtalo de nuevo."))
        accion()

# Función para agregar productos a la lista de compras
def agregar_producto(supermercado, secciones):
    supermercado.mostrar_secciones()
    indice_seccion = int(input("Ingrese el número de la sección: ")) - 1
    nombre_seccion = secciones[indice_seccion]
    supermercado.mostrar_productos(nombre_seccion)
    indice_producto = int(input("Ingrese el número del producto: ")) - 1
    producto = supermercado.secciones[nombre_seccion].productos[indice_producto]
    supermercado.agregar_producto_a_compras(producto)
    print(f"\nProducto '{producto.nombre}' agregado a la lista de compras.")

# Función para salir del programa
def salir_programa():
    print("Saliendo del programa...")
    exit()

# Ejecuta la función principal si el script es ejecutado directamente.
if __name__ == "__main__":
    main()
