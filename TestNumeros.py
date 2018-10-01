from unittest import TestCase
from KataSimpleTDD import EstadisticaArreglo


class TestLongitud(TestCase):

    def testElementosMinMax(self):
        self.assertEqual(EstadisticaArreglo().obtenerLongitud(""), [0, None, None,None], "cadena 0 elementos")
