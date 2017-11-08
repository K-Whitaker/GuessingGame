'''
Created on Nov 3, 2017

@author: Kyle Whitaker
'''

import random

def guess():

    run = True
    while run == True:

        max = int(input("Would you like to play the Guessing Game?\nHow high should I count?\n"))
        print("Which seed shall we use?")
        seed = int(input())
        random.seed(seed)
        print("Do you know the two numbers I'm thinking between 1 and", max)
        x = random.randint(1,max)
        y = random.randint(2,max - 1)
                           
       
        guessX = int(input())
        guessY = int(input())
        
        if guessX > x:
            print("Too high for the first number",insult())
        if guessX < x:
            print("Too low for the first number",insult())
        if guessX == x:
            print("THATS IT! YOU KNOW THE FIRST NUMBER!")
        if guessY > y:
            print("Too high on the second number",insult())
        if guessY < y:
            print("Too low on the second number",insult())
        if guessY == y:
            print("THATS IT! YOU KNOW THE SECOND NUMBER!")
        if guessX == x and guessY == y:
            print("A WINNER IS YOU! Would you like to play again?")
            run = False
    choice = str(input("Would you like to try again? Yes or No\n"))
    if choice == "No":
        run = False
    if choice == "Yes":
        run = True
    
def insult():
    insult = [", halfwit.", ", you trogloyte.", ", mouthbreather.", ", nice one poindexter.", ", was your crib lined with lead paint?"]
    return random.choice(insult)

guess()
    