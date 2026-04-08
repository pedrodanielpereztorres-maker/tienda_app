from src.controllers.producto_controller import crear_producto, obtener_productos, obtener_producto_por_id, actualizar_stock, eliminar_producto
from src.utils import leer_entero, leer_float


def producto_menu():
    while True:
        print("""
    MENÚ PRODUCTOS:
        1. Crear producto
        2. Listar productos
        3. Buscar producto por ID
        4. Actualizar stock
        5. Eliminar producto
        0. Volver al menú principal
        """.title())
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            print("\ncrear producto".title())
            nombre = input("Ingrese el nombre del producto: ")
            precio = leer_float("Ingrese el precio del producto: ")
            stock = leer_entero("Ingrese el stock inicial: ")
            categoria_id = leer_entero("Ingrese el ID de la categoría: ")
            crear_producto(nombre, precio, stock, categoria_id)
        elif opcion == "2":
            print("\nlistar productos".title())
            productos = obtener_productos()
            for producto in productos:
                print(producto)
        elif opcion == "3":
            print("\nbuscar producto por id".title())
            id_producto = leer_entero("Ingrese el ID del producto: ")
            producto = obtener_producto_por_id(id_producto)
            if producto:
                print(producto)
        elif opcion == "4":
            print("\n--- ACTUALIZAR STOCK (Suma) ---")
            id_producto = leer_entero("Ingrese el ID del producto: ")
            cantidad = leer_entero(
                "Ingrese la cantidad a añadir al stock actual: ")
            actualizar_stock(id_producto, cantidad)
        elif opcion == "5":
            print("\neliminar producto".title())
            id_producto = leer_entero(
                "Ingrese el ID del producto a eliminar: ")
            eliminar_producto(id_producto)
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
