def soma_elementos(lista):
    soma = 0
    for i in lista:
        if isinstance(i, int):
            soma += i
    return soma
