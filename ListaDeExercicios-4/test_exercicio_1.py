import unittest
from exercicio_1 import fizzbuzz


class FizzBuzzTestCase(unittest.TestCase):

    def test_fizz(self):
        return self.assertEqual(fizzbuzz(3), 'Fizz')

    def test_buzz(self):
        return self.assertEqual(fizzbuzz(5), 'Buzz')

    def test_fizzbuzz(self):
        return self.assertEqual(fizzbuzz(15), 'FizzBuzz')

    def test_not_fizzbuzz(self):
        return self.assertEqual(fizzbuzz(4), 4)

if __name__ == '__main__':
    unittest.main()
