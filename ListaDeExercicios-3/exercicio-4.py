num = int(input("Digite um número inteiro: "))

last = num % 10
yes = False

while True:
    num = num // 10
    tmp = num % 10
    if last == tmp:
        yes = True
        break
    last = tmp


if yes and num not in [0,1,2,3,4,5,6,7,8,9]:
    print('sim')
else:
    print('nao')
