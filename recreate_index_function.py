#for loop
#if statement
#errors
#print
def manual_index(text, sub):
    sub_len = len(sub)
    for i in range(len(text) - sub_len + 1):
        if text[i: i + sub_len] == sub:
            return i
    raise ValueError(f"substring '{sub}' not found")
print(manual_index("Snake", "ake"))