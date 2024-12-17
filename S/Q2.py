# Q2
# Create a function that accepts an array of two strings and
# checks if ALL the letters in the secondstring are present in the first string.
# The function will return true or false

# Example:
# ["melon", "lemon"] => true
# ["entrance", "nectar"] => true
# ["reap", "drape"] => false
# ["finished", "finnish"] => false

def present_letter(strings):

    first, second = strings[0], strings[1]

    for char in set (second):
        if second.count(char) > first.count(char):
            return False
    return True

first_string = input ("Enter first string: ")
second_string = input ("Enter second string: ")

results = present_letter([first_string, second_string])

print(results)