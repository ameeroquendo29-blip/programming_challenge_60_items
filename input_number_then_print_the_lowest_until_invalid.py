#input
#store
#if condition
#while loop
setnum = set()
while True:
    num = float(input("Enter a number: "))
    setnum.add(num)
    if num in setnum:
        print(min(setnum))
