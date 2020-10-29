# Functions to manipulate global variable count

count = 0
###################################################
# Student should enter function on the next lines.
# Reset global count to zero.
def reset():
    global count
    count = 0
    
# Increment global count.
def increment():
    global count
    count = count + 1

# Decrement global count.
def decrement():
    global count
    count = count - 1
# Print global count.
def print_count():
    global count
    print( count)

    
###################################################
# Test

# note that the GLOBAL count is defined inside a function
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
# Output
#1
#2
#-2


#http://www.codeskulptor.org/iipp-practice-experimental/#user47_YubkPM0wSh_0.py


# open frame
# http://www.codeskulptor.org/iipp-practice-experimental/#exercises_intapp_open_frame_template.py
#