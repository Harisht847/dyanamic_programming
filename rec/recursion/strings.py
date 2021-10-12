def reverseString(string): 
    if string == "":
        return ""
    return str(reverseString(string[1:])) + string[0]


print(reverseString("abc"))