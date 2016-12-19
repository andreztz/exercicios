import unittest
from exercicio_4 import maximo



class MaiorValorTestCase(unittest.TestCase):

    def test_maior(self):
        return self.assertEqual(maximo(30,14, 10), 30)

    def test_maior_com_negativo(self):
        return self.assertEqual(maximo(0, -1, 1), 1)

    def test_maior_com_zero(self):
        return self.assertEqual(maximo(0, 2, 4), 4)


    def test_maior_igual(self):
        return self.assertEqual(maximo(7, 7, 7), 7)
if __name__ == '__main__':
    unittest.main()
