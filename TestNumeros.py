from unittest import TestCase
from KataSimpleTDD import EstadisticaArreglo

class TestLongitud(TestCase):

       def testElementosMinMax(self):
            self.assertEqual(EstadisticaArreglo().obtenerLongitud("1"), [1, 1], "cadena vacia")