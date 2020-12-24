# import modules

import tkinter as tk
import random
from timer import Timer
import time

# classes (later)
class movingWord:
    def __init__(self, canvas, x, y):
        message = "python is Fun!"
        self.xpos = x
        self.ypos = y
        self.canvas = canvas
        self.movableText = self.canvas.create_text( self.xpos, self.xpos,  fill='Red',text = message)        
 
    def update (self, text):
        self.message = text
        
    def tick(self):
        self.xpos = random.randrange(50, 100)
        self.ypos = random.randrange(50, 100)

    def drawer(self):
        #self.tick()
        self.xpos = random.randrange(50, 100)
        self.ypos = random.randrange(50, 100)
        print("xpos : "+ str(self.xpos) +" ypos : "+ str(self.ypos))       
        self.canvas.after(1000, self.drawer )



# Helper functions 


# Define event handlers 

# event handler for input box

# event handler for timer

# event handler to draw canvas


# create a frame
frame = tk.Tk()
frame.title("Moving Word")
frame.geometry("600x310")
# Register event handlers
my_canvas = tk.Canvas(frame, width= 300, height = 300, bg = "Black")
my_canvas.pack()
my_canvas.place(x=280, y=5)

# create two ball objects and animate them
movingWord1 = movingWord(my_canvas, 10, 10)
movingWord1.drawer()

# t = frame.

# Start frame & timers
tk.mainloop()