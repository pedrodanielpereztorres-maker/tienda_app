from src.controllers.venta_controller import crear_venta, obtener_ventas, obtener_venta_por_id
from src.models.detalle_ventas import DetalleVenta
from src.utils import leer_entero


def venta_menu():
    while True:
        print("""
    MENÚ VENTAS:
        1. Crear venta
        2. Listar ventas
        3. Buscar venta por ID
        4. Detalles de venta por ID
        0. Volver al menú principal
        """.title())
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            print("\n--- CREAR VENTA ---")
            id_cliente = leer_entero("Ingrese el ID del cliente: ")
            items = []
            while True:
                id_producto = leer_entero(
                    "Ingrese el ID del producto (0 para terminar): ")
                if id_producto == 0:
                    break
                cantidad = leer_entero("Ingrese la cantidad: ")
                items.append(
                    {'id_producto': id_producto, 'cantidad': cantidad})
            crear_venta(id_cliente, items)
        elif opcion == "2":
            print("\nlistar ventas".title())
            ventas = obtener_ventas()
            for venta in ventas:
                print(venta)
        elif opcion == "3":
            print("\n--- BUSCAR VENTA ---")
            id_venta = leer_entero("Ingrese el ID de la venta: ")
            venta = obtener_venta_por_id(id_venta)
            if venta:
                print(venta)
            else:
                print("Venta no encontrada.")
        elif opcion == "4":
            print("\n--- DETALLES DE VENTA ---")
            id_venta = leer_entero("Ingrese el ID de la venta: ")
            venta = obtener_venta_por_id(id_venta)
            if venta:
                print(venta)
                print("\nProductos:")
                detalles = DetalleVenta.obtener_por_venta(id_venta)
                if not detalles:
                    print("  No hay detalles para esta venta.")
                else:
                    for d in detalles:
                        print(d)
            else:
                print("Venta no encontrada.")
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
