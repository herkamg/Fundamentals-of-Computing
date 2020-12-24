# first example of drawing on the canvas

#import simplegui
from tkinter import *

# define draw handler
def draw(canvas):
    canvas.draw_text("Hello!",[100, 100], 24, "White")
    canvas.draw_circle([100, 100], 2, 2, "Red")

# create frame
# frame = simplegui.create_frame("Text drawing", 300, 200)

frame = Tk()
frame.title("Text drawing")
w = Canvas(frame, width = 600, height = 300)
w.create_rectangle(300,0, 600, 300, fill = "Gray")
w.create_text(450,150, text= "Hello")
w.pack()

# register draw handler   
#def my_draw(Canvas):


#frame.set_draw_handler(draw)

# start frame
mainloop()