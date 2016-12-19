def cria_matriz(tot_lin, tot_col, valor):
    matriz = []  #lista vazia
    for i in range(tot_lin):
        linha = []
        for j in range(tot_col):
            linha.append(valor)
        matriz.append(linha)
        return matriz

x = cria_matriz(2, 3, 99)

print(x)

# [[99, 99, 99]]

def cria_matriz(tot_lin, tot_col, valor):
    matriz = []  #lista vazia
    for i in range(tot_lin):
        linha = []
        for j in range(tot_col):
            linha.append(valor)
        matriz.append(linha)
    return matriz

x = cria_matriz(2,3,99)

print(x)

# Nenhuma das alternativas representa a matriz resultante
# [[99, 99, 99], [99, 99, 99]]

def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        coluna = []
        for j in range(num_colunas):
            coluna.append(0)
        matriz.append(coluna)

    for i in range(num_linhas):
        for j in range(num_colunas):
            matriz[j][i] = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]: "))

    return matriz
x = cria_matriz(2,3)
print(x)
