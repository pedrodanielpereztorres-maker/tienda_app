from src.models.venta import Venta
from src.models.cliente import Cliente


def crear_venta(id_cliente, items):
    if id_cliente <= 0:
        print("El ID del cliente debe ser un número positivo.".upper())
        return None
    cliente = Cliente.obtener_por_id(id_cliente)
    if cliente is None:
        print("No existe un cliente con el ID especificado.".upper())
        return None
    if not items:
        print("La venta debe contener al menos un producto.".upper())
        return None
    return Venta.crear_venta(id_cliente, items)


def obtener_ventas():
    return Venta.obtener_todos()


def obtener_venta_por_id(id_venta):
    if id_venta <= 0:
        print("El ID de la venta debe ser un número positivo.".upper())
        return None
    venta = Venta.buscar_por_id(id_venta)
    if venta is None:
        print("No existe una venta con el ID especificado.".upper())
    return venta
