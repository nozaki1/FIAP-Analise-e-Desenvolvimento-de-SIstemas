segunda = int(input("Informe a quantidade de votos na segunda: "))
terca = int(input("Informe a quantidade de votos na terça: "))
quarta = int(input("Informe a quantidade de votos na quarta: "))
quinta = int(input("Informe a quantidade de votos na quinta: "))
sexta = int(input("Informe a quantidade de votos na sexta: "))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("O dia escolhido foi a segunda-feira!")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("O dia escolhido foi a terça-feira!")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("O dia escolhido foi a quarta-feira!")
elif quinta > segunda and quinta > quarta and quinta > terca and quinta > sexta:
    print("O dia escolhido foi a quinta-feira!")
elif sexta > segunda and sexta > quarta and sexta > quinta and sexta > terca:
    print("O dia escolhido foi a sexta-feira!")
else:
    print("Houve um empate!")