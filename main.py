#!/bin/python3

""" In this program, i will write a game that is executed in the terminal.
"""

def main():
    ## First defining the starting status, where you have 200hp, nothing in the inventory, ...
    hp = 200 # This is starting hp, this might process during the game
    Inventory = [] # This is a list for the inventory

    # Introduction
    print("Hello warrior, welcome")
    while True:
        name = input("Please warrior, tell me your name ")
        if not name:
            print("Please first enter a name")
        else:
            hello(name)
            break

    # Choosing a starter weapon:
    print("\nSo warrior, first it's time to choose your starter weapon, you have three options:")
    theSword()
    print("\nOR\n")
    theBow()
    firstWeapon = input("\nPlease, choose your first weapon ")
    Inventory.append(firstWeapon)
    print(Inventory)

    
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
def theSword():
    print(f" This is the SWORD!!!\n","*"*20,"\n")
    n=4 # first part spaces
    m=0 # second part spaces
    print(" "*5,"**")
    for i in range(15):
        # point of the sword
        if i < 2:
            print(" "*n,"*"," "*m*2,"*") # end is to print on same line without moving to the next
            n-=1
            m+=1
        # the handle, i can think i can do this part better with only one if statement!!!!!!!!!!, so this is a TODO
        elif i == 8:
            print("*"*14)
        elif 8 < i < 10:
            print("*", " "*10, "*")
        elif i == 10:
            print("*"*14)
        # end of the sword
        elif i == 14:
            print(" "*n, "*"*8)
        # the inbetween of the sword, idk what it's called and also part of the handle
        else:
            print(" "*n,"*"," "*m*2,"*")

        

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
    
# Bow
def theBow():
    print(f" This is the BOW!!!\n","*"*18,"\n")
    print("*"*3)
    for i in range(0, 7, +1):
        print("*"," "*i, "*")
    print("*"," "*7,"*")
    for i in range(7,-1,-1):
        print("*"," "*i, "*")
    print("*"*3)






main()