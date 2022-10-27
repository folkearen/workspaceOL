def isDigit(string):
    try:
        string = float(string)
        return True
    except:
        
        return False




print(isDigit("s2324"))
print(isDigit("-234.4"))