total_impar = 0
total_par = 0

for x in range(1,50,2):
    nota = float(input("VOCE ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES""\nPOR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(x)))
    total_impar = float(total_impar + nota)

for x in range(2,51,2):
    nota = float(input("VOCE ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES""\nPOR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(x)))
    total_par = float(total_par + nota)

media_impar = float(total_impar / 25)
media_par = float(total_par / 25)
print("A média da metade ímpar foi de {:.1f}.".format(media_impar))
print("A média da metade par foi de {:.1f}.".format(media_par))
if media_impar > media_par:
    print("A metade ímpar teve a maior média.")
elif media_par > media_impar:
    print("A metade par teve a maior média.")
else:
    print("As médias foram iguais.")