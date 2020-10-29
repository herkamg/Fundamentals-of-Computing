# Register three buttons
#http://www.codeskulptor.org/iipp-practice-experimental/#exercises_button_count_template.py
###################################################
# Student should add code where relevant to the following.

from tkinter import*
color = 'Gray'

# Handlers for buttons
def set_red():
    global color
    color = "red"
    
def set_blue():
    global color
    color = "blue"
    
def print_color():
    print(color)

# Create frame
frame = Tk()
frame.title("Set and print colors")
w = Canvas(frame, width = 600, height = 300)
w.pack()

btnset_red = Button(frame, text = "Background Red", width = 20 , command = set_red).place(x=10, y = 10)
btnset_blue = Button(frame, text = "Background Blue", width = 20, command = set_blue).place(x=10, y = 40)
btnprint_color = Button (frame, text = "print color", width = 20, command = print_color).place(x = 10, y = 70)
#frame = simplegui.create_frame("Set and print colors", 200, 200)

# Start the frame animation
mainloop()


###################################################
# Test

set_red()
print_color()
set_blue()
print_color()
set_red()
set_blue()
print_color()

###################################################
# Expected output from test

#red
#blue
#blue
