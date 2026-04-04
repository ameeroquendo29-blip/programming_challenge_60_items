#input
#counter
#if conditions
#while loop
numbers = set()
count = 0
while True:
    num = input("Enter a number: ")
    numbers.add(int(num))
    count += 1
    if not num.isdigit():
        print("Invalid input")
    if numbers:
        average = sum(numbers) / count
        print("The average is", average)




