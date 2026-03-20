#input
#change casing
#print
cutiepie = input("Enter a word or sentence: ")
words = cutiepie.split()
pascal_case = ""
for word in words:
    pascal_case += word.capitalize()
print(pascal_case)