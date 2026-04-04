#input
setnum = set()
while True:
    num = float(input("Enter a number: "))
#if conditions and print
    if num in setnum:
        print("Duplicate")
    else:
        print("Unique")
    setnum.add(num)
#while loop
#store

