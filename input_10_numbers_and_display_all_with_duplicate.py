#input
#for loop
#if conditions
#counter and print
numbers = []
duplicates = []
for i in range(10):
    num = int(input("Enter a number: "))
    if num in numbers:
        duplicates.append(num)
    else:
        numbers.append(num)
print(duplicates)
