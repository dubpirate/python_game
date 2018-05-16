from .Item import Item

class HealingSpell(Item):

    def __init__(self):
        Item.__init__(self, "Healing Spell")

    def cast(self, target):
        print("You heal", target.p_name, end='')

        if target.hp >= target.max_hp - 4:
            target.hp = target.max_hp
            print('to full health. (', str(target.hp),'HP )')
            return target

        target.hp = target.hp + 4
        print('for 4 health. (', str(target.hp), 'HP )')
        return target
