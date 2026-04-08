from src.controllers.categoria_controller import crear_categoria, obtener_categorias, obtener_categoria_por_id, eliminar_categoria
from src.utils import leer_entero


def categoria_menu():

    while True:
        print("""
    MENÚ CATEGORÍAS:
      1. Crear categoría
      2. Listar categorías
      3. Buscar categoría por ID
      4. Eliminar categoría
      0. Volver al menú principal
      """.title())
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            print("\ncrear categoria".title())
            nombre = input("Ingrese el nombre de la categoría: ")
            descripcion = input("Ingrese la descripción de la categoría: ")
            crear_categoria(nombre, descripcion)

        elif opcion == "2":
            print("\nlistar categorias".title())
            categorias = obtener_categorias()
            for categoria in categorias:
                print(categoria)
        elif opcion == "3":
            print("\nbuscar categoria por id".title())
            id_categoria = leer_entero("Ingrese el ID de la categoría: ")
            categoria = obtener_categoria_por_id(id_categoria)
            if categoria:
                print(categoria)
        elif opcion == "4":
            print("\neliminar categoria".title())
            id_categoria = leer_entero(
                "Ingrese el ID de la categoría a eliminar: ")
            resultado = eliminar_categoria(id_categoria)
            if resultado:
                print("Categoría eliminada exitosamente.".upper())
        elif opcion == "0":
            print("Volviendo al menú principal...".upper())
            break
