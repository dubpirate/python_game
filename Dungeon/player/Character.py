from random import randint
from Dungeon.inventory.Inventory import Inventory
from Dungeon.inventory.Weapon import Weapon
from Dungeon.inventory.HealingSpell import HealingSpell

class Character:
    def __init__(self, name, max_hp, speed, stealth, ac):
        self.inventory = Inventory()
        self.p_name = name

        self.max_hp = max_hp
        self.hp = max_hp
        self.speed = speed
        self.stealth = stealth
        self.ac = ac


    def choose_weapon(self):
        self.list_weapons()
        choice = str(input(" - "))
        for weapon in self.inventory.weapons:
            if weapon.name == choice:
                return weapon

    def choose_spell(self):
        choice = str(input(" - "))
        for spell in self.inventory.spells:
            if spell.name == choice:
                return spell

    def list_weapons(self):
        for weapon in self.inventory.weapons:
            weapon.print_name()

    def list_items(self):
        for item in self.inventory.items:
            item.print_name()

    def list_spells(self):
        for spell in self.inventory.spells:
            spell.print_name()

    def add_gold(self, amount):
        self.inventory.gold += amount

    def get_gold(self):
        return self.inventory.gold

class Rogue(Character):
    name = 'rogue'
    choice_1_description = '1: Knives ( 2 Damage ) + health potion'
    choice_2_description = '2: Knives ( 2 Damage ) + better cloak ( more actions )'

    def __init__(self, name):
        Character.__init__(self, name, 6, 3, 2, 0)
        self.subclass()

    def subclass(self):
        print(self.choice_1_description)
        print(self.choice_2_description)
        choice = int(input("- "))
        if choice == 1:
            self.choice_1()
        else:
            self.choice_2()

    def choice_1(self):
        self.inventory.add_weapon('knife')
        self.inventory.health_potions += 1

    def choice_2(self):
        self.inventory.add_weapon('knife')
        self.inventory.add_item('shawl of silence')
        self.stealth += 1

class Mage(Character):
    name = 'mage'
    choice_1_description = '1: One super damage spell ( 3 damage ) + health potion'
    choice_2_description = '2: One regular damage spell ( 2 damage ) + 1 healing spell'

    def __init__(self, name):
        Character.__init__(self, name, 8, 2, 1, 1)
        self.subclass()

    def subclass(self):
        print(self.choice_1_description)
        print(self.choice_2_description)
        choice = int(input("- "))
        if choice == 1:
            self.choice_1()
        else:
            self.choice_2()

    def choice_1(self):
        self.inventory.add_weapon('fireball')
        self.inventory.health_potions += 1

    def choice_2(self):
        self.inventory.add_weapon('frost ray')
        self.inventory.add_spell('healing spell')

class Warrior(Character):
    name = 'warrior'
    choice_1_description = '1: One long sword ( 5 damage )'
    choice_2_description = '2: One sword and sheild ( 3 damage, +1 AC )'

    def __init__(self, name):
        Character.__init__(self, name, 10, 1, 0, 2)
        self.subclass()

    def subclass(self):
        print(self.choice_1_description)
        print(self.choice_2_description)
        choice = int(input("- "))
        if choice == 1:
            self.choice_1()
        else:
            self.choice_2()

    def choice_1(self):
        self.inventory.add_weapon('long sword')

    def choice_2(self):
        self.inventory.add_weapon('broad sword')
        self.inventory.add_item('sheild')
        self.ac += 1
