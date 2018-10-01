import sys


class EstadisticaArreglo:
    def obtenerLongitud(self, cadenaString):
        if cadenaString == '':
            return [0, None]
        else:
            arraySplit = cadenaString.split(',')
            return [len(arraySplit),int(cadenaString)]
