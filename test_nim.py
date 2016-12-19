"""
O resultado dos testes com seu programa foi:

***** [0.1 pontos]: Testando validacao da entrada do usuario com erros (n = 3, m = 5, respostas 4, -1, 0, 1) - Falhou *****
Timeout







***** [0.5 pontos]: Checando partida unica (n = 5, m = 3, jogadas = (1,)) - Falhou *****
IndexError: list index out of range

***** [0.5 pontos]: Checando partida unica (n = 5, m = 3, jogadas = (2,)) - Falhou *****
IndexError: list index out of range

***** [0.5 pontos]: Checando partida unica (n = 9, m = 2, jogadas = (1, 2, 2)) - Falhou *****
IndexError: list index out of range

***** [0.5 pontos]: Checando partida unica (n = 9, m = 2, jogadas = (1, 2, 1)) - Falhou *****
IndexError: list index out of range

***** [0.5 pontos]: Checando partida unica (n = 2, m = 3, jogadas = ()) - Falhou *****
AssertionError: Computador deveria ter ganhado

***** [0.5 pontos]: Checando partida unica (n = 2, m = 2, jogadas = ()) - Falhou *****
IndexError: list index out of range

***** [0.2 pontos]: Checando campeonato ([5, 3, 1], [5, 3, 2], [9, 2, 1, 2, 2]) - Falhou *****
IndexError: list index out of range

***** [0.2 pontos]: Checando campeonato ([9, 2, 1, 2, 1], [2, 3], [2, 2]) - Falhou *****
AssertionError: Deveria comecar com o oponente



"""



import unittest
from jogo_nim import computador_escolhe_jogada



class NimTestCase(unittest.TestCase):

    def test_computador_escolhe_jogada_1(self):
        return self.assertEqual(computador_escolhe_jogada(5, 3), 1)

    def test_computador_escolhe_jogada_2(self):
        return self.assertEqual(computador_escolhe_jogada(3, 5), 3)

    def test_computador_escolhe_jogada_3(self):
        return self.assertEqual(computador_escolhe_jogada(6, 2), 2)

    def test_computador_escolhe_jogada_4(self):
        return self.assertEqual(computador_escolhe_jogada(2, 1), 1)

    def test_computador_escolhe_jogada_5(self):
        return self.assertEqual(computador_escolhe_jogada(1, 1), 1)
    
    def test_computador_escolhe_jogada_5(self):
        return self.assertEqual(computador_escolhe_jogada(2, 2), 2)

    def test_computador_escolhe_jogada_5(self):
        return self.assertEqual(computador_escolhe_jogada(3, 1), 1)


if __name__ == '__main__':
    unittest.main()
