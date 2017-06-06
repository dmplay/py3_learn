# !/usr/bin/python
# -*- coding: UTF-8 -*-
# This is a guess the number game.
import random
guessesTaken=0
print("hello,what's your name")
myName = input()
number = random.randint(1,20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
while guessesTaken < 6:
    print("show your num")
    guess = int(input())
    guessesTaken = guessesTaken+1
    if guess == number:
        print("You are Great")
        break
    elif guess > number:
        print("No,less please,Guess again")
    else :
        print("No,more please,Guess again")
