from random import randint
from .enemy.Enemy import Enemy
from .player.Character import *
from .area.Room import Room

class Game:

    players = []
    dead_players = []
    classes = {
        'mage':Mage,
        'rogue':Rogue,
        'warrior':Warrior}

    def run(self):
        self.init_players()

        while len(self.players) != 0:
            room = Room()
            room.start_combat()
            while (len(room.enemies) != 0):
                for player in self.players:
                    room.player_turn(player)
                self.players, self.dead_players = room.enemy_turn(self.players, self.dead_players)

            self.players = room.divy_treasure(self.players)

        self.game_over()

    def init_players(self):
        print('How many players? (1 - 3)')
        num_players = int(input('- '))

        for player in range(1,num_players+1):
                print('READY PLAYER', player)

                name = str(input('Name: '))

                self.players.append(self.class_select(name))

    def class_select(self, name):
        print('Choose a class: ')
        print(' Warrior: 10 HP, 2 AC, 0 stealth, 1 speed')
        print(' Mage:    8  HP, 1 AC, 1 stealth, 2 speed')
        print(' Rogue:   6  hp, 0 AC, 2 stealth, 3 speed\n')
        player_class = str(input('- '))

        return self.classes[player_class](name)


    def game_over(self):
        print('>>> GAME OVER <<< \n')
        for player in self.dead_players:
            print('Well done', player.p_name + '. You got', player.gold, 'gold. \n')
            _ = input('Hit return to finish')
