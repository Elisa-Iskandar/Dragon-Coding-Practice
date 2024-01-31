#Create a recursive function to check if a given string is a palindrome.
def palindromechecker(my_string):
    if len(my_string) <= 1:
        return "its a palindrome"
    elif my_string[0] == my_string[-1]:
        return palindromechecker(my_string[1:-1])
    else:
        return "its not a palindrome"

print(palindromechecker("racecar"))
