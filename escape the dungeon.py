# Escape the Dungeon: Advanced Edition
# Definitely not made by a freshman-year-old... maybe someone with *slightly* more experience!

import time
import random

def print_slow(text, delay=0.05):
    """Prints text one character at a time for dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def advanced_escape():
    print_slow("Welcome to 'Escape the Dungeon: Advanced Edition'!")
    print_slow("Your goal is simple: survive the dungeon and escape alive!")
    inventory = []
    health = 100

    def check_inventory():
        if inventory:
            print_slow(f"Inventory: {', '.join(inventory)}")
        else:
            print_slow("Inventory: (empty)")

    def encounter_dragon():
        print_slow("\nYou stumble into a massive cavern...")
        print_slow("A DRAGON is sleeping in the middle of the room!")
        if "Sword" in inventory:
            print_slow("You grip your sword tightly.")
            choice = input("Do you FIGHT the dragon or SNEAK past it? (fight/sneak): ").lower()
            if choice == "fight":
                print_slow("You charge at the dragon with your sword!")
                if "Shield" in inventory:
                    print_slow("The dragon breathes fire, but your shield protects you!")
                    print_slow("You land a killing blow and defeat the dragon. You find a treasure chest!")
                    inventory.append("Treasure")
                    print_slow("You open the chest and add the treasure to your inventory.")
                else:
                    print_slow("The dragon's fire scorches you completely. You perish. Game Over!")
                    return False
            elif choice == "sneak":
                print_slow("You quietly tiptoe past the dragon...")
                if random.choice([True, False]):
                    print_slow("You make it safely! Phew.")
                else:
                    print_slow("The dragon wakes up and eats you. Game Over!")
                    return False
        else:
            print_slow("You have no weapon. Sneaking is your only option.")
            if random.choice([True, False]):
                print_slow("You successfully sneak past the dragon!")
            else:
                print_slow("The dragon wakes up and eats you. Game Over!")
                return False
        return True

    def encounter_trap():
        print_slow("\nYou find a narrow corridor, but it looks suspicious...")
        choice = input("Do you SEARCH the corridor for traps or RUN through it? (search/run): ").lower()
        if choice == "search":
            print_slow("You carefully inspect the floor and walls...")
            if random.choice([True, False]):
                print_slow("You find and disarm a hidden trap! Safe passage!")
            else:
                print_slow("You missed a tripwire and set off a dart trap! You lose 20 health.")
                return -20
        elif choice == "run":
            print_slow("You sprint through the corridor at full speed!")
            if random.choice([True, False]):
                print_slow("You make it through unharmed!")
            else:
                print_slow("You trip a trap and get hit by arrows! You lose 30 health.")
                return -30
        else:
            print_slow("You hesitate too long and a hidden trap activates! You lose 10 health.")
            return -10
        return 0

    print_slow("\nYou begin your journey...")
    while health > 0:
        print_slow(f"\nHealth: {health}")
        check_inventory()

        print_slow("\nYou find yourself at a crossroads. Where do you go?")
        direction = input("Choose a path: LEFT, RIGHT, or STRAIGHT? (left/right/straight): ").lower()

        if direction == "left":
            if not encounter_dragon():
                break
        elif direction == "right":
            print_slow("\nYou find a small room with a chest.")
            if "Key" in inventory:
                print_slow("You use the key to open the chest and find a sword!")
                inventory.append("Sword")
            else:
                print_slow("The chest is locked. Maybe you need a key?")
        elif direction == "straight":
            trap_damage = encounter_trap()
            health += trap_damage
            if health <= 0:
                print_slow("You succumb to your injuries. Game Over!")
                break
        else:
            print_slow("Confused, you wander aimlessly and fall into a pit. Game Over!")
            break

        if "Treasure" in inventory:
            print_slow("\nYou find an exit door, glowing with light.")
            print_slow("You escape the dungeon with the treasure. You win!")
            break

    print_slow("\nThanks for playing 'Escape the Dungeon: Advanced Edition'!")
    if health <= 0:
        print_slow("Better luck next time!")

# Start the game
advanced_escape()
