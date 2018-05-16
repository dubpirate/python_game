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
            print(self.intros[i].format(
                self.enemies[i].name,
                self.enemies[i].weapon_name()))

        _ = input("(press any key to continue)")

    def player_actions(self, player):
        if self.first_run:
            self.first_run = False
            return player.stealth + player.speed

        return player.speed

    def player_turn(self, player):
        print('\nYour turn,', player.p_name)
        actions = self.player_actions(player)

        while actions > 0 and len(self.enemies) > 0:
            print('You got', actions, 'actions left.')
            print(' i: inventory \n a: attack \n s: cast a spell')
            print(' h: use a health potion \n e: end turn')
            choice = str(input('- '))

            if choice.lower() == 'i':
                player.inventory.list_items()

            elif choice.lower() == 'a':
                self.player_attack(player)

            elif choice.lower() == 's':
                self.player_cast_spell(player)

            elif choice.lower() == 'h':
                print('\nYou used a health potion to heal. \n')
                player.inventory.health_potions -= 1
                player.hp = player.max_hp
                print('You are at Full Health! ('+ str(player.hp) +')\n')
                actions -= 1

            elif choice == 'e':
                actions = 0

            actions -= 1
            _ = input('Press any key to continue.')

    def player_attack(self, player):
        weapon = player.choose_weapon()

        print('\nWho do you want to attack:')
        self.print_enemies()
        target = int(input('- '))

        self.enemies[target].hp -= weapon.damage
        print(self.enemies[target].name, "takes", weapon.damage, "points of damage", end='')

        if self.enemies[target].hp < 1:
            print(' and dies. \n')
            del self.enemies[target]
        else:
            print('.\n')

    def player_cast_spell(self, player):
        print('Choose your Spell:')
        player.list_spells()
        spell = player.choose_spell()

        print('Who do you want to cast it on:')
        target = self.print_players()

        players.remove(target)
        players.append(spell.cast(target))

    def print_enemies(self):
        for enemy in self.enemies:
            print("("+str(self.enemies.index(enemy))+")",enemy.name)


    def choose_players(self):
        for player in self.players:
            print("("+str(self.players.index(player))+")",player.p_name)

        return players[int(input('- '))]

    def enemy_turn(self, players, dead_players):
        for enemy in self.enemies:
            if len(players) > 0:
                chosen = randint(0,len(players)-1)
                if (enemy.attack() - players[chosen].ac <= 0):
                    print('\nThe', enemy.name + "'s attack was uneffective and did no damage.")

                else:
                    players[chosen].hp -= enemy.attack() - players[chosen].ac
                    print('\nThe', enemy.name, 'does', enemy.attack() - players[chosen].ac, 'damage.')
                    if players[chosen].hp <= 0:
                        print('oh no,', players[chosen].p_name, 'died')
                        dead_players.append(players[chosen])
                        players.remove(players[chosen])
                        break

                    else:
                        print('You now have', players[chosen].hp, 'health left')

        _ = input("(press any key to continue)")
        return players, dead_players

    def divy_treasure(self, players):
        print("The room is quiet. You find", self.loot, "pieces of gold.")
        for player in players:
            player.add_gold(self.loot)

        _ = input("(press any key to continue)")
        return players
