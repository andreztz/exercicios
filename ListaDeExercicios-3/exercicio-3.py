num = int(input("Digite um número inteiro: "))

resp = num % 10

cont = True

while cont:
    num = num // 10
    resp += num % 10
    if num == 0:
        cont = False
        print(resp)



