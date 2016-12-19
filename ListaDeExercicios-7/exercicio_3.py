def verifica_dimensoes(matriz):
    linhas = len(matriz)
    colunas = [len(linha) for linha in matriz if len(linha) > 1]
    if not (len(set(colunas)) == 1):
        return 0
    return 1
                

def soma_colunas(lista_colunas):
    for i, obj in enumerate(lista_colunas):
        lista_colunas[i] += obj
    return lista_colunas
        

def soma_matrizes(m1, m2):
    if len(m1) != len(m2):
        return False
    if not (verifica_dimensoes(m1) == verifica_dimensoes(m2)):
        return False
    return [soma_colunas(col) for col in m1]
