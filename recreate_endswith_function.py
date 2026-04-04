#if statement
#conditions
#print
def manual_startswith(text, prefix):
    if len(prefix) > len(text):
        return False
    return text[:len(prefix)] == prefix
print(manual_startswith("Pythonic", "Py"))