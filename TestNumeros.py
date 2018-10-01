from unittest import TestCase
from KataSimpleTDD import EstadisticaArreglo


class TestLongitud(TestCase):

    def testElementosMinMax(self):
        self.assertEqual(EstadisticaArreglo().obtenerLongitud("1,2"), [1, 1, 2], "cadena 1 elementos")
