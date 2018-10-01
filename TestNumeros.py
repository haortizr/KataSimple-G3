from unittest import TestCase
from KataSimpleTDD import EstadisticaArreglo

class TestLongitud(TestCase):
    def testEstadisticaArreglo(self):
        self.assertEqual(EstadisticaArreglo().obtenerLongitud(''),[0],"cadena vacia")

    def TestLongitudConNumero(self):
            self.assertEqual(EstadisticaArreglo().obtenerLongitud("1"), [1], "cadena con un numero")