from src.db import obtener_conexion


class Categoria:
    def __init__(self, id_categoria, nombre, descripcion):
        self.__id_categoria = id_categoria
        self.__nombre = nombre
        self.__descripcion = descripcion

    @property
    def id_categoria(self):
        return self.__id_categoria

    @id_categoria.setter
    def id_categoria(self, value):
        self.__id_categoria = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, value):
        self.__descripcion = value

    def __str__(self):
        return "\n".join([
            f"ID: {self.__id_categoria}",
            f"Nombre: {self.__nombre}",
            f"Descripción: {self.__descripcion}"
        ])

    @staticmethod
    def crear_categoria(nombre, descripcion):
        conn = obtener_conexion()
        if conn is None:
            print("No se pudo establecer la conexión para crear la categoría.")
            return None
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO categorias (nombre, descripcion) VALUES (%s, %s) RETURNING id;",
                        (nombre, descripcion)
                    )
                    id_categoria = cursor.fetchone()[0]
            return Categoria(id_categoria, nombre, descripcion)
        except Exception as e:
            print(f"Error al crear la categoría: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def obtener_todas():
        conn = obtener_conexion()
        if conn is None:
            print("No se pudo establecer la conexión para obtener las categorías.")
            return []
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT id, nombre, descripcion FROM categorias;")

                    filas = cursor.fetchall()
            return [Categoria(id_categoria, nombre, descripcion) for id_categoria, nombre, descripcion in filas]
        except Exception as e:
            print(f"Error al obtener todas las categorías: {e}")
            return []
        finally:
            conn.close()

    @staticmethod
    def obtener_por_id(id_categoria):
        conn = obtener_conexion()
        if conn is None:
            print("No se pudo establecer la conexión para obtener la categoría.")
            return None
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT id, nombre, descripcion FROM categorias WHERE id = %s;",
                        (id_categoria,)
                    )
                    fila = cursor.fetchone()
            if fila:
                return Categoria(*fila)
            return None
        except Exception as e:
            print(f"Error al obtener categoría por ID: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def eliminar_categoria(id_categoria):
        conn = obtener_conexion()
        if conn is None:
            print("No se pudo establecer la conexión para eliminar la categoría.")
            return False
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM categorias WHERE id = %s;",
                        (id_categoria,)
                    )
                    fila = cursor.rowcount
            return fila > 0
        except Exception as e:
            print(f"Error al eliminar categoría: {e}")
            return False
        finally:
            conn.close()
