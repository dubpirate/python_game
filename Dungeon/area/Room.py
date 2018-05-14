from random import randint
from Dungeon.enemy.Enemy import Enemy

class Room:

    def __init__(self):
        self.first_run = True
        self.enemies = self.generate_enemies()
        self.loot = randint(10, 50)
        self.intros = [
            '- A spoopy {0} with a {1}',
            '- Followed by a {0} holding a {1}',
            '- With his friend the {0} carrying a {1}' ]

    def generate_enemies(self):
        # This returns a list of Enemies
        _enemies = [Enemy()]
        for i in range(0, randint(0,2)):
            _enemies.append(Enemy())

        return _enemies

    def start_combat(self):
        print('\nIn the room, there is:')
        for i in range(0, len(self.enemies)):
            print(intros[i].format(
                enemies[i].name,
                enemies[i].wep))

    def player_actions(self, player):
        if self.first_run:
            self.first_run = False
            return player.stealth + player.speed

        return player.speed

    def player_turn(self, player, first_run):
        print('\nYour turn,', player.p_name)
        actions = self.player_actions(player)

        while actions > 0:
            print('You got', actions, 'actions left.')
            print(' i: inventory \n a: attack \n h: use a health potion \n s: cast a spell \n e: end turn')
            choice = str(input('- '))

            if choice.lower() == 'i':
                print("Items:", player.items, '\nWeapons:', str(player.weps), '\nSpells', str(player.spells))

            elif choice.lower() in ['s', 'a']:
                self.player_attack(choice, player)

            elif choice.lower() == 'h':
                print('\nYou used a health potion to heal. \n')
                player_1.hp = player_1.max_hp
                print('You have', player_1.hp, 'health points left. \n')
                actions -= 1

            elif choice == 'e':
                actions = 0

            _ = input('Press any key to continue.')

    def player_attack(self, choice, player):
        if choice.lower() == 's':
            type = 'spells'
        else:
            type = 'weapons'

        damage = player.attack(enemies, type)

        if damage == 0:
            pass
        else:
            numbered_opponents[target].hp -= damage
            actions -= 1
            if numbered_opponents[target].hp < 1:
                print('\nThe',numbered_opponents[target].name,'died. \n')
                del numbered_opponents[target]

    def enemy_turn(self, players, dead_players):
        for enemy in enemies:
            chosen = randint(0,len(players))
            if (enemy.dam - players[chosen].ac <= 0):
                print('\nThe', enemy.name + "'s attack was uneffective and did no damage.")

            else:
                players[chosen].hp -= enemy.dam - players[chosen].ac
                print('\nThe', enemy.name, 'does', enemy.dam - players[chosen].ac, 'damage.')
                if players[chosen].hp < 0:
                    print('oh no,', player[chosen].hp, 'died')
                    dead_players.append(players[chosen])
                    player.remove(chosen)

                else:
                    print('You now have', players[chosen].hp, 'health left \n')

        return players, dead_players

        _ = input('Press any key to continue.')

    def divy_treasure(self, players):
        print("The room is quiet. You each find", this.loot)
        for player in players:
            player.gold += self.loot

        return players
