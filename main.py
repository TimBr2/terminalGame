#!/bin/python3

""" In this program, i will write a game that is executed in the terminal.
"""
import os
import random

def main():
    ## First defining the starting status, where you have 200hp, nothing in the inventory, ...
    hp = 200 # This is starting hp, this might process during the game, TODO: making hp go up with leveling, same as weapon levels and enemy levels
    Inventory = [] # This is a list for the inventory, TODO: Should i make a different inventory for heals or make it a dictionary but than i can store multiple same heals so dictionary inside dictionary or dictionary inside list, idk

    # Introduction
    print("Hello warrior, welcome!\nMy name is Hendrik IV and i will guide you through this game.") #TODO, fix a better name than hendrik iv xd
    while True:
        name = input("Please warrior, tell me your name ")
        if not name:
            print("Please first enter a name")
        else:
            hello(name)
            break

    # Choosing a starter weapon:
    print("\nSo warrior, first it's time to choose your starter weapon, you have two options:")
    theSword()
    os.system("sleep 2") # give time to look at the beautifull sword
    print("\nOR\n")
    theBow()
    while True:
        firstWeapon = input("\nPlease, choose your first weapon ")
        if firstWeapon != "bow" and firstWeapon != "sword":
            print("You might get hurt doing that, please use a sword or a bow")
            continue
        elif firstWeapon == "sword":
            answer = input("The normal attack deals 25hp damage with 100% accuracy while the special attack deals 50hp damage with 50% accuracy."
                            "Are you sure you want to choose this weapon? Then press y: ")
            if answer == "y":
                Inventory.append(firstWeapon)
                break
            else:
                print("I guess you still have to think about your awnser")
                continue
        elif firstWeapon == "bow":
            answer = input("The normal attack deals 15hp damage with 100% accuracy while the special attack deals 70hp damage with 50% accuracy."
                            "Are you sure you want to choose this weapon? Then press y: ")
            if answer == "y":
                Inventory.append(firstWeapon)
                break
            else:
                print("Brrooo, don't be indecisive and just choose!!!")
                continue
            
    print(f"You have a {firstWeapon} in your inventory: ",Inventory)
    
    reset()

    # A fight, you have two attacks as starter, the normal(low damage, 100% hit chance) and special attack(high damage, 50% hit damage, code this like flipping a coin)
    print("Let's do some battling!!!")           
    enemyhp = 150
    while hp > 0 and enemyhp > 0:
        if Inventory[0] == "sword":
            damage = swordDamage()
        elif Inventory[0] == "bow":
            damage = bowDamage()
        else:
            print("Something went horribly wrong here")
        #damage = swordDamage()
        enemyhp = enemyhp - damage # This is to kill the enemy
        hp = hp-35 # this is a standard damage from the enemy
        print(f"Your hp: ",hp,"\t Enemy hp: ",enemyhp)
        
        # maybe adding a lil easter egg, for when you die together with your enemy, but will decide this later
        if hp <= 0 and enemyhp <= 0:
            print("Congrats, you can now fight your enemy in hell or heaven")
        elif hp <= 0 :
            print(f"I'm sorry {name}, you died") # TODO, fix the fact that when you're dead, you still play in the game, should i just end the game or let him revive?
        elif enemyhp <= 0:
            print(f"Congratulations {name}, you killed the enemy!!!")    
    
    reset()

    # After this battle, your hp is probably low, so now we let the player go to somewhere where he can play a game and get something in return like hp
    print(f"Oh no, you only have {hp}hp left!\n"
            "I know something! let's go to a magician, he can give you some health")
    # TODO: make some games to gain health: maybe a blackjack, or a hangman game or a guess the number game in less than 5 turns with higher and lower tips, ...


    




# Says hello to the warrior
def hello(to):
   print("Hello ", to)

# resetting the terminal
def reset():
    os.system("sleep 3") # Sleep 3 seconds before clearing
    os.system("clear") # to clear the terminal

### class of weapons with there damage
# Sword
def theSword():
    print(f" This is the SWORD!!!\n","*"*20,"\n")
    n=4 # leftside spaces
    # point of the sword
    print(" "*5,"**")
    for i in range(3):
        print(" "*n,"*"," "*i*2,"*") # end is to print on same line without moving to the next
        n-=1
    # sword
    for i in range(6):
        print(" "*n,"*"," "*6,"*")
    # between sword and handle
    print("*"*14)
    print("*", " "*10, "*")
    print("*"*14)
    # handle
    for i in range(3):
        print(" "*n,"*"," "*6,"*")
    print(" "*n,"*"*10)
        

def swordDamage():
    while True:
        attackType = input("\nChoose your attacktype ")  
        if attackType == "normal":
            damage = 25
            break
        elif attackType == "special":   # I still have to make the special attack have accuracy of 50% with the random()....
            accuracyList = ["hit","miss"]
            accuracy = random.choice(accuracyList)
            if accuracy == "hit":
                damage = 50
                break
            elif accuracy == "miss":
                print("Guess you missed noob, learn how to aim next time")
                damage = 0
                break
        else:
            print("This is not an attacktype, choose between a \"normal\" or \"special\" attack")
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
    
# The bow does less normal damage but a higher special attack damage
def bowDamage():
    while True:
        attackType = input("\nChoose your attacktype ")  
        if attackType == "normal":
            damage = 15
            break
        elif attackType == "special":   # I still have to make the special attack have accuracy of 50% with the random()....
            accuracyList = ["hit","miss"]
            accuracy = random.choice(accuracyList)
            if accuracy == "hit":
                damage = 70
                break
            elif accuracy == "miss":
                print("Guess you missed noob, learn how to aim next time")
                damage = 0
                break
        else:
            print("This is not an attacktype, choose between a \"normal\" or \"special\" attack")
            continue
    return damage
    






main()