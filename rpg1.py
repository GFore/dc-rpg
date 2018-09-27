"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

# Make a Hero class to store the health and power of the hero, and make a Goblin class to store the health and power of the goblin. Use a hero object in place of the variables hero.health and hero.power and use a goblin object in place of the variables goblin.health and goblin.power all through out the app.

def main():

    class Character:
        def __init__(self, name, health, power):
            self.name = name
            self.health = health
            self.power = power

    hero = Character('hero', 10, 5)
    goblin = Character('goblin', 6, 2)


    while goblin.health > 0 and hero.health > 0:
        print("You have %d health and %d power." % (hero.health, hero.power))
        print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            goblin.health -= hero.power
            print("You do %d damage to the goblin." % hero.power)
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            hero.health -= goblin.power
            print("The goblin does %d damage to you." % goblin.power)
            if hero.health <= 0:
                print("You are dead.")

main()
