# Convert input text into Pig Latin

#http://www.codeskulptor.org/iipp-practice-experimental/#exercises_button_pig_latin_template.py
###################################################
# Student should add code where relevant to the following.

from tkinter import* 


# Pig Latin helper function
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    
    first_letter = word[0]
    rest_of_word = word[1 : ]
    
    # Student should complete function on the next lines.
    if first_letter not in ['a', 'e', 'i', 'o', 'u', 'y']:
        return rest_of_word + first_letter + "ay"
    else:
        return word+ "way"

# Handler for input field    
def get_input():
    word = textentry.get()
    print(pig_latin(word))   
    

# Create frame and assign callbacks to event handlers
#frame = simplegui.create_frame("Pig Latin translator", 200, 200)

frame = Tk()
frame.title("Pig Latin translator")
w = Canvas(frame, width = 600, height = 300)
w.create_rectangle(300, 0, 600, 600, fill = 'Gray')
w.pack()
textentry = Entry(w)
# textentry.bind("<Return>", get_input(r.get()))
inp = w.create_window(60, 50, window=textentry, height=20, width=100)
btn_print_piglatin = Button(frame, text = "print pig latin", width= 20, command = get_input).place(x=10, y=100)
# Start the frame animation
mainloop()



###################################################
# Test

# get_input("pig")
# get_input("owl")
# get_input("tree")

###################################################
# Expected output from test

#igpay
#owlway
#reetay


