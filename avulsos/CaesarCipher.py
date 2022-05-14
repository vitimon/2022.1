import string

lowestValue = 97
highestValue = 123

def filterChar(char):
    return char if (char in string.ascii_lowercase) | (char == ' ') else " "
    
def shiftChar(char,salt=0):
    char = filterChar(char)
    charValue = (123 if char == ' ' else ord(char))
    shiftedValue = lowestValue + (charValue - lowestValue + salt) % (1 + highestValue - lowestValue)
    return " " if shiftedValue == 123 else chr(shiftedValue)

def codeCaesar(text,salt):
    codedText = ''
    for i in text:
        codedText += shiftChar(i,salt)
    return codedText

def decodeCaesar(text,salt):
    return codeCaesar(text,1 + highestValue - lowestValue - salt)

def LuidisFunction(inputTuple):
    return codeCaesar(inputTuple[1],inputTuple[2]) if inputTuple[0] else decodeCaesar(inputTuple[1],inputTuple[2])


for i in [(True, "abc", 1),(False, "bcd", 1),(True, "xyz", 5),(False, "bcd", 5)]:
    print(LuidisFunction(i))
