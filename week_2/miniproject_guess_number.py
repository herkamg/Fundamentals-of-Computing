# http://www.codeskulptor.org/#user47_bBGPE0a5fX_0.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

################ import #####################

################ End import #################

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
from tkinter import*
import random
import math

###### globals variable#########
secret_number = 0 
remaining_guess = 0
choosen_range = 0 # 0 : range100; 1: range1000

###### End globals variable#########

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global remaining_guess
    global choosen_range
    
    choosen_range = 0
    secret_number = random.randrange(0, 100)
    print("New game. Range is [0,100)")
    remaining_guess = int(math.ceil(math.log((100-1),2)))
    print( "Number of remaining guesses is", remaining_guess)
    print("")


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    global remaining_guess
    global choosen_range
    
    choosen_range = 0
    secret_number = random.randrange(0, 100)
    print( "New game. Range is [0,100)")
    remaining_guess = int(math.ceil(math.log((100-1),2)))
    print( "Number of remaining guesses is", remaining_guess)
    print( "")

def range1000():
    # button that changes the range to [0,1000) and starts a new game 
    global secret_number
    global remaining_guess
    global choosen_range
    
    choosen_range = 1    
    secret_number = random.randrange(0, 1000) 
    print( "New game. Range is [0,1000)" )
    remaining_guess = int(math.ceil(math.log((1000-1),2)))
    print ("Number of remaining guesses is", remaining_guess)
    print( "")
    
    
def input_guess(guess):
    # main game logic goes here	
    global remaining_guess
    
    guess_number = int(guess)
    print( "Guess was",guess_number)
    remaining_guess -=1
    print( "Number of remaining guesses is", remaining_guess)

    if secret_number > guess_number:
        if remaining_guess ==0:
            print( "You ran out of guesses.  The number was", secret_number)
            print( "")
            if choosen_range==0:
                range100()
            else: 
                range1000()
        else:
            print( 'Higher!')
        
    elif secret_number < guess_number:
        if remaining_guess ==0:
            print( "You ran out of guesses.  The number was", secret_number)
            print( "")
            if choosen_range==0:
                range100()
            else: 
                range1000()
        else:
            print( 'Lower!')
    else:
        print( 'Correct!')
        print( "")
        if choosen_range==0:
            range100()
        else:
            range1000()
        
    print( "")
    
    
# create frame
frame = Tk()
frame.title("GUESS THE NUMBER")
w = Canvas(frame, width = 600, height = 300)
w.create_rectangle(300,0, 600,300, fill = "Gray")
w.pack()

#btn_range100 = Button(frame, text = "Range [0, 100)", width = 20, command = range100 ).place(x= 10, y = 10)
Button(frame, text = "Range [0, 100)", width = 20, command = range100 ).place(x= 10, y = 10)
#btn_range1000 = Button(frame, text= "Range [0, 1000)", width = 20, command = range1000).place(x = 10, y = 40)
Button(frame, text= "Range [0, 1000)", width = 20, command = range1000).place(x = 10, y = 40)
Label(frame, text = "Enter the guess number").place(x = 10, y = 70 )
# input fied to enter the Guess number
inp_number = Entry(frame)
inp_number.bind('<Return>', (lambda event: input_guess(inp_number.get() ) ))
inp = w.create_window(80, 100, window = inp_number, width= 130, height = 20)

# frame = simplegui.create_frame("GUESS THE NUMBER", 200, 200)

# btn_range100 = frame.add_button("Range is [0,100)", range100, 150)
# btn_range1000 = frame.add_button("Range is [0,1000)", range1000, 150)

# guess = frame.add_input("Enter the guess number", input_guess, 100)

# register event handlers for control elements and start frame

#frame.start()

new_game()
mainloop()
# call new_game 


# always remember to check your completed program against the grading rubric
