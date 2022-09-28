BPM = input("Informe o seu número de batimentos por minuto(BPM): ")
BPM = int(BPM)
idade = input("Informe a sua idade: ")
idade = int(idade)
if 0 <= idade <= 2 and BPM > 140:
    print("Atenção, seus batimentos estão ACIMA da faixa adequada.")
elif 0 <= idade <= 2 and BPM <120:
    print("Atenção, seus batimentos estão ABAIXO da faixa adequada.")
elif 0 <= idade <= 2 and 120 <= BPM <= 140:
    print("Parabéns! Seus batimentos estão DENTRO da faixa adequada!")

if 8 <= idade <= 17 and BPM > 100:
    print("Atenção, seus batimentos estão ACIMA da faixa adequada.")
elif 8 <= idade <= 17 and BPM < 80:
    print("Atenção, seus batimentos estão ABAIXO da faixa adequada.")
elif 8 <= idade <= 17 and 80 <= BPM <= 100:
    print("Parabéns! Seus batimentos estão DENTRO da faixa adequada!")

if 18 <= idade <= 60 and BPM > 80:
    print("Atenção, seus batimentos estão ACIMA da faixa adequada.")
elif 18 <= idade <= 60 and BPM < 70:
    print("Atenção, seus batimentos estão ABAIXO da faixa adequada.")
elif 18 <= idade <= 60 and 70 <= BPM <= 80:
    print("Parabéns! Seus batimentos estão DENTRO da faixa adequada!")

if idade > 60 and BPM > 60:
    print("Atenção, seus batimentos estão ACIMA da faixa adequada.")
elif idade > 60 and BPM < 50:
    print("Atenção, seus batimentos estão ABAIXO da faixa adequada.")
elif idade > 60 and 50 <= BPM <= 60:
    print("Parabéns! Seus batimentos estão DENTRO da faixa adequada!")







