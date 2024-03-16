# Definición de la clase Producto
class Producto:
    def __init__(self, id, nombre, descripcion, cantidad, precio):
        # Inicialización de los atributos de Producto
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

    def obtener_informacion(self):
        # Método para obtener la información del producto como un diccionario
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "cantidad": self.cantidad,
            "precio": self.precio
        }
    
    # Métodos para actualizar los atributos del producto
    def actualizar_nombre(self, nombre):
        self.nombre = nombre
        
    def actualizar_descripcion(self, descripcion):
        self.descripcion = descripcion

    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        self.precio = precio

# Definición de la clase Inventario
class Inventario:
    def __init__(self):
        # Inicialización del inventario como un diccionario vacío
        self.productos = {}

    # Método para agregar un producto al inventario
    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print(f"Producto con id {producto.id} ya existe.")
        else:
            self.productos[producto.id] = producto
            print(f"Producto con id {producto.id} agregado al inventario.")

    # Método para eliminar un producto del inventario
    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print(f"Producto con id {id} eliminado del inventario.")
        else:
            print(f"Producto con id {id} no encontrado en el inventario.")

    # Método para actualizar un producto en el inventario
    def actualizar_producto(self, id, nombre=None, descripcion=None, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if nombre is not None:
                producto.actualizar_nombre(nombre)
            if descripcion is not None:
                producto.actualizar_descripcion(descripcion)
            if cantidad is not None:
                producto.actualizar_cantidad(cantidad)
            if precio is not None:
                producto.actualizar_precio(precio)
            print(f"Producto con id {id} actualizado en el inventario.")
        else:
            print(f"Producto con id {id} no encontrado en el inventario.")

    # Método para obtener la información de un producto en el inventario
    def obtener_informacion_producto(self, id):
        if id in self.productos:
            return self.productos[id].obtener_informacion()
        else:
            return f"Producto con id {id} no encontrado en el inventario."

    # Método para generar un informe del inventario
    def generar_informe(self):
        for producto in self.productos.values():
            print(producto.obtener_informacion())

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("Sistema de Gestión de Inventario")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Mostrar información de un producto")
    print("5. Generar informe del inventario") 
    print("6. Salir")
    return input("Seleccione una opción: ")

# Función para obtener un número entero del usuario
def obtener_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

# Función para obtener un número flotante del usuario
def obtener_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número flotante válido.")

# Función principal del programa
def main():
    inventario = Inventario()  # Creación de una instancia de Inventario

    while True:
        opcion = mostrar_menu()  # Mostrar el menú y obtener la opción del usuario

        # Opciones del menú
        if opcion == '1':
            id = obtener_entero("ID del producto: ")
            nombre = input("Nombre del producto: ")
            descripcion = input("Descripción del producto: ")
            cantidad = obtener_entero("Cantidad: ")
            precio = obtener_flotante("Precio: ")
            producto = Producto(id, nombre, descripcion, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            id = obtener_entero("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == '3':
            id = obtener_entero("ID del producto a actualizar: ")
            nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ")
            descripcion = input("Nueva descripción (dejar en blanco para no cambiar): ")
            cantidad_str = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio_str = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad_str) if cantidad_str.isdigit() else None
            precio = float(precio_str) if precio_str.replace('.', '', 1).isdigit() else None
            inventario.actualizar_producto(id, nombre if nombre else None, descripcion if descripcion else None,
                                            cantidad if cantidad is not None else None, precio if precio is not None else None)
        elif opcion == '4':
            id = obtener_entero("ID del producto a mostrar: ")
            info = inventario.obtener_informacion_producto(id)
            if info:
                print(info)
            else:
                print(f"Producto con id {id} no encontrado.")
        elif opcion == '5':
            inventario.generar_informe()
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
