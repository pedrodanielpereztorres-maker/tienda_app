from src.db import obtener_conexion


class Cliente:
    def __init__(self, id_cliente, nombre, email, telefono):
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono

    @property
    def id_cliente(self):
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, value):
        self.__id_cliente = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, value):
        self.__telefono = value

    def __str__(self):
        return "\n".join([
            f"ID: {self.__id_cliente}",
            f"Nombre: {self.__nombre}",
            f"Email: {self.__email}",
            f"Teléfono: {self.__telefono}"
        ])

    @staticmethod
    def crear_cliente(nombre, email, telefono):
        conn = obtener_conexion()
        if conn is None:
            print("No se pudo establecer la conexión para crear el cliente.".upper())
            return None
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO clientes (nombre,email,telefono) VALUES (%s,%s,%s) RETURNING id;",
                        (nombre, email, telefono)
                    )
                    id_cliente = cursor.fetchone()[0]
            return Cliente(id_cliente, nombre, email, telefono)
        except Exception as e:
            print(f"ERROR AL CREAR CLIENTE: {e}".upper())
            return None
        finally:
            conn.close()

    @staticmethod
    def obtener_todos():
        conn = obtener_conexion()
        if conn is None:
            print("No se pudo establecer la conexión para obtener los clientes.".upper())
            return []
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT id, nombre, email, telefono FROM clientes;")
                    filas = cursor.fetchall()
            return [Cliente(*f) for f in filas]
        finally:
            conn.close()

    @staticmethod
    def obtener_por_id(id_cliente):
        conn = obtener_conexion()
        if conn is None:
            print("No se pudo establecer la conexión para obtener el cliente.".upper())
            return None
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT id, nombre, email, telefono FROM clientes WHERE id = %s;",
                        (id_cliente,)
                    )
                    fila = cursor.fetchone()
            if fila:
                return Cliente(*fila)
            return None
        except Exception as e:
            print(f"ERROR AL OBTENER CLIENTE POR ID: {e}".upper())
            return None
        finally:
            conn.close()

    @staticmethod
    def eliminar_cliente(id_cliente):
        conn = obtener_conexion()
        if conn is None:
            print("No se pudo establecer la conexión para eliminar el cliente.".upper())
            return False
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM clientes WHERE id = %s;",
                        (id_cliente,)
                    )
                    fila = cursor.rowcount
            return fila > 0
        except Exception as e:
            print(f"ERROR AL ELIMINAR CLIENTE: {e}".upper())
            return False
        finally:
            conn.close()
