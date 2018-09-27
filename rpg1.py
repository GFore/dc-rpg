"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

# Step 5: Take the code for printing the health status of the hero and move it into a method called print_status of Hero. Do the same for the goblin.

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

        def print_status(self):
            if self.alive():
                print("You have %d health and %d power." % (self.health, self.power))
            else:
                print("You are dead.")

    class Goblin:
        def __init__(self):
            self.health = 6
            self.power = 2

        def attack(self, enemy):
            enemy.health -= self.power
            print("The goblin does %d damage to you." % self.power)

        def alive(self):
            return self.health > 0

        def print_status(self):
            if self.alive():
                print("The goblin has %d health and %d power." % (self.health, self.power))
            else:
                 print("The goblin is dead.")


    hero = Hero()
    goblin = Goblin()


    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end='')
        user_input = input()
        if user_input == "1":               # Hero attacks goblin
            hero.attack(goblin)
            if not goblin.alive(): goblin.print_status()
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.alive():               # Goblin attacks hero
            goblin.attack(hero)
            if not hero.alive(): hero.print_status()

main()
