def sumar (a,b):
    return a + b

def restar (a,b):
    return a - b

def multiplicar (a,b):
    return a * b

def dividir (a,b):
    if b == 0:
        raise ValueError ("No podes dividir por cero (0).")
    return a / b
