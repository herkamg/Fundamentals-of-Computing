# the following functin should convert hours to seconds
def total_seconds(hours, minutes, seconds):
    return (hours * 60 + minutes) * 60 +seconds


######################################################
# Test 
def test(hours,minutes,seconds):
    print(str(hours) + " hours " + str(minutes) + " minutes " + 
    str(seconds) + " seconds totals to ", 
    str(total_seconds(hours, minutes, seconds)) +" seconds")


test(7, 21, 37)
test(10, 1, 7)
test(1, 0, 1)