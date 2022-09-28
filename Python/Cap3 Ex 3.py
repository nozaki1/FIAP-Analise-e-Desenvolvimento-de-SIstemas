resposta = int(input("Digite um número inteiro para verificar se ele faz parte da sequência de Fibonnaci: "))
#fibonacci
anterior1 = 1
anterior2 = 0
for x in range(1,resposta+1,1):
    atual = anterior1 + anterior2
    anterior2 = anterior1
    anterior1 = atual
    if resposta == atual:
        print("Faz parte!")
        break
    elif resposta < atual:
        print("O número não faz parte da sequência.")
        break


