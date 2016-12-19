import unittest
from exercicio_3 import maior_primo

class MaiorPrimoTestCase(unittest.TestCase):

    def test_maior_primo(self):
        return self.assertEqual(maior_primo(100), 97)


    def test_maior_primo2(self):
        return self.assertEqual(maior_primo(7), 7)


if __name__ == '__main__':
    unittest.main()
