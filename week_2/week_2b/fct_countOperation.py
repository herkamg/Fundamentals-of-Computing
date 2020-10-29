# GUI with buttons to manipulate global variable count

###################################################
# Student should enter their code below

from tkinter import*

count = 0
# Define event handlers for four buttons
def reset():
    global count
    count = 0

def increment():
    global count
    count +=1
    
def decrement():
    global count
    count -=1
    
def print_count():
    print( count)
    
# Create frame and assign callbacks to event handlers
frame = Tk()
frame.title("count Operatons")
w = Canvas(frame, width= 600, height = 300)
w.pack()
w.create_rectangle(300, 0, 600, 600, fill = 'Gray')
btn_reset = Button(frame, text= "Reset", width= 20, command = reset).place(x=10, y= 10)
btn_increment = Button(frame, text = "increment", width = 20, command = increment).place(x=10, y= 40)
btn_decrement = Button(frame, text = "decrement", width= 20, command = decrement).place(x=10, y=70)
btn_print_count = Button(frame, text = "print", width= 20, command = print_count).place(x=10, y=100)

# Start the frame animation
mainloop()
#http://www.codeskulptor.org/iipp-practice-experimental/#exercises_button_count_template.py
    
###################################################
# Test

# Note that the GLOBAL count is defined inside a function
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Expected output from test

#1
#2
#-2
