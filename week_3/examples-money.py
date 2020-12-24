# http://www.codeskulptor.org/#user47_hCJBurcmQy_2.py

# http://www.codeskulptor.org/iipp-practice-experimental/#user47_Lnazp1xwsD_0.py
# http://www.codeskulptor.org/iipp-practice-experimental/#user47_AxK67PBGkT_0.py
# http://www.codeskulptor.org/iipp-practice-experimental/#user47_c3MriwLtyF_0.py
# http://www.codeskulptor.org/iipp-practice-experimental/#user47_3xXjNheWs6_2.py
# http://www.codeskulptor.org/iipp-practice-experimental/#user47_bjaLOv3uh7_1.py

# Handle single quantity
def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result
        
# convert xx.yy to xx dollars and yy cents
def convert(val):
    # Split into dollars and cents
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))

    # Convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string
  
    
    
# Tests
print( convert(11.23))
print( convert(11.20))
print( convert(1.12))
print( convert(12.01))
print( convert(1.01))
print( convert(0.01))
print( convert(1.00))
print( convert(0))