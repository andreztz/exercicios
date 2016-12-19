


def dimensoes(minha_matriz):
    linhas = len(minha_matriz) 
    colunas = 0
    for linha in range(len(minha_matriz)):        
        if len(minha_matriz[linha]) > colunas:
            colunas = len(minha_matriz[linha])        
    print('{}X{}'.format(linhas, colunas))


##minha_matriz = [[1], [2], [3]]
##dimensoes(minha_matriz)
### 3X1
##
##
##minha_matriz = [[1, 2, 3], [4, 5, 6]]
##dimensoes(minha_matriz)
### 2X3
##
##minha_matriz = [[1, 2, 3], [4, 5], [5, 6, 7]]
##dimensoes(minha_matriz)
### 3X3
