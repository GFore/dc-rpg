"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

# Step 3: Similarly, take the code for the goblin attacking the hero and extract it into a method (also call it attack) of the Goblin class. Replace the existing code with a call to the attack method. It should look like goblin.attack(hero)

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

    class Goblin:
        def __init__(self):
            self.health = 6
            self.power = 2

        def attack(self, enemy):
            enemy.health -= self.power
            print("The goblin does %d damage to you." % self.power)

    hero = Hero()
    goblin = Goblin()


    while goblin.health > 0 and hero.health > 0:
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
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:               # Goblin attacks hero
            goblin.attack(hero)
            if hero.health <= 0:
                print("You are dead.")

main()
