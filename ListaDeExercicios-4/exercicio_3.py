def e_primo(num):
    primo = True
    div = 2

    while div < num:
        if num % div == 0:
            primo = False
            break
        div += 1

    if primo and num > 1:
        return True
    else:
        return False


def maior_primo(num):
    cont = num
    while cont > 0:
        if e_primo(cont):
            return cont
        cont -= 1
