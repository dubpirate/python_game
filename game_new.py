from random import randint

class Character:
    def __init__(self, name):
        self.weps = {}
        self.spells = {}
        self.items = {'health potion':2}
        self.gold = 0
        self.p_name = name

class Rogue(Character):
    name = 'rogue'
    max_hp = 6
    speed = 3
    stealth = 2

    def __init__(self, option, name):
        Character.__init__(self, name)
        self.hp = 6
        self.ac = 0
        if option == 1:
            self.choice_1()
        elif option == 2:
            self.choice_2()

    def choice_1(self):
        self.weps['knives'] = 2
        self.items['health potion'] += 1

    def choice_2(self):
        self.weps['knives'] = 2
        self.items['shawl of silence'] = 1
        self.stealth += 1

class Mage(Character):
    name = 'mage'
    max_hp = 8
    speed = 2
    stealth = 1

    def __init__(self, option, name):
        Character.__init__(self, name)
        self.hp = 8
        self.ac = 1
        if option == 1:
            self.choice_1()
        elif option == 2:
            self.choice_2()

    def choice_1(self):
        self.spells['super spell'] = 3
        self.items['health potion'] += 1

    def choice_2(self):
        self.spells['attack spell'] = 2
        self.spells['healing spell'] = 4

class Warrior(Character):
    name = 'warrior'
    max_hp = 10
    speed = 1
    stealth = 0

    def __init__(self, option, name):
        Character.__init__(self, name)
        self.hp = 10
        self.ac = 2
        if option == 1:
            self.choice_1()
        elif option == 2:
            self.choice_2()

    def choice_1(self):
        self.weps['big sword'] = 5

    def choice_2(self):
        self.weps['broad sword'] = 3
        self.items['sheild'] = 1
        self.ac += 1

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
        if weapon in ['exit', 'cancel', 'stop']:
            return None, None

        if weapon in player.weps:
            damage = player.weps[weapon]
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

    return damage, opponent

    _condition = False
    print('Your spells are:')
    for spell, damage in player.spells:
        if spell == 'healing spell':
            print('- Healing spell ( fuck yeah )')

        else:
            print('- {0} ( does {1} damage)'.format(spell, damage))

    print('')
    while _condition == False:
        print('What spell:')
        spell = str(input('- '))
        if spell in player.spells:
            damage = player.spells[spell]

        elif spell == 'none' or spell == 'exit' or spell == 'stop':
            return None, None

    while _condition == False:
        print('Who you attacken')
        target = str(input('- '))
        if target in numbered_opponents:
            print('{0} took {1} damage.'.format(target.title(), damage))

    return damage, target


"""
        ### Enemy data structures
        ###     opponents:          LIST of Enemy() instances, for
        ###     num_oppo:           INT of how many instances there are, for
        ###     numbered_opponents: DICT of instnaces, with number keys to each instance, for
"""

def spell(player, numbered_opponents):
    _condition = False
    while _condition == False:
        print('What spell bruh: ')
        spell = str(input('- '))
        if spell.lower() in player.spells:
            damage = player.spells[spell]
            print('\nWho you attacken bruh?')
            for key, val in sorted(numbered_opponents.items()):
                print(key ,':', val.name, '( HP:',val.hp,'Damage:',val.dam,')')

            target = int(input('- '))
            if target in ['exit','stop','quit','cancel']:
                return None, None

            if target in numbered_opponents:
                print('{0} took {1} damage.'.format(numbered_opponents[target].name, damage))
                return damage, target


#
#       END OF FUNCTION DEFINITIONS
#
#       COMMENCING SCRIPT
#


print('How many players? (1 - 3)')
num_players = int(input('- '))
players = []
dead_players = []
classes = {'mage':Mage,'rogue':Rogue,'warrior':Warrior}
options = {'warrior':'1: One big sword ( 5 damage )or \n2: One sword and sheild ( 3 damage, +1 AC)','mage':'1: One super damage spell ( 3 ) + health potion \n2: One regular damage spell ( 2 damage ) + 1 healing spell','rogue':'1: Knives + health potion \n2: Knives + better cloak'}
for player in range(1,num_players+1):
    print('READY PLAYER',player)
    name = str(input('Name: '))
    print('Choose a class: ')
    print(' Warrior: 10 HP, 2 AC, 0 stealth, 1 speed')
    print(' Mage: 8 HP, 1 AC, 1 stealth, 2 speed')
    print(' Rogue: 6 hp, 0 AC, 2 stealth, 3 speed\n')
    player_class = str(input('- '))
    if player_class.lower() in classes:
        print(options[player_class.lower()])
        option = int(input('- '))
        new_player = classes[player_class.lower()](option, name)
        players.append(new_player)

while bool(players) == True:
    first_run = True
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

    while bool(numbered_opponents) == True:
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
            if first_run == True:
                actions += player_1.stealth
                first_run = False

            while actions > 0:
                print('')
                print('You got',actions,'actions left')
                print('What you do:')
                print(' i: inventory \n a: attack \n h: use a health potion \n s: cast a spell \n e: end turn')
                choice = str(input('- '))
                if choice.lower() == 'i':
                    print("Items:",player_1.items,'\nWeapons:',str(player_1.weps))

                elif choice == 'e':
                    actions = 0

                elif choice.lower() == 's':
                    damage, target = spell(player_1, numbered_opponents)
                    if damage and target == None:
                        pass

                    else:
                        numbered_opponents[target].hp -= damage
                        if numbered_opponents[target].hp < 1:
                            print('\nThe',numbered_opponents[target].name,'died. \n')
                            #opponents.remove(target)
                            del numbered_opponents[target]
                            actions -= 1

                elif choice.lower() == 'a':
                    damage, target = attack(player_1, numbered_opponents)
                    if (damage and target) == None:
                        pass

                    else:
                        numbered_opponents[target].hp -= damage
                        if numbered_opponents[target].hp < 1:
                            print('\nThe',numbered_opponents[target].name,'died. \n')
                            del numbered_opponents[target]
                            #opponents.remove(target)
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
                    player.gold += loot

                _ = input('\nPress any key to continue')

            else:
                iter_val = 1
                for key, _enemy in numbered_opponents.items():
                    if _enemy.dam - player_1.ac <= 0:
                        print('\nThe', _enemy.name + "'s attack was uneffective and did no damage.")

                    else:
                        print('\nThe', _enemy.name, 'does', _enemy.dam - player_1.ac, 'damage.')
                        player_1.hp = player_1.hp - (_enemy.dam - player_1.ac)

                    iter_val += 1
                    print('You now have',player_1.hp,'health left \n')

                _ = input('Press any key to continue.')

            if player_1.hp <= 0:
                print('Shit son, you dead.')
                dead_players.append(player_1)
                players.remove(player_1)
                numbered_opponents = []

print('>>> GAME OVER <<< \n')
for player in dead_players:
    print('Well done',player.p_name +'. You got', player.gold,'gold. Well done. \n')
    _ = input('Hit return to finish')
