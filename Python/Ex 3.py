voto1 = input("Voto do primeiro membro da equipe: ")
voto2 = input("Voto do segundo membro da equipe: ")
voto3 = input("Voto do terceiro membro da equipe: ")
voto4 = input("Voto do quarto membro da equipe: ")
voto5 = input("Voto do quinto membro da equipe: ")
playstation = 0
xbox = 0
switch = 0

if voto1.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto1.upper() == "XBOX":
    xbox = xbox + 1
elif voto1.upper() == "SWITCH":
    switch = switch + 1
else:
    print("O membro da equipe votou em um console inexistente e seu voto foi desconsiderado.")

if voto2.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto2.upper() == "XBOX":
    xbox = xbox + 1
elif voto2.upper() == "SWITCH":
    switch = switch + 1
else:
    print("O membro da equipe votou em um console inexistente e seu voto foi desconsiderado.")

if voto3.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto3.upper() == "XBOX":
    xbox = xbox + 1
elif voto3.upper() == "SWITCH":
    switch = switch + 1
else:
    print("O membro da equipe votou em um console inexistente e seu voto foi desconsiderado.")

if voto4.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto4.upper() == "XBOX":
    xbox = xbox + 1
elif voto4.upper() == "SWITCH":
    switch = switch + 1
else:
    print("O membro da equipe votou em um console inexistente e seu voto foi desconsiderado.")

if voto5.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto5.upper() == "XBOX":
    xbox = xbox + 1
elif voto5.upper() == "SWITCH":
    switch = switch + 1
else:
    print("O membro da equipe votou em um console inexistente e seu voto foi desconsiderado.")

if playstation > xbox and playstation > switch:
    print("O console mais votado foi o Playstation com {} votos!".format(playstation))
elif xbox > playstation and xbox > switch:
    print("O console mais votado foi o XBOX com {} votos!".format(xbox))
elif switch > playstation and switch > xbox:
    print("O console mais votado foi o Switch com {} votos!".format(switch))
else:
    print("Houve um empate!")