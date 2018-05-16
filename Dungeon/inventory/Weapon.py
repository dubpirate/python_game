from .Item import Item
class Weapon(Item):

    def __init__(self, name):
        Item.__init__(self, name)

        if name == "knife":
            self.damage = 2

        if name == "broad sword":
            self.damage = 3

        if name == "long sword":
            self.damage = 5

        if name == "fireball":
            self.damage = 3

        if name == "frost ray":
            self.damage = 2

    def print_name(self):
        message = " that does " + str(self.damage) + " damage."
        Item.print_name(self, message)
