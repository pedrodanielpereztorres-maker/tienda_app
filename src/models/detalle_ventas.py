from src.db import obtener_conexion


class DetalleVenta:
    def __init__(self, id_detalle, id_venta, id_producto, cantidad, precio_unit, nombre_producto=""):
        self.__id_detalle = id_detalle
        self.__id_venta = id_venta
        self.__id_producto = id_producto
        self.__cantidad = cantidad
        self.__precio_unit = precio_unit
        self.__nombre_producto = nombre_producto

    @property
    def id_detalle(self):
        return self.__id_detalle

    @id_detalle.setter
    def id_detalle(self, value):
        self.__id_detalle = value

    @property
    def id_venta(self):
        return self.__id_venta

    @id_venta.setter
    def id_venta(self, value):
        self.__id_venta = value

    @property
    def id_producto(self):
        return self.__id_producto

    @id_producto.setter
    def id_producto(self, value):
        self.__id_producto = value

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, value):
        self.__cantidad = value

    @property
    def precio_unit(self):
        return self.__precio_unit

    @precio_unit.setter
    def precio_unit(self, value):
        self.__precio_unit = value

    @property
    def nombre_producto(self):
        return self.__nombre_producto

    @nombre_producto.setter
    def nombre_producto(self, value):
        self.__nombre_producto = value

    def __str__(self):
        return "\n".join([
            f"ID Detalle: {self.__id_detalle}",
            f"ID Venta: {self.__id_venta}",
            f"ID Producto: {self.__id_producto}",
            f"Nombre Producto: {self.__nombre_producto}",
            f"Cantidad: {self.__cantidad}",
            f"Precio Unitario: {self.__precio_unit}"
        ])

    @staticmethod
    def obtener_por_venta(id_venta):
        conn = obtener_conexion()
        if conn is None:
            print(
                "No se pudo establecer la conexión para obtener los detalles de la venta.".upper())
            return None
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """SELECT detalle_ventas.id, detalle_ventas.id_venta, detalle_ventas.id_producto,
                            detalle_ventas.cantidad, detalle_ventas.precio_unit, productos.nombre
                            FROM detalle_ventas
                            INNER JOIN productos ON detalle_ventas.id_producto = productos.id
                            WHERE detalle_ventas.id_venta = %s;""",
                        (id_venta,)
                    )
                    filas = cursor.fetchall()
            return [DetalleVenta(*f) for f in filas]
        except Exception as e:
            print(f"Error al obtener detalles de venta: {e}")
            return []
        finally:
            conn.close()
