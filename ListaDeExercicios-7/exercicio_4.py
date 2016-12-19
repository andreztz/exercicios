def dimensoes(minha_matriz):
    linhas = len(minha_matriz) 
    colunas = 0
    for linha in range(len(minha_matriz)):        
        if len(minha_matriz[linha]) > colunas:
            colunas = len(minha_matriz[linha])        
    return linhas, colunas
    

def sao_multiplicaveis(m1, m2):
    if dimensoes(m1)[1] == dimensoes(m2)[0]:        
        return True
    else:
        return False

