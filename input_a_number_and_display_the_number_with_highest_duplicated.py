#input
#if conditions
#store
#loop
numbers = []
while True:
    num = input("Enter a number: ")
    if not num.isdigit():
        print("Invalid input")
        break
    numbers.append(int(num))
if numbers:
    highest_duplicate = max(set(numbers), key=numbers.count)
    print(highest_duplicate)


