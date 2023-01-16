class Dragon:

    def __init__(self, name):
        self.name = name
        self.health = 100

    def alive(self):
        return self.health > 0

    def get_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def talk(self):
        print(self.name, 'health', self.health, '.Hit me')


def main():
    enemy_list = [Dragon('Smouge'), Dragon('Hidra')]
    finish = False
    while not finish:
        enemy = enemy_list[0]
        enemy.talk()
        damage = int(input())
        enemy.get_damage(damage)
        if not enemy.alive():  # Удалить из списка мёртвого врага
            enemy_list.pop(0)
        if not enemy_list:  # Пусть ли список врагов
            finish = True
    print('You w0n!')


main()
