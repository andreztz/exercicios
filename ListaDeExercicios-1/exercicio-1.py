
nome_cliente = input('Digite o nome do cliente: ')

dia_vencimento = input('Digite o dia de vencimento: ')

mes_vencimento = input('Digite o mês de vencimento: ')

valor_fatura = input('Digite o valor da fatura: ')


print("Olá, {}".format(nome_cliente))
print("A sua fatura com vencimento em {} de {} no valor de R$ {} está fechada.".format(dia_vencimento, mes_vencimento, valor_fatura))
