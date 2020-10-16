''' Powerball is lottery game in which 6 numbers are drawn at random. 
Players can purchase a lottery ticket with a specific number combination and, 
if the number on the ticket matches the numbers generated in a random drawing, 
the player wins a massive jackpot. '''
import random

def powerball():
    n1 = random.randrange(0,60)
    n2 = random.randrange(0,60)
    n3 = random.randrange(0,60)
    n4 = random.randrange(0,60)
    n5 = random.randrange(0,60)
    n6 = random.randrange(0,36)
    print("Today's numbers are "+ str(n1)+ ", " + str(n2)+ ", " +str(n3)+ ", " 
        +str(n4)+ ", and " + str(n5) + ". The Powerball number is " + str(n6)+".")

powerball()
powerball()
powerball()