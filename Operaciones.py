# Jamil Marciaga - Suma
def sumar(a, b):
    return a + b


# Gilberto Cano - Resta
def restar(a, b):
    resultado = a - b
    return resultado


# Alexis Lopez - Multiplicación
def multiplicar(a, b):
    return a * b


# Esequiel Gonzalez - División
def dividir(a, b):
    """Realiza la división de dos números y valida la división entre cero."""
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b
