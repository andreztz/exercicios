import unittest
from exercicio_2 import maximo

class MaiorValorTestCase(unittest.TestCase):

    def test_maior(self):
        return self.assertEqual(maximo(3,4), 4)

    def test_maior_com_negativo(self):
        return self.assertEqual(maximo(0, -1), 0)

if __name__ == '__main__':
    unittest.main()
