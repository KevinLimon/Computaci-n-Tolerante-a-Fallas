from logger_base import log
from empleados import Empleados, listarEmpleados
opcion = None
lista = listarEmpleados()
while True:
    try:
        print('OPCIONES')
        print('1. Agregar clientes')
        print('2. Mostrar clientes')
        print('3. Buscar Empleado')
        print('4. Salir')
        opcion = int(input('Escoge una opción: '))
        if opcion == 1:
            nombre = input('Ingresa el nombre: ')
            apellido = input('Ingresa el apellido: ')
            empresa = input('Ingresa la empresa: ')
            sueldo = float(input('Ingresa el sueldo: '))
            aux = Empleados(nombre, apellido, empresa, sueldo)
            lista.agregarEmpleado(aux)
        elif opcion == 2:
            lista.mostrarEmpleado()
        elif opcion == 3:
            nom = input('Nombre del empleado: ')
            lista.buscarEmpleado(nom)
        elif opcion == 4:
            log.info('Fin del programa...')
            break
    except Exception as e:
        log.debug(f'Ocurrio un error {e}')
        opcion = None
# else:
#     log.info('Fin del programa...')