
title = 'pokeTest'

print(title)

poke = {'pokeName': 'name', 'health': 100}

pokeStats = {'att': 100, 'acc': 100, 'sp': 100, 'def': 100}

opponent = {'pokeName': 'rival', 'health': 100}

opponentStats = {'att': 100, 'acc': 100, 'sp': 100, 'def': 100}

nameSelection = True

gameSelection = 1

nameYES = 2

nameYES = True

pnameYES = 2

while gameSelection == 1:
    
    while nameYES == True:
        print('choose your name')
        mainCharName = input()
        print('Is '+mainCharName+' your name?')
        print('1) Yes')
        print('2) No')
        if input() == 2:
            nameYES = True
        else:
            nameYES = False
        
    # while pnameYES == 2:
    #     print('choose your poke name')
    #     pokeName = input()
    #     print('Is '+pokeName+' your poke name?')
    #     print('1) Yes')
    #     print('2) No')
    #     if input() ==2:
    #         pnameYES = 2
    #     else():
    #         nameYES = 1

    gameSelection = 0

    print('game start')

   