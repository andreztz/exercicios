import re
import string

##def media_simples_palavras(texto):
##    """Tamanho médio de palavra é a soma dos tamanhos das palavras
##    dividida pelo número total de palavras."""
##    texto = re.sub("[,.;:\(\)\"]+\ *", " ", texto)
##    texto = texto.replace('[d]', 'd ')
##    palavras = texto.split()
##    tamanho_palavras = 0
##
##    for palavra in palavras:
##        tamanho_palavras += len(palavra)
##    media = tamanho_palavras / len(palavras)
##    return media

def formata_saida(saida):
    """IMPLEMENTAR TEST"""
    return float(str(saida)[:5])

def separa_palavras(texto):
    """IMPLEMENTAR TEST"""
    texto = separa_frase(texto)
    texto = " ".join(texto)
    texto = separa_sentenca(texto)
    texto = " ".join(texto)    
    return texto


def media_simples_palavras(texto):
    texto = separa_palavras(texto)
    palavras = texto.split()
    tamanho_palavras = 0

    for palavra in palavras:
        tamanho_palavras += len(palavra)
    media = tamanho_palavras / len(palavras)
    return formata_saida(media)

def type_token(diferentes, total):
    """Relação type-token é a soma do número de palavras únicas dividas pelo
    número total de palavras. Por exemplo, na frase 'O gato caçava o rato',
    temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes
    (o, gato, caçava, rato). Nessa frase, a relação type-token vale 4/5 = 0.8"""   
    relacao = diferentes / total
    return formata_saida(relacao)


def hapax_legomana(palavras_unicas, total):
    """Razão Hapax Legomana é soma do número de palavras que aparecem uma única vez
    dividida pelo total de palavras. Por exemplo, na frase "O gato caçava o rato",
    temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem
    só uma vez (gato, caçava. rato). Nessa frase a relação Hapax Legomana
    vale 3/5 = 0.6"""
    relacao = palavras_unicas / total
    return formata_saida(relacao)


def complexidade_sentenca(numero_frases, numero_sentencas):
    '''IMPLEMENTAR TESTE. Complexidade de sentença é o número de frases
    em uma sentença dividido pelo número de sentenças.'''    
    complexidade = numero_frases / numero_sentencas
    return complexidade


def tamanho_medio_da_sentenca(caracteres, sentencas):
    """IMPLEMENTAR. Tamanho médio de sentença é a soma dos números de caracteres em uma
    sentença dividida pelo número de sentenças."""
    media = caracteres / sentencas
    return media


def tamanho_medio_da_frase(numero_caracteres, numero_frases):
    '''Tamanho médio de frase é a soma do número de
    caracteres em cada frase dividida pelo número de frases no texto.
    '''
    media_frase = numero_caracteres / numero_frases
    return media_frase


def total_de_frases(sentenca):
    frases = []
    for frase in separa_sentenca(sentenca):
        if frase:
            frases += separa_frase(frase)
    return frases


def soma_caracteres(texto):
    caracteres = 0
    for i in texto:
        caracteres += len(i)
    return caracteres


def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_texto():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


def separa_sentenca(texto):
    return re.split(r'[.!?]+', texto)

def separa_frase(sentenca):
    return re.split(r'[,:;]+', sentenca)


def n_palavras_unicas(lista_palavras):
    """Essa funcao recebe uma lista de palavras e retorna o número
    de palavras que aparecem uma única vez."""
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    """Essa funcao recebe uma lista de palavras e retorna o numero
    de palavras diferentes utilizadas"""
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)
    
def compara_assinatura(ass1, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto
    e deve retornar o grau de similaridade nas assinaturas.'''
    somatorio = 0
    for index, obj in enumerate(ass1):
        somatorio  += abs(ass1[index] - ass_cp[index])
    return round(somatorio / len(ass1), 2)

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto
    e deve retornar a assinatura do texto.'''

    """Tamanho médio de palavra é a soma dos tamanhos das palavras
    dividida pelo número total de palavras."""
    wal =  media_simples_palavras(texto)
    
    """Relação type-token é a soma do número de palavras únicas dividas pelo
    número total de palavras. Por exemplo, na frase 'O gato caçava o rato',
    temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes
    (o, gato, caçava, rato). Nessa frase, a relação type-token vale 4/5 = 0.8""" 
    palavras = separa_palavras(texto)
    diferentes = n_palavras_diferentes(palavras.split())
    total = len(palavras.split())
    ttr = type_token(diferentes, total)
    
    """Razão Hapax Legomana é soma do número de palavras que aparecem uma única vez
    dividida pelo total de palavras. Por exemplo, na frase "O gato caçava o rato",
    temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem
    só uma vez (gato, caçava. rato). Nessa frase a relação Hapax Legomana
    vale 3/5 = 0.6"""
    palavras = separa_palavras(texto)
    palavras_unicas = n_palavras_unicas(palavras.split())
    total = len(palavras.split())
    hlr = hapax_legomana(palavras_unicas, total)

    """Tamanho médio de sentença é a soma dos números de caracteres em uma
    sentença dividida pelo número de sentenças."""
    caracteres = 0
    sentencas = separa_sentenca(texto)[:-1]
    for sentenca in sentencas:
        caracteres += len(sentenca)
    sal = tamanho_medio_da_sentenca(caracteres, len(sentencas))

    """Complexidade de sentença é o número de frases
    em uma sentença dividido pelo número de sentenças."""
    numero_frases = len(total_de_frases(texto))
    numero_sentencas = len(separa_sentenca(texto)[:-1])
    sac = complexidade_sentenca(numero_frases, numero_sentencas)

    """Tamanho médio de frase é a soma do número de
    caracteres em cada frase dividida pelo número de frases no texto."""
    numero_caracteres = 0
    for palavra in total_de_frases(texto):
        numero_caracteres += soma_caracteres(palavra)

    numero_frases = len(total_de_frases(texto))
    pal = tamanho_medio_da_frase(numero_caracteres, numero_frases)
    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos
    e deve retornar o numero (0 a n-1) do texto com maior
    probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas = []
    for texto in textos:
        assinaturas.append(calcula_assinatura(texto))

    comparacoes = []
    
    for assinatura in assinaturas:
        comparacoes.append(compara_assinatura(assinatura, ass_cp))
    return comparacoes.index(min(comparacoes))

def main():
    ass_cp = le_assinatura()

    textos = le_texto()

    n = avalia_textos(textos, ass_cp)

    print("O autor do texto", n + 1, "esta infectado com COH-PIAH")
    
if __name__ == '__main__':
    main()
