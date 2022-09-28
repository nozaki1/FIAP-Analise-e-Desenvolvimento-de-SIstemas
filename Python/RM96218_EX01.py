faturamento = float(input("Por favor, informe o seu faturamento deste ano: "))
assinatura = input("Por favor, informe o nível de sua assinatura (basic, silver, gold ou platinum): ")
valor_bonus = float

if assinatura.upper() == 'BASIC':
    valor_bonus = faturamento * 0.3
elif assinatura.upper() == 'SILVER':
    valor_bonus = faturamento * 0.2
elif assinatura.upper() == 'GOLD':
    valor_bonus = faturamento * 0.1
elif assinatura.upper() == 'PLATINUM':
    valor_bonus = faturamento * 0.05
else:
    print("A assinatura digitada é inválida. Tente novamente.")

print("O valor do bônus a ser pago é de R${:.2f}.".format(valor_bonus))
