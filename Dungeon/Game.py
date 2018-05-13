from random import randint
from enemy.Enemy import Enemy
from player.Character import *

class Game:

    players = []
    dead_players = []
    classes = {
        'mage':Mage,
        'rogue':Rogue,
        'warrior':Warrior}

    def __init__(self):
        run()

    def run(self):
        init_players()
        while len(players) != 0:
            pass

    def init_players(self):
        print('How many players? (1 - 3)')
        num_players = int(input('- '))

        for player in range(1,num_players+1):
                print('READY PLAYER', player)

                name = str(input('Name: '))

                class_select(player, name)

    def class_select(self, player):
        print('Choose a class: ')
        print(' Warrior: 10 HP, 2 AC, 0 stealth, 1 speed')
        print(' Mage:    8  HP, 1 AC, 1 stealth, 2 speed')
        print(' Rogue:   6  hp, 0 AC, 2 stealth, 3 speed\n')
        player_class = str(input('- '))

        return classes[player_class]()




while bool(players) == True:
    first_run = True

    room(num_oppo, opponents)
    numbered_opponents = {}
    key_num = 1
    for _enemy in opponents:
        numbered_opponents[key_num] = _enemy
        key_num += 1

    _ = input('\nPress any key to continue')

    while bool(numbered_opponents) == True:
        if bool(numbered_opponents) == False:
            print('The room is quiet. \n')
            print('In the rubble you each find',loot,'pieces of gold.')
            for player in players:
                player.gold += loot

            _ = input('\nPress any key to continue')


            if player.hp <= 0:
                print('Shit son, you dead.')
                dead_players.append(player_1)
                players.remove(player_1)
                numbered_opponents = []

print('>>> GAME OVER <<< \n')
for player in dead_players:
    print('Well done', player.p_name + '. You got', player.gold, 'gold. \n')
    _ = input('Hit return to finish')
