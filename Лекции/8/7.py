def create_dragon():
    global health
    health = 100

def dragon_get_damage(damage):
    global


def alive_dragon():
    return health > 0


def main():
    create_dragon()
    finish = False
    while not finish:
        print('My health', health, '.Hit me')
        damage = int(input())
        dragon_get_damage(damage)
        if not alive_dragon():
            finish = True
    print('You win!')

main() 
