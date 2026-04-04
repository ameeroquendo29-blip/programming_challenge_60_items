#if statement
#conditions
#print
def manual_endswith(text, suffix):
    if len(suffix) > len(text):
        return False
    return text[-len(suffix):] == suffix
print(manual_endswith("document.pdf", ".pdf"))
print(manual_endswith("image.jpg", ".png"))