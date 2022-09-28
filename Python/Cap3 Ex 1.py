qtd_alimentos = int(input("Quantos alimentos você consumiu hoje? "))
total_calorias = 0
atual_caloria = 0
for alimento in range(1,qtd_alimentos + 1):
    atual_caloria = int(input("Informe o número de calorias do {} alimento: ".format(alimento)))
    total_calorias = int(total_calorias) + int(atual_caloria)
print("O total de calorias consumidas hoje foi de {}.".format(total_calorias))

