import sys


class EstadisticaArreglo:
    def obtenerLongitud(self, cadenaString):

        arraySplit = cadenaString.split(',')
        if cadenaString == '':
            return [0, None, None, None]
        else:

            sum = 0.0
            for i in range(0, len(arraySplit)):
                sum = sum + int(arraySplit[i])
            promedio = sum / len(arraySplit)

            return [len(arraySplit), int(min(arraySplit)), int(max(arraySplit)),float(promedio)]


