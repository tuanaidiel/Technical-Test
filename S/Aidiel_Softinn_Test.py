# Q1

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

print("---------------------------------------------")

# Q2

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

print("---------------------------------------------")

# Q3

def triangular (n):

    return n * (n + 1) // 2

n = int(input("Enter a number: "))

print(triangular(n))