
""""
altura = 5
linha = 1
while linha <= altura:
    print("*", end = "")
    coluna = 2
    while coluna < altura: 
        if linha == 1 or linha == altura:
            print("*", end="")
        else:
            print(end = " ")
        coluna = coluna + 1
    print("*")
    linha = linha + 1


x = 1
while x < 3:
    y = 1
    while y < 3:
        print(x*y, end = "\t")
        y = y + 1
    x = x + 1


def leitura():
    x = int(input("Digite um valor: "))
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x

def leitura():
    x = -1
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x
print(leitura())
"""

x = 10
y = 10
print(x !=y )
print()
print(not (x == y))
print(x > y or x < y)
print(x > y and x < y)
print(x >= y or x <= y)
