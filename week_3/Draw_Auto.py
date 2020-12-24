# drawing a car using line and circle
# http://www.codeskulptor.org/#user47_wH5s0CgdaU_2.py
from tkinter import*

frame = Tk()
# 
# Global (state)

# Helper functions    

# classes (later)

# Define event handlers 

# create a frame
frame.title("My Car")
frame.geometry("600x400")

my_canvas = Canvas(frame, width= 300, height = 300, bg = "Black")
my_canvas.pack()
my_canvas.place(x=280, y=5)



# Register event handlers
my_canvas.create_text( 50, 10,  fill='White',text = "Daniela")
my_canvas.create_oval((80,190),(100,210),width=8, fill='White', outline = 'White')
my_canvas.create_oval((200,190),(220,210),width=8, fill='White', outline = 'White')
my_canvas.create_line((50,180), (250,180), width=40, fill='Red')
my_canvas.create_line((55,170), (90,120), width=5, fill='Red')
my_canvas.create_line((90,120), (190,120),width = 5, fill = 'Red')
my_canvas.create_line((185,118), (230,170),width = 5, fill = 'Red')
my_canvas.create_line((150,105), (150,160),width = 5, fill = 'Orange')
my_canvas.create_oval((145,100),(155,105),width=5, fill = 'Yellow', outline ='Yellow')
my_canvas.create_line((90,118), (90,160),width = 5, fill = 'Orange')
my_canvas.create_oval((170,110),(180,120),width=5, fill = 'Orange', outline ='Orange')
my_canvas.create_oval((165,110),(175,120),width=5, fill = 'Yellow', outline ='Yellow')
# Start frame & timers
mainloop()