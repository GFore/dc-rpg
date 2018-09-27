"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

# Step 7: The alive methods on Hero and Goblin should be identical. Move it into Character, and remove them from Hero and Goblin - now they can simply inherit it from Character.
# Step 7: Bonus Challenge: The methods attack and print_status method in Hero and Goblin look almost identical, but not quite. Is it possible to move them into the Character class as well? Give it a try

def main():

    class Character:
        def __init__(self, name, health, power):
            self.name = name
            self.health = health
            self.power = power

        def alive(self):
            return self.health > 0

        def attack(self, enemy):
            enemy.health -= self.power
            if self.name == 'hero':
                print("You do %d damage to the goblin." % self.power)
            else:
                print("The goblin does %d damage to you." % self.power)

        def print_status(self):
            if self.alive():
                if self.name == 'hero':
                    print("You have %d health and %d power." % (self.health, self.power))
                else:
                    print("The goblin has %d health and %d power." % (self.health, self.power))
            else:
                if self.name == 'hero':
                    print("You are dead.")
                else:
                    print("The goblin is dead.")


    hero = Character('hero', 10, 5)
    goblin = Character('goblin', 6, 2)


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
