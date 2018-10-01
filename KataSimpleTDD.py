import sys

class EstadisticaArreglo:
    def obtenerLongitud(self, cadenaString):
        arraySplit = cadenaString.split(',')
        if cadenaString == '':
            return [0, None]
        elif len(cadenaString) >1:
            if arraySplit[0] < arraySplit[1]:
                return [len(arraySplit),int( arraySplit[0])]
            else:
                return [len(arraySplit), int(arraySplit[1])]

