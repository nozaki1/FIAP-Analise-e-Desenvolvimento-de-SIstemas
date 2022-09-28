adobe = [2013, 10, 'Adobe', 'email', 'dica_senha', 'senha', 'nome']
aipai_com = [2016, 9, 'Aipai.com', 'email', 'senha']
ancestry = [2015, 11, 'Ancestry', 'email', 'senha']
anime_game = [2020, 2, 'Anime Game', 'email', 'nome', 'senha']
cafe_mom = [2014, 4, 'CafeMom', 'email', 'senha']
catho = [2020, 3, 'Catho', 'email', 'nome', 'senha']
cdek = [2022, 3, 'CDEK', 'email', 'nome', 'telefone']
dangdang = [2011, 6, 'Dangdang', 'email']
descomplica = [2021, 3, 'Descomplica', 'email', 'nome', 'senha']
dropbox = [2012, 7, 'Dropbox', 'email', 'senha']
dubsmash = [2018, 12, 'Dubsmash', 'email', 'nome', 'senha']
forbes = [2014, 2, 'Forbes', 'email', 'nome', 'senha']
gamingo = [2012, 3, 'Gamingo', 'email', 'senha']
linkedin = [2012, 5, 'Linkedin', 'email', 'senha']
mathway = [2020, 1, 'Mathway', 'email', 'nome', 'senha']

lista = [adobe, aipai_com, ancestry, anime_game, cafe_mom, catho, cdek, dangdang, descomplica, dropbox, dubsmash,
         forbes, gamingo, linkedin, mathway]

empresas = lista

# vazou a senha ou dica da senha criticidade 1
peso1 = []
# vazou o telefone ou nome criticidade 2
peso2 = []
# vazou o e-mail criticidade 3
peso3 = []

# ordenação por peso de vazamento
for empresa in empresas:
    if 'senha' in empresa or 'dica_senha' in empresa:
        peso1.append(empresa)
    elif 'telefone' in empresa or 'nome' in empresa:
        peso2.append(empresa)
    elif 'email' in empresa:
        peso3.append(empresa)

# ordenação por data de vazamento
peso1.sort(reverse=True)
peso2.sort(reverse=True)
peso3.sort(reverse=True)


# função para a saída com as informações de nome da empresa, e data (mês e ano)
def mostra_ranking(peso):
    for x in range(len(peso)):
        print(f'{peso[x][2]} em {peso[x][1]}/{peso[x][0]}')


print('Das empresas com vazamento de criticidade 1 (senha e/ou dica da senha) estão:')
mostra_ranking(peso1)

print('\nDas empresas com vazamento de criticidade 2 (telefone e/ou nome) estão:')
mostra_ranking(peso2)

print('\nDas empresas com vazamento de criticidade 3 (endereço de e-mail) estão:')
mostra_ranking(peso3)
