#!/bin/python3

""" In this program, i will write a game that is executed in the terminal.
"""

def main():
    ## First defining the starting status, where you have 200hp, nothing in the inventory, ...
    hp = 200 # This is starting hp, this might process during the game
    Inventory = []

    # Introduction
    print("Hello warrior, welcome")
    while True:
        name = input("Please warrior, tell me your name ")
        if not name:
            print("Please first enter a name")
        else:
            hello(name)
            break
    
    # let them choose between three starter weapons

    # A fight, you have two attacks as starter, the normal(low damage, 100% hit chance) and special attack(high damage, 50% hit damage, code this like flipping a coin)
    print("Let's do some battling!!!")
    enemyhp = 150
    while hp > 0 | enemyhp > 0:
        damage = swordDamage()
        enemyhp = enemyhp - damage # This is to kill the enemy
        hp = hp-35 # this is a standard damage from the enemy
        print(f"Your hp: ",hp,"\t Enemy hp: ",enemyhp)
        
        # maybe adding a lil easter egg, for when you die together with your enemy, but will decide this later
        if hp <= 0 & enemyhp <= 0:
            print("Congrats, you can now fight your enemy in hell or heaven")
        elif hp <= 0 :
            print(f"I'm sorry {name}, you died")
        elif enemyhp <= 0:
            print(f"Congratulations {name}, you killed the enemy!!!")        


    




# Says hello to the warrior
def hello(to):
   print("Hello ", to)

### class of weapons with there damage
# Sword
def swordDamage():
    while True:
        attackType = input("Choose your attacktype ")
        if attackType == "normal":
            #print("normal")
            damage = 20
        elif attackType == "special":   # I still have to make the special attack have accuracy of 50% with the random()....
            #print("special")
            damage = 50
        else:
            print("This is not an attacktype")
            continue
        return damage



main()