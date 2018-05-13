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
