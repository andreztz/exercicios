num = 1
nums = []

while num:
    num = int(input("Digite um número: "))
    if num != 0:
        nums.append(num)

for i in nums[::-1]:
    print(i)


