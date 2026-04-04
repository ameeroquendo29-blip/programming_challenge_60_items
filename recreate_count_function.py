#while loop
#if else statement
#print
def manual_count(text, sub):
    count = 0
    sub_len = len(sub)
    i = 0
    while i <= len(text) - sub_len:
        if text[i: i + sub_len] == sub:
            count += 1
            i += sub_len
        else:
            i += 1
    return count
print(manual_count("aaaa", "aa")) 