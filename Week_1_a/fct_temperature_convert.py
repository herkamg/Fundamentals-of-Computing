# convert temperature from Fahrenheit in Celsius
def fahrenheit2celsius(fahrenheit):
    Celsuis = (5.0 / 9.0) * (fahrenheit - 32)
    return Celsuis


# Test !!!!!!!!!!!!!!!!
tempCeluis = fahrenheit2celsius(32)

print(" 32 fahrenheit is :",tempCeluis, "celsius")

tempCeluis = fahrenheit2celsius(212)

print(" 212 fahrenheit is :",tempCeluis, "celsius \n")

# convert fahrenheit to Kelvin
def fahrenheit2kelvin(fahrenheit):
    #kelvin = (5.0/9.0)* (fahrenheit - 32 ) + 237.15
    celsius = fahrenheit2celsius(fahrenheit)
    kelvin = celsius + 237.15 
    return kelvin
# Test !!!!!!!!!!!!!!!!!
Kelvin1 = fahrenheit2kelvin(32)
Kelvin2 = fahrenheit2kelvin(212)

print(" 32 fahrenheit is :",Kelvin1, "Kelvin")
print(" 212 fahrenheit is :",Kelvin2, "Kelvin")


# print Hello world !
def hello():
    print("Hello World !")

hello()
h = hello()
print(h)