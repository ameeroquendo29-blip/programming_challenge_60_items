#input
numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
for num in numbers:
    if numbers.count(num) == 1:
        print(num, end=',')
#for loop
#if condition
#counter and print

