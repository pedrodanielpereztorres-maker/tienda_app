from src.db import init_db
from src.views.categoria_view import categoria_menu
from src.views.cliente_view import cliente_menu
from src.views.producto_view import producto_menu
from src.views.venta_view import venta_menu


def main():
    init_db()
    while True:
        print("""
        TIENDA APP:
        1. Categorías
        2. Clientes
        3. Productos
        4. Ventas
        5. Salir
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            categoria_menu()
        elif opcion == '2':
            cliente_menu()
        elif opcion == '3':
            producto_menu()
        elif opcion == '4':
            venta_menu()
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente nuevamente.".upper())


if __name__ == "__main__":
    main()
