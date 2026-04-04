#input
#while function
#print
text = input("Enter a string: ")
def manual_rstrip(text, chars_to_remove=" "):
    i = len(text) - 1
    while i >= 0 and text[i] in chars_to_remove:
        i -= 1
    return text[:i + 1]
print(f"{manual_rstrip(text , '. ')}")