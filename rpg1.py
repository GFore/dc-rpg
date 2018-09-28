"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

# Step 8: Bonus Challenge 2: Create a zombie character that cannot die and have it fight the hero instead of the goblin.

def main():

    def menu_choice(ename):
        print()
        print("What do you want to do?")
        print("1. fight " + ename)
        print("2. do nothing")
        print("3. flee")
        print("> ", end='')
        return input()

    class Character:
        def __init__(self, name, health, power):
            self.name = name
            self.health = health
            self.power = power

        def alive(self):
            return self.health > 0

        def attack(self, enemy):
            if enemy.name != 'zombie':
                enemy.health -= self.power
            if self.name == 'hero':
                print("You do %d damage to the %s." % (self.power if enemy.name != 'zombie' else 0, enemy.name))
            else:
                print("The %s does %d damage to you." % (self.name, self.power))

        def print_status(self):
            if self.alive():
                whohas = "You have" if self.name == 'hero' else "The %s has" % (self.name)
                print('%s %d health and %d power.' % (whohas, self.health, self.power))
            else:
                print("You are dead." if self.name == 'hero' else "The %s is dead." % (self.name))

    hero = Character('hero', 10, 5)
    zombie = Character('zombie', 6, 2)
    goblin = Character('goblin', 6, 2)
 
    try:
        enemy_choice = int(input("Enemy? 1) Goblin or 2) Zombie: "))
        if enemy_choice == 1:
            enemy = goblin
        else:
            enemy = zombie
    except:
        enemy = goblin

    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        user_input = menu_choice(enemy.name)

        if user_input == "1":               # Hero attacks
            hero.attack(enemy)
            if not enemy.alive(): enemy.print_status()
        elif user_input == "3":
            print("Goodbye.")
            break
        else: print("Invalid input %r" % (user_input))

        if enemy.alive(): enemy.attack(hero)         # enemy attacks hero    
        
        if not hero.alive(): hero.print_status()

main()
