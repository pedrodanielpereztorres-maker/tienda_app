from src.db import obtener_conexion
from datetime import date


class Venta:
    def __init__(self, id_venta, id_cliente, total, fecha, nombre_cliente=""):
        self.__id_venta = id_venta
        self.__id_cliente = id_cliente
        self.__total = total
        self.__fecha = fecha
        self.__nombre_cliente = nombre_cliente

    @property
    def id_venta(self):
        return self.__id_venta

    @id_venta.setter
    def id_venta(self, value):
        self.__id_venta = value

    @property
    def id_cliente(self):
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, value):
        self.__id_cliente = value

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, value):
        self.__total = value

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, value):
        self.__fecha = value

    @property
    def nombre_cliente(self):
        return self.__nombre_cliente

    @nombre_cliente.setter
    def nombre_cliente(self, value):
        self.__nombre_cliente = value

    def __str__(self):
        fecha_arreglada = self.__fecha.strftime("%d/%m/%Y")
        return "\n".join([
            f"ID Venta: {self.__id_venta}",
            f"ID Cliente: {self.__id_cliente}",
            f"Nombre Cliente: {self.__nombre_cliente}",
            f"Total: {self.__total}",
            f"Fecha: {fecha_arreglada}"
        ])

    @staticmethod
    def crear_venta(id_cliente, items):
        conn = obtener_conexion()
        if conn is None:
            print("No se pudo establecer la conexión para crear la venta.".upper())
            return None
        id_venta = None
        fecha_hoy = date.today()
        try:
            with conn:
                with conn.cursor() as cursor:
                    total = 0
                    detalles = []
                    for item in items:
                        cursor.execute(
                            "SELECT precio,stock FROM productos WHERE id = %s;",
                            (item['id_producto'],)
                        )
                        fila = cursor.fetchone()
                        if fila is None:
                            raise Exception(
                                f"Producto {item['id_producto']} no encontrado.")

                        precio, stock = fila
                        if stock < item['cantidad']:
                            raise Exception(
                                f"Stock insuficiente para el producto {item['id_producto']}.")

                        subtotal = precio * item['cantidad']
                        total += subtotal
                        detalles.append({
                            'id_producto': item['id_producto'],
                            'cantidad': item['cantidad'],
                            'precio': precio,
                        })

                    cursor.execute(
                        "INSERT INTO ventas (cliente_id,total,fecha) VALUES (%s,%s,%s) RETURNING id;",
                        (id_cliente, total, fecha_hoy)
                    )
                    id_venta = cursor.fetchone()[0]

                    for d in detalles:
                        cursor.execute(
                            "INSERT INTO detalle_ventas (id_venta,id_producto,cantidad,precio_unit) VALUES (%s,%s,%s,%s);",
                            (id_venta, d['id_producto'],
                             d['cantidad'], d['precio'])
                        )
                        cursor.execute(
                            "UPDATE productos SET stock = stock - %s WHERE id = %s;",
                            (d['cantidad'], d['id_producto'])
                        )
            return Venta(id_venta, id_cliente, total, fecha_hoy)
        except Exception as e:
            print(f"Error al crear la venta: {e}".upper())
            return None
        finally:
            conn.close()

    @staticmethod
    def obtener_todos():
        conn = obtener_conexion()
        if conn is None:
            print(
                "no se pudo establecer la conexion para obetener todos las ventas".upper())
            return []
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT ventas.id, ventas.cliente_id, ventas.total, ventas.fecha, clientes.nombre FROM ventas INNER JOIN clientes ON ventas.cliente_id = clientes.id;"
                    )
                    filas = cursor.fetchall()
            return [Venta(*f) for f in filas]
        except Exception as e:
            print(f"Error al obtener todas las ventas: {e}")
            return []
        finally:
            conn.close()

    @staticmethod
    def buscar_por_id(id_venta):
        conn = obtener_conexion()
        if conn is None:
            print(
                "no se pudo establecer la conexion para buscar la venta".upper())
            return None
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """SELECT ventas.id, ventas.cliente_id, ventas.total, ventas.fecha, clientes.nombre
                        FROM ventas
                        INNER JOIN clientes ON ventas.cliente_id = clientes.id
                        WHERE ventas.id = %s;""",
                        (id_venta,)
                    )
                    fila = cursor.fetchone()
            if fila:
                return Venta(*fila)
            return None
        except Exception as e:
            print(f"Error al buscar venta por ID: {e}")
            return None
        finally:
            conn.close()
