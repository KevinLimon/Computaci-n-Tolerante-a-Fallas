
# Raise: Sirve para lanzar (de forma intencional) excepciones de python.

def evaluarCalificacion(cal):
    if cal < 0:
        raise ValueError('No se permiten valores menores a cero')
    elif cal >= 10:
        print('Calificación excelente')
    elif cal >= 6:
        print('Aprobado')
    else:
        print('Reprobado')
evaluarCalificacion(-1)