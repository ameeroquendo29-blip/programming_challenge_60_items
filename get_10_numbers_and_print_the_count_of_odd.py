#input
#if statement
#count
#print
odd = 0
for i in range (10):
    num = input(f"Enter number {i}: ")
    if int(num) % 2 == 1:
        odd += 1
print(odd)