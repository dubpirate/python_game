from random import randint

class Character:
    def __init__(self, player_num):
        print('\nREADY PLAYER', player_num)
        self.p_name = str(input('Name:'))
        self.inventory = {'weps':{},'items':{'health potion':2}, 'gold':0}
        print('\nclasses')
        print(' Warrior: 10 HP, 2 AC, 0 stealth, 1 speed')
        print(' Mage: 8 HP, 1 AC, 1 stealth, 2 speed')
        print(' Rogue: 6 hp, 0 AC, 2 stealth, 3 speed')
        dave = False
        while dave == False:
            self.p_class = str(input('class:'))
            dave = self.setup(self.p_class.lower())

    def bonus(self, bools):
        if bools[0] == True:
            self.stealth += 1
        elif bools[1] == True:
            self.speed += 1
        elif bools[2] == True:
            self.ac += 1
        elif bools[3] == True:
            self.hp += 1
        elif bools[4] == True:
            self.inventory['items']['health potion'] += 1
        elif bools[5] == True:
            self.inventory['weps']['Health Spell'] = 2

    def setup(self,clss):
        """
            Class dic works like:
            After Name:
                0=[stealth, speed, ac, hp],
                1= The option prompts to print,
                2.0= first option
                2.1= List of Bools. Bools go 0:stealth, 1:speed, 2:ac, 3:HP, 4: health potion, 5: Health spell
        """
        classes = {
            'warrior':
            [
            [0,1,2,10],
            '1: One big sword ( 5 damage )or \n2: One sword and sheild ( 3 damage, +1 AC)',
            [
            [['Big sword',5], [False,False,False,False,False,False]],
            [['Sword', 3], [False,False,True,False,False,False]]
            ]
            ],

            'mage':
            [
                [1,2,1,8],
                '1: One super damage spell ( health ) + health potion \n2: One regular damage spell ( 2 damage ) + 1 healing spell',
                [
                    [
                        ['Super Spell',4],
                        [False,False,False,False,True,False]
                    ],
                    [
                        ['Attack Spell',2],
                        [False,False,False,False,False,True]
                    ]
                ]
            ],
            'rogue':
            [
                [2,3,0,6],
                '1: Knives + health potion \n2: Knives + better cloak',
                [
                    [
                        ['Knives',2],
                        [False,False,False,False,True,False]
                    ],
                    [
                        ['Knives',2],
                        [True,False,False,False,False,False]
                    ]
                ]
            ]
            }

        if clss in classes:
            self.stealth = classes[clss][0][0]
            self.speed = classes[clss][0][1]
            self.ac = classes[clss][0][2] #ac stands for Armour Class
            self.hp = classes[clss][0][3]
            self.max_hp = classes[clss][0][3]
            print(classes[clss][1])
            choice = int(input('- '))
            if choice == 1:
                self.inventory['weps'][classes[clss][2][0][0][0]] = classes[clss][2][0][0][1]
                #print(classes[clss][2][0][0][0], classes[clss][2][0][0][1])
                self.bonus(classes[clss][2][0][1])
                #print(classes[clss][2][0][1])
                return True
            elif choice == 2:
                self.inventory['weps'][classes[clss][2][1][0][0]] = classes[clss][2][1][0][1]
                #print(classes[clss][2][1][0][0], classes[clss][2][1][0][1])
                self.bonus(classes[clss][2][1][1])
                #print(classes[clss][2][1][1])
                return True
        return False

    def setup(self,clss):
        """
            Class dic works like:
            After Name:
                0=[stealth, speed, ac, hp],
                1= The option prompts to print,
                2.0= first option
                2.1= List of Bools. Bools go 0:stealth, 1:speed, 2:ac, 3:HP, 4: health potion, 5: Health spell
        """
        classes = {
            'warrior':
            [
            [0,1,2,10],
            '1: One big sword or \n2: One sword and sheild',
            [
            [['big sword',5], [False,False,False,False,False,False]],
            [['sword', 3], [False,False,True,False,False,False]]
            ]
            ],

            'mage':
            [
                [1,2,1,8],
                '1: One super damage spell + health potion \n2: One reg damage spell + 1 healing spell',
                [
                    [
                        ['super spell',4],
                        [False,False,False,False,True,False]
                    ],
                    [
                        ['attack spell',2],
                        [False,False,False,False,False,True]
                    ]
                ]
            ],
            'rogue':
            [
                [2,3,0,6],
                '1: Knives + health potion \n2: Knives + better cloak',
                [
                    [
                        ['knives',2],
                        [False,False,False,False,True,False]
                    ],
                    [
                        ['knives',2],
                        [True,False,False,False,False,False]
                    ]
                ]
            ]
            }

        if clss in classes:
            self.stealth = classes[clss][0][0]
            self.speed = classes[clss][0][1]
            self.ac = classes[clss][0][2] #ac stands for Armour Class
            self.hp = classes[clss][0][3]
            print(classes[clss][1])
            choice = int(input('- '))
            if choice == 1:
                self.inventory['weps'][classes[clss][2][0][0][0]] = classes[clss][2][0][0][1]
                #print(classes[clss][2][0][0][0], classes[clss][2][0][0][1])
                self.bonus(classes[clss][2][0][1])
                #print(classes[clss][2][0][1])
                return True
            elif choice == 2:
                self.inventory['weps'][classes[clss][2][1][0][0]] = classes[clss][2][1][0][1]
                #print(classes[clss][2][1][0][0], classes[clss][2][1][0][1])
                self.bonus(classes[clss][2][1][1])
                #print(classes[clss][2][1][1])
                return True
        return False

class Enemy:
    def __init__(self):
        _types = ['Gnome', 'Orc', 'Goblin', 'Rat', 'Skellington']
        _weps = ['Knife', 'Sword', 'Stick', 'Pie']
        self.hp = randint(5,10)
        self.name = _types[randint(0,4)]
        self.wep = _weps[randint(0,3)]
        self.dam = randint(2,4)

def room(num_oppo, opponents):
    print('\nIn the room, there is:')
    intros = ['- A spoopy {0} with a {1}', '- Followed by a {0} holding a {1}', '- With his friend the {0} carrying a {1}']
    _enemy_iter = 0
    for number in range(0,len(opponents)):
        print(intros[_enemy_iter].format(opponents[_enemy_iter].name,opponents[_enemy_iter].wep))
        _enemy_iter += 1

def attack(player, numbered_opponents):
    _condition = False
    while _condition == False:
        print('What fight with bruh')
        weapon = str(input('- '))
        weapon = weapon.lower()
        if weapon == 'exit' or weapon == 'quit' or weapon == 'stop':
            return None, None
        if weapon in player.inventory['weps']:
            damage = player.inventory['weps'][weapon]
            _condition = True

    _condition = False
    while _condition == False:
        print('Who you attacking.')
        for key, val in sorted(numbered_opponents.items()):
            print(key ,':', val.name, '( HP:',val.hp,'Damage:',val.dam,')')

        try:
            opponent = int(input('- '))

        except ValueError:
            print('Try again')

        if opponent in numbered_opponents:
            print('The',numbered_opponents[opponent].name,'took',damage,'damage.')
            _condition = True

    #if numbered_opponents[opponent].hp < 1:
    #    _ = input('Press any key to continue. \n')

    return damage, opponent


"""
        ### Enemy data structures
        ###     opponents:          LIST of Enemy() instances, for
        ###     num_oppo:           INT of how many instances there are, for
        ###     numbered_opponents: DICT of instnaces, with number keys to each instance, for
"""

print('How many players? (1 - 3)')
num_players = int(input('- '))
players = []
dead_players = []
for player in range(1,num_players+1):
    players.append(Character(player))

while bool(players) == True:
    enemies = randint(1,3) # Chooses how many enemies to create
    loot = randint(10, 50)
    num_oppo = enemies
    opponents = [] # We add each new enemy to this because we don't know how many enemeis we'll have
    enemy_1 = Enemy() # Makes the first enemy
    opponents.append(enemy_1) # Adds it to the list
    enemies -= 1 # takes off one to create
    if enemies >= 1:
        enemy_2 = Enemy()
        opponents.append(enemy_2)
        enemies -= 1
        if enemies >= 0:
            enemy_3 = Enemy()
            opponents.append(enemy_3)

    room(num_oppo, opponents)
    numbered_opponents = {}
    key_num = 1
    for _enemy in opponents:
        numbered_opponents[key_num] = _enemy
        key_num += 1

    _ = input('\nPress any key to continue')

    for player_1 in players:
        print('\nYour turn',player_1.p_name)
        '''
            _choices = {
            'a':attack,
            'h':heal,
            'n':nothing
            }
        '''
        actions = player_1.speed
        while actions > 0:
            print('')
            print('You got',actions,'actions left')
            print('What you do:')
            print(' i: inventory \n a: attack \n h: use a health potion \n')
            choice = str(input('- '))
            if choice.lower() == 'i':
                print("Items:",player_1.inventory['items'],'\nWeapons:',str(player_1.inventory['weps']))

            elif choice.lower() == 'a':
                damage, target = attack(player_1, numbered_opponents)
                if damage == None and target == None:
                    break
                numbered_opponents[target].hp -= damage
                if numbered_opponents[target].hp < 1:
                    print('\nThe',numbered_opponents[target].name,'died. \n')
                    del numbered_opponents[target]
                actions -= 1

            elif choice.lower() == 'h':
                print('\nYou used a health potion to heal. \n')
                player_1.hp = player_1.max_hp
                print('You have',player_1.hp,'health points left. \n')
                actions -= 1
            _ = input('Press any key to continue.')

        if bool(numbered_opponents) == False:
            print('The room is quiet. \n')
            print('In the rubble you each find',loot,'pieces of gold.')
            for player in players:
                player.inventory['gold'] += loot
            _ = input('\nPress any key to continue')

        else:
            iter_val = 0
            for item in numbered_opponents:
                if opponents[iter_val].dam - player_1.ac <= 0:
                    print(' The', opponents[iter_val].name + "'s attack was uneffective and did no damage.")
                else:
                    print(' The', opponents[iter_val].name, 'does',opponents[iter_val].dam - player_1.ac, 'damage.')
                    player_1.hp = player_1.hp - (opponents[iter_val].dam - player_1.ac)
                iter_val += 1
                print('\nYou now have',player_1.hp,'health left')
                _ = input('Press any key to continue.')

        if player_1.hp <= 0:
            print('Shit son, you dead.')
            _ = input('Press any key to continue.')
            dead_players.append(player_1)
            del player_1



print('>>> GAME OVER <<< \n')
for player in dead_players:
    print('Well done',player.p_name,'. You got', player.inventory['gold'],'gold. Well done. \n')
    _ = input('Hit return to continue')
