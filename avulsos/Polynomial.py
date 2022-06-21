def filterOnes(x):
    return x if x != 1 | x != -1 else ""

def mergeLists(list1,list2):
        lenght1,lenght2 = len(list1),len(list2)
        minLenght = min(lenght1,lenght2)
        result = []
        for sum in range(minLenght):
            result += [list1[sum]+list2[sum]]
        return result + list1[minLenght:] if lenght1 >= lenght2 else result + list2[minLenght:]

def negativeList(list):
    resultList =[]
    for coefficient in list:
        resultList += [coefficient*(-1)]
    return resultList

def trimRightmostZeroes(list):
    return list if ((list[-1] != 0) | (len(list) == 1)) else trimRightmostZeroes(list[0:-1])

def getLeftmostNonZero(list):
    return list[0] if (list[0] != 0) | (list == [0]) else getLeftmostNonZero(list[1:])

def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)

class Polynomial:
    def __mergeLists(list1,list2):
        lenght1,lenght2 = len(list1),len(list2)
        minLenght = min(lenght1,lenght2)
        result = []
        for sum in range(minLenght):
            result += [list1[sum]+list2[sum]]
        return result + list1[minLenght:] if lenght1 >= lenght2 else result + list2[minLenght:]

    def __init__(self,coefficients=[0]):
        self.coefficients = trimRightmostZeroes(coefficients)
        self.dimensions = len(self.coefficients) - 1
    
    def __neg__(self):
        return Polynomial(negativeList(self.coefficients))

    def __add__(self,other):
        return Polynomial(mergeLists(self.coefficients,other.coefficients))
    
    def __sub__(self,other):
        return Polynomial(mergeLists(self.coefficients,negativeList(other.coefficients)))
    
    def __str__(self):
        if self.coefficients == [0]: return "0"
        stringfyed = ""
        if self.coefficients[0]: stringfyed += "{} ".format(self.coefficients[0])
        for index in range(1,self.dimensions + 1):
            if self.coefficients[index] != 0:
                stringfyed += "{} {}x{} ".format("+" if self.coefficients[index] > 0 else "-",filterOnes(self.coefficients[index]),get_super(str(index)))
        if ((self.coefficients[0] == 0) & (getLeftmostNonZero(self.coefficients) < 0)): stringfyed = "--"+stringfyed
        return stringfyed if self.coefficients[0] else stringfyed[2:]