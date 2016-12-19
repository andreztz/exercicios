
def soma_hipotenusas(n):
    hipotenusa = 1
    cat1 = 1
    cat2 = 1
    soma = 0
    resp = 0

    while hipotenusa <= n:
        while cat1 < hipotenusa:
            while cat2 < hipotenusa:
                if cat1 * cat1 + cat2 * cat2 == hipotenusa * hipotenusa:
                    resp = hipotenusa
                    soma += 1
                cat2 += 1
            cat2 = 1
            cat1 += 1
        hipotenusa += 1
    return resp



# print(soma_hipotenusas(6))
print(soma_hipotenusas(20))
