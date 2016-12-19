def imprime_matriz(minha_matriz):
    for linha, obj_linha in enumerate(minha_matriz):
        for col, obj_col in enumerate(obj_linha):
            if col == len(obj_linha) -1:
                print(obj_col, )
            else:
                print(obj_col, end=" ")

