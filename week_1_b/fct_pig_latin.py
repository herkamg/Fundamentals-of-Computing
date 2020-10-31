def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    first_letter = word[0]
    rest_of_word = word[1 : ]
    if first_letter not in ['a', 'e', 'i', 'o', 'u', 'y']:
        return rest_of_word + first_letter + "ay"
    else:
        return word + "way"

###################################################
# Tests
# Student should not change this code.

def test(word):
	"""Tests the pig_latin function."""
	
	print(pig_latin(word))
	
test("pig")
test("owl")
test("python")
