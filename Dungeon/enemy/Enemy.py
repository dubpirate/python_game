from random import randint

class Enemy:
    def __init__(self):
        _types = ['Gnome', 'Orc', 'Goblin', 'Rat', 'Skellington']
        _weps = ['Knife', 'Sword', 'Stick', 'Pie']
        self.hp = randint(5,10)
        self.name = _types[randint(0,4)]
        self.wep = _weps[randint(0,3)]
        self.dam = randint(2,4)
