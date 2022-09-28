valor_bruto = float(input("Por favor, informe o valor bruto de sua viagem: "))
categoria = input("Por favor, informe a categoria dos assentos (econômica, executiva ou primeira classe): ")
qtd_viajantes = int(input("Por favor, informe a quantidade de viajantes: "))
valor_liquido = int
valor_medio = int
valor_desconto = int

#
if categoria == 'econômica':
    if qtd_viajantes == 2:
        valor_liquido = valor_bruto * 0.97
    elif qtd_viajantes == 3:
        valor_liquido = valor_bruto * 0.96
    elif qtd_viajantes >= 4:
        valor_liquido = valor_bruto * 0.95
elif categoria == 'executiva':
    if qtd_viajantes == 2:
        valor_liquido = valor_bruto * 0.95
    elif qtd_viajantes == 3:
        valor_liquido = valor_bruto * 0.93
    elif qtd_viajantes >= 4:
        valor_liquido = valor_bruto * 0.92
elif categoria == 'primeira classe':
    if qtd_viajantes == 2:
        valor_liquido = valor_bruto * 0.90
    elif qtd_viajantes == 3:
        valor_liquido = valor_bruto * 0.85
    elif qtd_viajantes >= 4:
        valor_liquido = valor_bruto * 0.80
else:
    print("Desculpe, não há desconto para a categoria selecionada.")
#
valor_medio = valor_liquido / qtd_viajantes
valor_desconto = valor_bruto - valor_liquido
print("Valor Bruto: R${:.2f}".format(valor_bruto))
print("Valor do Desconto: R${}".format(valor_desconto))
print("Valor Líquido da Viagem: R${:.2f}".format(valor_liquido))
print("Valor Médio por Viajante: R${:.2f}".format(valor_medio))









