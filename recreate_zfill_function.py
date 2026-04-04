#if statement
#count
#print
def manual_zfill(text, width):
    if len(text) >= width:
        return text
    padding_count = width - len(text)
    zeros = "0" * padding_count
    if text[0] in ("+", "-"):
        return text[0] + zeros + text[1:]
    return zeros + text
print(manual_zfill("-7", 4))