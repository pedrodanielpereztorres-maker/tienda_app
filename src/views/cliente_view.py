from src.controllers.cliente_controller import crear_cliente, obtener_clientes, obtener_cliente_por_id, eliminar_cliente
from src.utils import leer_entero


def cliente_menu():
    while True:
        print("""
    MENÚ CLIENTES:
        1. Crear cliente
        2. Listar clientes
        3. Buscar cliente por ID
        4. Eliminar cliente
        0. Volver al menú principal
        """.title())
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            print("\ncrear cliente".title())
            nombre = input("Ingrese el nombre del cliente: ")
            email = input("Ingrese el email del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            crear_cliente(nombre, email, telefono)
        elif opcion == "2":
            print("\nlistar clientes".title())
            clientes = obtener_clientes()
            for cliente in clientes:
                print(cliente)
        elif opcion == "3":
            print("\nbuscar cliente por id".title())
            id_cliente = leer_entero("Ingrese el ID del cliente: ")
            cliente = obtener_cliente_por_id(id_cliente)
            if cliente:
                print(cliente)
        elif opcion == "4":
            print("\neliminar cliente".title())
            id_cliente = leer_entero("Ingrese el ID del cliente a eliminar: ")
            eliminar_cliente(id_cliente)
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
