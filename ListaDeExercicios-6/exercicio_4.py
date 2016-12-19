def remove_repetidos(lista):
    lista = list(set(lista))
    lista.sort()
    return lista

print(remove_repetidos([12, 12, 1, 2, 3, 3, 4, 5]))
print(remove_repetidos([7,3,33,12,3,3,3,7,12,100]))
