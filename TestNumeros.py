from unittest import TestCase
from KataSimpleTDD import EstadisticaArreglo

class TestLongitud(TestCase):
    def testEstadisticaArreglo(self):
        self.assertEqual(EstadisticaArreglo().obtenerLongitud(''),[0],"cadena vacia")


    def TestLongitudConNumero(self):
        self.assertEqual(EstadisticaArreglo().obtenerLongitud("1"), [1], "cadena con un numero")

    def TestLongitudDosNumero(self):
        self.assertEqual(EstadisticaArreglo().obtenerLongitud("1,2"), [2], "cadena con dos numero")

    def TestLongitudNNumero(self):
        self.assertEqual(EstadisticaArreglo().obtenerLongitud("1,2,3,4"), [4], "cadena con cuatro numero")
        self.assertEqual(EstadisticaArreglo().obtenerLongitud("1,2,3,4,5"), [5], "cadena con cinco numero")