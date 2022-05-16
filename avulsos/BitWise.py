from math import log2, ceil

def getFull(number):
    scale = ceil(log2(number))
    return 2**scale -1

def flipBits(number):
    fullBits = getFull(number)
    return fullBits ^ number

def invertBits(number):
    invertedNumber = 0
    while(number):
        invertedNumber = (invertedNumber << 1) + (number % 2)
        number = number >> 1
    return invertedNumber

def getOnes(number):
    ones = 0
    while(number):
        if(number % 2):
            ones += 1
        number = number >> 1    
    return ones

def getZeroes(number):
    zeroes = 0
    while(number):
        if((number % 2)==0):
            zeroes += 1
        number = number >> 1
    return zeroes

