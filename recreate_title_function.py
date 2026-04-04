#input
#split function
#capitalize function
#print
text = input("Enter some words: ")
def manual_title(text):
    words = text.split()
    return " ".join(word.capitalize() for word in words)
print(manual_title(text))