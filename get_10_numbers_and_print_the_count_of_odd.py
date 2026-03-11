#input
#if statement
#count
#print
even = 0
for i in range (10):
    num = input(f"Enter number {i}: ")
    if int(num) % 2 == 1:
        even += 1
print(even)