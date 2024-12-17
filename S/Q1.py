# Q1
# Create a function that accepts a string and change
# every letter in the string to the next letter.
# The function will display the converted string and will not return any value.
# Example: "a" becomes "b", "b" becomes "c" and so on.
# Note: "z" will be changed to "a". The function is case-sensitive.

def change_to_next_letter (string):
    result = ""
    for char in string:
        if char.islower():
            if (char == 'z'):
                result = result + 'a'

            else:
                result = result + chr(ord(char) + 1)

        elif char.isupper():
            if (char == 'Z'):
                result = result + 'A'

            else:
                result = result + chr(ord(char) + 1)

        else:
            result = result + char
    
    print (result)

user_input = input("Enter a string: ")
change_to_next_letter(user_input)