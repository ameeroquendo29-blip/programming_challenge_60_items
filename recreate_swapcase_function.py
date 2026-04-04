#for loop
#if statements
#print
text = input("Enter some text: ")
def manual_swapcase(text):
    result = ""
    for character in text:
        if character.isupper():
            result += character.lower()
        elif character.islower():
            result += character.upper()
        else:
            result += character
    return result
print(manual_swapcase(text))