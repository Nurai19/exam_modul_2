import numbers


def nums(*args):
    suma = 0
    for i in args:
        if isinstance(i, (i, numbers.Number)):
            suma = suma + i
    return suma




