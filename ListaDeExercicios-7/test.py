import os

import unittest
from unittest.mock import patch

from ep2_barebones import media_simples_palavras
from ep2_barebones import type_token
from ep2_barebones import hapax_legomana
from ep2_barebones import complexidade_sentenca
from ep2_barebones import tamanho_medio_da_sentenca
from ep2_barebones import tamanho_medio_da_frase

from ep2_barebones import total_de_frases
from ep2_barebones import soma_caracteres

from ep2_barebones import separa_sentenca
from ep2_barebones import separa_frase
from ep2_barebones import separa_palavras

from ep2_barebones import le_assinatura
from ep2_barebones import n_palavras_unicas
from ep2_barebones import n_palavras_diferentes
from ep2_barebones import compara_assinatura
from ep2_barebones import calcula_assinatura
from ep2_barebones import avalia_textos


class Textos:
    pass

titulos = [txt for txt in os.listdir() if ".txt" in txt]

txt = Textos()

for titulo, texto in enumerate(titulos):
    with open(texto) as output:
        content = output.read()
        content = "".join(content.split('\n'))
    setattr(txt, titulos[titulo].split('.')[0], content)


class TestEp2(unittest.TestCase):
    
    texto = "O gato caçava o rato"


    def test_media_simples_palavras(self):
        return self.assertEqual(media_simples_palavras(self.texto), 3.2)

    def test_type_token(self):
        texto = len(self.texto.split(' '))
        conjunto = len(['o', 'gato', 'caçava', 'rato'])
        resposta = 0.8
        return self.assertEqual(type_token(conjunto, texto), resposta)

    def test_hapax_legomana(self):
        palavras_unicas = n_palavras_unicas(self.texto.split())
        total = len(self.texto.split())
        resposta = 0.6
        return self.assertEqual(hapax_legomana(palavras_unicas, total), resposta)

    def test_complexidade_sentenca(self):

        texto = 'O gato caçava o rato, com uma pá. O rato era esperto, no entanto morreu.'       

        numero_frases = len(total_de_frases(texto))
        numero_sentencas = len(separa_sentenca(texto)[:-1])
        return self.assertEqual(complexidade_sentenca(numero_frases, numero_sentencas), 2.0)

    def test_tamanho_medio_da_sentenca(self):
        """IMPLEMENTAR."""
        texto = 'O gato caçava o rato, com uma pá. O rato era esperto, no entanto morreu.'
        caracteres = 0
        for c in separa_sentenca(texto):
            caracteres += len(c)
        sentencas = len(separa_sentenca(texto)[:-1])
        resposta = 35.0
        return self.assertEqual(tamanho_medio_da_sentenca(caracteres, sentencas), resposta)

    def test_tamanho_medio_da_frase(self):
        """IMPLEMENTAR."""
        texto = 'O gato caçava o rato, com uma pá. O rato era esperto, no entanto morreu.'
        numero_caracteres = 0
        for c in total_de_frases(texto):
            numero_caracteres += len(c)            
        numero_frases = len(total_de_frases(texto))
        resposta = 17.0
        return self.assertEqual(tamanho_medio_da_frase(numero_caracteres, numero_frases), resposta)


    def test_total_de_frases(self):
        sentenca = 'O gato caçava o rato, com uma pá. O rato era esperto, no entanto morreu.'
        resposta = ['O gato caçava o rato', ' com uma pá', ' O rato era esperto', ' no entanto morreu']
        return self.assertEqual(total_de_frases(sentenca), resposta)

    def test_soma_caracteres(self):
        
        return self.assertEqual(soma_caracteres(self.texto), 20)

    def test_le_assinatura(self):
        entradas = [4.33, 0.23, 0.14, 13.28, 1.86, 0.0]
        saidas = [4.33, 0.23, 0.14, 13.28, 1.86, 0.0]
        with patch('builtins.input', side_effect=entradas):
            print('Testando entradas do usuário...\n')
            resp = self.assertEqual(le_assinatura(), saidas)
            print('\nEntradas do usuário OK.\n')
        return resp

    def test_separa_sentenca(self):
        texto = 'Voltei-me para ela; Capitu tinha os olhos no chão.'
        resposta = ['Voltei-me para ela; Capitu tinha os olhos no chão', '']
        return self.assertEqual(separa_sentenca(texto), resposta)

    def test_separa_frase(self):
        sentenca = 'Voltei-me para ela; Capitu tinha os olhos no chão.'
        resposta = ['Voltei-me para ela', ' Capitu tinha os olhos no chão.']
        return self.assertEqual(separa_frase(sentenca), resposta)

    def test_compara_assinatura_1(self):
        ass1 = [4.33, 0.23, 0.14, 13.28, 1.86, 0.0]
        ass2 = [4.33, 0.23, 0.14, 13.28, 1.86, 0.0]
        return self.assertEqual(compara_assinatura(ass1, ass2), 0.0)

    def test_compara_assinatura_1(self):
        ass1 = [4.34, 0.05, 0.02, 12.81, 2.16, 0.0]
        ass2 = [3.96, 0.05, 0.02, 22.22, 3.41, 0.0]
        return self.assertEqual(compara_assinatura(ass1, ass2), 1.84)

    def test_calcula_assinatura_texto1_index_0(self):
        return self.assertEqual(calcula_assinatura(txt.texto1)[0], 5.189)

    def test_calcula_assinatura_texto2_index_0(self):
        return self.assertEqual(calcula_assinatura(txt.texto2)[0], 4.507)

    def test_calcula_assinatura_texto3_index_0(self):
        return self.assertEqual(calcula_assinatura(txt.texto3)[0], 4.409)

    def test_calcula_assinatura_texto1_index_1(self):
        return self.assertEqual(calcula_assinatura(txt.texto1)[1], 0.743)

    def test_calcula_assinatura_texto2_index_1(self):
        return self.assertEqual(calcula_assinatura(txt.texto2)[1], 0.777)

    def test_calcula_assinatura_texto3_index_1(self):
        return self.assertEqual(calcula_assinatura(txt.texto3)[1], 0.59)

    def test_calcula_assinatura_texto1_index_2(self):
        return self.assertEqual(calcula_assinatura(txt.texto1)[2], 0.608)

    def test_calcula_assinatura_texto2_index_2(self):
        return self.assertEqual(calcula_assinatura(txt.texto2)[2], 0.666)

    def test_calcula_assinatura_texto3_index_2(self):
        pass

    def test_calcula_assinatura_texto1_index_3(self):
        return self.assertEqual(calcula_assinatura(txt.texto2)[3], 88.875)

    def test_calcula_assinatura_texto2_index_3(self):
        return self.assertEqual(calcula_assinatura(txt.texto3)[3], 85.25)

    def test_avalia_textos(self):
        assinatura = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]
        textos = [txt.texto3, txt.texto2, txt.texto1]
        return self.assertEqual(avalia_textos(textos, assinatura), 1)

def main():
    unittest.main()
    

if __name__ == '__main__':
    main()
