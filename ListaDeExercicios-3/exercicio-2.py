num = int(input("Digite o valor de n: "))

odd = 0
yes = True
cont = 0

while yes:
    odd += 1
    if odd % 2 == 1:
        print(odd)
        cont += 1
        if cont == num:
            yes = False

