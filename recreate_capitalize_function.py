#input
#if statements
#print
text = input("Enter some text: ")
def manual_capitalize(text):
    if not text:
        return ""
    return text[0].upper() + text[1:].lower()
print(manual_capitalize(text))