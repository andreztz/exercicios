num = int(input("Digite um número inteiro: "))

primo = True
div = 2

while div < num:
    if num % div == 0:
        primo = False
        break
    div += 1

if primo and num > 1:
    print('primo')
else:
    print('não primo')

