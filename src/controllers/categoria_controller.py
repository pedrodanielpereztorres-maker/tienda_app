from src.models.categoria import Categoria


def crear_categoria(nombre, descripcion):
    if not nombre.strip():
        print("El nombre de la categoría no puede estar vacío.".upper())
        return None
    return Categoria.crear_categoria(nombre, descripcion)


def obtener_categorias():
    return Categoria.obtener_todas()


def obtener_categoria_por_id(id_categoria):
    if id_categoria <= 0:
        print("El ID de la categoría debe ser un número positivo.".upper())
        return None
    categoria = Categoria.obtener_por_id(id_categoria)
    if categoria is None:
        print("No existe una categoría con el ID especificado.".upper())
    return categoria


def eliminar_categoria(id_categoria):
    if id_categoria <= 0:
        print("El ID de la categoría debe ser un número positivo.".upper())
        return None
    resultado = Categoria.eliminar_categoria(id_categoria)
    if not resultado:
        print("No existe una categoría con el ID especificado.".upper())
    return resultado
