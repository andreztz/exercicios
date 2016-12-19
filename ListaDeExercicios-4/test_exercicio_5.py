import unittest
from exercicio_5 import vogal

class VogalOrConsoanteTestCase(unittest.TestCase):

    def test_vogal(self):
        return self.assertTrue(vogal('i'))

    def test_consoante(self):
        return self.assertFalse(vogal('c'))


if __name__ == '__main__':
    unittest.main()
