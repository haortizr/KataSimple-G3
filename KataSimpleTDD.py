class EstadisticaArreglo:
    def obtenerLongitud(self, cadenaString):
        if cadenaString == '':
            return [0]
        elif len(cadenaString) > 1:
            return [len(cadenaString) - 1]
        else:
            return [int( cadenaString.split(','))]
