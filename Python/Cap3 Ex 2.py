qtd_transacoes = int(input("Informe quantas transações financeiras você realizou hoje: "))
valor_total = float(0)
for transacao in range(1,qtd_transacoes +1,1):
    valor_atual = float(input("Informe o valor gasto na {} transação: ".format(transacao)))
    valor_total = valor_total + valor_atual
valor_medio = float(valor_total / qtd_transacoes)
print("O valor total gasto hoje foi de R${:.2f}, com um valor médio de R${:.2f} para cada transação.".format(valor_total,valor_medio ))
