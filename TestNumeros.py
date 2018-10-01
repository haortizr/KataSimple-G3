from unittest import TestCase
from KataSimpleTDD import EstadisticaArreglo


class TestLongitud(TestCase):

    def testElementosMinMax(self):
        self.assertEqual(EstadisticaArreglo().obtenerLongitud("1,2,3,4"), [4, 1, 4], "cadena 1 elementos")
