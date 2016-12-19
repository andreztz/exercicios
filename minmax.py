# Problema
# Dado um lista de temperatura imprimir a temperatura min e max.

# Quebrar o problema em problemas menores.

def maxima(temperaturas):
    m = temperaturas[0]
    i = 1
    while i < len(temperaturas):
        if temperaturas[i] < m:
            m = temperaturas[i]
        i += 1
    return m

def minima(temperaturas):
    m = temperaturas[0]
    i = 1
    while i < len(temperaturas):
        if temperaturas[i] < m:
            m = temperaturas[i]
        i += 1
    return m
            

def MinMax(temperaturas):
    print("A menor temperatura do mes foi: {} Cº".format(minima(temperaturas)))
    print("A maior temperatura do mes foi: {} Cº".format(maxima(temperaturas)))

def teste_pontual(temp, valor):
    temp = temp
    calculado = minima(temp)
    if calculado  != valor:
        print("Valor errado para array", temp)
        print("O valor esperado: ", valor, ". Valor calculado: ", calculado)


def testa_minima():
    print("Iniciando os testes...")
    teste_pontual([0], 0)
    teste_pontual([0, 0, 0], 0)
    teste_pontual([1,2,3,4,5,6,7,8,9,0], 0)
    teste_pontual([30, 27, 25, 26, 22], 22)
    teste_pontual([-15, -12, 0, 20, 30], -15)
    print("Testes finalizados...")


testa_minima()
