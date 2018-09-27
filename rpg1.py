"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

# Step 4: Refactor the while condition:
#       while goblin.health > 0 and hero.health > 0:
# to
#       while goblin.alive() and hero.alive():
# The health checks should be moved to within the alive methods of Hero and Goblin respectively.

def main():

    # class Character:
    #     def __init__(self, name, health, power):
    #         self.name = name
    #         self.health = health
    #         self.power = power

    class Hero:
        def __init__(self):
            self.health = 10
            self.power = 5

        def attack(self, enemy):
            enemy.health -= self.power
            print("You do %d damage to the goblin." % self.power)

        def alive(self):
            return self.health > 0

    class Goblin:
        def __init__(self):
            self.health = 6
            self.power = 2

        def attack(self, enemy):
            enemy.health -= self.power
            print("The goblin does %d damage to you." % self.power)

        def alive(self):
            return self.health > 0

    hero = Hero()
    goblin = Goblin()


    while goblin.alive() and hero.alive():
        print("You have %d health and %d power." % (hero.health, hero.power))
        print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end='')
        user_input = input()
        if user_input == "1":               # Hero attacks goblin
            hero.attack(goblin)
            if not goblin.alive():
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.alive():               # Goblin attacks hero
            goblin.attack(hero)
            if not hero.alive():
                print("You are dead.")

main()
