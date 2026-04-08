from src.models.cliente import Cliente


def crear_cliente(nombre, email, telefono):
    if not nombre.strip():
        print("El nombre del cliente no puede estar vacío.".upper())
        return None
    if not email.strip():
        print("El email del cliente no puede estar vacío.".upper())
        return None
    if not telefono.strip():
        print("El teléfono del cliente no puede estar vacío.".upper())
        return None
    return Cliente.crear_cliente(nombre, email, telefono)


def obtener_clientes():
    return Cliente.obtener_todos()


def obtener_cliente_por_id(id_cliente):
    if id_cliente <= 0:
        print("El ID del cliente debe ser un número positivo.".upper())
        return None
    cliente = Cliente.obtener_por_id(id_cliente)
    if cliente is None:
        print("No existe un cliente con el ID especificado.".upper())
    return cliente


def eliminar_cliente(id_cliente):
    if id_cliente <= 0:
        print("El ID del cliente debe ser un número positivo.".upper())
        return None
    resultado = Cliente.eliminar_cliente(id_cliente)
    if not resultado:
        print("No existe un cliente con el ID especificado.".upper())
    return resultado
