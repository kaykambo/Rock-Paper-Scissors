#!/usr/bin/env python
from random import randint
player = input('rock (r), paper (p), scissors (s)')

options = ['rock', 'paper', 'scissors']

chosen1 = randint(1,3)
chosen = options[chosen1-1]

print (player, "vs", chosen)


#game logic
if (player == 'rock' and chosen == 'paper') or (player == 'paper' and chosen == 'scissors') or (player == 'scissors' and chosen == 'rock'):
    print (chosen, "beats", player, "You lose!")
elif (player == 'rock' and chosen == 'rock') or (player == 'paper' and chosen == 'paper') or (player == 'scissors' and chosen == 'scissors'):
    print ("It's a tie!")
elif (player == 'paper' and chosen == 'rock') or (player == 'scissors' and chosen == 'paper') or (player == 'rock' and chosen == 'scissors'):
    print (player, "beats", chosen, "You win!")
else:
    print (player, "is not a valid option. Please pick again")
    player = input('rock (r), paper (p), scissors (s)')
    
