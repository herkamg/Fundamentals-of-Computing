from tkinter import*
# Add "Hello" and "Goodbye" buttons
# http://www.codeskulptor.org/iipp-practice-experimental/#exercises_button_print_goodbye_template.py
###################################################
# Student should add code where relevant to the following.

#import simplegui 


# Handlers for buttons
def print_hello():
    print ("Hello")
    
def print_goodbye():
    print ("Goodbye")

# Create frame and assign callbacks to event handlers
frame = Tk()
frame.title("Hello Goodbye")
w = Canvas(frame, width = 600, height = 300)
w.pack()
w.create_rectangle(300, 0, 600, 600, fill = 'Gray')
btnhello = Button(frame, text = 'Hello', width = 20, command = print_hello).place(x=10, y = 10)
btngoodbye = Button(frame, text = 'Goodbye', width = 20, command = print_goodbye).place(x=10, y = 40)



# Start the frame animation
# frame.start()
mainloop()


###################################################
# Test

print_hello()
print_hello()
print_goodbye()
print_hello()
print_goodbye()

###################################################
# Expected output from test

#Hello
#Hello
#Goodbye
#Hello
#Goodbye


