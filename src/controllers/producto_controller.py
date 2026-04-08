from src.models.producto import Producto


def crear_producto(nombre, precio, stock, categoria_id):
    if not nombre.strip():
        print("El nombre del producto no puede estar vacío.".upper())
        return None
    if precio < 0:
        print("El precio del producto no puede ser negativo.".upper())
        return None
    if stock < 0:
        print("El stock del producto no puede ser negativo.".upper())
        return None
    return Producto.crear_producto(nombre, precio, stock, categoria_id)


def obtener_productos():
    return Producto.obtener_todos()


def obtener_producto_por_id(id_producto):
    if id_producto <= 0:
        print("El ID del producto debe ser un número positivo.".upper())
        return None
    producto = Producto.buscar_por_id(id_producto)
    if producto is None:
        print("No existe un producto con el ID especificado.".upper())
    return producto


def actualizar_stock(id_producto, cantidad):
    if id_producto <= 0:
        print("El ID del producto debe ser un número positivo.".upper())
        return None
    if cantidad <= 0:
        print("La cantidad debe ser mayor que cero.".upper())
        return None
    producto = Producto.buscar_por_id(id_producto)
    if producto is None:
        print("No existe un producto con el ID especificado.".upper())
        return None
    nuevo_stock = producto.stock + cantidad
    if nuevo_stock < 0:
        print("El stock resultante no puede ser negativo.".upper())
        return None
    return Producto.actualizar_stock(id_producto, cantidad)


def eliminar_producto(id_producto):
    if id_producto <= 0:
        print("El ID del producto debe ser un número positivo.".upper())
        return None
    resultado = Producto.eliminar_producto(id_producto)
    if not resultado:
        print("No existe un producto con el ID especificado.".upper())
    return resultado
