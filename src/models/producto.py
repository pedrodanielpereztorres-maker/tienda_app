from src.db import obtener_conexion


class Producto:
    def __init__(self, id_producto, nombre, precio, stock, categoria_id, categoria_nombre=""):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__categoria_id = categoria_id
        self.__categoria_nombre = categoria_nombre

    @property
    def id_producto(self):
        return self.__id_producto

    @id_producto.setter
    def id_producto(self, value):
        self.__id_producto = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, value):
        if value < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__precio = value

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        self.__stock = value

    @property
    def categoria_id(self):
        return self.__categoria_id

    @categoria_id.setter
    def categoria_id(self, value):
        self.__categoria_id = value

    @property
    def categoria_nombre(self):
        return self.__categoria_nombre

    @categoria_nombre.setter
    def categoria_nombre(self, value):
        self.__categoria_nombre = value

    def __str__(self):
        return "\n".join([
            f"ID: {self.id_producto}",
            f"Nombre: {self.nombre}",
            f"Precio: {self.precio}",
            f"Stock: {self.stock}",
            f"Categoría: {self.categoria_nombre}"
        ])

    @staticmethod
    def crear_producto(nombre, precio, stock, categoria_id):
        conn = obtener_conexion()
        if conn is None:
            print("No se pudo establecer la conexión para crear el producto.")
            return None
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO productos (nombre,precio,stock,categoria_id) VALUES (%s,%s,%s,%s) RETURNING id;",
                        (nombre, precio, stock, categoria_id)
                    )
                    id_producto = cursor.fetchone()[0]
            return Producto(id_producto, nombre, precio, stock, categoria_id)
        except Exception as e:
            print(f"Error al crear producto: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def obtener_todos():
        conn = obtener_conexion()
        if conn is None:
            print(
                "no se pudo establecer la conexion para obetener todos los productos".upper())
            return []
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """SELECT productos.id, productos.nombre, productos.precio, productos.stock,
                          productos.categoria_id, categorias.nombre FROM productos
                        INNER JOIN categorias ON productos.categoria_id = categorias.id;"""
                    )
                    filas = cursor.fetchall()
            return [Producto(*f) for f in filas]
        finally:
            conn.close()

    @staticmethod
    def buscar_por_id(id_producto):
        conn = obtener_conexion()
        if conn is None:
            print(
                "no se pudo establecer la conexion para buscar el productos".upper())
            return None
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """SELECT productos.id, productos.nombre, productos.precio, productos.stock,
                                    productos.categoria_id, categorias.nombre
                            FROM productos
                            INNER JOIN categorias ON productos.categoria_id = categorias.id
                            WHERE productos.id = %s;""",
                        (id_producto,)
                    )
                    fila = cursor.fetchone()
            if fila:
                return Producto(*fila)
            return None
        finally:
            conn.close()

    @staticmethod
    def actualizar_stock(id_producto, cantidad):
        conn = obtener_conexion()
        if conn is None:
            print("no se pudo establecer la conexion para actualizar stock".upper())
            return None
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "UPDATE productos SET stock = stock + %s WHERE id = %s;",
                        (cantidad, id_producto)
                    )
                    filas = cursor.rowcount
            return filas > 0
        except Exception as e:
            print(f"Error al actualizar stock: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def eliminar_producto(id_producto):
        conn = obtener_conexion()
        if conn is None:
            print("no se pudo establecer la conexion para eliminar producto".upper())
            return False
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM productos WHERE id=%s;",
                        (id_producto,)
                    )
                    fila = cursor.rowcount
            return fila > 0
        except Exception as e:
            print(f"Error al eliminar producto: {e}")
            return False
        finally:
            conn.close()
