num = int(input("Digite o valor de n: "))

fat = 1

while num:
    fat *= num
    num -= 1

print(fat)
