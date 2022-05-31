
spaceOrd = ord(' ')
lowestDigit = ord('0')
highestDigit = ord('9')
lowestUppercase = ord('A')
highestUppercase = ord('Z')
lowestLowercase = ord('a')
highestLowercase = ord('z')


def makeTrail():
    charTrail = [32]
    for i in range(lowestDigit,highestDigit + 1):
        charTrail += [i]
    for i in range(lowestUppercase,highestUppercase + 1):
        charTrail += [i]
    for i in range(lowestLowercase,highestLowercase + 1):
        charTrail += [i]
    return charTrail

trailLenght = len(makeTrail())

def shiftedTrail(salt,trail):
    return shiftedTrail((salt % trailLenght)-1, trail + [trail.pop(0)]) if salt > 0 else  trail

def makeTranslationTable(salt):
    normalTrail = makeTrail()
    translated = shiftedTrail(salt,makeTrail())
    translationTable = {}
    for i in range(len(normalTrail)):
        translationTable.update({normalTrail[i] : translated[i]})
    return translationTable

def codeCaesar(text,salt):
    return text.translate(makeTranslationTable(salt))

def decodeCaesar(text,salt):
    return codeCaesar(text, trailLenght - (salt % trailLenght))



"""
def makeShiftMap(salt):
    targetTrail = 

def filterChar(char):
    return char if char in charTrail else ' '

def shiftChar(char,salt=0):
    charValue = filterChar(char)
    shiftedValue = ####
    return #######


def LuidisFunction(inputTuple):
    return codeCaesar(inputTuple[1],inputTuple[2]) if inputTuple[0] else decodeCaesar(inputTuple[1],inputTuple[2])
"""
