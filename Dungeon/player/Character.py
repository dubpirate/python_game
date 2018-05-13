from random import randint

class Character:
    def __init__(self, name, max_hp, speed, stealth, ac):
        self.weps = {}
        self.spells = {}
        self.items = {'health potion':2}
        self.gold = 0
        self.p_name = name

        self.max_hp = max_hp
        self.hp = max_hp
        self.speed = speed
        self.stealth = stealth
        self.ac = ac

    def attack(self, enemies, type):
        if type == 'weapons':
            attack_type = self.weps
        else:
            attack_type = self.spells

        print('Your ', type + ':')
        print_item_options(attack_type)

        print('Choose your', type + ':')
        choice = str(input('- '))

        if choice.lower() in attack_type:
            return attack_type[choice]

        return 0

    def print_item_options(self, group):
        for item, _ in group:
            print(' > ', item)

class Rogue(Character):
    name = 'rogue'
    choice_1_description = '1: Knives ( 2 Damage ) + health potion'
    choice_2_description = '2: Knives ( 2 Damage ) + better cloak'

    def __init__(self, name):
        Character.__init__(self, name, 6, 3, 2, 0)
        subclass

    def subclass():
        print(self.choice_1_description)
        print(self.choice_2_description)
        choice = int(input("- "))
        if choice == 1:
            choice_1()
        else:
            choice_2()

    def choice_1(self):
        self.weps['knives'] = 2
        self.items['health potion'] += 1

    def choice_2(self):
        self.weps['knives'] = 2
        self.items['shawl of silence'] = 1
        self.stealth += 1

class Mage(Character):
    name = 'mage'
    choice_1_description = '1: One super damage spell ( 3 damage ) + health potion'
    choice_2_description = '2: One regular damage spell ( 2 damage ) + 1 healing spell'

    def __init__(self, name):
        Character.__init__(self, name, 8, 2, 1, 1)
        subclass()

    def subclass():
        print(self.choice_1_description)
        print(self.choice_2_description)
        choice = int(input("- "))
        if choice == 1:
            choice_1()
        else:
            choice_2()

    def choice_1(self):
        self.spells['super spell'] = 3
        self.items['health potion'] += 1

    def choice_2(self):
        self.spells['attack spell'] = 2
        self.spells['health potion'] += 2

class Warrior(Character):
    name = 'warrior'
    choice_1_description = '1: One big sword ( 5 damage )'
    choice_2_description = '2: One sword and sheild ( 3 damage, +1 AC )'

    def __init__(self, name):
        Character.__init__(self, name, 10, 1, 0, 2)
        subclass()

    def subclass():
        print(self.choice_1_description)
        print(self.choice_2_description)
        choice = int(input("- "))
        if choice == 1:
            choice_1()
        else:
            choice_2()

    def choice_1(self):
        self.weps['big sword'] = 5

    def choice_2(self):
        self.weps['broad sword'] = 3
        self.items['sheild'] = 1
        self.ac += 1
