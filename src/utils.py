def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")


def leer_float(mensaje):
    while True:
        try:
            val = float(input(mensaje))
            if val < 0:
                print("Error: El valor no puede ser negativo.")
                continue
            return val
        except ValueError:
            print("Error: Por favor, ingrese un número decimal válido.")
