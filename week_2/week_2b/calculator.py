from tkinter import*
# codeskulptur : http://www.codeskulptor.org/#user47_hzpfOuMAQc9aSuY_3.py
#initialize globals
store = 12
operand = 3

#define helper function that manipulate store and operand


#define classes

# define eventhandler

def output():
    print("Store = ", store)
    print("Operand = ", operand)
    print("")

def swap():
    global store , operand
    # mem = store
    # store = operand
    # operand = mem
    store, operand = operand, store
    output()

def add():
    global store
    store = store + operand
    output()

def substract():
    global store, operand
    store = store - operand
    output()
    
def mult():
    global store, operand
    store = store * operand
    output()
    
def div():
    global store, operand
    store = store / operand
    output()
    
def getoperand(inp):
    global operand
    operand = float(inp)

# output()
# swap()
# swap()
# create frame
master = Tk()
master.title("Calculator")
w = Canvas(master, width = 600, height = 300)
w.pack()

w.create_rectangle(200, 0, 600, 300, fill ='Gray')
btnprint = Button(master, text = 'Print', width =20, command = output).place(x=10, y=10)
btnswap = Button(master, text = 'Swap', width =20, command = swap).place(x=10, y=50)
btnadd = Button(master, text = 'Add', width =20, command = add).place(x=10, y=90)
btnsubstract = Button(master, text = 'Substract', width =20, command = substract).place(x=10, y=130)
#fbc 


# register event

#start frame
mainloop()

