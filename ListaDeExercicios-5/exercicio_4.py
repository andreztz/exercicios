largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
top = altura

while altura:

    if altura == top or altura == 1:
        print("#" * largura)
    else:
        print("#" + " " * (largura - 2) + "#")

    altura -= 1
