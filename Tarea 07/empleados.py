
from logger_base import log
import pickle

class Empleados:
    def __init__(self, nombre, apellido, empresa, sueldo):
        self._nombre = nombre
        self._apellido = apellido
        self._empresa = empresa
        self._sueldo = sueldo
        log.info('Se agrego un empleado exitosamente')

    def __str__(self):
        return f'''
            Cliente: {self._nombre} {self._apellido}
            Empresa: {self._empresa}
            Sueldo: {self._sueldo}
        '''

class listarEmpleados:
    _empleados = []

    def __init__(self):
        listaDeEmpleados = open('ArchivoEmpleados', "ab+")
        listaDeEmpleados.seek(0)

        try:
            self._empleados = pickle.load(listaDeEmpleados)
        except:
            print("El Archivo esta vacio")
        finally:
            listaDeEmpleados.close()
            del (listaDeEmpleados)

    def guardarEmpleado(self):
        listaDeEmpleados = open('ArchivoEmpleados', 'wb')
        pickle.dump(self._empleados, listaDeEmpleados)
        del(listaDeEmpleados)

    def agregarEmpleado(self, empleado):
        self._empleados.append(empleado)
        self.guardarEmpleado()

    def mostrarEmpleado(self):
        for empleado in self._empleados:
            log.info(empleado)

    def buscarEmpleado(self, nombre):
        for empleado in self._empleados:
            if empleado._nombre == nombre:
                print('Empleado encontrado')
                log.info(f'Nombre: {empleado._nombre} {empleado._apellido} \n '
                         f'Empresa: {empleado._empresa} Sueldo: {empleado._sueldo}')
                break


