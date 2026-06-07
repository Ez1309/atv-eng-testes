# test_calculadora.py

import unittest
from calculadora import dividir, multiplicar, somar, subtrair, potencia, calcular_media

class TestCalculadora(unittest.TestCase):
    """Classe de testes para as funções do arquivo calculadora.py."""

    def test_somar_com_varios_casos(self):
        casos = [(2, 3, 5), (5, 0, 5), (0, 0, 0), (-2, 5, 3), (-2, -3, -5)]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(somar(a, b), esperado)

    def test_subtrair_com_varios_casos(self):
        casos = [(10, 5, 5), (5, 10, -5), (0, 0, 0), (-5, -2, -3)]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(subtrair(a, b), esperado)

    def test_multiplicar_com_varios_casos(self):
        casos = [(3, 4, 12), (5, 0, 0), (-2, 3, -6), (-2, -3, 6)]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(multiplicar(a, b), esperado)

    def test_dividir_com_varios_casos(self):
        casos = [(10, 2, 5), (5, 2, 2.5), (-10, 2, -5), (0, 5, 0)]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(dividir(a, b), esperado)

    def test_dividir_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    def test_potencia_com_varios_casos(self):
        casos = [(2, 3, 8), (5, 0, 1), (10, 2, 100), (2, -1, 0.5)]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(potencia(a, b), esperado)

    def test_calcular_media_com_varios_casos(self):
        """Testes gerados com apoio de IA e refatorados com subTest."""
        casos = [
            ([10, 8, 6], 8.0),
            ([2.5, 7.5], 5.0),
            ([-2, -4, -6], -4.0),
            ([10], 10.0),
            ([0, 0, 0], 0.0),
        ]
        for lista, esperado in casos:
            with self.subTest(lista=lista):
                self.assertEqual(calcular_media(lista), esperado)

    def test_calcular_media_lista_vazia(self):
        with self.assertRaises(ValueError):
            calcular_media([])

if __name__ == "__main__":
    unittest.main()
