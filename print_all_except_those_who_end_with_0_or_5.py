#input
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
#for loop statement
for num in range(num1, num2 + 1):
    if num % 5 != 0:
        print(num)
#conditions