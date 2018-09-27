"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

# Step 6: Do you see a lot of duplicated or similar code between Hero and Goblin? What if you can share the duplicated code between them? You can by using inheritance! Create a new class called Character and make both Hero and Goblin inherit from it.

def main():

    class Character:
        def __init__(self, name, health, power):
            self.name = name
            self.health = health
            self.power = power

    class Hero(Character):
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

    class Goblin(Character):
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


    hero = Hero('hero', 10, 5)
    goblin = Goblin('goblin', 6, 2)


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
