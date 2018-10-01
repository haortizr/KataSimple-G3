import sys


class EstadisticaArreglo:
    def obtenerLongitud(self, cadenaString):

        arraySplit = cadenaString.split(',')
        if cadenaString == '':
            return [0, None, None, None]
        else:
            return [len(arraySplit), int(min(arraySplit)), int(max(arraySplit))]
