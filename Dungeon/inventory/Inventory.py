from .Item import Item
from .Weapon import Weapon
from .HealingSpell import HealingSpell

class Inventory:

    def __init__(self):
        self.weapons = []
        self.spells = []
        self.items = []
        self.health_potions = 1
        self.gold = 0

    def add_weapon(self, weapon):
        self.weapons.append(Weapon(weapon))

    def add_spell(self, name):
        self.spells.append(HealingSpell())

    def add_item(self, name):
        self.items.append(name)

    def list_weapons(self):
        for weapon in self.weapons:
            weapon.print_name()

    def list_items(self):
        for item in self.items:
            item.print_name()
